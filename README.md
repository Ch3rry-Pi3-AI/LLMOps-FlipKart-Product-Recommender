# 🧩 **Data Loading Stage — LLMOps Flipkart Product Recommender System**

This stage establishes the **data ingestion and preparation layer** for the **LLMOps Flipkart Product Recommender System**.
It introduces the foundational modules that load, process, and embed Flipkart product reviews into an **AstraDB vector store**, preparing the data for downstream retrieval and recommendation tasks.

The three new modules created in this stage — `config.py`, `data_converter.py`, and `data_ingestion.py` — enable the system to connect securely to AstraDB, handle raw CSV review data, and populate the vector database with embedded text representations.


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
│   ├── config.py               # ⚙️ Loads env vars + model/DB settings (new)
│   ├── data_converter.py       # 🔄 CSV → LangChain Documents (new)
│   └── data_ingestion.py       # 🧠 Embeddings + AstraDB vector store (new)
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


## ⚙️ **Overview of the Data Loading Components**

This update introduces the three key modules that together form the **data loading pipeline**:

### 1. `flipkart/config.py`

Defines and loads all environment variables required for connecting to AstraDB and Hugging Face services.
It centralises key configuration settings such as API tokens, model identifiers, and database endpoints, keeping credentials safely stored in the `.env` file.

### 2. `flipkart/data_converter.py`

Handles reading the Flipkart review dataset from CSV format, removing missing entries, and converting each row into a **LangChain `Document`**.
Each document stores the review text as its content and the product title as metadata — ideal for embedding and later retrieval.

### 3. `flipkart/data_ingestion.py`

Initialises the **Hugging Face embedding model** and the **AstraDB vector store** using the configuration parameters.
It can either load an existing vector store or ingest new review documents by embedding and uploading them into the AstraDB collection.


## 🧩 **Example Usage**

```python
from flipkart.data_ingestion import DataIngestor

# Initialise the ingestion process
ingestor = DataIngestor()

# Option 1: Load existing AstraDB vector store
vstore = ingestor.ingest(load_existing=True)

# Option 2: Ingest new documents into the store
# vstore = ingestor.ingest(load_existing=False)

print("Vector store ready:", vstore)
```

### Example Output

```
Vector store ready: <AstraDBVectorStore(collection_name='flipkart_database')>
```

## ✅ **In Summary**

This stage lays the groundwork for all subsequent LLM-powered components:

* Introduces environment-based configuration through `config.py`.
* Converts raw Flipkart review data into structured `LangChain Document` objects.
* Builds and populates an **AstraDB vector store** using **Hugging Face embeddings**.
* Creates a clean, modular entry point for future retrieval and reasoning stages.

The **data loading stage** is now complete — paving the way for the **RAG pipeline and recommendation logic** to follow in the next phase.
