
class Plant:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


# This class is inheriting from the Plant class
# Petals are only going to the flower class
# You cannot create a subclass without first creating an instance of the superclass
# The init method of the sub class will always call the init method of the superclass

class Flower(Plant):
    def __init__(self, color, petals):
        Plant.__init__(self, color)

        self.__petals = petals

    def get_petals(self):
        return self.__petals
