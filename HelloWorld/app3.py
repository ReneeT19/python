# MODULES - Files that have python code; so far we only have one py file/module but in real life we want several modules
# build a sales.py
# app3.py is the entry/main module
# import functions from sales.py
# * might not be a good practice

# import sales  # one way to immport module line 20
# another way to import module line 17-18

# import sys  # module search path
# from ecommerce.sales import calc_tax, calc_shipping
# # or
# # from ecommerce import sales  then use sales. to get all methods in this sales module

# # from sales import calc_shipping, calc_tax

# calc_shipping()
# calc_tax()

# # sales.calc_shipping()

# # when you run python app3.py it creates a new folder that combines app3 and sales modules
# print(sys.path)


# Packages - subdirectories just like packages in Java to categorize modules
# we need to have an init.py module and import in this way: from ecommerce.sales import calc_tax, calc_shipping
# sub packages like shopping to further organize modules, make sure you have the __init__.py module under it and import `from ecommerce.shopping import sales`
# sibling packages customer   if you want to use contact module from the sibling customer module, look what we have in sales.py


# dir
from ecommerce.shopping import sales
print(dir(sales))  # prints the built-in methods
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)   # path of the module
