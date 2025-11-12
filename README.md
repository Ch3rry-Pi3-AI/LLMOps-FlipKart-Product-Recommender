# 🔗 **GitHub Integration and Firewall Configuration — LLMOps Flipkart Product Recommender**

In this stage, we connect the **LLMOps Flipkart Product Recommender** GitHub repository to the **Google Cloud Platform (GCP) Virtual Machine**, allowing direct version control operations from the VM.
We also configure a **firewall rule** to ensure the VM can communicate securely with GitHub and external services.

## 🧭 **Step 1 — Clone the GitHub Repository**

Go to your project’s GitHub repository.
Click the green **“<> Code”** dropdown and copy the **HTTPS URL** of the repository.

Example:

```
https://github.com/Ch3rry-Pi3-AI/LLMOps-Anime-Recommender-System.git
```

Now, in your GCP VM terminal, run:

```bash
git clone https://github.com/Ch3rry-Pi3-AI/LLMOps-Anime-Recommender-System.git
```

(Replace this URL with your own repository link.)

Next, navigate into the cloned directory:

```bash
cd LLMOps-Anime-Recommender-System
```

You are now inside your project folder within the VM.

## ⚙️ **Step 2 — Configure Git Identity**

Set up your Git global configuration so commits made from the VM are correctly attributed to you.

```bash
git config --global user.email "the_rfc@hotmai.co.uk"
git config --global user.name "Roger J. Campbell"
```

Verify the configuration with:

```bash
git config --list
```

You should see your email and username listed.

## 🔑 **Step 3 — Generate a GitHub Personal Access Token**

1. Go to your **GitHub Profile → Settings**.
2. Scroll down to **Developer Settings**.
3. Under **Personal access tokens**, click **Tokens (classic)**.
4. Select **Generate new token → Generate new token (classic)**.
5. For the **Note**, enter something like `anime-recommend`.
6. Under **Scopes**, select the following options:

   * `repo`
   * `workflow`
   * `admin:org`
   * `admin:repo_hook`
   * `admin:org_hook`
7. Click **Generate token**.

Make sure to **copy the token immediately** — GitHub will not show it again.

## 🚀 **Step 4 — Authenticate and Pull from GitHub**

Now that your token is ready, you can pull from the GitHub repository to your VM.

```bash
git pull origin main
```

When prompted:

* **Username:** your GitHub username
* **Password:** your newly generated **personal access token**

Once authenticated, the push will complete successfully.

## 🔥 **Step 5 — Create a GCP Firewall Rule**

Next, configure a firewall rule in GCP to ensure your VM can communicate with GitHub and other services.

1. In the **Google Cloud Console**, navigate to the **Network Security** service.
2. Under **Cloud NGFW**, click **Firewall rule → + Create firewall policy**.
3. Set the **Policy name** to:

```
allow-llmops
```

4. Configure the remaining fields as follows:

| Field                   | Setting                      |
| ----------------------- | ---------------------------- |
| **Targets**             | All instances in the network |
| **Source IPv4 ranges**  | `0.0.0.0/0`                  |
| **Protocols and ports** | Allow all                    |

5. Click **Create**.

Your firewall policy is now active and allows full communication between your VM, GitHub, and related deployment services.

## ✅ **In Summary**

You have now successfully:

* Cloned your **GitHub repository** into the **GCP VM**.
* Configured your Git identity for authenticated pushes.
* Created a **personal access token** for secure GitHub access.
* Set up a **GCP firewall rule** to allow outgoing and incoming connections.

Your VM is now fully connected to GitHub and ready for CI/CD integration and future Kubernetes deployments.