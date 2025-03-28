import os

# setting up directory paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "../data/")
VECTOR_INDEX = os.path.join(BASE_DIR, "../index/vector_store.index")
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'