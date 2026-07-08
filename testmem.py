import memory

memory.save_all_chats({"test": {"title": "hello"}})
print(memory.load_all_chats())
