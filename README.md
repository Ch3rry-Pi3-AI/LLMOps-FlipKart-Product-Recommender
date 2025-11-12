# ☸️ **Minikube and kubectl Setup — LLMOps Flipkart Product Recommender**

In this stage, we install and configure **Minikube** and **kubectl** on our **Google Cloud Platform (GCP) Virtual Machine**.
These tools allow us to create and manage a **local Kubernetes cluster** within the VM, which will later be used to deploy and orchestrate the **LLMOps Flipkart Product Recommender**.

## 🧭 **Step 1 — Install Minikube**

Go to the official Minikube documentation:
👉 [https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)

Select **Linux** as the operating system, then copy and paste the first installation command into your VM terminal:

```bash
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
```

You should see output similar to this:

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  133M  100  133M    0     0   132M      0  0:00:01  0:00:01 --:--:--  132M
```

Now install Minikube and remove the downloaded file:

```bash
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```

Once installed, start your Minikube cluster:

```bash
minikube start
```

You should see output similar to the following:

```
😄  minikube v1.37.0 on Ubuntu 24.04 (amd64)
✨  Automatically selected the docker driver. Other choices: none, ssh
📌  Using Docker driver with root privileges
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.48 ...
💾  Downloading Kubernetes v1.34.0 preload ...
    > preloaded-images-k8s-v18-v1...:  337.07 MiB / 337.07 MiB  100.00% 212.84 
    > gcr.io/k8s-minikube/kicbase...:  488.51 MiB / 488.52 MiB  100.00% 108.37 
🔥  Creating docker container (CPUs=2, Memory=3900MB) ...
🐳  Preparing Kubernetes v1.34.0 on Docker 28.4.0 ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
💡  kubectl not found. If you need it, try: 'minikube kubectl -- get pods -A'
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

This confirms that your Minikube cluster has been created and is running successfully.

## ⚙️ **Step 2 — Install kubectl**

Now we will install **kubectl**, the command-line tool used to manage Kubernetes clusters.

Go to the official Kubernetes documentation:
👉 [https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

Scroll down to **“1. Install kubectl binary with curl on Linux”** and copy the following command:

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```

You should see output similar to:

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   138  100   138    0     0   2486      0 --:--:-- --:--:-- --:--:--  2509
100 57.7M  100 57.7M    0     0   115M      0 --:--:-- --:--:-- --:--:--  115M
```

Next, scroll further down to the **“Install using other package management”** section.
Ensure **“Snap”** is selected, then copy and paste the following commands into your terminal:

```bash
sudo snap install kubectl --classic
kubectl version --client
```

You should see output confirming the installation:

```
kubectl 1.34.1 from Canonical✓ installed
Client Version: v1.34.1
Kustomize Version: v5.7.1
```

Your **kubectl** installation is now complete and configured to work with the **Minikube** cluster.

## ✅ **In Summary**

You have now successfully:

* Installed **Minikube** and started a local Kubernetes cluster.
* Installed **kubectl** and verified connectivity to the cluster.

Your GCP VM is now fully configured with **Docker**, **Minikube**, and **kubectl**, enabling you to deploy and manage the **LLMOps Flipkart Product Recommender** in a Kubernetes environment.