"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When anything other than a value is entered
        eg. float, or string
2. When will a ZeroDivisionError occur?
    When the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, by adding an input validation loop
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:  # #Input validation loop
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero!")
except ValueError:  # #If float or string is entered
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
