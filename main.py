from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://simonemartini.site:8000"
]

app = FastAPI()
app.add_middleware(CORSMiddleware,  allow_origins=origins, allow_credentials=True, allow_methods=["GET", "POST"], allow_headers=["*"])


@app.get("/chatbot")
async def chatbot(data:dict):

    if not data.message or not data.role:
        raise HTTPException(status_code=400, detail="no valid data send")

    

    # funzione mattew
    return {"response":""}