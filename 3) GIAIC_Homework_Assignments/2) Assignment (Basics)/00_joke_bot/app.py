import random

def joke_bot():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!"
    ]
    
    print("Hi! I'm Joke Bot. Type 'joke' to hear a joke or 'quit' to exit.")
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'joke':
            print("Joke Bot:", random.choice(jokes))
        elif user_input == 'quit':
            print("Joke Bot: Goodbye! Have a great day!")
            break
        else:
            print("Joke Bot: I didn't understand that. Type 'joke' for a joke or 'quit' to exit.")

if __name__ == "__main__":
    joke_bot()