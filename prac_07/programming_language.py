"""ProgrammingLanguage class"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object"""

    def __init__(self, name='', typing='', reflection='', year=0):
        """Initialise a programming language instance """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Set the default printing for class"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        """Checks if language is dynamically typed"""
        if self.typing == 'Dynamic':
            return True
        else:
            return False
