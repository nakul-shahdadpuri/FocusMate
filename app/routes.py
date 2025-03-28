from flask import Blueprint, request, jsonify
from services.document_loader import load_documents
from models.embedder import load_vector_store, create_vector_store, search
from services.answer_generator import generate_answer
import os
from config.settings import VECTOR_INDEX

main = Blueprint('main', __name__)

# Load documents and sources
documents, sources = load_documents()

# Check if the FAISS index file exists, and create it if not
if not os.path.exists(VECTOR_INDEX):
    print("Vector index not found. Creating a new one...")
    create_vector_store(documents)

# Load the vector index
index = load_vector_store()

@main.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    indices = search(question, index)

    # Retrieve the context and sources from the most similar documents
    context = ""
    source_list = []
    for i in indices:
        context += f"{documents[i]} "
        source_list.append(sources[i])

    # Generate the answer using the combined context
    answer = generate_answer(context, question)

    # Return the answer and the sources
    return jsonify({
        "answer": answer,
        "sources": source_list
    })
