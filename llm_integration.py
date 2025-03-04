from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# ANSWER_MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"
ANSWER_MODEL_NAME = "Qwen/Qwen2-1.5B-Instruct"
TOKEN = os.getenv("HUGGINGFACE_TOKEN")


answer_tokenizer = AutoTokenizer.from_pretrained(ANSWER_MODEL_NAME, use_auth_token=TOKEN)
answer_model = AutoModelForCausalLM.from_pretrained(
    ANSWER_MODEL_NAME,
    device_map="auto",
    torch_dtype=torch.float16,
    use_auth_token=True
)

def get_answer(prompt: str) -> str:
    """
    Sends the prompt to the Llama2 model and returns the generated answer.
    """
    inputs = answer_tokenizer(prompt, return_tensors="pt")
    inputs = {k: v.to(answer_model.device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = answer_model.generate(
            **inputs,
            max_length=256,
            temperature=0.7,
            top_p=0.9,
            do_sample=True
        )
    return answer_tokenizer.decode(outputs[0], skip_special_tokens=True)

