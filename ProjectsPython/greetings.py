name = input("Whats your name?: ")
print(f'Hello {name}! I am your phonebook.')
while True:
    try:
        age_string: str = input("How old are you?: ")
        age: int = int(age_string)
        break
    except ValueError:
        print("That doesn't seem to be an integer.")
if age < 18:
    print("You are so young! Life is ahead of you!")
elif age <= 40:
    print("That's a nice age!")
elif age > 40:
    print("You must be very wise!")
