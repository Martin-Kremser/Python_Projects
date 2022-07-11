import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(mail):
    if re.search(regex, mail):
        print("Valid Email")

    else:
        print("Invalid Email")


if __name__ == '__main__':
    email = input('Gib hier deine E-Mail Adresse ein: ')
    check(email)
