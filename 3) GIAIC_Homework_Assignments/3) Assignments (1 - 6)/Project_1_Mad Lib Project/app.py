import colorama
from colorama import Fore,Back,Style
colorama.init()
import time

print(Fore.YELLOW + "Assalam u Alikum !")
print(Fore.BLUE +"I am Detective Umer.")
print("Kindly Give Some Answers Of My Questions")
name = input(Fore.RED + "Enter Your Name ? : ")
number = input("Enter How Many Years Of Experience Do You Have ? : ")
profession = input ("Enter What Your Profession ? : ")
time.sleep(1.5)
print( Fore.GREEN +"Hmm?".upper())
time.sleep(0.5)
print(Fore.CYAN + name.upper() + ", You Are a Best " + profession +".") 
print("\t=> I Heared About Your Work .")
print("\t=> You Are Very Honest In Your Profession .")
print("\t=> You Have "  +number+  " Years Experience .")
print("\t=> You Are Doing A Great Job !")

