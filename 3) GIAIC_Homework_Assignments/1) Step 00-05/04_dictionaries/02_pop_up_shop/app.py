# Dictionary of fruits with their prices per unit
fruits = {
    "apple": 2.5,
    "durian": 15.0,
    "jackfruit": 20.0,
    "kiwi": 1.5,
    "rambutan": 5.0,
    "mango": 10.0
}

total_cost = 0

# Loop through the dictionary and prompt the user
for fruit, price in fruits.items():
    try:
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price
    except ValueError:
        print("Invalid input. Please enter a number.")

# Print the total cost
print(f"Your total is ${total_cost:.2f}")