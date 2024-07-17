import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Define responses for the chatbot
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    "goodbye": ["Goodbye!", "Bye!", "See you later!"],
    "thanks": ["You're welcome!", "No problem.", "My pleasure!"],
    "options": ["I can help with queries about stocks.", "I am good at sorting arrays."]
}

# Define patterns for the chatbot to match against
patterns = [
    (r'hello|hi|hey|good morning|good afternoon', 'greeting'),
    (r'bye|goodbye|see you later', 'goodbye'),
    (r'thank you|thanks|thank you very much', 'thanks'),
    (r'help', 'options')
]

# Define a function to respond to user input
def respond(message):
    for pattern, intent in patterns:
        if nltk.regexp_tokenize(message.lower(), pattern):
            return random.choice(responses[intent])

    return "I'm sorry, I don't understand your question."

# Define a function to handle a conversation
def chat():
    print("Hello! I'm your chatbot. How can I assist you today?")
    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = respond(message)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
