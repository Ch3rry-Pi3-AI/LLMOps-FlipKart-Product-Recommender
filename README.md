# 🌐 **Flask Application Deployment — LLMOps Flipkart Product Recommender System**

This stage transforms the **RAG reasoning pipeline** of the **LLMOps Flipkart Product Recommender System** into an **interactive web application** using **Flask**.

It introduces a lightweight **front-end chat interface** that allows users to engage with the model conversationally, sending product-related queries and receiving grounded recommendations through the RAG pipeline.

The Flask layer wraps the existing backend components — `DataIngestor` and `RAGChainBuilder` — and exposes them via simple HTTP endpoints.
In addition, it integrates **Prometheus metrics** for observability, enabling fine-grained tracking of user requests and RAG activity.

<p align="center"> <img src="img/flask/flask_app.gif" alt="Flask Chat Application Demo" style="width:100%; height:auto;"> </p>

## 🗂️ **Project Structure (Updated)**

```text
llmops-flipkart-product-recommender/
├── .env
├── .gitignore
├── .python-version
├── data/
│   └── flipkart_product_review.csv
├── flipkart/
│   ├── __init__.py
│   ├── config.py
│   ├── data_converter.py
│   ├── data_ingestion.py
│   └── rag_chain.py
├── grafana/
├── prometheus/
├── static/
│   └── style.css                 # 🎨 Defines dark, frosted-glass chat styling and layout
├── templates/
│   └── index.html                # 💬 Front-end chatbot UI rendered by Flask
├── utils/
│   ├── __init__.py
│   ├── custom_exception.py
│   └── logger.py
├── app.py                        # 🚀 Flask app exposing RAG endpoint and Prometheus metrics
├── main.py
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
└── README.md
```



## ⚙️ **Overview of the Flask Application Layer**

### **`app.py`**

This script serves as the **entry point** for the web application.
It creates and configures a Flask server that connects the RAG backend to an interactive front-end interface.

Key components:

* **Flask routes**

  * `/` – renders the chatbot interface (`index.html`)
  * `/get` – handles POST requests from the chat UI, invokes the RAG chain, and returns model responses
  * `/metrics` – exposes Prometheus metrics for monitoring request volume and system activity
  * `/health` – returns a simple JSON health check
* **Integration with RAG Chain**
  The app initialises `DataIngestor` and `RAGChainBuilder` once on startup for efficient, low-latency inference.
* **Prometheus Counters**
  Tracks both total HTTP requests and RAG-specific queries in real time.



### **`templates/index.html`**

This file defines the **chat interface** for user interaction.
It combines Bootstrap, Font Awesome, and jQuery to provide a dynamic, responsive user experience.

Features:

* A **dark-themed chat window** with frosted-glass transparency
* Smooth **auto-scroll** to the latest message
* Live **AJAX-based message exchange** with the Flask backend
* Integrated timestamps for both user and model messages

The front-end connects to `/get` via AJAX, passing the user’s query and displaying the model’s response without reloading the page.



### **`static/style.css`**

This stylesheet provides the **visual foundation** of the chatbot interface.

Highlights:

* Implements a **modern, dark UI** with blurred-glass panels
* Styles message bubbles for user and model exchanges
* Customises scrollbars, timestamps, and message layout
* Ensures full responsiveness across devices

The CSS complements the Bootstrap structure in `index.html`, keeping design logic separate from layout.



## 🧩 **How It All Fits Together**

1. The user enters a query into the chatbox on the `/` page.
2. The front-end script sends this query via AJAX to the Flask `/get` endpoint.
3. The backend processes the query using the RAG chain (`rag_chain.py`) and retrieves relevant product reviews.
4. The model generates a **contextually grounded** answer, which is returned to the browser and displayed instantly.
5. Each interaction increments the Prometheus counters, which can be visualised in Grafana dashboards.



## 💬 **Example Interaction**

**User:**

> Which laptop has the best battery life for travel?

**Model Response:**

> Based on customer reviews, the Lenovo ThinkBook X1 Carbon offers excellent battery life, often lasting 14–16 hours on moderate use.



## ✅ **In Summary**

This stage delivers the **interactive application layer** of the Flipkart Product Recommender System:

* Introduces `app.py` — a **Flask-powered RAG API and chat interface**
* Adds `index.html` — a **responsive, dark-themed chatbot front-end**
* Includes `style.css` — a **dedicated stylesheet** defining layout and visual polish
* Integrates **Prometheus metrics** for system observability
* Enables **real-time, conversational product recommendations** through the browser

The **Flask application stage** transforms the backend intelligence into a **user-accessible, monitored web experience**, completing the operational front-end of your LLMOps pipeline.
