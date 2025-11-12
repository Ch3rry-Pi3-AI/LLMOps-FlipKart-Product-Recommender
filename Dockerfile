# ---------------------------------------------------------------------
# 🐍 LLMOps Flipkart Product Recommender — Dockerfile
# ---------------------------------------------------------------------
# This Dockerfile builds a lightweight Python 3.12 container
# for running the Flipkart Product Recommender backend.
# It installs dependencies, sets up the working environment,
# and launches the application entry point.
# ---------------------------------------------------------------------

# --------------------------------------------------------------
# 🧩 Base Image
# --------------------------------------------------------------
# Use the official slim variant of Python 3.12 for a lightweight image
FROM python:3.12-slim

# --------------------------------------------------------------
# ⚙️ Environment Variables
# --------------------------------------------------------------
# PYTHONDONTWRITEBYTECODE : prevents Python from writing .pyc files
# PYTHONUNBUFFERED        : ensures real-time output logging to console
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# --------------------------------------------------------------
# 📂 Working Directory
# --------------------------------------------------------------
# All subsequent commands will run inside the /app directory
WORKDIR /app

# --------------------------------------------------------------
# 🧱 System Dependencies
# --------------------------------------------------------------
# Install essential build tools and cURL for network operations,
# then clean up package lists to reduce image size
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# --------------------------------------------------------------
# 📦 Copy Project Files
# --------------------------------------------------------------
# Copy all local project files into the container's /app directory
COPY . .

# --------------------------------------------------------------
# 🔧 Install Python Dependencies
# --------------------------------------------------------------
# Use pip in editable mode (-e) to install dependencies defined in setup.py
RUN pip install --no-cache-dir -e .

# --------------------------------------------------------------
# 🚪 Expose Application Port
# --------------------------------------------------------------
# The Flask or API application listens on port 5000
EXPOSE 5000

# --------------------------------------------------------------
# 🚀 Run Application
# --------------------------------------------------------------
# Launch the main application file when the container starts
CMD ["python", "app.py"]
