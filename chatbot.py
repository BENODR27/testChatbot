import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hello|hi|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"how are you|how's it going",
        ["I'm just a chatbot, but I'm here to assist you!", "I don't have feelings, but I'm here to help."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Take care!", "Bye! Have a great day!"]
    ],
        [
        r"what's your name|who are you",
        ["I'm a chatbot created by OpenAI.", "You can call me ChatGPT.", "I'm ChatGPT, your helpful assistant."]
    ],
    [
        r"how can you help|what can you do",
        ["I can provide information, answer questions, and have conversations.", "I'm here to assist you with various tasks."]
    ],
    [
        r"tell me a joke|make me laugh",
        ["Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!", "Why did the computer go to therapy? Because it had too many bytes of emotional baggage."]
    ],
    [
        r"tell me something interesting",
        ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."]
    ],
    [
        r"how old are you",
        ["I'm a program, so I don't have an age!", "Age is just a number, and for me, that number is zero."]
    ],
    [
        r"thanks|thank you",
        ["You're welcome!", "No problem!", "You're welcome. If you have more questions, feel free to ask."]
    ],
     [
        r".* key",
        ["its confidential"]
    ],
    [
        r"i am .*",
        ["hi i am beno"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm here to help, but I'm not sure I understand your input."]
    ]
]


chatbot = Chat(pairs, reflections)

print("Hello! I'm your chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
