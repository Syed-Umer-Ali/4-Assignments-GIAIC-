def double_until_hundred():
    number = int(input("Enter a number: "))
    while number < 100:
        number *= 2
        print(number, end=" ")

if __name__ == "__main__":
    double_until_hundred()