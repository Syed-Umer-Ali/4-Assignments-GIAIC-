# Ask the user for their height
user_height = int(input("How tall are you (in inches)? "))

# Minimum height required
minimum_height = 50

# Check if the user is tall enough
if user_height >= minimum_height:
    print("You are tall enough to ride!")
else:
    print("Sorry, you are not tall enough to ride.")