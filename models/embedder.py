import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from config.settings import VECTOR_INDEX, EMBEDDING_MODEL

# Load the SentenceTransformer model using the specified embedding model
model = SentenceTransformer(EMBEDDING_MODEL)

def embed_documents(documents):
    """
    Generate embeddings for a list of documents using the SentenceTransformer model.

    Args:
        documents (list of str): List of text documents to embed.

    Returns:
        numpy.ndarray: Array of embeddings for the input documents.
    """
    embeddings = model.encode(documents, convert_to_tensor=True)
    return embeddings.detach().cpu().numpy()

def create_vector_store(documents):
    """
    Create a FAISS vector store from the embeddings of the provided documents.

    Args:
        documents (list of str): List of text documents to embed and store.

    Returns:
        faiss.IndexFlatL2: The FAISS index containing the document embeddings.
    """
    embeddings = embed_documents(documents)
    # Initialize a FAISS index for L2 (Euclidean) distance
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    # Ensure the directory for the vector index file exists
    os.makedirs(os.path.dirname(VECTOR_INDEX), exist_ok=True)
    # Save the FAISS index to the specified file
    faiss.write_index(index, VECTOR_INDEX)
    print(f"Vector store created and saved at {VECTOR_INDEX}")
    return index

def load_vector_store():
    """
    Load a FAISS vector store from the specified file.

    Returns:
        faiss.IndexFlatL2: The loaded FAISS index.

    Raises:
        FileNotFoundError: If the vector index file does not exist.
    """
    if not os.path.exists(VECTOR_INDEX):
        raise FileNotFoundError(f"Vector index file not found: {VECTOR_INDEX}")
    return faiss.read_index(VECTOR_INDEX)

def search(query, index):
    """
    Search the FAISS vector store for the closest embeddings to the query.

    Args:
        query (str): The query text to search for.
        index (faiss.IndexFlatL2): The FAISS index to search in.

    Returns:
        list of int: Indices of the top-k closest embeddings in the index.
    """
    # Generate the embedding for the query
    query_embedding = model.encode([query])
    # Perform the search in the FAISS index
    distances, indices = index.search(np.array(query_embedding), k=5)
    return indices[0]
