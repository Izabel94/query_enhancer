# model_manager.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

MODEL_NAME = "Qwen/Qwen2-1.5B-Instruct"
TOKEN = os.getenv("HUGGING_FACE_TOKEN")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=TOKEN)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="cpu",              # Force CPU usage
    torch_dtype=torch.float32, 
    use_auth_token=TOKEN
)
