"""
CP1404 automatic_password_generator
Combination of two previous practical tasks:
    word_generator
    password_checker
"""

import random

MIN_LENGTH = int(input("Minimum length of password: "))
MAX_LENGTH = int(input("Maximum length of password: "))
SPECIAL_CHARS_REQUIRED = input("Are special characters required? (Y/N): ").upper()


def main():
    """Main function"""
    password = generating_random_word(MIN_LENGTH, MAX_LENGTH)
    while not is_valid_password(password, SPECIAL_CHARS_REQUIRED):
            password = generating_random_word(MIN_LENGTH, MAX_LENGTH)
    print("Your {} character password is valid: {}".format(len(password), password))


def generating_random_word(MIN_LENGTH, MAX_LENGTH):
    """Generates random password to be error checked"""
    VOWELS = "aeiouAEIOU"
    CONSONANTS = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    DIGITS = "0123456789"
    SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}\|"
    SELECTION = "cvds"
    word_format_length = random.choice(range(MIN_LENGTH, MAX_LENGTH))
    word_format = ""
    while word_format_length != 0:
        word_format += random.choice(SELECTION)
        word_format_length -= 1

    word = ""
    for kind in word_format:
        if SPECIAL_CHARS_REQUIRED == "Y":
            if kind == "s":
                word += random.choice(SPECIAL_CHARACTERS)
            elif kind == "c":
                word += random.choice(CONSONANTS)
            elif kind == "v":
                word += random.choice(VOWELS)
            else:
                word += random.choice(DIGITS)
        elif kind == "c":
            word += random.choice(CONSONANTS)
        elif kind == "v":
            word += random.choice(VOWELS)
        else:
            word += random.choice(DIGITS)


    return word


def is_valid_password(password, SPECIAL_CHARS_REQUIRED):
    """Determine if the provided password is valid."""
    SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}\|"

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
    if count_lower == 0 or count_digit == 0 or count_upper == 0:
        return False

    if SPECIAL_CHARS_REQUIRED == "Y":
        for char in password:
            if SPECIAL_CHARACTERS.__contains__(char):
                count_special += 1
        if count_special == 0:
            return False
    # if we get here (without returning False), then the password must be valid
    return True


main()
