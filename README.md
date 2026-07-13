# 🤖 ModelVerse — Multi-LLM Chatbot

👥 **Contributors:**
- **Ma'am Aisha Khan** *(Instructor)*
- **Ibadat Ullah** *(Student)*

📘 **Subject:** Artificial Intelligence

🏫 **Institute:** Comsats University Islamabad, Abbottabad Campus

---

A single Streamlit interface for chatting with multiple large language models from different providers, side by side. Switch models mid-conversation, apply different personas, tune temperature, and save/reload past chats — all from one lightweight app.

## Features

- **Multi-provider model switching** — instantly swap between 8 models from 7 providers without changing code:
  - OpenAI (`gpt-5.6-luna`)
  - Groq (`llama-3.1-8b-instant`, `qwen/qwen3.6-27b`)
  - Google Gemini (`gemini-2.5-flash-lite`)
  - Cerebras (`gemma-4-31b`)
  - Mistral (`mistral-small-latest`)
  - Cohere (`command-r7b-12-2024`)
  - Z.ai (`glm-4.7-flash`)
- **Personas** — 7 built-in system prompts (Default, Student, Teacher, Researcher, Interviewer, Code Reviewer, Programmer) that shape how the model responds.
- **Temperature control** — adjustable per conversation via a slider.
- **Chat history management** — start a new chat, save the current one, reload a saved chat, or delete it — all persisted locally to a JSON file.
- **Automatic history trimming** — keeps only the most recent messages so long conversations don't blow past context limits.
- **Graceful error handling** — a failed provider call returns an inline warning instead of crashing the app.

## Project structure

```
.
├── app.py              # Streamlit UI: layout, sidebar controls, chat rendering, session state
├── dispatcher.py       # Routes requests to the right model function, applies persona + history trimming
├── models.py           # Provider-specific API client setup and chat-completion wrappers
├── personas.py         # System prompt definitions for each persona
├── memory.py           # Local JSON-based save/load/delete for chat history
├── requirements.txt    # Python dependencies
└── memory.json         # Auto-created at runtime to store saved chats
```

## How it works

1. `app.py` renders the sidebar (model, persona, temperature, chat management) and the chat window, keeping conversation state in `st.session_state`.
2. On each user message, `dispatcher.trim_history()` caps the conversation to the last 20 messages, and `dispatcher.apply_persona()` prepends the selected persona's system prompt.
3. `dispatcher.get_response()` looks up the selected model in `MODEL_REGISTRY` and calls its corresponding function in `models.py`.
4. Each function in `models.py` normalizes the request into the target provider's SDK format (e.g. converting OpenAI-style messages into Gemini's `contents` format) and returns the plain text reply.
5. `memory.py` reads/writes a flat `memory.json` file to persist chat title, model, persona, and full message history per chat ID.

## Setup

### 1. Clone and install dependencies

```bash
git clone https://github.com/Ibadat-Ullah/ModelVerse---Multi-LLM-Chatbot.git
cd modelverse
pip install -r requirements.txt
```

### 2. Configure API keys

Create a `.env` file in the project root with the keys for whichever providers you want to use:

```env
OPENAI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
CEREBRAS_API_KEY=your_key_here
MISTRAL_API_KEY=your_key_here
COHERE_API_KEY=your_key_here
Z_AI_API_KEY=your_key_here
```

> Note: if a key is missing, calls to that specific provider will fail with an inline error in the chat — other models will continue to work normally.

### 3. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## Usage

1. Pick a **model** and **persona** from the sidebar, and adjust **temperature** if needed.
2. Type a message in the chat box at the bottom.
3. Use **🆕 New Chat** to start fresh, **💾 Save Chat** to persist the current conversation, and the saved chats list to reload or delete past sessions.

## Roadmap / possible improvements

- Move chat storage from a flat JSON file to a proper database for concurrent/multi-user use.
- Add streaming responses instead of waiting for the full reply.
- Add per-model token/cost tracking.
- Unify the app's display name (currently set as "MetaVerse" in the page config but "ModelVerse" in the title).

## License

Add a license of your choice (e.g. MIT) before publishing publicly.
