'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Classes in Python
---------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
# In Python, a class is a user-defined data type. Classes are defined using the `class` keyword.
# Class definitions start with the `class` keyword and contain valid Python statements for defining class constants and methods.


'''
_________________________________________________________________________________________________
Defining a Class
_________________________________________________________________________________________________
'''
# You can define a class from scratch like this:
# class ClassName:
    # Class statements


# Alternatively, you can create a new class that inherits properties from other classes, known as subclassing:
# class SubclassName(BaseClass):
    # Class statements


'''
_________________________________________________________________________________________________
Class Methods 
_________________________________________________________________________________________________
'''
# Methods are how you call functions in a class. All methods in a class must start with the `def` keyword. 
# Every method has `self` as the first argument in the method header, representing the object itself.

class MyClass:
    def __init__(self):
        # Constructor method

    def some_method(self):
        # Regular method


'''
_________________________________________________________________________________________________
Class Variables
_________________________________________________________________________________________________
'''
# A class can also contain class variable assignments that are shared by all instances of the class. 
# Class variables are useful for defining default values for instances.

class MyClass:
    class_variable = 20  # Class variable

    def __init__(self):
        self.instance_variable = MyClass.class_variable  # Instance variable


'''
_________________________________________________________________________________________________
Accessing Attributes
_________________________________________________________________________________________________
'''
# To reference an attribute within a class, use either `self.attribute` or `classname.attribute`. 
# The `self.attribute` syntax is used to avoid ambiguities between instance variables and local variables.

class MyClass:
    def __init__(self, value=None):
        self.instance_variable = value

obj = MyClass()
print(obj.instance_variable)


'''
_________________________________________________________________________________________________
Special Methods
_________________________________________________________________________________________________
'''
# Python has special methods that start and end with double underscores and can be overridden to customize behavior.
# Common special methods include:

# - `__init__(self)`: Constructor method
# - `__str__(self)`: Customizes the object's string representation
# - `__repr__(self)`: Returns a readable representation of the object
# - `__add__(self, other)`: Defines the behavior of the `+` operator
# - `__sub__(self, other)`: Defines the behavior of the `-` operator
# - `__call__(self)`: Allows instances to be callable like functions

 
'''
_________________________________________________________________________________________________
Operator Overloading
_________________________________________________________________________________________________
'''
# Python allows you to implement operators for a class by defining special methods like `__add__` and `__sub__`. 
# This feature is called operator overloading and enables customization of how operators work for your class instances.

class MyClass:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value

obj1 = MyClass(5)
obj2 = MyClass(3)
result = obj1 - obj2  # Customized subtraction operator
print(result)

 
'''
_________________________________________________________________________________________________
Instance Attributes
_________________________________________________________________________________________________
'''
# Instance attributes are accessible using `obj.__dict__`, `obj.__class__`, and other methods.
# They provide information about the instance and its attributes.


'''
_________________________________________________________________________________________________
Checking Types and Subclasses
_________________________________________________________________________________________________
'''
# You can use `isinstance()` to check if an object is an instance of a class and `issubclass()` to check if a class is a subclass of another class. 
# These built-in functions are part of Python's standard library.

class MyParent:
    pass

class MyChild(MyParent):
    pass

obj = MyChild()

is_instance = isinstance(obj, MyChild)  # Check if obj is an instance of MyChild
is_subclass = issubclass(MyChild, MyParent)  # Check if MyChild is a subclass of MyParent
