"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
MENU = """Pick the format of the word
(C) for constants
(V) for vowels
eg. ccvc"""

def main():
    invalid_format = False
    while invalid_format is False:
        print(MENU)
        word_format = str(input(">>> ")).lower()
        if is_valid_format(word_format) == True:
            invalid_format = True
        else:
            print("Invalid format")

    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)

def is_valid_format(word_format):
    invalid_character = 0
    for char in word_format:
        if char == "c" or char == "v":
            pass
        else:
            invalid_character += 1
    if invalid_character == 0:
        return True

main()

# TODO: Validate user input string if it's an empty string
