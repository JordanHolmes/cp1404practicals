""" """

def main():

    guitars = []
    users_name = input("Name: ")
    users_year = input("Year: ")
    users_cost = input("Cost: $")
    

    for i, guitar in enumerate(guitars):
        print("Guitar {}: {} ({}), worth ${:.2f} {}".format(i+1, guitar.name, guitar.year, guitar.cost, vintage_string))