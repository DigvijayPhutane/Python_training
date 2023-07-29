""""""
"""

class Car:
    def __init__(self, model, color ):
        self.model = model
        self.color = color
    def displayCar(self):
        print(self.model)
        print(self.color)
____________________________________
"""
from Car import Car
  # lets start using the class

car1 = Car("Tesla", "Red")

car1.displayCar()

car2 = Car("Ford", "Green")

print(car2.model)
print(car2.color)

car3 = Car("Volvo", "Blue")

print(car3.model)
print(car3.color)
car3.color="Black"
car3.displayCar()

