print("Select your Operation: ")
print("Type 1 for Addition")
print("Type 2 for Subtraction")
print("Type 3 for Multiply")
print("Type 4 for Divide")

operation = input()

if operation == "1":
    while True:
        try:
            num_1: float = float(input("Enter first Number: "))
            num_2: float = float(input("Enter second Number: "))
            print(f"The sum is {num_1 + num_2}")
            break
        except ValueError:
            print("This dosen´t looks like a Number. Try again!")
elif operation == "2":
    while True:
        try:
            num_1: float = float(input("Enter first Number: "))
            num_2: float = float(input("Enter second Number: "))
            print(f"The difference is {num_1 - num_2}")
            break
        except ValueError:
            print("This dosen´t looks like a Number. Try again!")
elif operation == "3":
    while True:
        try:
            num_1: float = float(input("Enter first Number: "))
            num_2: float = float(input("Enter second Number: "))
            print(f"The product is {num_1 * num_2}")
            break
        except ValueError:
            print("This dosen´t looks like a Number. Try again!")
elif operation == "4":
    while True:
        try:
            num_1: float = float(input("Enter first Number: "))
            num_2: float = float(input("Enter second Number: "))
            print(f"The result is {num_1 / num_2}")
            break
        except ZeroDivisionError:
            print("Division by zero is not allowed!")
        except ValueError:
            print("This dosen´t looks like a Number. Try again!")
else:
    print("Invalid entry!")

