import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import concurrent.futures

# Set the model identifier for Qwen2-1.5B-Instruct
model_name = "Qwen/Qwen2-1.5B-Instruct"

# Retrieve token from environment variables
token = os.getenv("HUGGING_FACE_TOKEN")
if token is None:
    raise ValueError("Please set your HUGGINGFACE_TOKEN environment variable.")

# Since we are running on CPU, we use torch.float32
device = "cpu"

# Load the tokenizer and model with authentication and force CPU usage
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=token)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    use_auth_token=token,
    device_map={"": device},  # force model to CPU
    torch_dtype=torch.float32  # use full precision on CPU
)

def inference(prompt: str, timeout: int = 30) -> str:
    """
    Runs inference on the given prompt with a timeout.
    """
    def generate_text(prompt_text):
        inputs = tokenizer(prompt_text, return_tensors="pt")
        inputs = {k: v.to(device) for k, v in inputs.items()}
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=50,
                temperature=0.7,
                top_p=0.9,
                do_sample=True
            )
        return tokenizer.decode(outputs[0], skip_special_tokens=True)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(generate_text, prompt)
        try:
            result = future.result(timeout=timeout)
            return result
        except concurrent.futures.TimeoutError:
            return "[Error: Inference timed out]"

# Simple prompt for testing
prompt = "Hello, how are you today?"

# Run the inference with a timeout of 30 seconds
result = inference(prompt, timeout=30)
print("Generated Output:")
print(result)
