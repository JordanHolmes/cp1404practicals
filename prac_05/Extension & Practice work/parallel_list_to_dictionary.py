"""
CP1404 practical
name to date of birth dictionary
display individual ages
"""

names_to_dobs = {}

for i in range(4):
    user_name = input("Please enter your name: ")
    user_dob = input("Enter you date of birth (eg. 16/07/1997): ").split("/")
# TODO: turn the string ('16', '07', '1997') into integers (16, 07, 1997)
    names_to_dobs[user_name] = user_dob

print(names_to_dobs)
