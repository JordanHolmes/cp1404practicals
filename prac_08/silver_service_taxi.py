"""SilverServiceTaxi class"""

from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi object"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=1):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

