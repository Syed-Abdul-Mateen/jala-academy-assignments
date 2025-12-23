# Create an abstract class with abstract and non-abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def speed(self):
        pass

    def fuel_type(self):
        print("Petrol")
