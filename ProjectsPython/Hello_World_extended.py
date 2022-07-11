"""
def get_hello_message():
    message = input("What´s your Name?")
    if message == "":
        print("Hello, World")
    else:
        return message


def say_hello():
    print(f"Hello, {get_hello_message()}")


say_hello()"""


def get_hello_message(message):
    if not message:
        message = "World"
    return f"Hello, {message}!"


def get_user_name():
    entered_name = input("What´s your Name? ")
    return entered_name.capitalize()


def say_hello():
    user_name = get_user_name()
    output_message = get_hello_message(user_name)
    print(output_message)


say_hello()
