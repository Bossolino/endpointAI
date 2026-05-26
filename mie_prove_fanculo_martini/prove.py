import requests

print("waiting")

try:
    response = requests.post(
        "http://10.132.228.225/api/generate",
        json={
            "model": "qwen3.5:0.8b",
            "prompt": "ciao",
            "stream": False
        },
        timeout=60
    )

    data = response.json()
    print(data["response"])

except requests.exceptions.Timeout:
    print("timeout: server troppo lento o bloccato")

except Exception as e:
    print("errore:", e)