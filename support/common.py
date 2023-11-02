import random
import string


def generate_email(length, is_digit=True, is_letter=True, is_symbol=False):
    if is_digit and is_letter and is_symbol:
        characters = string.ascii_letters.lower() + string.digits + string.punctuation
    elif is_digit and is_letter and not is_symbol:
        characters = string.ascii_letters.lower() + string.digits
    elif is_digit and not is_letter and is_symbol:
        characters = string.digits + string.punctuation
    elif not is_digit and is_letter and is_symbol:
        characters = string.ascii_letters.lower() + string.punctuation
    elif is_digit and not is_letter and not is_symbol:
        characters = string.digits
    elif not is_digit and is_letter and not is_symbol:
        characters = string.ascii_letters.lower()
    elif not is_digit and not is_letter and is_symbol:
        characters = string.punctuation
    else:
        raise ValueError("Invalid combination of options")

    return ''.join(random.choice(characters) for _ in range(length))

