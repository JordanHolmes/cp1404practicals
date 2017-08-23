import random


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for quick_pick in range(number_of_quick_picks):
        quick_pick = []
        for i in range(0, 6):
            new_number = random.randint(1, 45)
            quick_pick.append(check_if_unique_number(new_number, quick_pick))
            quick_pick.sort()
        print("{:2} {:2} {:2} {:2} {:2} {:2}".format(quick_pick[0], quick_pick[1], quick_pick[2], quick_pick[3],
                                                     quick_pick[4],
                                                     quick_pick[5]))


def check_if_unique_number(new_number, quick_pick):
    while new_number in quick_pick:
        new_number = random.randint(1, 45)
    return new_number


main()

# TODO: Change print line to a neater format
