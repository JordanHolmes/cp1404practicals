""""""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    ongoing_message_header = "Taxis available:"
    final_message_header = "Taxis are now:"

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            display_taxis(ongoing_message_header, taxis)
            user_car = taxis[int(input("Choose taxi: "))]
            display_current_bill(total_bill)
        elif menu_choice == "D":
            user_car.start_fare()
            user_car.drive(int(input("Drive how far? ")))
            print("Your {} trip cost you ${:.2f}".format(user_car.name, user_car.get_fare()))
            total_bill += user_car.get_fare()
            display_current_bill(total_bill)
        else:
            print("Invalid menu choice!")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("Total trip cost: ${:.2f}".format(total_bill))
    display_taxis(final_message_header, taxis)


def display_taxis(header, taxis):
    print(header)
    for index, taxi in enumerate(taxis):
        print("{} - {}".format(index, taxi))


def display_current_bill(total_bill):
    print("Bill to date: ${:.2f}".format(total_bill))


main()
