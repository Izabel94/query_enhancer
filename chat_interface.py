# chat_interface.py

from query_enhancer import enhance_query
from lm_integration import get_response_from_model

def run_cli():
    print("Welcome to the Enhanced Chatbot CLI!")
    print("Type 'exit' or press Ctrl+C to quit.\n")

    while True:
        user_input = input("User Query: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break

        # 1) Show the original query
        original_query = user_input
        # 2) Enhance the query
        enhanced_query = enhance_query(original_query)

        # 3) Get responses (both original and enhanced)
        print("\n[Original Query]")
        print(f"Q: {original_query}")
        original_response = get_response_from_model(original_query)
        print(f"A: {original_response}\n")

        print("[Enhanced Query]")
        print(f"Q: {enhanced_query}")
        enhanced_response = get_response_from_model(enhanced_query)
        print(f"A: {enhanced_response}\n")
