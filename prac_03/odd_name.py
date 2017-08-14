"""Jordan Holmes"""

valid_user_name = False
user_name = str

while valid_user_name is not True:
    user_name = str(input("What is your name?: "))
    if user_name == "":
        print("Invalid entry!")
    else:
        valid_user_name = True

for char in range(0, (len(user_name) + 1), 2):
    print(user_name[char])
