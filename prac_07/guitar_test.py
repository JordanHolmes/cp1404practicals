"""Testing the guitar class and methods"""

from prac_07.guitar import Guitar


def main():
    gibson_l5_ces = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012, 4206.9)

    gibson_l5_ces_age = gibson_l5_ces.get_age()
    gibson_l5_ces_vin = gibson_l5_ces.is_vintage()
    another_guitar_age = another_guitar.get_age()
    another_guitar_vin = another_guitar.is_vintage()

    print("""{0} get_age() - Expected 95. Got {2}
{1} get_age() - Expected 5. Got {3}

{0} is_vintage() - Expected True. Got {4}
{1} is_vintage() - Expected False. Got {5}""".format(gibson_l5_ces.name, another_guitar.name, gibson_l5_ces_age,
                                                          another_guitar_age, gibson_l5_ces_vin, another_guitar_vin))


main()
