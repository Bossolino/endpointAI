from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.ai_service import resChatbot

origins = [
    "https://simonemartini.site:8000"
]

app = FastAPI()
app.add_middleware(CORSMiddleware,  allow_origins=origins, allow_credentials=True, allow_methods=["GET", "POST"], allow_headers=["*"])


@app.get("/chatbot")
async def chatbot(msg:str):

    if not msg or msg == "":
        raise HTTPException(status_code=400, detail="no valid data send")

    response = await resChatbot(msg)

    return {"response":response}