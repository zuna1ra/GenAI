import streamlit as st
import requests
from datetime import datetime

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------
st.set_page_config(
    page_title="Local LLM Chatbot",
    page_icon="🤖",
    layout="centered"
)
#CUSTOM CSS STYLING
st.markdown("""
<style>

/* Main App Background */
.stApp {
    background-color: #0E1117;
    color: white;
}

/* Chat Input Box */
.stChatInput input {
    background-color: #262730 !important;
    color: white !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161A23;
}

/* Buttons */
.stButton button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px;
}

/* Download Button */
.stDownloadButton button {
    background-color: #2196F3;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)
# --------------------------------
# TITLE
# --------------------------------
st.title("🤖 Local LLM Chatbot")
st.write("Chat with your locally hosted AI model using Ollama")

# --------------------------------
# SESSION STATE
# Stores chat history
# --------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------
# SIDEBAR
# --------------------------------
with st.sidebar:

    st.header("⚙️Chat Controls")
    #Model Selection
    model_name=st.selectbox(
        "Choose AI Model",
        [
            "gemma:2b",
            "llama3",
            "mistral"
        ]
    )
    #Temprature Slider
    temperature=st.slider(
        "Creativity Level",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

    # Reset button
    if st.button("🗑️Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    
    #Information Section

    st.markdown("---")
    st.info("This chatbot runs locally using Ollama.")

# DISPLAY OLD MESSAGES
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(
            f"""
            {message['content']}
            {message['time']}
            """
        )

#Download Chat
chat_text=""
for msg in st.session_state.messages:
    chat_text += (
        f"{msg['role']}:"
        f"{msg['content']}\n"
    )
st.download_button(
    label="Download Chat",
    data=chat_text,
    file_name="chat_history.txt",
    mime="text/plain"
)    

# USER INPUT
user_input = st.chat_input("Type your message...")

# WHEN USER SENDS MESSAGE
if user_input:

# Display user message
    st.chat_message("user").markdown(user_input)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time":datetime.now().strftime("%H:%M")
    })

    # CREATE CONVERSATION HISTORY
    conversation = """You are a helpful AI Assistance."""

    for msg in st.session_state.messages:
        conversation += f"{msg['role']}: {msg['content']}\n"


    # API REQUEST TO OLLAMA    
    try:
        with st.spinner("Thinking..."):
            response = requests.post(
               "http://localhost:11434/api/generate",

            json={
                "model": model_name,
                "prompt": conversation,
                "stream": False,
                "options":{"temperature":temperature}
                
            }
        )

        # Convert response into JSON
        if response.status_code==200:
          data = response.json()

        # Extract AI response
          bot_reply = data.get("response", "No response from model")
        else:
            bot_reply=(f"Error: " f"{response.status_code}")

    except Exception as e:

        bot_reply = f"Error: {e}"

   
    # DISPLAY AI RESPONSE
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply,
        "time": datetime.now().strftime("%H:%M")
    })
#Footer
st.markdown("---")
st.markdown("Built with Streamlit + Ollama + Python")
