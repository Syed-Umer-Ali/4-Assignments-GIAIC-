def add_three_copies(lst, data):
    # Add three copies of the data to the list
    lst.append(data)
    lst.append(data)
    lst.append(data)

# Main program
if __name__ == "__main__":
    # Get user input
    message = input("Enter a message to copy: ")

    # Initialize an empty list
    my_list = []

    # Print the list before modification
    print("List before:", my_list)

    # Call the function to add three copies
    add_three_copies(my_list, message)

    # Print the list after modification
    print("List after:", my_list)