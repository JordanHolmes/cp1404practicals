from prac_07.car import Car


def main():
    hotrod = Car("Hot Rod")

    print(hotrod)
    add_fuel(hotrod)


def add_fuel(Car):
    amount_of_added_fuel = input("How many units of fuel do you want to add to the car? ")
    valid_input = check_if_integer(amount_of_added_fuel)
    while valid_input is False:
        print("Fuel amount must be >= 0")
        amount_of_added_fuel = input("How many units of fuel do you want to add to the car? ")
        valid_input = check_if_integer(amount_of_added_fuel)

    Car.add_fuel(amount_of_added_fuel)
    print("Added {} units of fuel".format(amount_of_added_fuel))
    print(Car)


def check_if_integer(users_input):
    try:
        if int(users_input) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


main()
