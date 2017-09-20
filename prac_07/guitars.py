""" """

from prac_07.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    blank_name = False
    while not blank_name:
        users_name = input("Name: ")
        if users_name == '':
            blank_name = True
        else:
            users_year = int(input("Year: "))
            users_cost = float(input("Cost: $"))
            guitar = Guitar(users_name, users_year, users_cost)
            guitars.append(guitar)
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.4))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(
            "Guitar {0}: {self.name:>20} ({self.year}), worth ${self.cost:10,.2f} {1}".format(i + 1, vintage_string,
                                                                                              self=guitar))


main()
