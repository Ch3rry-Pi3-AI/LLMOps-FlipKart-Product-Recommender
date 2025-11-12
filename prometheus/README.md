# 📊 **Prometheus — Monitoring Configuration**

This folder contains the **Prometheus configuration and deployment files** used to monitor the **LLMOps Flipkart Product Recommender System**.
Prometheus continuously collects application metrics (such as request counts, response times, and system health) from the Flask backend and exposes them for visualisation in **Grafana**.



## 🗂️ **Folder Contents**

```text
prometheus/
├── prometheus-configmap.yaml     # ⚙️ Prometheus scrape configuration
└── prometheus-deployment.yaml    # 🚀 Deployment + Service manifest
```



## ⚙️ **Overview**

### **`prometheus-configmap.yaml`**

Defines the **Prometheus configuration file (`prometheus.yml`)**, including:

* Global scrape interval (set to 15 seconds)
* Targets for:

  * Prometheus itself (`localhost:9090`)
  * The Flask app’s `/metrics` endpoint

### **`prometheus-deployment.yaml`**

Deploys Prometheus within the `monitoring` namespace.
It mounts the configuration from the ConfigMap and exposes Prometheus externally via a **NodePort (32001)** for dashboard or API access.



## 🧩 **Integration Summary**

* Collects runtime and application-level metrics from the **Flask app**.
* Runs alongside **Grafana** (in the same `monitoring` namespace) for visual dashboards.
* Supports observability for the full LLMOps pipeline, including API health and latency tracking.



### ✅ **In Summary**

Prometheus forms the **metrics backbone** of the monitoring setup:

* Periodically scrapes the Flask app’s `/metrics` endpoint.
* Stores time-series data for analysis and alerting.
* Provides data for Grafana dashboards used in the next monitoring stage.
