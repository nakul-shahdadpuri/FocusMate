import ollama

def generate_answer(context, question):
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    response = ollama.generate(model="llama3.2:1b", prompt=prompt)
    print(response)
    # Ensure result aggregation
    result = ""
    for chunk in response:
        if chunk[0] == "response":
            result = chunk[1]
    

    return result
