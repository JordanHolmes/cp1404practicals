import random

number_of_quick_picks = int(input("How many quick picks? "))

for quick_pick in range(number_of_quick_picks):
    quick_pick = []
    for i in range(0, 6):
        new_number = random.randint(1, 45)
        quick_pick.append(new_number)
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format(quick_pick[0], quick_pick[1], quick_pick[2], quick_pick[3], quick_pick[4],
                                     quick_pick[5]))

# import random
# number_of_quick_picks = int(input("How many quick picks? "))
# for quick_pick in range(number_of_quick_picks):
#     quick_pick = random.sample(range(1, 46), 6)
#     print("{:2} {:2} {:2} {:2} {:2} {:2}".format(quick_pick[0], quick_pick[1], quick_pick[2], quick_pick[3],
#                                                  quick_pick[4], quick_pick[5]))
