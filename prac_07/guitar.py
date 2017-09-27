"""Guitar class"""


class Guitar:
    """Represent a Guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance"""

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Set the default printing for class"""

        return "{} ({}) : {:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Calculate the age of a guitar"""

        age = 2017 - self.year
        return age

    def is_vintage(self):
        """Use age to check if vintage"""

        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False
