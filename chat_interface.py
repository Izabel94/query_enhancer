# chat_interface.py

from query_enhancer import rewrite_query
from llm_integration import get_answer

def run_cli():
    print("=== Enhanced Chatbot CLI ===")
    print("Type 'exit' or 'quit' to terminate.\n")


    while True:
        user_input = input("Your Query: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # 1) Original Query
        original_query = user_input
        original_answer = get_answer(original_query)

        # 2) Rewritten / Enhanced Query
        enhanced_query = rewrite_query(raw_query=original_query)
        enhanced_answer = get_answer(enhanced_query)

        print("\n--- Original Query & Response ---")
        print(f"Q: {original_query}")
        print(f"A: {original_answer}\n")

        print("--- Enhanced Query & Response ---")
        print(f"Q: {enhanced_query}")
        print(f"A: {enhanced_answer}\n")
