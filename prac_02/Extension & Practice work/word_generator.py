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
invalid_format = True
while invalid_format is True:
    print(MENU)
    word_format = str(input(">>> ")).lower()
    invalid_character = 0
    for char in word_format:
        if char == "c" or char == "v":
            pass
        else:
            invalid_character += 1
    if invalid_character == 0:
        invalid_format = False
    else:
        print("Invalid word format")

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
print(word)

# TODO: Validate user input string if it's an empty string
