import random

AMOUNT_OF_NUMBERS_IN_QUICK_PICK = 6

MAX_VALUE = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for quick_pick in range(number_of_quick_picks):
        quick_pick = []
        for i in range(AMOUNT_OF_NUMBERS_IN_QUICK_PICK):
            new_number = random.randint(1, MAX_VALUE)
            quick_pick.append(generate_unique_number(new_number, quick_pick))
            quick_pick.sort()
        print("{:2} {:2} {:2} {:2} {:2} {:2}".format(*quick_pick))


def generate_unique_number(new_number, quick_pick):
    while new_number in quick_pick:
        new_number = random.randint(1, MAX_VALUE)
    return new_number


main()
