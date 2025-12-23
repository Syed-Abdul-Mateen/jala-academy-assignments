# Create a sub class for an abstract class and access non-abstract methods

from abstract_base import Vehicle

class Bike(Vehicle):

    def speed(self):
        print("Speed is 80 km/h")
