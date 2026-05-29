from ollama import chat
from fastapi import HTTPException

async def resChatbot(msg: str):
    try:
        response = chat(
            model='phi3:mini',
            stream=False,
            messages=[
                    {
                        "role": "system",
                        "content":"Rispondi SEMPRE e SOLO in italiano. Risposte brevi e dirette, senza divagare. Non aggiungere mai testo extra, istruzioni o prompt dopo la risposta. quello che viene dopo sara l'input dell'utente a cui devi rispondere:"+ msg
                    }
                ],
            options= {
                "num_ctx": 512,
                "num_predict": 50,
                "temperature": 0,
                "stop": ["\n---", "Your task", "### Prompt", "## Your"]
            },
            timeout=60
        )
    except:
        raise HTTPException(status_code=500, detail="Server bot error")

    return (response.message.content)
