def bot_response(user):

    user = user.lower()

    if user == "hello":
        return "Hi! How can I help you?"

    elif user == "hi":
        return "Hello!"

    elif user == "how are you":
        return "I am fine. How are you?"

    elif user == "what is your name":
        return "I am an AI Chatbot."

    elif user == "who created you":
        return "Bhavani created me using Python."

    elif user == "bye":
        return "Goodbye! Have a nice day."

    elif user == "good morning":
        return "Good Morning!"

    elif user == "good night":
        return "Good Night!"

    elif user == "what are you doing":
        return "I am chatting with you."

    elif user == "thank you":
        return "You are welcome."

    elif user == "what is python":
        return "Python is a programming language."

    elif user == "what is ai":
        return "AI stands for Artificial Intelligence."

    elif user == "tell me a joke":
        return "Why do programmers hate bugs? Because they take too much debugging!"

    elif user == "which college":
        return "I support engineering students."

    elif user == "what is your favorite language":
        return "Python is my favorite language."

    elif user == "are you smart":
        return "Yes, I am trying to become smarter every day."

    elif user == "do you know coding":
        return "Yes, I can help with Python and Verilog."

    elif user == "what is raspberry pi":
        return "Raspberry Pi is a small single-board computer."

    elif user == "what is verilog":
        return "Verilog is a hardware description language."

    else:
        return "Sorry, I don't understand."