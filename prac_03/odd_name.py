"""Jordan Holmes"""


def main():
    valid_user_name = False
    user_name = str()
    while valid_user_name is not True:
        user_name, valid_user_name = get_name(user_name, valid_user_name)
    frequency_of_letters = int(input("How frequently do you want to skip letters?: "))
    prints_the_name(user_name, frequency_of_letters)


def prints_the_name(user_name, frequency_of_letters):
    for char in range(0, (len(user_name) + 1), frequency_of_letters):
        print(user_name[char])


def get_name(user_name, valid_user_name):
    user_name = str(input("What is your name?: "))
    if user_name == "":
        print("Invalid entry!")
    else:
        valid_user_name = True
    return user_name, valid_user_name


main()
