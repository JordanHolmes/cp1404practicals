name = str(input("Enter your name: ")).capitalize()
MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello {}".format(name))
    elif choice == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid message")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished")
