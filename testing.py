from dispatcher import apply_persona, get_response, trim_history

if __name__ == "__main__":
    messages = [{"role": "user", "content": "What is a python list"}]
    trimmed = trim_history(messages)
    final_messages = apply_persona("Teacher", trimmed)

    reply = get_response("llama-3.1-8b-instant", final_messages, temperature=0.7)
    print(reply)