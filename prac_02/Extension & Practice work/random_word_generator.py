"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
SELECTION = "cv"
word_format_length = random.choice(range(5, 10))
word_format = ""
while word_format_length != 0:
    word_format += random.choice(SELECTION)
    print(word_format_length)
    print(word_format)
    word_format_length -= 1

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
print(word)
