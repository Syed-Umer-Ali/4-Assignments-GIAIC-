def get_first_element(lst):
    # Print the first element of the list
    print(lst[0])

# Prompt the user to input the list
n = int(input("Enter the number of elements in the list: "))
user_list = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

# Call the function with the user-provided list
get_first_element(user_list)