# 📈 **Monitoring and Observability — LLMOps Flipkart Product Recommender System**

This stage introduces the **monitoring and observability layer** for the **LLMOps Flipkart Product Recommender System** using **Prometheus** and **Grafana**.
With these integrations, the deployed application gains **real-time metrics tracking, performance visibility, and system health monitoring** across the Kubernetes cluster.

Prometheus collects metrics from the **Flask RAG backend**, while Grafana provides interactive dashboards to visualise performance trends, latency, and throughput — completing the project’s **MLOps observability stack**.

<p align="center">
  <img src="img/monitoring/monitoring_dashboard.gif" alt="Prometheus and Grafana Monitoring Dashboard" style="width:100%; height:auto;">
</p>



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
│   └── grafana-deployment.yaml          # 📊 Deploys Grafana dashboard service (new)
├── prometheus/
│   ├── prometheus-configmap.yaml        # ⚙️ Prometheus scrape configuration (new)
│   └── prometheus-deployment.yaml       # 🚀 Prometheus Deployment + Service (new)
├── img/
│   ├── flask/
│   │   └── flask_app.gif
│   └── monitoring/
│       └── monitoring_dashboard.gif
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── utils/
│   ├── __init__.py
│   ├── custom_exception.py
│   └── logger.py
├── app.py
├── Dockerfile
├── flask-deployment.yaml
├── main.py
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
└── README.md
```



## ⚙️ **Overview of the Monitoring Components**

### **1. `prometheus/prometheus-configmap.yaml`**

Defines the Prometheus configuration file (`prometheus.yml`) containing:

* Global scrape interval of **15 seconds**
* Targets for:

  * **Prometheus itself** (`localhost:9090`)
  * **Flask app metrics** (`/metrics` endpoint on port `5000`)

This enables continuous metrics collection from the deployed RAG application.



### **2. `prometheus/prometheus-deployment.yaml`**

Deploys Prometheus within the **`monitoring` namespace**, using the ConfigMap above.
It mounts the configuration file into the Prometheus container and exposes the service via **NodePort `32001`** for external access.

This setup allows Prometheus to:

* Scrape metrics from the Flask backend
* Store time-series performance data
* Provide a data source for Grafana visualisation



### **3. `grafana/grafana-deployment.yaml`**

Deploys **Grafana** in the `monitoring` namespace and exposes it on **NodePort `32000`**.
Grafana connects to Prometheus (`prometheus-service:9090`) as its data source, offering interactive dashboards for:

* Application performance (response time, requests per second)
* Resource utilisation
* Error tracking and uptime monitoring



## 🧩 **Example Usage**

### **Step 1 — Create the Monitoring Namespace**

```bash
kubectl create ns monitoring
```

### **Step 2 — Deploy Prometheus**

```bash
kubectl apply -f prometheus/prometheus-configmap.yaml
kubectl apply -f prometheus/prometheus-deployment.yaml
```

### **Step 3 — Deploy Grafana**

```bash
kubectl apply -f grafana/grafana-deployment.yaml
```

### **Step 4 — Access Dashboards**

* **Prometheus:** `http://<node-ip>:32001`
* **Grafana:** `http://<node-ip>:32000` (default login: `admin / admin`)



## ✅ **In Summary**

This stage introduces the **monitoring and observability layer** for the Flipkart Product Recommender System:

* Adds `prometheus-configmap.yaml` and `prometheus-deployment.yaml` — to **collect and store metrics** from the Flask backend.
* Adds `grafana-deployment.yaml` — to **visualise metrics and performance dashboards**.
* Establishes a **monitoring namespace** in Kubernetes for Prometheus and Grafana.
* Enables continuous visibility into system health, latency, and performance across the cluster.

With this stage complete, the project now includes **end-to-end monitoring**, transforming it into a **fully observable, production-grade MLOps system**.
