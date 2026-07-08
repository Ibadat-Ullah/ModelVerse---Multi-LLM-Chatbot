import streamlit as st
from dispatcher import get_response, apply_persona, trim_history

st.set_page_config(
    page_title="MetaVerse - A Multi-LLM Chatbot",
    page_icon="🤖",
    layout="wide",
)

if "messages" not in st.session_state:
    st.session_state.messages = []

left, right = st.columns([4, 1])

with left:
    st.title("🤖 ModelVerse - Multi-LLM Chatbot")
    st.caption("Interact with multiple AI models in one place.")

with right:
    st.subheader("👥 Contributors")
    st.caption("Ma'am Aisha Khan (Instructor)")
    st.caption("Ibadat Ullah (Student)")

with st.sidebar:

    st.header("⚙️ Settings")

    model = st.selectbox(
        "Model",
        [
            "gpt-5.4-mini",
            "llama-3.1-8b-instant",
            "gemini-2.5-flash-lite",
            "qwen/qwen3.6-27b",
            "gemma-4-31b",
            "mistral-small-latest",
            "command-r7b-12-2024",
            "glm-4.7-flash",
        ],
    )

    persona = st.selectbox(
        "Persona",
        [
            "Default",
            "Student",
            "Teacher",
            "Researcher",
            "Interviewer",
            "Code_Reviewer",
            "Programmer",
        ],
    )

    temperature = st.slider(
        "Temperature",
        0.0,
        2.0,
        0.7,
    )

    if st.button("🆕 New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.button("💾 Save Chat", use_container_width=True)

    st.button("📂 Export Chat", use_container_width=True)

st.caption(
    f"📦 **Model:** {model} &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; "
    f"🎭 **Persona:** {persona}"
)

st.divider()

if len(st.session_state.messages) == 0:
    st.markdown("### 👋 Welcome")
    st.caption("Select a model from the sidebar and start chatting.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your message...")

if prompt:

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    trimmed = trim_history(st.session_state.messages)
    final_messages = apply_persona(persona, trimmed)

    with st.spinner(f"🤔 {model} is thinking..."):
        reply = get_response(model, final_messages, temperature)

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply,
        }
    )
