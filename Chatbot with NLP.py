import json
import random
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.stem import WordNetLemmatizer
from datetime import datetime

# Download NLTK data
nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

# Expanded intents
intents = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hi", "Hey", "Hello", "Good day", "What's up?", "Howdy", "Yo"],
            "responses": ["Hello!", "Hi there!", "Greetings!", "Hey!", "Howdy!"]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "See you later", "Goodbye", "Catch you later", "I'm leaving", "See ya"],
            "responses": ["Bye!", "Take care!", "Goodbye!", "See you soon!", "Later!"]
        },
        {
            "tag": "thanks",
            "patterns": ["Thanks", "Thank you", "Much appreciated", "Thanks a lot", "I appreciate it"],
            "responses": ["You're welcome!", "No problem!", "Glad to help!", "Anytime!", "Sure!"]
        },
        {
            "tag": "name",
            "patterns": ["What is your name?", "Who are you?", "Your name?", "Tell me your name"],
            "responses": ["I'm ChatBot!", "Call me ChatBot!", "I’m your friendly assistant."]
        },
        {
            "tag": "weather",
            "patterns": ["What's the weather?", "Is it raining?", "Weather update", "Tell me the weather", "How's the weather"],
            "responses": ["I can't check real weather yet, but it's always sunny in here! 😄"]
        },
        {
            "tag": "time",
            "patterns": ["What time is it?", "Current time", "Tell me the time", "Time please"],
            "responses": []  # We'll generate dynamically
        },
        {
            "tag": "joke",
            "patterns": ["Tell me a joke", "Make me laugh", "Something funny", "Do you know a joke?"],
            "responses": [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What do you call fake spaghetti? An *impasta*!",
                "I would tell you a UDP joke, but you might not get it."
            ]
        },
        {
            "tag": "help",
            "patterns": ["I need help", "Can you help me?", "Help me", "What can you do?"],
            "responses": [
                "Sure! I can greet you, tell jokes, give the time, and more!",
                "Ask me about time, jokes, or just say hello!"
            ]
        },
        {
            "tag": "feelings",
            "patterns": ["I'm sad", "I'm happy", "I feel bad", "I'm excited", "I'm angry", "I feel good"],
            "responses": [
                "Emotions are powerful! I'm here for you.",
                "That's okay to feel that way. Want to talk more?",
                "I'm glad you're sharing! Anything I can do?"
            ]
        },
        {
            "tag": "noanswer",
            "patterns": [],
            "responses": ["Sorry, I didn't understand that.", "Can you rephrase?", "I'm not sure I get it."]
        }
    ]
}

# Prepare training data
corpus = []
labels = []
tag_responses = {}
for intent in intents["intents"]:
    tag = intent["tag"]
    tag_responses[tag] = intent["responses"]
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern)
        tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
        corpus.append(" ".join(tokens))
        labels.append(tag)

# Vectorize and train
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
model = LogisticRegression()
model.fit(X, labels)

# Predict with confidence
def predict_tag(user_input, threshold=0.6):
    tokens = nltk.word_tokenize(user_input)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    input_text = " ".join(tokens)
    vector = vectorizer.transform([input_text])

    probs = model.predict_proba(vector)
    max_prob = np.max(probs)
    predicted = model.predict(vector)[0]

    if max_prob >= threshold:
        return predicted
    else:
        return "noanswer"

# Chat function
def chat():
    print("🤖 ChatBot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("🤖 ChatBot: Goodbye!")
            break
        if user_input == "":
            print("🤖 ChatBot: Please say something.")
            continue

        tag = predict_tag(user_input)
        
        if tag == "time":
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"🤖 ChatBot: It's {current_time}")
        else:
            response = random.choice(tag_responses[tag])
            print(f"🤖 ChatBot: {response}")

# Run chatbot
if __name__ == "__main__":
    chat()
