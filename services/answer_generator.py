import ollama

def generate_answer(context, question):
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    response = ollama.generate(model="llama3.2:1b", prompt=prompt)

    result = ""
    for chunk in response:
        result += chunk["text"]
    return result
