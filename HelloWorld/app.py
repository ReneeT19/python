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

# list methods
# numbers = [1,2,3,4,5]
# numbers.append(6)  # add an element to the end of the list
# numbers.insert(2,-1)  # type of object is T which means any type # the first parameter is where you want to insert the value
# numbers.remove(1)
# print(1 in numbers) # whether a value exists in the list
# print(len(numbers)) # how many elements are in the list
# numbers.clear() # remove all
# print(numbers)

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

# # tuples - use () - immutable - no append, insert,etc.
# numbers = (1,2,3)
# print(numbers)
# print(numbers.count(3))


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
def fizz_buzz(input):
    if input % 15 == 0:
        return "Fizz_Buzz"
    elif input % 5 == 0:
        return "Buzz"
    elif input % 3 == 0:
        return "Fizz"

    return input


print(fizz_buzz(15))
