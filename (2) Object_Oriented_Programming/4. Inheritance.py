'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Inheritance in Python
---------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
# Inheritance serves as a fundamental concept within object-oriented programming. It enables one class to inherit attributes and methods from another. This process is termed subclassing. 


'''
Subclassing and Base Classes
_____________________________
'''
# Subclassing involves creating a new class that inherits attributes and methods from another class known as the base class or superclass.
# In Python, base classes are denoted within parentheses in a subclass header with commas separating them.
# Within a subclass, we can override methods inherited from the base class.


'''
Creating Class in Python
__________________________
'''
# We can create Python class from scratch:
# Example
class A:
    pass

# Single inheritance allows a class to inherit from a single base class:
# Example
class B(A):
    pass

# Multiple inheritance facilitates a class inheriting from several base classes:
# Example
class D(B, C):
    pass


'''
Real-World Example: Vehicle and Car Classes
___________________________________________
'''
# Base Class: Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model}'s engine is now running.")

    def stop_engine(self):
        self.is_running = False
        print(f"The {self.year} {self.make} {self.model}'s engine is now stopped.")

# Subclass: Car
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.is_accelerating = False

    def accelerate(self):
        self.is_accelerating = True
        print(f"The {self.year} {self.make} {self.model} is accelerating.")

    def brake(self):
        self.is_accelerating = False
        print(f"The {self.year} {self.make} {self.model} is braking.")

# Create instances of Vehicle and Car
my_vehicle = Vehicle("Toyota", "Camry", 2022)
my_car = Car("Tesla", "Model 3", 2023, "Electric")

# Interact with the classes
my_vehicle.start_engine()
my_car.start_engine()
my_car.accelerate()
my_vehicle.stop_engine()
my_car.brake()
