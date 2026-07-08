import json
import os

MEMORY_FILE = "memory.json"


def load_all_chats():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_all_chats(all_chats):
    with open(MEMORY_FILE, "w") as f:
        json.dump(all_chats, f, indent=2)


def save_chat(chat_id, title, model, persona, messages):
    all_chats = load_all_chats()
    all_chats[chat_id] = {
        "title": title,
        "model": model,
        "persona": persona,
        "messages": messages,
    }
    save_all_chats(all_chats)


def list_saved_chats():
    all_chats = load_all_chats()
    return {chat_id: chat_data["title"] for chat_id, chat_data in all_chats.items()}


def load_chat(chat_id):
    all_chats = load_all_chats()
    return all_chats.get(chat_id)


def delete_chat(chat_id):
    all_chats = load_all_chats()

    if chat_id in all_chats:
        del all_chats[chat_id]
        save_all_chats(all_chats)
