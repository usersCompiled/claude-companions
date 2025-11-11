from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    model_dir: str = os.getenv("MODEL_DIR", r"models\tinyllama")
    max_new_tokens: int = int(os.getenv("MAX_NEW_TOKENS", "256"))
    temperature: float = float(os.getenv("TEMPERATURE", "0.7"))
    top_p: float = float(os.getenv("TOP_P", "0.95"))
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))

settings = Settings()
