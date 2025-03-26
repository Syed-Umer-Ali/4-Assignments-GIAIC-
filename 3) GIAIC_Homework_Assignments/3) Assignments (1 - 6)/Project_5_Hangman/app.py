import random

# ye hangman ky stages ho gye
def print_hangman(stage):
    hangman_stages = [
        """
        _______
        |       |
        |
        |
        |
        |
        |____________
        """,
        """
        _______
        |       |
        |       O
        |
        |
        |
        |_____________
        """,
        """
        _______
        |       |
        |       O
        |       |
        |
        |
        |_____________
        """,
        """
        _______
        |       |
        |       O
        |      /|
        |
        |
        |_____________
        """,
        """
        _______
        |       |
        |       O
        |      /|\\
        |
        |
        |_____________
        """,
        """
        _______
        |       |
        |       O
        |      /|\\
        |      /
        |
        |_____________
        """,
        """
        _______
        |       |
        |       O
        |      /|\\
        |      / \\
        |
        |_____________
        """,
    ]
    print(hangman_stages[stage])

def hangman_game():
    print("Let's Play Hangman!!\n")
    print("You Have Only 6 Lives. Try To Guess The Word Within 6 Attempts. Good Luck!!\n")

    # List of fruits
    list_fruits = ["apple", "banana", "orange", "strawberry", "grape", "pineapple", "kiwi", "mango", "watermelon", "papaya"]
    random_fruit = random.choice(list_fruits)  # Randomly choose a fruit
    length = len(random_fruit)
    guessed_word = ['_'] * length  # Initial guessed word with underscores
    attempts_left = 6  # Number of attempts
    guessed_letters = set()

    print(" ".join(guessed_word))  # Display the initial word with blanks

    while attempts_left > 0:
        letter = input("\nGuess a Letter: ").lower()

        if letter in guessed_letters:
            print("You already guessed this letter. Try a different one!")
            continue

        guessed_letters.add(letter)

        if letter in random_fruit:
            for i in range(length):
                if random_fruit[i] == letter:
                    guessed_word[i] = letter
            print("Correct Guess!")
        else:
            attempts_left -= 1
            print(f"Wrong Guess! You have {attempts_left} attempts left.")
            print_hangman(6 - attempts_left)

        print(" ".join(guessed_word))

        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word!")
            break
    else:
        print("\nYou lost the game! Better luck next time.")
        print(f"The word was: {random_fruit.upper()}")

# Run the game
hangman_game()
