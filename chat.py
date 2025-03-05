import streamlit as st
from query_enhancer import rewrite_query
from llm_integration import get_answer

# Initialize session state for conversation history
if 'context' not in st.session_state:
    st.session_state.context = []
if 'current_chain' not in st.session_state:
    st.session_state.current_chain = []

# Title and description
st.title("Enhanced Query Chatbot")
st.markdown("""
This interactive demo shows:
1. Original query and response
2. Enhanced/rewritten query
3. Improved response using prompt engineering
*Context is maintained between queries!*
""")

# Input and controls
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input("Enter your message:", key="input")
with col2:
    st.markdown("##")
    submit_btn = st.button("Send")

# Add a button to clear history
if st.button("New Query Chain"):
    st.session_state.current_chain = []
    st.session_state.context = []

# Conversation handling
if submit_btn and user_input:
    with st.spinner("Processing..."):
        # Get answers
        original_answer = get_answer(user_input, context=st.session_state.context)
        enhanced_query = rewrite_query(user_input, context=st.session_state.context)
        enhanced_answer = get_answer(enhanced_query, context=st.session_state.context)
        
        # Update context
        st.session_state.context.append({
            "user_query": user_input,
            "enhanced_query": enhanced_query,
            "answer": enhanced_answer
        })
        
        # Store current chain
        st.session_state.current_chain.append({
            "original_query": user_input,
            "original_answer": original_answer,
            "enhanced_query": enhanced_query,
            "enhanced_answer": enhanced_answer
        })

# Display conversation history
st.markdown("---")
st.subheader("Conversation History")

for i, interaction in enumerate(st.session_state.current_chain):
    with st.expander(f"Query Chain #{i+1}", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Original")
            st.markdown(f"**Query:** {interaction['original_query']}")
            st.markdown(f"**Response:** {interaction['original_answer']}")
        
        with col2:
            st.markdown("### Enhanced")
            st.markdown(f"**Rewritten Query:** {interaction['enhanced_query']}")
            st.markdown(f"**Improved Response:** {interaction['enhanced_answer']}")
    
    st.markdown("---")

# Quick response display at bottom
if st.session_state.current_chain:
    latest = st.session_state.current_chain[-1]
    st.subheader("Latest Response")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Original Response**")
        st.info(latest['original_answer'])
    
    with col2:
        st.markdown("**Enhanced Response**")
        st.success(latest['enhanced_answer'])