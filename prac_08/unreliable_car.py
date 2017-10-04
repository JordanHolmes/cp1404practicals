"""Class module for UnreliableCar"""

from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Represent a UnreliableCar object"""

    def __init__(self, name, fuel, reliability=50):
        """Initialise a UnreliableCar instance"""
        super().__init__(name, fuel)
        self.odometer = 0
        self.reliability = float(reliability)

    def __str__(self):
        """Default printing for UnreliableCar"""
        return "{}, reliability={:.2f}%".format(super().__str__(), self.reliability)

    def drive(self, distance):
        car_random = randint(0, 100)
        if self.reliability >= car_random:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance
        else:
            return distance
