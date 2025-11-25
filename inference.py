import torch
from transformers import pipeline
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
from config import Config

def load_trained_model():
    tokenizer = AutoTokenizer.from_pretrained(Config.MODEL_NAME)
    base_model = AutoModelForCausalLM.from_pretrained(
        Config.MODEL_NAME,
        device_map="auto",
        torch_dtype=torch.float16
    )
    model = PeftModel.from_pretrained(base_model, Config.OUTPUT_DIR)
    return model, tokenizer

if __name__ == "__main__":
    model, tokenizer = load_trained_model()
    generator = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=0 if Config.DEVICE == "cuda" else -1
    )
    
    print("LUMEN chat started. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        prompt = Config.PROMPT_TEMPLATE.format(input=user_input)
        response = generator(
            prompt,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.92,
            top_p=0.95,
            repetition_penalty=1.1
        )[0]["generated_text"]
        print("LUMEN:", response[len(prompt):].strip() + "\n")