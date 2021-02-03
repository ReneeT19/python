# CLASSES - blueprint for creating new objects
# Object: - instance of a class
# Class: Human
# Object: John, Mary, Jack

# variable and function - lowercase; class - uppercase for the first letter of each word and no _
# create custom class
class Point:
    # create constructor
    # magic method
    # at least one parameter, self by convention; # self is the reference to the current object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):   # all functions within a class should have at least one parameter; self is the current object Point(1,2)
        print(f"Point ({self.x},{self.y})")

# point = Point()   # returns a point object
# print(type(point))  # main is the name of the module
# print(isinstance(point, Point))   # point is an object of Point


# no need to pass argument for self as Python does it for us so just pass x and y
point = Point(1, 2)
point.draw()  # no need to pass argument in the draw method as Python does it by default
print(point.x)

# TAKEAWAY:
# A method defined in a class should have at least one parameter, by convention called self, referencing the current object
# When calling a method of an object, no need to pass argument as Python does it for us
