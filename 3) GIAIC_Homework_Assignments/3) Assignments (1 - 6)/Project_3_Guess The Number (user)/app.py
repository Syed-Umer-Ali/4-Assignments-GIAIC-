def computer_guess():
    print("Think of a number between 1 and 20, and I will try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 20
    feedback = ""
    attempts = 0

    while feedback != "c":
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        
        feedback = input("Is my guess too high (H), too low (L), or correct (C)? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"Yay! I guessed your number {guess} correctly in {attempts} attempts!")
        else:
            print("Please enter 'H', 'L', or 'C'.")

computer_guess()
