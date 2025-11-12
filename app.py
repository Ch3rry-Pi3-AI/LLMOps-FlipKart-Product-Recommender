"""
app.py

Flask application exposing a Retrieval-Augmented Generation (RAG) endpoint 
with integrated Prometheus metrics. Compatible with LCEL-based 
`rag_chain.py` and `data_ingestion.py` modules.

The application:
    - Loads environment variables for API keys and database credentials.
    - Initialises the vector store and RAG chain on start-up.
    - Exposes routes for:
        * Chat interaction (`/` and `/get`)
        * Health checks (`/health`)
        * Prometheus monitoring metrics (`/metrics`)
"""

# =============================================================================
# Imports
# =============================================================================

from __future__ import annotations

# Flask and HTTP utilities
from flask import Flask, request, Response, render_template, jsonify

# Prometheus client for metrics tracking
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

# Environment variable loader
from dotenv import load_dotenv

# Custom modules for ingestion and RAG pipeline building
from flipkart.data_ingestion import DataIngestor
from flipkart.rag_chain import RAGChainBuilder


# =============================================================================
# Environment Configuration
# =============================================================================

# Load environment variables (e.g., GROQ_API_KEY, HUGGINGFACEHUB_API_TOKEN, AstraDB credentials)
load_dotenv()


# =============================================================================
# Prometheus Metrics
# =============================================================================

# Count all HTTP requests received by the Flask server
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests")

# Count RAG-specific POST requests (used for chatbot queries)
RAG_REQUEST_COUNT = Counter("rag_requests_total", "Total RAG Requests")


# =============================================================================
# Application Factory
# =============================================================================

def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Returns
    -------
    Flask
        A configured Flask application instance with RAG endpoints and metrics.
    """
    # Instantiate the Flask app
    app = Flask(__name__)

    # -------------------------------------------------------------------------
    # Initialise the RAG pipeline components
    # -------------------------------------------------------------------------

    # Load existing vector store (or ingest new data if unavailable)
    vector_store = DataIngestor().ingest(load_existing=True)

    # Build the RAG chain that will process user queries
    rag_chain = RAGChainBuilder(vector_store).build_chain()

    # -------------------------------------------------------------------------
    # Route: Root Page (Chat Interface)
    # -------------------------------------------------------------------------

    @app.route("/", methods=["GET"])
    def index():
        """
        Render the chatbot’s front-end interface.

        Returns
        -------
        Response
            The rendered HTML template for the chatbot UI.
        """
        # Increment total request counter
        REQUEST_COUNT.inc()
        # Render HTML page from templates/
        return render_template("index.html")

    # -------------------------------------------------------------------------
    # Route: RAG Query Endpoint
    # -------------------------------------------------------------------------

    @app.route("/get", methods=["POST"])
    def get_response():
        """
        Process a user message via the RAG pipeline and return the model’s reply.

        Returns
        -------
        str | tuple
            The chatbot’s generated answer if successful, or an error message
            with status code 400 if the input message is empty.
        """
        # Increment request counters
        REQUEST_COUNT.inc()
        RAG_REQUEST_COUNT.inc()

        # Retrieve and sanitise user input
        user_input = request.form.get("msg", "").strip()
        if not user_input:
            return jsonify({"error": "Empty message"}), 400

        # Invoke the RAG chain with session context for message history tracking
        result = rag_chain.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": "user-session"}},
        )

        # Extract and return the model’s answer from the response dictionary
        return result["answer"]

    # -------------------------------------------------------------------------
    # Route: Prometheus Metrics Endpoint
    # -------------------------------------------------------------------------

    @app.route("/metrics", methods=["GET"])
    def metrics():
        """
        Expose application metrics in Prometheus-compatible format.

        Returns
        -------
        Response
            A plain-text response containing current Prometheus metrics.
        """
        # Increment total request counter
        REQUEST_COUNT.inc()
        # Generate metrics data
        data = generate_latest()
        # Return formatted metrics output
        return Response(data, mimetype=CONTENT_TYPE_LATEST)

    # -------------------------------------------------------------------------
    # Route: Health Check Endpoint
    # -------------------------------------------------------------------------

    @app.route("/health", methods=["GET"])
    def health():
        """
        Simple health check endpoint to verify application status.

        Returns
        -------
        Response
            JSON response confirming service health.
        """
        # Return basic JSON payload with 200 status
        return jsonify(status="ok"), 200

    # Return the configured Flask app instance
    return app


# =============================================================================
# Application Entry Point
# =============================================================================

if __name__ == "__main__":
    # Create the Flask app
    app = create_app()

    # Run the server on all network interfaces (port 5000)
    app.run(host="0.0.0.0", port=5000, debug=True)
