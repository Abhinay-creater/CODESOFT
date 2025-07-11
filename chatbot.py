# Simple rule-based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Define rules for responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help you!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day!"
    elif "name" in user_input:
        return "I'm a simple chatbot. What's your name?"
    else:
        return "I'm sorry, I don't understand that. Can you ask something else?"

# Main loop for the chatbot
def main():
    print("Welcome to the Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
