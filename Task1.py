print("--- Rule-Based AI Chatbot Initialized ---")
print("Type your message below (or type 'bye' to exit the conversation):")

while True:
    
    user_input = input("\nYou: ")
    
    
    clean_input = user_input.lower().strip()
    
    
    if clean_input == "":
        continue
        
    elif clean_input == "hello" or clean_input == "hi" or clean_input == "hey":
        print("Bot: Hello! I am your rule-based AI assistant. How can I help you today?")
        
    elif clean_input == "how are you":
        print("Bot: I am functioning perfectly at 100% efficiency, thank you!")
        
    elif clean_input == "what is your purpose" or clean_input == "help":
        print("Bot: My purpose is to demonstrate transparent, rule-based logic gates without hallucinations.")
        
    elif clean_input == "bye" or clean_input == "exit" or clean_input == "quit":
        print("Bot: Goodbye! Safely closing the feedback loop interface.")
        break  
        
    else:
        print("Bot: Input unrecognized. I am a white-box system matching exact predefined rules.")