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
    faiss.write_index(index, VECTOR_INDEX)
    return index

def load_vector_store():
    return faiss.read_index(VECTOR_INDEX)

def search(query, index):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k=5)
    return indices[0]
