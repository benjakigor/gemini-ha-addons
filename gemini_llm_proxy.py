from fastapi import FastAPI, Request
import httpx
import os

app = FastAPI()

GEMINI_API_KEY = os.environ.get("API_KEY") or os.environ.get("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

@app.post("/v1/completions")
async def completions(req: Request):
    data = await req.json()
    prompt = data.get("prompt", "")

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GEMINI_URL, json=payload)

    try:
        result = response.json()
        text = result["candidates"][0]["content"]["parts"][0]["text"]
    except:
        text = "Greška u odgovoru iz Gemini-ja."

    return {"response": text}
