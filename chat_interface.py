from query_enhancer import rewrite_query
from llm_integration import get_answer


def run_cli():
    print("=== Enhanced Chatbot CLI ===")
    context = []  # Initialize empty context
    
    while True:
        user_input = input("Your Query: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # Pass both required parameters
        enhanced_query = rewrite_query(
            raw_query=user_input,
            context=context  # Now passing the context
        )
        
        # Get answers
        original_answer = get_answer(user_input)
        enhanced_answer = get_answer(enhanced_query, context=context)
        
        # Update context
        context.append({
            "user_query": user_input,
            "enhanced_query": enhanced_query,
            "answer": enhanced_answer
        })
        
        # Display results
        print(f"\nOriginal Answer: {original_answer}")
        print(f"\nEnhanced Query: {enhanced_query}")
        print(f"Enhanced Answer: {enhanced_answer}\n")
