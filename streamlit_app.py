import streamlit as st
import requests

st.title("🎙️ VENNALA Voice Assistant")
st.write("Your personal assistant powered by FastAPI and Streamlit 💡")

# API endpoint
API_URL = "http://localhost:8000/execute"

# Input form
command = st.text_input("Enter your command:", placeholder="e.g., play a song, what's the time, who is Elon Musk")
if st.button("Execute"):
    if command:
        try:
            response = requests.post(API_URL, json={"command": command})
            response.raise_for_status()
            result = response.json().get("response", "No response received")
            st.success(result)
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to API: {e}")
    else:
        st.warning("Please enter a command.")

st.markdown("""
### Available Commands:
- **Play a song**: "play [song name]"
- **Get time**: "what's the time"
- **Learn about someone**: "who is [person name]"
- **Hear a joke**: "joke"
""")