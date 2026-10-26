
import requests
import streamlit as st

# -------------------------------
# 1. Page configuration
# -------------------------------
st.set_page_config(
    page_title="GenAI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 My GenAI Chatbot")
st.caption("Powered by Qwen 2.5 and Ollama")

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen2.5:3b"

# -------------------------------
# 2. Initialize chat history
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! 👋 Main tumhara AI assistant hoon. Kuch bhi poochho!"
        }
    ]

# -------------------------------
# 3. Display previous messages
# -------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------
# 4. Handle user's new message
# -------------------------------
user_prompt = st.chat_input("Yahan apna message likho...")

if user_prompt:
    # Display user's message
    st.session_state.messages.append(
        {"role": "user", "content": user_prompt}
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Ask the AI model
    with st.chat_message("assistant"):
        with st.spinner("AI soch raha hai..."):
            try:
                payload = {
                    "model": MODEL_NAME,
                    "messages": [
                        {
                            "role": "system",
                            "content": (
                                "You are a helpful AI assistant. "
                                "Give clear, friendly and easy-to-understand "
                                "answers. Explain technical topics simply."
                            )
                        },
                        *st.session_state.messages
                    ],
                    "stream": False
                }

                response = requests.post(
                    OLLAMA_URL,
                    json=payload,
                    timeout=180
                )

                response.raise_for_status()
                result = response.json()

                ai_reply = result["message"]["content"]

            except requests.exceptions.ConnectionError:
                ai_reply = (
                    "Ollama connect nahi ho raha. "
                    "Check karo ki Ollama installed aur running hai."
                )

            except requests.exceptions.Timeout:
                ai_reply = (
                    "AI response mein zyada time lag raha hai. "
                    "Dobara try karo ya lighter model use karo."
                )

            except requests.exceptions.RequestException as error:
                ai_reply = f"Request error: {error}"

            except (KeyError, ValueError):
                ai_reply = (
                    "AI ka response read nahi ho paya. "
                    "Model aur Ollama status check karo."
                )

        st.markdown(ai_reply)

    # Save assistant response in chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_reply}
    )

# -------------------------------
# 5. Clear chat history
# -------------------------------
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Chat clear ho gayi! Naya question poochho."
        }
    ]
    st.rerun()
