# 🚀 **Kubernetes Deployment — LLMOps Flipkart Product Recommender**

In this stage, we deploy the **LLMOps Flipkart Product Recommender** onto a **Kubernetes cluster** running on our **Minikube setup within a GCP VM**.
This stage brings the entire project to life — containerising the application and serving it publicly via Kubernetes services.

## 🧭 **Step 1 — Connect Docker to Minikube**

In your VM terminal, run the following command:

```bash
eval $(minikube docker-env)
```

This command ensures Docker points to Minikube’s internal environment so that your image builds directly inside Minikube’s Docker daemon.

Now, build your Docker image:

```bash
docker build -t flask-app:latest .
```

This may take a few minutes to complete, as it will install all dependencies and package your Streamlit app into a container.

Once complete, verify that your image was successfully built:

```bash
docker images
```

You should see output similar to:

```
IMAGE                                             ID             DISK USAGE   
gcr.io/k8s-minikube/storage-provisioner:v5        6e38f40d628d       31.5MB      
flask-app:latest                                  bd292243bb00        964MB      
registry.k8s.io/coredns/coredns:v1.12.1           52546a367cc9         75MB      
registry.k8s.io/etcd:3.6.4-0                      5f1f5298c888        195MB      
registry.k8s.io/kube-apiserver:v1.34.0            90550c43ad2b         88MB      
registry.k8s.io/kube-controller-manager:v1.34.0   a0af72f2ec6d       74.9MB      
registry.k8s.io/kube-proxy:v1.34.0                df0860106674       71.9MB      
registry.k8s.io/kube-scheduler:v1.34.0            46169d968e92       52.8MB      
registry.k8s.io/pause:3.10.1                      cd073f4c5f6a        736kB 
```

Your `flask-app:latest` image is now built and ready to deploy.

## 🔐 **Step 2 — Inject Secrets into Kubernetes**

Next, we need to securely inject your **Groq** and **Hugging Face API keys** into the Kubernetes environment.

Run the following command:

```bash
kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY="" \
  --from-literal=ASTRA_DB_APPLICATION_TOKEN="" \
  --from-literal=ASTRA_DB_KEYSPACE="default_keyspace" \
  --from-literal=ASTRA_DB_API_ENDPOINT="" \
  --from-literal=HF_TOKEN="" \
  --from-literal=HUGGINGFACEHUB_API_TOKEN=""
```

Make sure to replace the empty quotation marks `""` with your actual API keys.

You should see confirmation:

```
secret/llmops-secrets created
```

## 🧩 **Step 3 — Deploy the Application**

Now apply your Kubernetes deployment and service configuration:

```bash
kubectl apply -f flask-deployment.yaml
```

Expected output:

```
deployment.apps/flask-app created
service/flask-service created
```

You can verify the pods are running with:

```bash
kubectl get pods
```

Example output:

```
NAME                         READY   STATUS    RESTARTS   AGE
flask-app-58b5995844-66kth   1/1     Running   0          32s
```

This confirms that your container is up and running successfully inside the cluster.

## 💻 **Step 4 — Forward Ports and Access the App**

In your terminal, run:

```bash
kubectl port-forward svc/llmops-service 5000:80 --address 0.0.0.0
```

This forwards external traffic from port **5000** to your Flask app inside Kubernetes.

Keep this terminal open while your application is running.

Now, return to your **GCP Console → VM Instances** page, find your **External IP address**, and click **Copy**.
In your browser, visit:

```
http://<YOUR_EXTERNAL_IP>:5000
```

For example:

```
http://136.114.199.97:5000
```

*(Note: do not use `https://` — it may cause connection issues in some environments.)*

If everything is configured correctly, your **LLMOps Flipkart Product Recommender** web app will load in your browser and be fully interactive!

## ✅ **In Summary**

You have now successfully:

* Built and containerised your application using **Docker**.
* Deployed it on **Kubernetes** via **Minikube**.
* Injected API secrets into the cluster securely.
* Exposed the service externally using **port forwarding**.

Your **LLMOps Flipkart Product Recommender** is now live and running inside a fully functional Kubernetes environment on **Google Cloud Platform** — completing your end-to-end cloud deployment.