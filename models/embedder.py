import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from config.settings import VECTOR_INDEX, EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def embed_documents(documents):
    embeddings = model.encode(documents, convert_to_tensor=True)
    return embeddings.detach().cpu().numpy()

def create_vector_store(documents):
    embeddings = embed_documents(documents)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    # Ensure the index directory exists
    os.makedirs(os.path.dirname(VECTOR_INDEX), exist_ok=True)
    faiss.write_index(index, VECTOR_INDEX)
    print(f"Vector store created and saved at {VECTOR_INDEX}")
    return index

def load_vector_store():
    if not os.path.exists(VECTOR_INDEX):
        raise FileNotFoundError(f"Vector index file not found: {VECTOR_INDEX}")
    return faiss.read_index(VECTOR_INDEX)

def search(query, index):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k=5)
    return indices[0]
