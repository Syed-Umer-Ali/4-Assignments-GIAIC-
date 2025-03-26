def feet_to_inches(feet):
    inches_per_foot = 12
    return feet * inches_per_foot

print("\t\t\tThis program converts feet to inches.\t\t\t\n \t\t\tthere are 12 inches in one feet".title())
feet = float(input("Enter the measurement in feet: "))
inches = feet_to_inches(feet)
print(f"{feet} feet is equal to {inches} inches.")