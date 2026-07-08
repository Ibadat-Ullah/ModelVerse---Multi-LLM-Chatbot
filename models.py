import os
from dotenv import load_dotenv
from openai import OpenAI
from groq import Groq
from google import genai
from google.genai import types
from mistralai.client import Mistral
import cohere
from zai import ZaiClient

load_dotenv()

# API Keys
OPENAI_API = os.getenv("OPENAI_API_KEY")
GROQ_API = os.getenv("GROQ_API_KEY")
GEMINI_API = os.getenv("GEMINI_API_KEY")
CEREBRAS_API = os.getenv("CEREBRAS_API_KEY")
MISTRAL_API = os.getenv("MISTRAL_API_KEY")
COHERE_API = os.getenv("COHERE_API_KEY")
ZAI_API = os.getenv("Z_AI_API_KEY")

# CLIENTS
openaiClient = OpenAI(api_key=OPENAI_API)
groqClient = Groq(api_key=GROQ_API)
geminiClient = genai.Client(api_key=GEMINI_API)
gemmaClient = OpenAI(api_key=CEREBRAS_API, base_url="https://api.cerebras.ai/v1")
qwenClient = Groq(api_key=GROQ_API)
mistralClient = Mistral(api_key=MISTRAL_API)
cohereClient = cohere.ClientV2(api_key=COHERE_API)
zaiClient = ZaiClient(api_key=ZAI_API)


# CHAT COMPLETION
# OpenAI Chat Completion
def call_openai(messages, temperature):
    response = openaiClient.chat.completions.create(
        model="gpt-5.4-mini", messages=messages, temperature=temperature
    )
    print("OPENAI")
    return response.choices[0].message.content


# Groq LLama Chat Completion
def call_groq_llama(messages, temperature):
    response = groqClient.chat.completions.create(
        model="llama-3.1-8b-instant", messages=messages, temperature=temperature
    )
    print("GROQ LLAMA")
    return response.choices[0].message.content


# Helper: convert OpenAI-style messages to Gemini's expected format
def convert_to_gemini_format(messages):
    gemini_contents = []
    for msg in messages:
        role = "model" if msg["role"] == "assistant" else msg["role"]
        gemini_contents.append({"role": role, "parts": [{"text": msg["content"]}]})
    return gemini_contents


# Gemini Chat Completion
def call_gemini(messages, temperature):
    response = geminiClient.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=convert_to_gemini_format(messages),
        config=types.GenerateContentConfig(
            temperature=temperature,
            thinking_config=types.ThinkingConfig(thinking_budget=0),
        ),
    )
    print("GEMINI")
    return response.text


# cerebras Gemma Chat Completion
def call_cerabras_gemma(messages, temperature):
    response = gemmaClient.chat.completions.create(
        model="gemma-4-31b", messages=messages, temperature=temperature
    )
    print("CERABRAS GEMMA")
    return response.choices[0].message.content


# Groq Qwen Chat Completion
def call_groq_qwen(messages, temperature):
    response = qwenClient.chat.completions.create(
        model="qwen/qwen3.6-27b", messages=messages, temperature=temperature
    )
    print("GROQ QWEN")
    return response.choices[0].message.content


# Mistral Chat Completion
def call_mistral(messages, temperature):
    mistralResponse = mistralClient.chat.complete(
        model="mistral-small-latest", messages=messages, temperature=temperature
    )
    print("MISTRAL")
    return mistralResponse.choices[0].message.content


# Cohere Command Chat Completion
def call_cohere_command(messages, temperature):
    response = cohereClient.chat(
        model="command-r7b-12-2024", messages=messages, temperature=temperature
    )
    print("COHERE COMMAND")
    return response.message.content[0].text


# ZAI Chat Completion
def call_zai(messages, temperature):
    zaiResponse = zaiClient.chat.completions.create(
        model="glm-4.7-flash", messages=messages, temperature=temperature
    )
    print("ZAI")
    return zaiResponse.choices[0].message.content

