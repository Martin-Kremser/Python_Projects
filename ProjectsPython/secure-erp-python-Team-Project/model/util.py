import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
# use itertools? chain?
    id = []
    for _ in range(number_of_small_letters):
        id.append(random.choice(string.ascii_lowercase))
    for _ in range(number_of_capital_letters):
        id.append(random.choice(string.ascii_uppercase))
    for _ in range(number_of_digits):
        id.append(random.choice(string.digits))
    for _ in range(number_of_special_chars):
        id.append(random.choice(allowed_special_chars))
    random.shuffle(id)
    return "".join(id)
             
    return 'T!uq6-b4Yq'

