# `flipkart/` README — Core Backend Logic

This folder contains the **core backend logic** for the **LLMOps Flipkart Product Recommender System**.
It handles configuration, data processing, ingestion, and the construction of the **Retrieval-Augmented Generation (RAG)** chain — forming the foundation of the system’s intelligent recommendation and reasoning pipeline.



## 📁 Folder Overview

```text
flipkart/
├── __init__.py
├── config.py          # ⚙️  Centralised configuration for environment and models
├── data_converter.py  # 🔄  Converts Flipkart CSV reviews into LangChain Documents
├── data_ingestion.py  # 🧠  Builds AstraDB vector store and ingests review documents
└── rag_chain.py       # 🧩  Constructs history-aware RAG chain with Groq + AstraDB
```



## ⚙️ **Module Descriptions**

### **`config.py`**

Loads environment variables from the `.env` file and defines all key configuration values — including AstraDB credentials, Groq API keys, and model identifiers for embedding and generation.
This ensures all services (AstraDB, Hugging Face, Groq) remain securely and consistently accessible across the project.



### **`data_converter.py`**

Reads the Flipkart product review CSV file and converts each row into a **LangChain `Document`**.
Each document contains:

* **`page_content`** — the product review text
* **`metadata`** — the corresponding product title

This conversion step ensures uniform text objects suitable for embedding and vector search.



### **`data_ingestion.py`**

Initialises a **Hugging Face embedding model** and an **AstraDB Vector Store**.
It can:

* Return an existing AstraDB collection if available
* Or ingest all Flipkart reviews as new embedded documents for retrieval

This forms the persistent vector layer that powers semantic product recommendation.



### **`rag_chain.py`**

Builds a **history-aware Retrieval-Augmented Generation (RAG)** chain using **LangChain Core Runnable Expressions (LCEL)**.
It integrates:

* **Groq Chat Models** — for fast, contextually grounded responses
* **AstraDB Vector Store** — as a retriever for relevant product context
* **Message History** — to enable memory and conversational continuity

The `RAGChainBuilder` class rewrites user queries based on chat history, retrieves relevant review context, and generates accurate, concise responses.



## 🧠 **In Summary**

Together, these modules form the **core intelligence layer** of the LLMOps Flipkart Product Recommender:

* `config.py` — manages environment and model configuration.
* `data_converter.py` — transforms raw CSV data into structured documents.
* `data_ingestion.py` — builds and populates the AstraDB vector database.
* `rag_chain.py` — orchestrates retrieval-augmented reasoning using Groq and LangChain.

This backend foundation enables the next stages of the project — including **query handling**, **recommendation generation**, and **frontend integration** for an end-to-end intelligent product recommender system.
