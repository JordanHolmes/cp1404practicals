import math

square_numbers = 0
x = int(input("x value: "))
y = int(input("y value: "))

while x > y:  # input validation loop, otherwise range function doesnt work.
    print(""""Invalid numbers, y must be larger than x""")
    x = int(input("x value: "))
    y = int(input("y value: "))

MENU = """(E)ven numbers between x and y
(O)dd numbers between x and y
(S)quares between x and y
(Q)uit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "E":
        for i in range(x, (y + 1)):
            if i % 2 == 0:
                print("{:4}".format(i))
    elif choice == "O":
        for i in range(x, (y + 1)):
            if i % 2 == 1:
                print("{:4}".format(i))
    elif choice == "S":
        for i in range(x, (y + 1)):
            if math.sqrt(i) % 2 == 0 or math.sqrt(
                    i) % 2 == 1:  # floats that are divided by 2 should return a float remainder
                print("{:4}".format(i))  # square root of a square must be a integer
                square_numbers += 1
        if square_numbers == 0:
            print("No square numbers between{:4} and{:4}".format(x, y))
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished")
