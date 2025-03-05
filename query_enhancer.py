# query_enhancer.py
from model_manager import tokenizer, model  

def rewrite_query(raw_query: str, context: list = None) -> str:  # Make context optional
    context = context or []  # Handle None case
    # Build conversation history from context

    if context:
        last_interaction = context[-1]
        user_query = last_interaction.get("user_query", "") 
        previous_answer = last_interaction.get("answer", "")
        conversation_history = (
        f"Previous Query: {user_query}\n"
        f"Previous Answer: {previous_answer}\n"
    )
    else:
        conversation_history = ""

    system_prompt = (
        "Rewrite the user's query to be clear and specific, while preserving intent. "
        "Incorporate context from the previous interaction if relevant.\n\n"
        "DO NOT ADD MULTIPLE SUB-QUESTIONS. "
        "OUTPUT ONLY ONE REWRITTEN QUERY.\n\n"
        f"{conversation_history}"
        f"New User Query: {raw_query}\n"
        "Rewritten Query: "
    )

    inputs = tokenizer(system_prompt, return_tensors="pt").to(model.device)

    # Rest of your generation code (with strict parameters)
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        temperature=0.3,
        eos_token_id=tokenizer.eos_token_id,
        do_sample=True
    )

    # Extract rewritten query
    rewritten = tokenizer.decode(outputs[0], skip_special_tokens=True)
    rewritten = rewritten.split("Rewritten Query:")[-1].strip()
    return rewritten