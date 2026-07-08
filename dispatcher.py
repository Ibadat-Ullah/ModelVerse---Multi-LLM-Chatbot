from models import (
    call_openai,
    call_groq_llama,
    call_gemini,
    call_groq_qwen,
    call_cerabras_gemma,
    call_mistral,
    call_cohere_command,
    call_zai,
)

from personas import PERSONAS

MODEL_REGISTRY = {
    "gpt-5.4-mini": {"function": call_openai, "context_window": 128000},
    "llama-3.1-8b-instant": {"function": call_groq_llama, "context_window": 131072},
    "gemini-2.5-flash-lite": {"function": call_gemini, "context_window": 1000000},
    "qwen/qwen3.6-27b": {"function": call_groq_qwen, "context_window": 131072},
    "gemma-4-31b": {"function": call_cerabras_gemma, "context_window": 8192},
    "mistral-small-latest": {"function": call_mistral, "context_window": 32000},
    "command-r7b-12-2024": {"function": call_cohere_command, "context_window": 128000},
    "glm-4.7-flash": {"function": call_zai, "context_window": 128000},
}


def trim_history(messages, max_messages=20):
    return messages[-max_messages:]


def apply_persona(persona_label, messages):
    system_prompt = PERSONAS.get(persona_label, PERSONAS["Default"])
    return [{"role": "system", "content": system_prompt}] + messages


def get_response(model_label, messages, temperature):
    entry = MODEL_REGISTRY.get(model_label)

    if entry is None:
        return f"⚠️ Unknown model selected: {model_label}"

    try:
        return entry["function"](messages, temperature)
    except Exception as e:
        return f"⚠️ Error from {model_label}: {e}"


