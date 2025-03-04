# query_enhancer.py

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

# REWRITER_MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"
REWRITER_MODEL_NAME = "Qwen/Qwen2-1.5B-Instruct"
TOKEN = os.getenv("HUGGINGFACE_TOKEN")

rewriter_tokenizer = AutoTokenizer.from_pretrained(REWRITER_MODEL_NAME, use_auth_token = TOKEN)
rewriter_model = AutoModelForCausalLM.from_pretrained(
    REWRITER_MODEL_NAME,
    device_map="auto",       
    torch_dtype=torch.float16, 
    use_auth_token=True
)

def rewrite_query(raw_query: str, context: str = "") -> str:
    """
    Use an instruct model to rewrite 'raw_query' into a clearer, more specific query,
    incorporating context if available.
    """
    system_prompt = (
        "You are an AI writing assistant. Your goal is to rewrite the user's query "
        "in a more detailed and contextually rich manner, while preserving the user's intent.\n\n"
        f"Context: {context}\n"
        "User Query:\n"
        f"{raw_query}\n\n"
        "Rewrite it as a more specific, clear, grammatically correct question or instruction."
    )

    # Tokenize
    inputs = rewriter_tokenizer(system_prompt, return_tensors="pt")
    inputs = {k: v.to(rewriter_model.device) for k, v in inputs.items()}

    # Generate
    with torch.no_grad():
        outputs = rewriter_model.generate(
            **inputs,
            max_length=128,
            temperature=0.7,
            top_p=0.9,
            do_sample=True
        )
    rewritten = rewriter_tokenizer.decode(outputs[0], skip_special_tokens=True)

    return rewritten.strip()

