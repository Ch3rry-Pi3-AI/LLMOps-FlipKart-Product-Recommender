"""
app.py

Flask app exposing a simple RAG endpoint with Prometheus metrics.
Compatible with LCEL-based rag_chain.py and DataIngestor.
"""

from __future__ import annotations

from flask import Flask, request, Response, render_template, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from dotenv import load_dotenv

from flipkart.data_ingestion import DataIngestor
from flipkart.rag_chain import RAGChainBuilder

# Load environment variables (GROQ_API_KEY, HUGGINGFACEHUB_API_TOKEN, AstraDB creds, etc.)
load_dotenv()

# Prometheus metrics
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests")
RAG_REQUEST_COUNT = Counter("rag_requests_total", "Total RAG Requests")


def create_app() -> Flask:
    app = Flask(__name__)

    # Initialise vector store and RAG chain once per app
    vector_store = DataIngestor().ingest(load_existing=True)
    rag_chain = RAGChainBuilder(vector_store).build_chain()

    @app.route("/", methods=["GET"])
    def index():
        REQUEST_COUNT.inc()
        return render_template("index.html")

    @app.route("/get", methods=["POST"])
    def get_response():
        REQUEST_COUNT.inc()
        RAG_REQUEST_COUNT.inc()

        user_input = request.form.get("msg", "").strip()
        if not user_input:
            return jsonify({"error": "Empty message"}), 400

        # RunnableWithMessageHistory expects a session_id in config.configurable
        result = rag_chain.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": "user-session"}},
        )
        return result["answer"]

        # LCEL chain (per our wrapper) returns {"answer": "..."}
        return result["answer"]

    @app.route("/metrics", methods=["GET"])
    def metrics():
        REQUEST_COUNT.inc()
        data = generate_latest()
        return Response(data, mimetype=CONTENT_TYPE_LATEST)

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify(status="ok"), 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
