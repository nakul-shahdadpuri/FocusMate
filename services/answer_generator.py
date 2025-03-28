import ollama

def generate_answer(context, question):
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    response = ollama.generate(model="llama2", prompt=prompt)

    result = ""
    for chunk in response:
        result += chunk["text"]
    return result
