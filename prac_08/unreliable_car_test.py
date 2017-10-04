"""Testing for the class UnreliableCar"""

from prac_08.unreliable_car import UnreliableCar


def main():
    car_one = UnreliableCar(name="Boom tube", fuel=100)
    assert car_one.name == "Boom tube", "Name is not set as 'Boom tube'"
    assert car_one.fuel == 100, "Fuel is not set as 100"
    print(car_one)
    car_one.drive(30)
    print(car_one)
    car_one.drive(40)
    print(car_one)
    car_one.drive(10)
    print(car_one)
    car_one.drive(5)
    print(car_one)


main()
