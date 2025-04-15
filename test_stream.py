import requests

question = "Find out all the answers from the uploaded RFP responses that discuss Omm's past and current federal and commercial experience/contracts. Capture the original answers and do not shorten or modify them"

response = requests.post(
    "http://127.0.0.1:5000/ask_stream",
    json={"question": question},
    stream=True
)

if response.status_code == 200:
    print("\n=== Streamed Answer ===\n")
    for line in response.iter_lines(decode_unicode=True):
        if line:  # skip empty lines
            clean_line = line.strip()
            if clean_line.startswith("data:"):
                print(clean_line.replace("data:", "").strip(), end="", flush=True)
else:
    print(f"Error {response.status_code}: {response.text}")
