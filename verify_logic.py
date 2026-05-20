from chatbot_logic import FUTOChatbot

def verify():
    bot = FUTOChatbot()
    test_queries = [
        "what is the motto of futo",
        "who is the vc",
        "where is futo located",
        "tell me about futo",
        "what is jamb",
        "tell me about seet",
        "what is a carryover",
        "where to stay in futo",
        "what are futo colors",
        "who made you"
    ]
    
    print("--- Verification Results ---")
    for q in test_queries:
        response = bot.respond(q)
        print(f"Q: {q}")
        print(f"A: {response}\n")

if __name__ == "__main__":
    verify()
