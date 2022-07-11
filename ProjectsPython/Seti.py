def decimal_to_binary():
    dez = int(input("Gib hier deine Dezimalzahl (keine Kommazahl) ein: "))
    conv = "{0:b}".format(dez)
    print(conv)


def binary_to_decimal():
    dual = input("Gib hier deine Binärzahl ein: ")
    return int(dual, 2)


def dec_to_base(decimal_number, destination_base):
    base_num = ""
    while decimal_number > 0:
        dig = int(decimal_number % destination_base)
        if dig < 10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A') + dig - 10)
        decimal_number //= destination_base
    base_num = base_num[::-1]
    return base_num


