import requests

# Define your question
question = "Find out all the answers from the uploaded RFP responses that discuss Omm's past and current federal and commercial experience/contracts. Capture the original answers and do not shorten or modify them"

# Send the POST request
response = requests.post("http://127.0.0.1:5000/ask", json={"question": question})

# Check response
if response.status_code == 200:
    data = response.json()
    print("\n=== Answer ===")
    print(data["answer"])
    print("\n=== Sources ===")
    for source in data["sources"]:
        print(f"- {source}")
else:
    print(f"Error {response.status_code}: {response.text}")
