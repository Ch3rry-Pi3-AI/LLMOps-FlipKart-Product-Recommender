# 🛒 **LLMOps Flipkart Product Recommender System — Project Overview**

This repository presents a **complete end-to-end LLMOps pipeline** for a **Flipkart Product Recommender System**, integrating **retrieval-augmented generation (RAG)**, **Flask-based web deployment**, **containerisation**, and **Kubernetes-based orchestration and monitoring** using **Prometheus** and **Grafana**.

The system allows users to query the model for product recommendations while tracking performance and metrics in real time — demonstrating how **LLMOps practices** can take an **LLM-powered application** from local prototype to full-scale **cloud-deployed microservice**.

<p align="center">
  <img src="img/flask/flask_app.gif" alt="Flask App Overview" width="100%">
</p>

## 🧩 **Grouped Stages**

|     #     | Stage                                       | Description                                                                                                                                         |
| :-------: | :------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
|   **00**  | **Project Setup**                           | Created the base folder structure, configured environment files, and established Python environment management using `uv`.                          |
| **01–02** | **Core RAG Logic**                          | Implemented the RAG pipeline, including data ingestion, vector conversion, and Groq-powered language model integration.                             |
|   **03**  | **Flask Application**                       | Built the user-facing Flask web application with HTML/CSS front end for interactive recommendation queries.                                         |
|   **04**  | **Containerisation & Deployment Files**     | Authored the Dockerfile and Kubernetes deployment manifest (`flask-deployment.yaml`) for containerised application rollout.                         |
|   **05**  | **Monitoring Setup (Prometheus & Grafana)** | Defined manifests to deploy Prometheus and Grafana services within the Kubernetes cluster for performance and health monitoring.                    |
| **06–08** | **Cloud & Cluster Configuration**           | Set up GCP Virtual Machine, installed Docker Engine, Minikube, and kubectl; configured GitHub linking and Firewall permissions for external access. |
| **09–10** | **Kubernetes Deployment & Monitoring**      | Deployed the Flask containerised app to Kubernetes and integrated live monitoring via Prometheus and Grafana dashboards.                            |



## 🗂️ **Project Structure**

```text
llmops-flipkart-product-recommender/
├── .env                                 # 🔐 Environment variables (API keys for Groq, Hugging Face, AstraDB)
├── .gitignore                           # 🚫 Ignored files and directories for Git
├── .python-version                      # 🐍 Specifies Python version for consistent environments
│
├── data/
│   └── flipkart_product_review.csv      # 🧾 Raw product review dataset used for embedding generation
│
├── flipkart/
│   ├── __init__.py                      # 🧩 Marks the directory as a Python package
│   ├── config.py                        # ⚙️ Central configuration file for environment variables and constants
│   ├── data_converter.py                # 🔄 Converts review data into suitable text chunks for embedding
│   ├── data_ingestion.py                # 📥 Handles data loading and pre-processing for the RAG pipeline
│   └── rag_chain.py                     # 🧠 Builds and executes the Retrieval-Augmented Generation chain
│
├── grafana/
│   └── grafana-deployment.yaml          # 📊 Deploys Grafana dashboard service within the monitoring namespace
│
├── prometheus/
│   ├── prometheus-configmap.yaml        # ⚙️ Prometheus configuration defining scrape targets (Flask, internal metrics)
│   └── prometheus-deployment.yaml       # 🚀 Prometheus Deployment and Service manifests
│
├── img/
│   ├── flask/
│   │   └── flask_app.gif                # 🎬 Animated demo of Flask application
│   └── monitoring/
│       └── monitoring_dashboard.gif     # 📈 GIF showing live monitoring dashboards (Prometheus & Grafana)
│
├── static/
│   └── style.css                        # 🎨 Stylesheet for the Flask front end
│
├── templates/
│   └── index.html                       # 🧱 HTML layout template for the Flask web app
│
├── utils/
│   ├── __init__.py                      # 📦 Package initializer
│   ├── custom_exception.py              # ❗ Custom exception handling logic
│   └── logger.py                        # 🪵 Logging utilities for application tracking
│
├── app.py                               # 🌐 Flask entry point — connects UI to the RAG pipeline backend
├── Dockerfile                           # 🐳 Builds container image for the Flask app
├── flask-deployment.yaml                # ⚓ Kubernetes Deployment + Service manifest for Flask application
│
├── main.py                              # 🚀 Entry script for initialising and running the RAG pipeline
├── pyproject.toml                       # 🧰 Project configuration and dependency metadata
├── requirements.txt                     # 📦 Python dependencies list
├── setup.py                             # 🔧 Package setup configuration
├── uv.lock                              # 🔒 Locked dependency versions (ensures reproducibility)
└── README.md                            # 📘 Project documentation
```



## 🚀 **Summary**

The **LLMOps Flipkart Product Recommender System** demonstrates how to operationalise a **retrieval-augmented recommendation pipeline** within an **MLOps/LLMOps framework**.
It connects every layer — from **data ingestion and model inference** to **observability and orchestration** — using tools like **Docker**, **Kubernetes**, **Prometheus**, and **Grafana**.

<p align="center">
  <img src="img/monitoring/monitoring_dashboard.gif" alt="Monitoring Dashboard Overview" width="100%">
</p>

This project serves as a **blueprint for deploying LLM-powered recommendation systems** in a **scalable, cloud-native** manner — merging **intelligent retrieval**, **application interactivity**, and **real-time monitoring** into a single cohesive production pipeline.
