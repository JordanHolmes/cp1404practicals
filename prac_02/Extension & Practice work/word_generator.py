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
print(MENU)
word_format = str(input(">>> ")).lower()
word = ""

for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
print(word)


# TODO: Validate user input string as a combination of c and v
# TODO: Look at practical outline. wildcards. randomly generate word_format
