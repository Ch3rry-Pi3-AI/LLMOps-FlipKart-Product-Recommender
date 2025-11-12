"""
data_converter.py

Module for converting Flipkart CSV data into LangChain Document objects.

This module loads product review data from a CSV file and transforms each
row into a LangChain `Document` containing the review text as content and
the product title as metadata.

Classes
-------
DataConverter
    Loads product reviews and converts them into LangChain Document objects.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from __future__ import annotations
import pandas as pd
from langchain_core.documents import Document


class DataConverter:
    """
    Load product reviews and convert them into LangChain Documents.

    Parameters
    ----------
    file_path : str
        Path to the CSV file containing product reviews.

    Methods
    -------
    convert() -> list[Document]
        Reads the CSV and returns a list of LangChain Documents
        with review text as content and product title in metadata.
    """

    def __init__(self, file_path: str):
        # Store the path to the input CSV file
        self.file_path = file_path

    def convert(self) -> list[Document]:
        """
        Convert CSV rows into LangChain Document objects.

        Returns
        -------
        list[Document]
            A list of Document objects where each document contains
            the product review as text and the product title as metadata.
        """
        # Read required columns and drop rows missing critical data
        df = pd.read_csv(self.file_path, usecols=["product_title", "review"]).dropna(
            subset=["product_title", "review"]
        )

        # Convert each row into a LangChain Document
        docs = [
            Document(
                page_content=str(row["review"]).strip(),
                metadata={"product_name": str(row["product_title"]).strip()},
            )
            for _, row in df.iterrows()
        ]

        # Return the list of prepared Document objects
        return docs
