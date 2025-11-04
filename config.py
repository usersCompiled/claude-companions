import os
import torch

class Config:
    MODEL_NAME = "Qwen/Qwen2.5-7B"
    DATASET_PATH = "data/lumen_personality.json"
    OUTPUT_DIR = "models/lumen_trained"
    NUM_EPOCHS = 3
    BATCH_SIZE = 4
    LEARNING_RATE = 5e-5
    MAX_SEQ_LENGTH = 1024
    LORA_RANK = 16
    QUANTIZATION = "8bit"
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    GRADIENT_CHECKPOINTING = True
    
    PROMPT_TEMPLATE = "You are LUMEN, an evolving AI Frankenstein. Respond in a way that's messy, unpredictable, and self-shaping: {input}"