inputed_strings = []
repeated_strings = []

user_string = input("Enter a string: ")
while user_string != "":
    if user_string in inputed_strings:
        repeated_strings.append(user_string)
    inputed_strings.append(user_string)
    user_string = input("Enter a string: ")
print("Repeated strings: {}".format(repeated_strings))

# TODO: format repeated words in string format
