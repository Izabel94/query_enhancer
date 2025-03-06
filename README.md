# AI Query Enhancement System

## Project Overview
A Python application that improves user queries through prompt engineering techniques to optimize responses from generative AI models. Demonstrates the impact of query refinement on response quality across CLI and web interface.

## File Structure
| File               | Purpose                                                                 |
|--------------------|-------------------------------------------------------------------------|
| `query_enhancer.py`| Contains query rewriting logic using language models                   |
| `model_manager.py` | Handles model loading and configuration for the enhancement pipeline   |
| `llm_integration.py`| Manages API/Local model interactions and response generation           |
| `cli_interface.py` | Command-line interface implementation                                  |
| `chat.py`        | Streamlit-based web interface                                            |

## Installation
1. Clone repository:
   git clone https://github.com/Izabel94/query-enhancer.git
   cd query-enhancer

2. Install dependencies:
   pip install -r requirements.txt

3. Run the CLI interface:
   python main.py

4. Run the web interface:
   streamlit run chat.py

## Example Output:
=== Enhanced Chatbot CLI ===
Your Query: i am going to japa. what to see?

Original Answer: 
1) Tokyo Tower
2) Sensoji Temple
3) Roppongi Hills
4) Shibuya Crossing

Tokyo is a vibrant city with many must-see attractions, including:

1) **Tokyo Tower**: One of Japan's most iconic landmarks, it offers stunning views of the city from its observation deck.   

2) **Sensoji Temple**: A historic Buddhist temple located in the heart of Tokyo, known for its wooden gates and intricate gardens.

3) **

Enhanced Query: 1) What are some must-see places in Japan? 2) Are there any cultural events or festivals happening soon in Japan? 3) Can you recommend a good local cuisine that I should try during my visit?

The rewritten query is now
Enhanced Answer: 1) Tokyo Tower, Senso-ji Temple, Mount Fuji, and Osaka Castle are must-see places in Japan.
2) The upcoming cultural events include the Cherry Blossom Festival (March), the Fukuoka International Film Festival (June), and the Gion Matsuri festival (July).
3) For local cuisine recommendations, try sushi at Tsukiji Market, ramen at Ichiran, and tonkatsu at Takoyakiya.

## Enhancement Techniques
Contextual Rewriting - Adds missing context: "food?" → "What are traditional Japanese foods?"

Fixes spelling: "japa" → "Japan"

Error Correction: Grammar fixes: "what to do ?" → "What should I do?"

Specificity Boost: Converts vague requests - "see things" → "Top cultural landmarks"

Intent Clarification: Resolves ambiguity - "weather?" → "Current weather in Tokyo"

## Libraries used
Transformers (Hugging Face): For query rewriting and response generation

Qwen-1.5B Model: Base language model for understanding queries

Streamlit: Web interface construction
