FROM python:3.10

WORKDIR /app

RUN pip install fastapi uvicorn httpx

COPY gemini_llm_proxy.py .

CMD ["uvicorn", "gemini_llm_proxy:app", "--host", "0.0.0.0", "--port", "8000"]
