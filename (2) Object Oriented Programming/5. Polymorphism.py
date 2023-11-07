'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Polymorphism in Python
---------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
# Polymorphism in Python differs from statically-typed languages like C++ or Java. Python's dynamic typing system eliminates the need for explicit type declarations. Polymorphism, the ability of functions or methods to work with multiple argument types, naturally emerges in Python due to this dynamic typing. The interpretation of a method depends on the object's type or class, a determination made by Python at runtime, referred to as runtime binding.


'''
Dynamic Typing
_______________
'''
# In Python, variables acquire their types based on the values they hold. For example, when you use `abs(x)`, Python assumes that `x` is a number. This informal typing is a distinctive characteristic of Python.


'''
Handling Different Types
________________________
'''
# Python's dynamic typing allows you to manage objects of diverse types flexibly. You can employ a single function to achieve polymorphism.
# Example
class PolymorphismHandler:
    def handle_int(self, arg_int):
        print(f"{arg_int} is an integer")

    def handle_str(self, arg_str):
        print(f"{arg_str} is a string")

    def handle(self, arg):
        if isinstance(arg, int):
            self.handle_int(arg)
        elif isinstance(arg, str):
            self handle_str(arg)
        else:
            print(f"{arg} is neither a string nor an integer")

p = PolymorphismHandler()
p.handle(10)
p.handle("Albatross!!")


'''
Avoiding Method Overloading
____________________________
'''
# Python does not support method overloading in the same manner as languages like C++. Creating multiple methods with the same name but varying argument signatures won't work as expected.
# Example
class PolymorphismError:
    def __init__(self):
        print('No arguments!')

    def __init__(self, args):
        print('One argument!')
        self.args = args

x = PolymorphismError()  # This leads to a TypeError


'''
Using Default Arguments
________________________
'''
# Python does not support method overloading based on argument count or types. To address this situation, you can use default arguments or explicitly inspect argument types. You can implement constructors or methods with default arguments in Python.
# Example
class Animal:
    def __init__(self, name="Parrot"):
        self.name = name

    def print_animal(self):
        print(self.name)

p1 = Animal()
p1.print_animal()  # Output: Parrot

p2 = Animal("Monkey")
p2.print_animal()  # Output: Monkey


'''
Handling Unspecified Types
__________________________
'''
# To initialize a variable without imposing a specific object type, you can employ `None`.
# Example
class Animal:
    def __init__(self, name=None):
        self.name = name

    def print_animal(self):
        print(self.name)

a1 = Animal()
a2 = Animal("Tiger")

a1.print_animal()  # Output: None
a2.print_animal()  # Output: Tiger
