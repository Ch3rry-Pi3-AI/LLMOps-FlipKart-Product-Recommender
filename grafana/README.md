# 📈 **Grafana — Metrics Visualisation**

This folder contains the **Grafana deployment configuration** used to visualise system and application metrics collected by **Prometheus**.
Grafana provides real-time dashboards for tracking the performance and reliability of the **LLMOps Flipkart Product Recommender System**.



## 🗂️ **Folder Contents**

```text
grafana/
└── grafana-deployment.yaml    # 🚀 Deployment + Service manifest
```



## ⚙️ **Overview**

### **`grafana-deployment.yaml`**

Deploys **Grafana** within the `monitoring` namespace and exposes it via a **NodePort (32000)** for browser access.
Once deployed, Grafana can be configured to connect to the **Prometheus Service** (`prometheus-service:9090`) as a data source.



## 🧩 **Integration Summary**

* Visualises metrics scraped by **Prometheus**, including:

  * Request counts and latency from the Flask API
  * Resource utilisation metrics (CPU, memory, etc.)
  * Application health and response time trends
* Enables creation of custom dashboards for tracking performance of the **RAG pipeline** and recommendation workflows.



### ✅ **In Summary**

Grafana provides the **observability interface** for the monitoring layer:

* Connects to Prometheus as a data source.
* Offers rich dashboards for tracking backend performance.
* Completes the **Prometheus–Grafana monitoring stack** for the project’s production environment.
