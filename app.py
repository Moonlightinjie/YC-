import streamlit as st
import openai
import os

# Get API key from Streamlit Cloud secrets
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.set_page_config(page_title="CSEC AI Tutor Chatbot")
st.title("📚 CSEC AI Tutor Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("Ask a CSEC question:")

# Send button
if st.button("Send") and user_input:
    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-5-mini",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response.choices[0].message['content']

        # Save chat history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", answer))
    except Exception as e:
        st.error(f"Error: {e}")

# Display chat history
for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")

