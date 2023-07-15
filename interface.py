from chatbot import intent_chatbot  # Update the import statement here

def run_chatbot():
    print("Welcome to the Intent Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        intent_chatbot.chatbot(user_input)

if __name__ == "__main__":
    run_chatbot()
