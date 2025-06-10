"""
    Classes are blueprints for creating objects
    They define the structure and behavior (attributes and methods)
    that the created objects will have.

    Objects are instances of classes.
    Each object can have its own unique values
    for the attributes defined in the class,
    but they all share the same structure and behavior as specified by the
    class.
"""


class Car:
    def __init__(self, brand, model, colour, year):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.year = year

    def start(self):
        print(f"The {self.colour} {self.brand} {self.model} is starting.")

    def stop(self):
        print(f"The {self.colour} {self.brand} {self.model} is stopping.")


# Creating an instance of the Car class
myCar = Car("Toyota", "Corolla", "blue", 2020)
myCar.start()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Creating an instance of the Person class
p1 = Person("John", 30)
p1.greet()
