# import io
# file = io.open('twitter.csv', "w", encoding="utf-8")

# print('Hello World')
# print('*' * 10)
# print("Hi")

# Python variables - numbers, strings, and booleans
# age = 20
# price = 19.95
# first_name = "Soren"   # use _ to declare variable names
# is_online = True   # Python is case sensitive
# print(age)
# print(first_name)
# print(is_online)

# Exercise
# name = input("What is your name? ") # take user input in Python
# print("Hello " + name)

# Convert variable type
# birth_year = input("Enter your birth year: ")
# age = 2020 - int(birth_year)     # convert string to integer
# print(age)
# built-in methods in Python for converting type of varibles: int(), float(), bool(),str()
# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# Exercise
# first = input("First number is: ")
# second = input("Second number is: ")
# sum = int(first) + float(second)  # you can also convert the type in line 24 by using int(input(""))
# print("The sum of two numbers is: " + str(sum))

# # Python Strings - string is an object and has built-in methods that belong to the object
# course = "Python for Beginners"
# print(course.upper())  # upper method doens't change the original string but returns a new string
# print(course.find("y"))  # find contains a char or a sequence of a char; returns the index of the first finding of y
# # index in Python starts with 0
# print(course.title())  # prints the course string
# print(course.find("for")) # returns the index of the first letter found in the sequence of characters
# print(course.replace("for", "4"))  # won't modify the original string but return a new string as string is immutable
# print(course.find("Python"))
# print("Python" in course) # the same as line 36 # returns true or false   you can use not in as well
# print(course.strip())  # removes the white spaces on the beggining and the end; you can do lstrip for left space or rstrip for right space

# escape sequence  \"   \'  \\  \n
# course = "Python \"Programming"
# print(course)

# # format strings
# first = "Renee"
# last = "Thomsen"
# full = f"{first} {last}"   # equavilent to concactenation
# full_length = f"{len(first)} {2 + 2}"
# print(full)
# print(full_length)


# Numbers and Arithmetic Operators
# integer: x = 1, float: x = 1.1, complex number: x = 1 + 2j
# print(10 * 3)
# print(10 / 3)  #use // to get an integer
# print(10 % 3)
# print(10 ** 3) #10 to the power of 3
# print(round(2.9))  # will get 3
# print(abs(-2.9))   # will get 2.9
# you can import math on the top of a project
# print(math.ceil(2.2))  # get 3

# x += 3
# boolean expression
# x = 3 > 2
# logical operators - and, or, not
# price = 25
# print(price > 10 and price <30) # or
# print(not price > 10)

# chain comparison operators - the same as how we do it in math
# if 18 <= age < 65:
# print("Eligible")


# if statement
# tem = 45
# if tem > 30:
#     print("It's a hot day")
# elif tem > 20:
#     print("It's a nice day")
# elif tem > 10:
#     print("It's a bit cold")
# else:
#     print("It's cold")
# print("Done")

# ternary operator
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

# Exercise
# weight = float(input("What is your weight? "))
# measurement = input("(K)g or (L)bs: ")
# if measurement.upper() == "L":
#     print("Weight in Kg is: " + str(weight * 0.45359237))
# elif measurement.upper() == "k":
#     print("Weight in lbs is: " + str(weight / 0.45359237))
# else:
#     print("Not valid measurement input")
# print("Finished")

# while loop
# i = 1
# while i <= 10: # 1_000 for readability
#     print(i * "*")
#     i += 1
# command = ""
# while command.lower() != "quit":  # takes both uppercase and lowercase
#     command = input(">")
#     print("ECHO", command)

# infinite loops
# while True:  # no need to define command here
#     command = input(">")
#     print("ECOH", command)
#     if command.lower() == "quit":
#         break

# Exercise
# for number in range(2, 10, 2):
#     print(number)
# print("We have 4 even numbers")

# # another way to do it
# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We have {count} even numbers.")

# lists
# primitive variables: int, float, string, boolean
# names = ["Soren", "Renee", "Erik"] #add multiple objects inside the brackets
# print(names)
# # get individual element from the list
# print(names[2])
# you can use negative index in Python - the last element from the last of the list
# print(names[-1])
# # reset the value
# names[0] = "S"
# print(names)
# # return all elements starting from 0 but not 2; it doesn't modify the original list but reset value will change the original list
# print(names[0:2])
# print(names[0:])  #will print the whole thing
# print(names[:3])   #will print everything before the 3rd character
# print(names[:])   #will print the copy of the original string
# print(names)


# for loops
# numbers = [1,2,3,4,5]
# for item in numbers:
#     print(item)
# # equivalent while loop below, but for loop is more concise
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1

# for number in range(3):
# print("Attempt", number + 1, (number + 1) * ".")
# or
# for number in range(1, 4):    ## you can change to range(1,10,2) to only print every 2nd number starting from 1 and ending before 10
# print("Attempt", number, number * ".")

# for else
# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")

# nested loop
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")


# range() function - generate a sequence of numbers
# numbers = range(5,10,2)  # (5) return a range object 0-4; (5,10) returns a range object 5-9
# # for number in numbers: another way to do it is in line 120 so two lines can solve the problem
# for number in range(5):
#     print(number)

# iterables
# print(type(5))
# print(type(range(5)))  # range is one example of complex types in Python
# for x in [1, 2, 3, 4, 5]:     # could be list of strings
#     print(x)


# Functions
# def greet():
#     print("Hi there")
#     print("Welcomd aboard")


# greet()  # call the function


# def greet2(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")


# greet2("Renee", "Thomsen")
# # if you put the line 233 into a print function it prints None in terminal but if you have return keyword in the function body it won't print None

# # functions that perform a task
# # functions that return a value (not something to print in terminal but returns a value that can be printed or use built-in methods such as open and write)


# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("Soren")
# file = open("content.txt", "w")
# file.write(message)


# # 3 keyword arguments
# def increment(number, by):
#     return number + by


# print(increment(2, 1))  # or store it in a variable result
# # to make it more readable:
# print(increment(2, by=1))  # by=1 is a keyword argument

# # default argument


# def increment2(number, by=1):  # default by 1 but you can alter it in the function call
#     return number + by


# print(increment2(2))


# xargs
# def multiple(x, y):  # only takes two parameters
# return x * y

# def multiple(*numbers):  # takes any number of parameters
#     total = 1
#     for number in numbers:
#         total *= number
#         # the indention is important; indented: result 6; not indented: result 1 (use debugging)
#     return total


# # debugging: added debugger extension and create json file based on your file type
# # print(multiple(2, 3, 4, 5))

# print("Start")  # F9 to set a breakpoint; F5 to start debugging; f10 to go through the lines one by one, if it's not shown on the left side, it's not executed; f11
# print(multiple(1, 2, 3))

# # dioctionary - another complex variable type

# def save_user(**user):  # pass multiple key value pairs or keyword argument functions and Python will package them into a dictionary
#     print(user["name"])


# save_user(id=1, name="R", age=10)


# Scope
# message = "a"  # global variable; try to avoid using it


# def greeting(name):
#     message = "b"  # local variable


# greeting("Renee")
# print(message)  # will print a


# Fizz Buzz Exercise
# def fizz_buzz(input):
#     if input % 15 == 0:
#         return "Fizz_Buzz"
#     elif input % 5 == 0:
#         return "Buzz"
#     elif input % 3 == 0:
#         return "Fizz"

#     return input


# print(fizz_buzz(15))


# LIST
# numbers = [1,2,3,4,5]
# numbers.append(6)  # add an element to the end of the list
# numbers.insert(2,-1)  # type of object is T which means any type # the first parameter is where you want to insert the value
# numbers.remove(1)  3 use .pop() to remove items by index
# print(1 in numbers) # whether a value exists in the list
# print(len(numbers)) # how many elements are in the list
# del numbers[0:2] # delete a range of elements
# numbers.clear() # remove all
# print(numbers)

# letters = ["a", "b", "c"]
# # letters[0] = "A"  # modify the list
# # print(letters[0])
# # print(letters[0:2])
# # print(letters[::2])  # return every second element
# print(letters.index("a"))  # to find something
# print(letters.count("a"))

# # loop over the list
# # returns a tumple that has index and the value
# for index, letter in enumerate(letters):
#     print(index, letter)


# matrix = [[0, 1], [2, 3]]
# print(matrix)
# zeros = [0] * 5
# combined = zeros + letters
# print(combined)
# # creates a list of numbers from 0 to 20 but not including 20
# numbers = list(range(20))
# print(numbers[::2])
# print(numbers[::-1])  # print in a reverse order
# print(list("Hello World"))  # print chars

# list unpacking
# numbers = [1, 2, 3, 4, 5, 5, 5, 5, 7]
# # first, second, *other = numbers  # pack the rest as other
# first, *other, last = numbers
# print(first, last)
# print(other)

# sort list
# numbers = [3, 5, 1, 8, 2]
# numbers.sort()
# # numbers.sort(reverse=True)  # reverse the order
# print(sorted(numbers))  # you can reverse the order by using (numbers, reverse)
# print(numbers)
# sort tuples
# from collections import deque
# items = [
#     ("Product1", 10),  # a tuple
#     ("Product2", 9),
#     ("Product3", 12),
# ]


# def sort_items(item):
#     return item[1]


# you need to have the key word here to call the function
# items.sort(key=sort_items)
# use lambda expression: key=lambda parameters:expression  and you can delete the sort_item function
# items.sort(key=lambda item: item[1])
# print(items)

# Map function - iterate over iterables - just map prices item[1] - just map item names item[0]
# products = list(map(lambda item: item[0], items))
# prices = list(map(lambda item: item[1], items))
# # equal to prices = [item[1] for item in items] - recommended as it's more readable
# print(products)
# print(prices)


# # filter function - just like map function that takes two parameters
# filtered = list(filter(lambda item: item[1] >= 10, items))
# # equal to filtered = [item for item in items if item[1] >= 10] - recommended as it's more readable
# print(filtered)


# Zip function
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# # returns a zip object that's iterable and prints this [(1, 10), (2, 20), (3, 30)]
# print(list(zip(list1, list2)))
# you can replace list1 with "abc"


# STACK
# # LIFO - LAST IN FIRST OUT
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# # remove the last one from the stack and return it
# print(browsing_session.pop())
# if not browsing_session:  # if the stack is empty
#     print("redirect", browsing_session[-1])


# QUEUE
# FIFO
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()  # remove 1
# print(queue)
# if not queue:  # check if queue is empty
#     print("empty")


# # tuples - use () - immutable - no append, insert,etc. a read-only list; contain a sequence of object
# numbers = (1,2,3)
# print(numbers)
# print(numbers.count(3))

# point = 1, 2
# point2 = ()
# print(type(point))
# print(type(point2))
# point3 = (1, 2) * 3
# print(point3)
# point4 = tuple([1, 2])  # convert a list to a tuple
# print(point4)
# point5 = tuple(["Hi"])
# print(point5)
# print(point5[0:1])
# x, y = point
# if 10 in point:
#     print("exists")


# Swapping variables
# x = 10
# y = 11

# x, y = y, x  # swap in Python
# print(x, y)


# Arrays - large dataset (10,000 or more) - more efficient than list (even though list is used 90% of the cases)
# from array import array  # import the array module

# search for type code in Python    create an object numbers
# numbers = array("i", [1, 2, 3])
# numbers.append(4)
# print(numbers)
# the type is "i" integer so you can't change the value to a float, different from list


# SET - collection with no duplicates - unordered collection - can't be access using index. use list
# numbers = [1, 2, 3, 4, 4]
# first = set(numbers)  # to convert it to set to remove duplicates
# second = {1, 5}  # create a set for practice
# second.add(5)
# second.remove(5)
# len(second)
# print(first)

# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# if 1 in first:
#     print("yes")


# DICTIONARY - collection of key value pairs like a phone book
## list(), tuple(), set(), dict()
# point = {"x": 1, "y": 2}  # use string for the key and integer for the value
# point = dict(x=1, y=2)    # x=1 is a keyword argument
# point["x"] = 10  # can't access items using numeric values
# point["z"] = 20
# print(point)
# if "a" in point:
#     print(point["a"])
# print(point.get("a", 0))  # if no a, return a 0
# del point["x"]
# print(point)
# # iterate dictionary
# for key in point:
#     print(key, point[key])
# # another way to do it
# for key, value in point.items():
#     print(key, value)

# Dictionary comprehension - can be used for set, list, and dictionary, but not tuple
# a list below using comprehension expression
# values0 = [x * 2 for x in range(5)]
# a set below using comprehension expression
# values = {x * 2 for x in range(5)}
# print(values)
# # dictionary using comprehension expression
# values2 = {x: x * 2 for x in range(5)}
# print(values2)


# Generators - what you get when using comprehension expression for tuples; when you deal with big dataset
# unlike list that stores values in memory
# from sys import getsizeof
# values = (x * 2 for x in range(100000))
# # if using list, it takes 824464 bytes of memory while generator takes 120
# print("gen:", getsizeof(values))  # generators have no lens


# Unpacking Operator - unpack any iterables and take out individual variables - unique in Python
# numbers = [1, 2, 3]
# print(*numbers)
# # when creating list
# values = [*range(5), *"Hello"]  # you can unpack a string with the same token
# print(values)

# first = [1, 2]
# second = [3]
# values1 = [*first, "a", *second, *"Hello"]
# print(values1)

# first1 = {"x": 25}
# second1 = {"x": 10, "y": 2}
# combined = {**first1, **second1, "z": 1}
# print(combined)

# # Exercise - a common interview question
# from pprint import pprint   # format the output
# sentence = "This is a common interview question"

# char_frequency = {}  # char as the keys, repetition as the value, using dictionary
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# pprint(char_frequency, width=1)
# # sort it by the frequency; take out and convert to tuple and put in a list
# char_frequency_sorted = sorted(
#     char_frequency.items(),
#     key=lambda kv: kv[1],
#     reverse=True)  # return key values as tuples, not sorted yet; sort after adding the key lambda function, the 3rd argument reversed it
# print(char_frequency_sorted[0])  # prints the most repetitive character


# Handle Exceptions
# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):  # you can do single error without () or multiple ones within ()
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")
# finally:   # it always executes to release external resources
#     file.close()   # close the file object so other people can use it

# another way is to use with statement
# try:
#     # with open("app.py") as file, open("another.txt") as target: to release more than one file
#     with open("app.py") as file:
#         print("File opened.")
#         # if an object has enter and exit methods, we can use it with the with statement and no need for finally clause
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):  # you can do single error without () or multiple ones within ()
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")

# raise exception - not recommended
from timeit import timeit
# run the entire block
code1 = """   

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can't be 0 or negative.")
    return 10 / age  # google python 3 built-in exceptions


# after raising the exception, use try block to handle it
try:
    calculate_xfactor(-1)
except ValueError as error:  # give it a name error
    pass
"""

code2 = """   

def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age 

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))  # almost 4 times faster
