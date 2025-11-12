"""
rag_chain.py

Builds a history-aware Retrieval-Augmented Generation (RAG) chain for the
LLMOps Flipkart Product Recommender System.

This module integrates:
- Groq chat models for conversational responses.
- AstraDB vector store as a retriever for contextual grounding.
- LCEL (LangChain Core Runnable Expressions) for composable chain logic.

Classes
-------
RAGChainBuilder
    Builds and manages a message-history-aware RAG pipeline using LCEL.

Functions
---------
_format_docs(docs: list) -> str
    Utility function to join retrieved document text into a single string.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from __future__ import annotations
from typing import Dict, List

from langchain_groq import ChatGroq
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory

from flipkart.config import Config


# --------------------------------------------------------------
# Helper Functions
# --------------------------------------------------------------
def _format_docs(docs) -> str:
    """
    Combine the content of multiple retrieved documents into one text block.

    Parameters
    ----------
    docs : list
        List of retrieved Document objects.

    Returns
    -------
    str
        Concatenated string of document page contents.
    """
    return "\n\n".join(d.page_content for d in docs)


# --------------------------------------------------------------
# RAG Chain Builder
# --------------------------------------------------------------
class RAGChainBuilder:
    """
    Build a message-history-aware RAG chain using LCEL.

    The RAG chain:
    1. Rewrites user questions based on conversation history.
    2. Retrieves relevant documents from AstraDB.
    3. Generates concise, context-grounded answers using Groq chat models.

    Parameters
    ----------
    vector_store : AstraDBVectorStore
        The AstraDB vector store instance providing document retrieval.

    Attributes
    ----------
    model : ChatGroq
        Groq chat model instance used for rewriting and answering.
    history_store : Dict[str, ChatMessageHistory]
        In-memory dictionary storing per-session chat histories.
    """

    def __init__(self, vector_store):
        # Store reference to AstraDB vector store
        self.vector_store = vector_store

        # Initialise the Groq model with a moderate creativity level
        self.model = ChatGroq(model=Config.RAG_MODEL, temperature=1)

        # Session-based message history storage
        self.history_store: Dict[str, ChatMessageHistory] = {}

    def _get_history(self, session_id: str) -> BaseChatMessageHistory:
        """
        Retrieve or create chat history for a given session.

        Parameters
        ----------
        session_id : str
            Unique identifier for the user session.

        Returns
        -------
        BaseChatMessageHistory
            The chat history object associated with the session.
        """
        if session_id not in self.history_store:
            self.history_store[session_id] = ChatMessageHistory()
        return self.history_store[session_id]

    def build_chain(self) -> RunnableWithMessageHistory:
        """
        Construct the complete LCEL-based RAG chain with history awareness.

        Returns
        -------
        RunnableWithMessageHistory
            Runnable chain that supports message persistence and retrieval.
        """
        # Create retriever from the AstraDB vector store
        retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})

        # ----------------------------------------------------------
        # 1. Question Rewriting — make questions standalone
        # ----------------------------------------------------------
        rephrase_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    (
                        "Given the chat history and user question, "
                        "rewrite it as a standalone question."
                    ),
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}"),
            ]
        )
        rephrase_chain = rephrase_prompt | self.model | StrOutputParser()

        # ----------------------------------------------------------
        # 2. History-Aware Retrieval — use rewritten query
        # ----------------------------------------------------------
        def retrieve_with_history(inputs: dict):
            # Rephrase the user’s query using conversation context
            rewritten = rephrase_chain.invoke(
                {"input": inputs["input"], "chat_history": inputs["chat_history"]}
            )
            # Retrieve relevant context from AstraDB
            return retriever.invoke(rewritten)

        history_aware_retriever = RunnableLambda(retrieve_with_history)

        # ----------------------------------------------------------
        # 3. QA Prompt — combine context with rewritten question
        # ----------------------------------------------------------
        qa_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    (
                        "You're an e-commerce assistant answering product-related queries "
                        "using reviews and titles. Stick to the provided context. "
                        "Be concise and helpful.\n\n"
                        "CONTEXT:\n{context}\n\nQUESTION: {input}"
                    ),
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}"),
            ]
        )

        # ----------------------------------------------------------
        # 4. RAG Assembly — combine retriever, prompt, model, and parser
        # ----------------------------------------------------------
        rag_chain = (
            {
                "context": history_aware_retriever | RunnableLambda(_format_docs),
                "input": RunnablePassthrough(),                                 # Forward the user query
                "chat_history": RunnableLambda(lambda x: x["chat_history"]),    # Include message history
            }
            | qa_prompt
            | self.model
            | StrOutputParser()
        )

        # ----------------------------------------------------------
        # 5. Message History Integration
        # ----------------------------------------------------------

        # base_chain currently returns a string (from StrOutputParser)
        rag_chain_dict = rag_chain | RunnableLambda(lambda s: {"answer": s})
        
        return RunnableWithMessageHistory(
            rag_chain_dict,
            self._get_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )
