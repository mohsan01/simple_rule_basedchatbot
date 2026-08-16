
print("Chatbot: Hello! I am a simple chatbot created by mohsan .")
print("Chatbot: You can say hello, how are you, or bye.")

while True:
    user_input = input("You: ").lower()
    if user_input in ["hello", "hi", "hey"]:
        print("Chatbot: Hello! Nice to meet you.")
    elif user_input == "how are you":
        print("Chatbot: I'm doing great! Thanks for asking.")
    elif user_input == "what is your name":
        print("Chatbot: My name is SimpleBot.")
    elif user_input in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a nice day.")
        break
    else:
        print("Chatbot: Sorry, I don't understand that.")