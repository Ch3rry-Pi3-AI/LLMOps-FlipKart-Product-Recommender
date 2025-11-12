"""
config.py

Configuration module for the FlipKart Product Recommender project.
Loads environment variables and defines key settings for database
and model integration.

Attributes
----------
ASTRA_DB_API_ENDPOINT : str
    The API endpoint URL for the Astra DB instance.
ASTRA_DB_APPLICATION_TOKEN : str
    Authentication token for accessing Astra DB.
ASTRA_DB_KEYSPACE : str
    The keyspace name within Astra DB.
GROQ_API_KEY : str
    API key for the Groq inference service.
EMBEDDING_MODEL : str
    Identifier for the sentence embedding model.
RAG_MODEL : str
    Identifier for the retrieval-augmented generation (RAG) model.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
import os
from dotenv import load_dotenv


# --------------------------------------------------------------
# Load environment variables
# --------------------------------------------------------------
load_dotenv()


class Config:
    """
    Central configuration class that stores environment
    variables and model identifiers for the application.
    """

    # Astra DB API endpoint URL
    ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")

    # Astra DB application token
    ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")

    # Astra DB keyspace name
    ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

    # Groq API key for LLM model access
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # Sentence embedding model used for vector representations
    EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"

    # RAG (Retrieval-Augmented Generation) model used for response generation
    RAG_MODEL = "llama-3.1-8b-instant"
