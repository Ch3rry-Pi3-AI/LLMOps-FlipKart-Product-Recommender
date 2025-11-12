# 🐳 **Containerisation and Kubernetes Deployment — LLMOps Flipkart Product Recommender System**

This stage packages the **Flask-based RAG application** of the **LLMOps Flipkart Product Recommender System** into a **Docker container** and deploys it on a **Kubernetes cluster**.

By containerising the application, this stage ensures **portability, reproducibility, and scalability** across environments.
The Kubernetes manifest then defines how the container is deployed, networked, and monitored within the cluster — forming the foundation of a production-ready **MLOps deployment pipeline**.

<p align="center">
  <img src="img/flask/flask_app.gif" alt="Deployed Flask Application Overview" style="width:100%; height:auto;">
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
├── prometheus/
├── img/
│   └── flask/
│       └── flask_app.gif
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── utils/
│   ├── __init__.py
│   ├── custom_exception.py
│   └── logger.py
├── app.py
├── Dockerfile                      # 🐳 Defines container image for Flask RAG application
├── flask-deployment.yaml           # ☸️ Kubernetes manifest for cluster deployment
├── main.py
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
└── README.md
```

## ⚙️ **Overview of the Containerisation and Deployment Layer**

### **`Dockerfile`**

The `Dockerfile` defines the **container image** for the Flask application.
It ensures a clean, reproducible environment with all dependencies, environment variables, and entrypoints configured.

Key steps include:

1. **Base Image**
   Uses an official lightweight Python base (e.g., `python:3.12-slim`) for a minimal runtime footprint.
2. **Dependency Installation**
   Copies `requirements.txt` and installs dependencies in a virtual environment.
3. **Environment Setup**
   Copies application files, loads environment variables, and sets working directory to `/app`.
4. **Port Exposure**
   Exposes port `5000`, matching the Flask service port.
5. **Startup Command**
   Launches the application via:

   ```dockerfile
   CMD ["python", "app.py"]
   ```

This container image can be built locally or in CI/CD pipelines and pushed to a registry such as **Google Artifact Registry**, **Docker Hub**, or **GitHub Packages** for deployment.

### **`flask-deployment.yaml`**

This manifest defines the **Kubernetes resources** required to deploy the Flask container in a cluster.

It automates the deployment, scaling, and service exposure of the RAG-powered chatbot.

Key sections:

* **Deployment**

  * Creates and manages Pods running the Flask container.
  * Specifies the container image and tag (e.g., `flask-llmops:latest`).
  * Defines resource requests and limits for stable operation.
  * Uses multiple replicas for high availability.
* **Service**

  * Exposes the Flask Pods internally or externally depending on the chosen type:

    ```yaml
    type: LoadBalancer
    ports:
      - port: 80
        targetPort: 5000
    ```
  * Routes incoming traffic to the Flask app.
* **Labels and Selectors**

  * Labels Pods with `app: llmops-flipkart-flask` for easy monitoring and routing.
* **Health Probes (Optional)**

  * Liveness and readiness probes hit `/health` to ensure Pods are running properly before serving traffic.

Together, the Deployment and Service definitions automate the process of rolling out updates, ensuring uptime, and providing cluster-level observability.

## ✅ **In Summary**

This stage delivers the **containerisation and orchestration layer** of the Flipkart Product Recommender System:

* Introduces `Dockerfile` — a **reproducible container image definition** for the Flask-based RAG application
* Adds `flask-deployment.yaml` — a **Kubernetes manifest** for scalable deployment and load-balanced access
* Supports **Prometheus metrics integration** for cluster monitoring
* Enables **rapid deployment** to both local and cloud Kubernetes environments
* Establishes the foundation for **CI/CD automation and cloud-native scaling**

The **containerisation and Kubernetes deployment stage** marks the transition from development to **operational MLOps infrastructure**, enabling scalable, monitored, and portable deployments of your intelligent recommender system.
