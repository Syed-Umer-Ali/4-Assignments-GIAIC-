import colorama
from colorama import Fore,Back,Style
colorama.init()

import random
num = random.randint(0,100)

print(Fore.CYAN + "\t\t\tWelcome The Number Guessing Game \t\t\t")
print(Fore.CYAN + "\t\tYou Have Five Chance To Guess The Correct Number! \t\t")

Chance= 0
while True:
    if (Chance == 5 ):
        print (Fore.RED + " \t\t\tOpps !! \n \t\tYou Lost The Game ! \n \t\tPlease Try Again\t\t\t");
        print (Fore.LIGHTRED_EX63 + f" \t\tThe Correct Number is : {num} \t\t")
        break
    else:
        user = int(input(Fore.YELLOW + "Guess The Number Between 1 to 100 : ")) 
        if(user < num):
            print(Fore.GREEN + " \tWrong!!! "+ "Hint : Think Little Higher Number.")
            Chance = Chance + 1
        elif(user > num):
            print(Fore.GREEN + " \tWrong!!! "+ "Hint : Think Little Lower Number.") 
            Chance = Chance + 1
        elif(user == num ):
            print(Fore.LIGHTMAGENTA_EX + "\t\t\tCongratulation ! \n You Won This Game\t\t\t" )  
            break  

