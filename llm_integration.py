# llm_integration.py
from model_manager import tokenizer, model
import torch

def get_answer(prompt: str, context: list = None) -> str:
    # Build context-aware prompt
    context_str = ""
    if context:
        last_interaction = context[-1]
        context_str = (
            f"Context: The user previously asked about {last_interaction['user_query']}, "
            f"and the response was {last_interaction['answer']}.\n"
        )

    full_prompt = (
        f"{context_str}"
        f"Answer this query concisely and stay on-topic. "
        f"Reference the context if needed:\n\nQuery: {prompt}\nAnswer: "
    )

    # Generate response
    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        temperature=0.5,
        eos_token_id=tokenizer.eos_token_id
    )

    # Extract answer
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer.split("Answer:")[-1].strip()

