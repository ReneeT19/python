# print('Hello World')

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
# print(course.find("for")) # returns the index of the first letter found in the sequence of characters
# print(course.replace("for", "4"))  # won't modify the original string but return a new string as string is immutable
# print(course.find("Python"))
# print("Python" in course) # the same as line 36 # returns true or false

# Arithmetic Operators
# print(10 * 3)
# print(10 / 3)  #use // to get an integer
# print(10 % 3)
# print(10 ** 3) #10 to the power of 3
#
# x += 3
# boolean expression
# x = 3 > 2
# logical operators - and, or, not
# price = 25
# print(price > 10 and price <30) # or
# print(not price > 10)

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

# range() function - generate a sequence of numbers
# numbers = range(5,10,2)  # (5) return a range object 0-4; (5,10) returns a range object 5-9
# # for number in numbers: another way to do it is in line 120 so two lines can solve the problem
# for number in range(5):
#     print(number)

# tuples - use () - immutable - no append, insert,etc.
numbers = (1,2,3)
print(numbers)
print(numbers.count(3))

