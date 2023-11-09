'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Metaclasses in Python
---------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
# Metaclasses are an advanced concept in Python that allow you to control and customize the creation of classes. To make this concept more approachable, let's break it down into simpler terms: Think of classes as templates for creating objects. You create instances (objects) from these templates. Metaclasses are like templates for creating these templates (classes). They give you the ability to customize how classes are created.

# Example
class MetaClass(type):
    def __init__(cls, name, bases, attrs):
        super(MetaClass, cls).__init__(name, bases, attrs)

class MyClass(metaclass=MetaClass):
    class_var = 10

    def __init__(self, value):
        self.instance_var = value

my_instance = MyClass(42)
print(my_instance.class_var)  # Accessing a class variable
print(my_instance.instance_var)  # Accessing an instance variable


# In above example:
# -> `MetaClass` is a metaclass that derives from the built-in `type` metaclass.
# -> When we define `MyClass` and set its metaclass to `MetaClass`, we are effectively using `MetaClass` as a template to create our class.
# -> The `__init__` method in `MetaClass` is called when `MyClass` is created, allowing us to customize the class's attributes and behavior.
# -> When you create an instance of `MyClass`, it behaves just like any other class, but you've used a metaclass to influence how it was created. This gives you a way to customize class creation, which can be valuable in certain situations.

# It's important to note that metaclasses are a powerful and advanced Python feature, and they may not be necessary for most programming tasks. However, they can be incredibly useful when you need to control class creation and behavior at a deeper level.
