from flask import Blueprint, request, jsonify
from services.document_loader import load_documents
from models.embedder import load_vector_store, search
from services.answer_generator import generate_answer

main = Blueprint('main', __name__)

# Load documents and sources
documents, sources = load_documents()
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
