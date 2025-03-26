import random 

def rock_paper_scissor():
    options = ['rock','paper','scissor']
    user_choice = input('Enter Your Choice : [rock,paper,scissor] : ').lower()

    if user_choice not in options:
        print('Invalid Choice !! Please TRY AGIAN.')
        return

    computer_choice = random.choice(options)
    print(f'Computer Choose {computer_choice}')

    if user_choice == computer_choice:
        print('Match Tie...')
    elif (user_choice == 'rock' and computer_choice == "scissor") or (user_choice == 'paper' and computer_choice == "rock") or (user_choice == 'scissor' and computer_choice == "paper"):
        print('Congratulations !! You Win!')
    else:
        print('You Lost The Game!')

rock_paper_scissor()
