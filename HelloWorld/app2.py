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
class Animal:  # parent, base
    # constructor
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):  # child, sub
    def walk(self):
        print("walk")


class Fish(Animal):  # fish eats but doesn't walk
    def swim(self):
        print("swim")


m = Mammal()  # create a Mammal object; it has the age attribute automatically
m.eat()
print(m.age)
