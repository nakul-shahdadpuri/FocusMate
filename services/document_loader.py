import os
import PyPDF2
from config.settings import DATA_FOLDER

def pdf_to_text(file_path):
    text = ''
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)  # Updated line
        for page in reader.pages:
            text += page.extract_text()
    return text

def load_documents():
    documents = []
    sources = []
    for file_name in os.listdir(DATA_FOLDER):
        file_path = os.path.join(DATA_FOLDER, file_name)
        content = ""
        if file_name.endswith(".txt"):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
        elif file_name.endswith(".pdf"):
            content = pdf_to_text(file_path)
        
        if content:
            documents.append(content)
            sources.append(file_name)  # Track the source of each document
    return documents, sources
