import nltk
import re

# Initialize NLTK
nltk.download("punkt")

# Define predefined responses
responses = {
    "hello": "Hi there!",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "hi": "Hello!",
    "hey": "Hey, how can I assist you today?",
    "good morning": "Good morning!",
    "good afternoon": "Good afternoon!",
    "good evening": "Good evening!",
    "how can I help you": "You can ask me anything you'd like.",
    "what's your name": "I'm just a chatbot, so I don't have a name.",
    "who created you": "I was created by a developer.",
    "tell me a joke": "Why did the computer keep freezing? Because it left its Windows open!",
    "tell me something interesting": "Did you know that honey never spoils?",
    "how's the weather today": "I'm sorry, I don't have access to real-time weather information.",
    "what's the capital of France": "The capital of France is Paris.",
    "how old are you": "I don't have an age. I'm just a computer program.",
    "what's the meaning of life": "The meaning of life is a philosophical question with many interpretations.",
    "tell me a fun fact": "A group of flamingos is called a 'flamboyance.'",
    "do you have any siblings": "No, I don't have any siblings. I'm a solo chatbot.",
    "can you dance": "I can't dance, but I can help you find dance tutorials!",
    "what's your favorite color": "I don't have personal preferences, so I don't have a favorite color.",
    "who won the last Super Bowl": "I'm not up to date with current events. You may want to check the latest news.",
    "are you a human": "No, I'm not a human. I'm an AI chatbot.",
    "what's the time": "I'm sorry, I don't have access to real-time data, including the current time.",
    "tell me a riddle": "Sure! What has keys but can't open locks? A piano!",
    "what's your favorite food": "I don't eat, so I don't have a favorite food.",
    "do you dream": "No, I don't dream. I'm just a computer program.",
    "what's the tallest mountain in the world": "Mount Everest is the tallest mountain in the world.",
    "tell me a science fact": "A day on Venus is longer than its year. Venus rotates very slowly on its axis.",
    "what's the answer to the universe": "The answer to the ultimate question of life, the universe, and everything is 42 (according to Douglas Adams' 'The Hitchhiker's Guide to the Galaxy').",
    "how do I learn programming": "You can start learning programming by taking online courses and practicing regularly.",
    "tell me a famous quote": "Here's one: 'The only way to do great work is to love what you do.' – Steve Jobs",
    "what's the largest planet in our solar system": "Jupiter is the largest planet in our solar system.",
    "do you like music": "I don't have personal preferences, but I can help you discover music!",
}


# Create a function to generate responses
def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check for predefined responses
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    # If no predefined response, use the default response
    return responses["default"]

# Main loop for chatting
print("Chatbot: Hi there! How can I assist you today? (Type 'bye' to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)
