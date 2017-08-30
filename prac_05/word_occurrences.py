"""
CP1404/CP5632 Practical
Word occurences in a dictionary
"""


def main():
    words_to_word_count = {}
    user_words = input("Text: ").lower().split()
    for user_word in user_words:
        if user_word in words_to_word_count:
            words_to_word_count[user_word] += 1
        else:
            words_to_word_count[user_word] = 1

    words = sorted(list(words_to_word_count))
    longest_word = max(len(word) for word in words)

    for word in words:
        print("{:{}} : {:2}".format(word, longest_word, words_to_word_count[word]))


main()
