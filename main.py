 #Rule Based Personal Chat Assistant

import datetime

# Greeting
name = input("Swagat h, enter your name: ")
hour = datetime.datetime.now().hour

if 5 <= hour < 12:
    print(f"Good morning, {name}")
elif 12 <= hour < 17:
    print(f"Good afternoon, {name}")
elif 17 <= hour < 21:
    print(f"Good evening, {name}")
else:
    print(f"Good night, {name}")

print("Namaste! Welcome to your chatbot")
print("Type 'bye' to exit")

# Chatbot responses
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there!",
    "how are you": "I am doing great 😊",
    "happy": "Great to hear that!",
    "your name": "I am your personal chat assistant",
    "functions kya hote hai": "Functions are blocks of reusable code. Chapter 7 padho.",
    "bye": "Goodbye! Have a nice day 😊"
}

# Function to get chatbot response
def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    for key in responses:
        if key in userQuestion:
            return responses[key]
    return "I am not able to tell that yet. I am still in learning mode."

# Chat loop
while True:
    userInput = input("You: ")
    reply = getResponseBot(userInput)
    print("Bot:", reply)

    if "bye" in userInput.lower():
        break
