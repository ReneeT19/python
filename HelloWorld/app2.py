# CLASSES - blueprint for creating new objects
# Object: - instance of a class
# Class: Human
# Object: John, Mary, Jack

# variable and function - lowercase; class - uppercase for the first letter of each word and no _
# # create custom class
# class Point:
#     # class level attribute - shared across all instances of a class
#     default_color = "red"

#     # create constructor
#     # magic method
#     # at least one parameter, self by convention; # self is the reference to the current object
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # magic method
#     def __str__(self):
#         return f"({self.x},{self.y})"

#     # compare objects magic method
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     # both def methods above are instance methods, call them using instance.methodname()
#     # class method (it has to go here):

#     @ classmethod
#     def zero(cls):  # convention; a reference to the class itself
#         return cls(0, 0)  # same as calling Point(0,0)

#     def draw(self):   # all functions within a class should have at least one parameter; self is the current object Point(1,2)
#         print(f"Point ({self.x},{self.y})")

# # point = Point()   # returns a point object
# # print(type(point))  # main is the name of the module
# # print(isinstance(point, Point))   # point is an object of Point


# # will change the class level attribute for all instances point and another_point
# Point.default_color = "yellow"
# # no need to pass argument for self as Python does it for us so just pass x and y
# point = Point(1, 2)
# # define attributes (x,y,z are instance attributes that belong to point instance or point object)
# point.z = 10
# point.draw()  # no need to pass argument in the draw method as Python does it by default
# print(point.x)

# another_point = Point(3, 4)
# another_point.draw()
# print(another_point.default_color)

# print(point.default_color)  # two ways to get the class attribute
# print(Point.default_color)  # use Point class to access the attribute

# new_point = Point.zero()
# new_point.draw()

# # TAKEAWAY:
# # A method defined in a class should have at least one parameter, by convention called self, referencing the current object
# # When calling a method of an object, no need to pass argument as Python does it for us
# # You will use the instance attributes most of the time (x,y,z) but sometimes you want to use the class level attribute that can be shared across the instances (default_color)

# # Python 3 magic methods - a guide to Python's magic methods: _str_(self) is useful
# print(str(point))

# # compare objects - can't use == as it compares the memory spot which two objects with same attributes are two memory spots
# point1 = Point(1, 2)
# point2 = Point(10, 20)
# print(point == point1)
# print(point1 < point2)  # you can use the < without implementing another method

# # arithmetic operations - use magic method
# print(point + point1)
# combined = point + point1
# print(combined.x)


# # CUSTOMER CONTAINERS
# class TagCloud:
#     # use dictionary and start with a constructor
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag):
#         # get an item by this key and apply a default value if we don't have it
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):  # key is tag in this case
#         return self.tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):  # key is tag, value is count
#         self.tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.tags)

#     def __iter__(self):
#         # make it durable and iterate in a for loop; get one item at a time from the container and iterate over self.tags
#         return iter(self.tags)


# cloud = TagCloud()  # create a cloud object
# # uppercase or lowercase matter in dictionary but we can take out the case sensitivity above by setting to lower()
# # use getitem magic method, easily get the item with given tag python by implementing the method; use setitem magic method to assign a count value 10 to it
# cloud["python"] = 10
# len(cloud)  # get the number of items in the TagCloud by implememting the len magic method
# cloud.add("pyThon")
# cloud.add("python")
# cloud.add("python")
# print(cloud.tags)


# PRIVATE MEMBERS
# cloud.__tags to prevent accident access to private members; you can access them by using cloud._TagCloud_tags and change all the tags to __tags

# properties - before the attribute
# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property   # to build the getter
#     def price(self):
#         return self.__price

#     @price.setter  # to build the setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value

#     # four parameters are optional; return a property object; getter and setter
#     # price = property(get_price, set_price)


# product = Product(-10)
# # product.price = -1
# print(product.price)


# Inheritance
# class Animal(object):  # parent, base
#     # object class that is the base object class that other classes can inherit from
#     # constructor
#     def __init__(self):
#         print("Animal constructor")
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):  # child, sub
#     def __init__(self):
#         super().__init__()
#         print("Mamml constructor")
#         self.weight = 2  # method overriding; the self.age attribute is not executed in this case; if we want to call the animal constructor we insert super()
# # you can also call the super after the self.weight to change the order of execution

#     def walk(self):
#         print("walk")


# class Fish(Animal):  # fish eats but doesn't walk
#     def swim(self):
#         print("swim")


# m = Mammal()  # create a Mammal object; it has the age attribute automatically
# m.eat()
# print(m.age)

# # object class
# print(isinstance(m, Mammal))  # true
# print(isinstance(m, Animal))  # true as well as mammal inherits from animal
# # returns true because mammal indirectly inherits from the object class
# print(issubclass(Mammal, object))

# Method overriding
# a constructor in mammal class that has a different attribute weight

# Multi-level inheritance - limit it to 2 levels cause if you have more than that you are complicating the problem
# Below is an example of multi-level inheritance which is not recommended
# class Animal:
#     def eat(self):
#         print("eat")


# class Bird(Animal):
#     def fly(self):
#         print("fly")


# class Chicken(Bird):

# # Multiple Inheritance - use with caution
# class Employee:
#     def greet(self):
#         print("Employee greet")


# class Person:
#     def greet(self):
#         print("Person greet")


# class Manager(Employee, Person):  # if you change the order it will execute person first
#     pass


# manager = Manager()
# manager.greet()  # if employee has greet method it executes that first

# a good example of inheritance - no multi-level or multiple inheritance
# # Python doesn't have this built in so we customize it
# from abc import ABC, abstractmethod


# class InvalidOpeationError(Exception):
#     pass


# class Stream:
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOpeationError("Stream is already open.")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOpeationError("Stream is already closed.")
#         self.opened = False


# class FileStream(Stream):
#     def read(self):
#         print("Read data from a a file.")


# class NetworkStream(Stream):
#     def read(self):
#         print("Read data from a a network.")


# Polymorphism - many forms; useful for forms that takes different content at runtime like a form taking button, textbox, list, etc.

# from abc import ABC, abstractmethod


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")


# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")


# def draw(controls):
#     for control in controls:  # objects have to be iterable like string, list, etc.
#         control.draw()  # depending on the object you work with at runtime, this draw method takes different forms


# ddl = DropDownList()
# tb = TextBox()
# draw([ddl, tb])

# Built-in Method


# from collections import namedtuple


# class Text(str):  # the built-in str class
#     def duplicate(self):
#         return self + self


# text = Text("Python")
# print(text.lower())
# print(text.duplicate())


# class TrackableList(list):  # the built-in list class
#     def append(self, object):
#         print("Append called")
#         super().append(object)


# list = TrackableList()
# list.append("1")

# Data Classes


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # after adding this method it will return true

    def __eq__(self, other):
        return self.x == other.x and self.y == other.

    p1 = Point(1, 2)
    p2 = Point(1, 2)
    # false as they are stored in different locations; look at the id locations below for proof
    print(p1 == p2)
    print(id(p1))
    print(id(p2))


# tedious above, look at the code below:

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)  # use keyword arguments to make the code easier to read
print(p1.x)  # the tuple can't be altered; we need to create a new object to alter it p1 = Point(x=2, y=3) for example
p2 = Point(x=1, y=2)
print(p1 == ps)

# if you work with only data no methods, use tuple like above
