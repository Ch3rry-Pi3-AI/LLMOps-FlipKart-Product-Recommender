"""
data_ingestion.py

Module for building and managing the AstraDB vector store used in the
Flipkart Product Recommender project.

This module connects to AstraDB, initialises a Hugging Face embedding model,
and optionally ingests product review documents from CSV into the vector store.

Classes
-------
DataIngestor
    Handles embedding model setup, vector store connection,
    and ingestion of review documents into AstraDB.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from __future__ import annotations

from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from flipkart.data_converter import DataConverter
from flipkart.config import Config


class DataIngestor:
    """
    Initialise embeddings and vector store; optionally ingest documents.

    Attributes
    ----------
    embedding : HuggingFaceEndpointEmbeddings
        Embedding model initialised via Hugging Face Inference API.
    vstore : AstraDBVectorStore
        Vector store connected to AstraDB for storing embedded documents.

    Methods
    -------
    ingest(load_existing: bool = True) -> AstraDBVectorStore
        Return an existing vector store or ingest documents from CSV before returning it.
    """

    def __init__(self):
        # Initialise the Hugging Face embedding model using Config parameters
        self.embedding = HuggingFaceEndpointEmbeddings(model=Config.EMBEDDING_MODEL)

        # Create the AstraDB vector store connection
        self.vstore = AstraDBVectorStore(
            embedding=self.embedding,
            collection_name="flipkart_database",
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace=Config.ASTRA_DB_KEYSPACE,
        )

    def ingest(self, load_existing: bool = True) -> AstraDBVectorStore:
        """
        Create or load an AstraDB vector store containing review documents.

        Parameters
        ----------
        load_existing : bool, default=True
            If True, returns the existing store without re-ingestion.
            If False, loads review data from CSV and adds it to the store.

        Returns
        -------
        AstraDBVectorStore
            The AstraDB vector store instance containing embedded documents.
        """
        # Return the existing store without adding new documents
        if load_existing:
            return self.vstore

        # Convert CSV data into LangChain Document objects
        docs = DataConverter("data/flipkart_product_review.csv").convert()

        # Add documents to the vector store if any exist
        if docs:
            self.vstore.add_documents(docs)

        # Return the prepared AstraDB vector store
        return self.vstore
