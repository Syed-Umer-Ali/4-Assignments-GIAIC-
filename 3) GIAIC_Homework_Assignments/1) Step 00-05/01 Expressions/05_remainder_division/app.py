# Ask the user for the first number
num1 = int(input("Please enter an integer to be divided: "))

# Ask the user for the second number
num2 = int(input("Please enter an integer to divide by: "))

# Perform the division and calculate the remainder
quotient = num1 // num2
remainder = num1 % num2

# Print the result
print(f"The result of this division is {quotient} with a remainder of {remainder}")