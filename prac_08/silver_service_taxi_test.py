"""Testing for the class SilverServiceTaxi"""

from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    car_one = SilverServiceTaxi("Test", 100, 2)
    assert car_one.name == "Test", "Name has not been set as Test"
    assert car_one.fuel == 100, "Fuel has not been set as 100"
    # assert car_one.fanciness == 1, "Default fanciness has not been set properly"
    print("${:.2f}/km".format(car_one.price_per_km))
    assert car_one.flagfall == 4.50, "Default flagfall has not been set properly"
    car_one.drive(60)
    print("${:.2f}".format(car_one.get_fare()))
    car_two = SilverServiceTaxi("Hummer", 200, 4)
    print(car_two)
    car_one.start_fare()
    car_one.drive(18)
    print("${:.2f}".format(car_one.get_fare()))

main()
