"""Testing the code for the class taxi"""

from prac_08.taxi import Taxi


def main():
    car_one = Taxi("Prius 1", 100)
    print(car_one)
    car_one.drive(40)
    print(car_one)
    car_one.start_fare()
    car_one.drive(100)
    print(car_one)
    print(car_one.get_fare())



main()