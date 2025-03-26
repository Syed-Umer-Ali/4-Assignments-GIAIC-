import math

print("\t\t\tWelcome to the Pythagorus theorem calculator!\t\t\t")
print("\t\tThis program will calculate the length of the hypotenuse of a right-angled triangle.\t\t")

ab = float(input("Enter the length of AB: "))
ac = float(input("Enter the length of AC: "))

# Calculate the hypotenuse
bc = math.sqrt(ab**2 + ac**2)

# Output the result
print(f"The length of BC (the hypotenuse) is: {bc}")