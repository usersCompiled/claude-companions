from fastapi import FastAPI
from .inference import generate, load_model
from .schemas import ChatRequest, ChatResponse
from .model_info import get_model_info

app = FastAPI(title="Bloomed Terminal", version="0.1.0")

@app.on_event("startup")
def warmup():
    load_model()

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/v1/model_info")
def model_info():
    return get_model_info()

@app.post("/v1/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    text = generate(
        [m.model_dump() for m in req.messages],
        max_new_tokens=req.max_new_tokens,
        temperature=req.temperature,
        top_p=req.top_p,
        stop=req.stop,
    )
    return ChatResponse(content=text)
