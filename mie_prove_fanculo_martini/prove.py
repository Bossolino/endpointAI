import requests

user_input = str(input('input: '))

try:
    response = requests.post(
        "http://10.132.228.225:11434/api/chat",
        json={
            "model": "phi3:mini",
            "stream": False,
            "messages": [
                {
                    "role": "system",
                    "content": "Rispondi SEMPRE e SOLO in italiano. Risposte brevi e dirette, senza divagare."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        },
        timeout=60
    )

    data = response.json()
    print(data["message"]["content"])

except requests.exceptions.Timeout:
    print("timeout: server troppo lento o bloccato")

except Exception as e:
    print("errore:", e)