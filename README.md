# 🧩 **RAG Chain Construction — LLMOps Flipkart Product Recommender System**

This stage introduces the **Retrieval-Augmented Generation (RAG)** pipeline for the **LLMOps Flipkart Product Recommender System**.
It builds upon the previously completed data ingestion layer by integrating a **Groq-powered conversational model** with the **AstraDB vector store**, enabling **context-aware product reasoning and dialogue continuity**.

The newly added module — `rag_chain.py` — defines a history-aware RAG chain capable of retrieving relevant product reviews and generating **concise, grounded responses** based on prior user interactions.


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
│   └── rag_chain.py             # 🧩 Builds history-aware RAG chain (new)
├── grafana/
├── prometheus/
├── static/
├── templates/
├── utils/
│   ├── __init__.py
│   ├── custom_exception.py
│   └── logger.py
├── main.py
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
└── README.md
```

## ⚙️ **Overview of the RAG Chain Component**

### **`flipkart/rag_chain.py`**

This module defines the **`RAGChainBuilder`** class — a composable, history-aware RAG pipeline built using **LangChain Core Runnable Expressions (LCEL)**.
It tightly integrates the previously established AstraDB vector store with a **Groq chat model**, allowing for conversational product queries that reference relevant reviews and maintain session memory.

The RAG chain performs three key functions:

1. **Question Rewriting** – reformulates user queries using chat history for better retrieval context.
2. **Context Retrieval** – fetches the most relevant product reviews from AstraDB.
3. **Grounded Response Generation** – produces concise, contextually accurate answers using Groq’s LLM.

## 🧩 **Example Usage**

```python
from flipkart.data_ingestion import DataIngestor
from flipkart.rag_chain import RAGChainBuilder

# Step 1: Load or create the AstraDB vector store
vstore = DataIngestor().ingest(load_existing=True)

# Step 2: Build the RAG chain
rag_builder = RAGChainBuilder(vstore)
rag_chain = rag_builder.build_chain()

# Step 3: Invoke the RAG chain with session tracking
response = rag_chain.invoke(
    {"input": "Which phone has the best battery life?", "chat_history": []},
    config={"configurable": {"session_id": "user123"}}
)

print(response)
```

### Example Output

```
Based on customer reviews, the XYZ Pro Max is praised for its long-lasting battery life,
often lasting more than a day under heavy use.
```

## ✅ **In Summary**

This stage completes the **intelligent reasoning layer** of the Flipkart Product Recommender:

* Introduces `rag_chain.py` — a **Groq-integrated RAG pipeline** with conversational memory.
* Connects to the **AstraDB vector store** for context retrieval.
* Implements **question rewriting**, **retrieval**, and **response generation** within a unified LCEL framework.
* Enables **context-aware, human-like product interactions**.

The **RAG chain construction stage** now bridges your data and model layers, paving the way for the **interactive recommendation interface** in the next phase.
