# Program to count the occurrences of numbers in a list using a dictionary

def main():
    number_counts = {}
    
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        
        try:
            number = int(user_input)
            if number in number_counts:
                number_counts[number] += 1
            else:
                number_counts[number] = 1
        except ValueError:
            print("Please enter a valid number.")
    
    print("\nNumber counts:")
    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")

if __name__ == "__main__":
    main()