# `flipkart/` README — Core Backend Logic

This folder contains the **core source code** for the **Flipkart Product Recommender System**.
It handles configuration, data preparation, and ingestion into a **vector database**, forming the foundation for downstream **retrieval-augmented generation (RAG)** and recommendation workflows.

## 📁 Folder Overview

```text
flipkart/
├── config.py         # ⚙️  Centralised configuration for environment and models
├── data_converter.py # 🔄  Converts Flipkart CSV reviews into LangChain Documents
└── data_ingestion.py # 🧠  Builds AstraDB vector store and ingests review documents
```

## ⚙️ Description

* **`config.py`**
  Loads environment variables from the `.env` file and defines key constants for the project, including AstraDB connection details, Groq API credentials, and model identifiers for embeddings and RAG generation.

* **`data_converter.py`**
  Reads the Flipkart product review CSV, validates essential columns, and converts each row into a **LangChain `Document`**. Each document stores the review text as content and the corresponding product title as metadata.

* **`data_ingestion.py`**
  Initialises a **Hugging Face embedding model** and connects to an **AstraDB Vector Store**.
  It can either return an existing collection or ingest all Flipkart review documents into the database, ready for efficient semantic retrieval.

Together, these modules form the **data and configuration backbone** of the Flipkart Product Recommender, enabling:

* Seamless integration between environment configuration and model settings
* Clean transformation of raw review data into structured, searchable documents
* Persistent vector storage for high-performance retrieval and reasoning
