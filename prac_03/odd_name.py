"""Jordan Holmes"""


def main():
    valid_user_name = False
    user_name = str(input("What is your name?: "))
    while valid_user_name is False:
        valid_user_name = verifying_name(user_name, valid_user_name)
    frequency_of_letters = int(input("How frequently do you want to skip letters?: "))
    prints_the_name(user_name, frequency_of_letters)


def prints_the_name(user_name, frequency_of_letters):
    for char in range(0, (len(user_name) + 1), frequency_of_letters):
        print(user_name[char])


def verifying_name(user_name, valid_user_name):
    if user_name == "":
        print("Invalid entry!")
    else:
        valid_user_name = True
    return valid_user_name


main()
