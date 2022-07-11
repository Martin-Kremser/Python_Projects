def min():
    num_1: float = float(input("Give me a number: "))
    num_2: float = float(input("Give me another number: "))
    if num_1 > num_2:
        return num_2
    else:
        return num_1


def multiply():
    num_1: int = int(input("Give me a number: "))
    num_2: int = int(input("Give me another number: "))
    index = 0
    result = 0
    while index < num_1:
        result = result + num_2
        index += 1
    print(result)


def pow():
    grundwert: int = int(input("Give me a number: "))
    exponent: int = int(input("Give me another number: "))
    result = grundwert
    for index in range(exponent - 1):
        result = result * grundwert
    print(result)


list = [89, 8, 3, 6, 7, 74, 100]


def max_value():
    max_value = None
    for num in list:
        if max_value is None or num > max_value:
            max_value = num
    print('Maximum value:', max_value)


def len():
    counter = 0
    for index in list:
        counter = counter + 1
    print(f"The length of the list is: {str(counter)}")


def divmod(x, y):
    divfloor_start = x / y
    divfloor = int(divfloor_start)
    modulo = x - (divfloor * y)
    return divfloor, modulo


print('check', divmod(20, 6))
