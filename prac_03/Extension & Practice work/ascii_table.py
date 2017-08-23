# UPPER_LIMIT = 127
# LOWER_LIMIT = 33
#
# MENU = """(C)haracter to ASCII code
# (A)SCII code to character
# (Q)uit"""
# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         user_character = input("Enter a character: ")
#         ascii_value = ord(user_character)
#         print("The ASCII code for {} is {}".format(user_character, ascii_value))
#     elif choice == "A":
#         user_number = int(input("Enter a number between 33 and 127: "))
#         while user_number < LOWER_LIMIT or user_number > UPPER_LIMIT:
#             print("Invalid selection, must be a number between {} and {}".format(LOWER_LIMIT, UPPER_LIMIT))
#             user_number = int(input("Enter a number between 33 and 127: "))
#         output_character = chr(user_number)
#         print("The character for {} is {}".format(user_number, output_character))
#     else:
#         print("Invalid choice!")
#     print(MENU)
#     choice = input(">>> ").upper()
# print("Finished")


lower_limit = int(input("Lower limit of table: "))
upper_limit = int(input("Upper limit of table: "))

for i in range(lower_limit, upper_limit + 1):
    character = chr(i)
    print("{:3} {:>6}".format(i, character))

    # TODO: Create columns? ask for how many columns to print
