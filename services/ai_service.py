from ollama import chat

async def resChatbot(msg: str):
    response = chat(
        model='phi3:mini',
        stream=False,
        messages=[
                {
                    "role": "system",
                    "content": "Rispondi SEMPRE e SOLO in italiano. Risposte brevi e dirette, senza divagare."
                },
                {
                    "role": "user",
                    "content": msg
                }
            ],
        timeout=60
    )
    
    return (response.message.content)