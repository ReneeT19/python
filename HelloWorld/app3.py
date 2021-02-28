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
# from ecommerce.shopping import sales
# print(dir(sales))  # prints the built-in methods
# print(sales.__name__)
# print(sales.__package__)
# print(sales.__file__)   # path of the module


# working with paths
# from pathlib import Path
# from time import ctime
# import shutil  # work with files
# # different ways to create a path
# # Path(r"C:\Program FileMicrosoft")
# # Path("/usr/local/bin")
# # Path()
# # use this one and store it in a path object
# path = Path("ecommerce/__init__.py")

# source = Path("ecommerce/__init__.py")
# target = Path() / "__init__.py"

# shutil.copy(source, target)
# Path() / "ecommerce" / " __init__.py"
# Path.home()
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_name("file.txt")
# print(path)
# print(path.absolute())  # this file doesn't really exist yet it's just the path
# # you can rename the suffix too `path = path.with_suffix("text")  print(path)
# path.rename("init.txt")
# path.unlink()
# print(ctime(path.stat().st_ctime)

# work with directories
# path = Path("ecommerce")
# paths = [p for p in path.iterdir() if p.is_dir()]:
# py_files = [p for p in path.glob("*.py")]
# print(paths)
# print(py_files)

# print(path.read_byte())
# print(path.read_text())
# path.write_text("....")
# path.write_bytes()

# work with zipfile
# from pathlib import Path
# from zipfile import ZipFile

# # no need to call close method if using with statement
# # with ZipFile("files.zip", "w") as zip:
# #     for path in Path("ecommerce").rglob("*.*"):
# #         zip.write(path)
# # zip.close()

# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("ecommerce/__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")  # created an extract directory


# work with csv files
# import csv

# # how to write a csv file
# with open("data.csv", "w") as file:  # read or write mode as the second parameter
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 5])

# # how to read csv file
# with open("data.csv") as file:  # read or write mode as the second parameter
#     reader = csv.reader(file)
#     # print(list(reader))
#     for row in reader:
#         print(row)

# work with json files
# import json
# from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "ABC", "year": 1993},
# ]

# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)  # write data to json file


# # data as a string
# data = Path("movies.json").read_text()
# movies = json.loads(data)
# # you can get any movie from this dictionary by using index such as movies[0]["title"]
# print(movies)
# print(movies[0]["title"])


# work with a SQLite database
# import sqlite3
# # read json file and store in the sqlite db
# import json
# from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())  # a list of dictionaries
# print(movies)

# # create a connection object with with statement
# # insert
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?,?,?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()  # changes written to database

# select
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "SELECT * FROM Movies"
#     # returns a cursor, an iterable object and get one row at a time
#     cursor = conn.execute(command)
#     for row in cursor:
#         print(row)
#     # if you have fetchall method, comment out the for loop above
#     movies = cursor.fetchall()
#     print(movies)

# work with timestamps
# import time

# print(time.time())  # for calculation purpose


# def send_emails():
#     for i in range(10_000):
#         pass


# start = time.time()
# send_emails()
# end = time.time()
# duration = end - start
# print(duration)

# work with date time object
# from datetime import datetime, timedelta
# import time

# dt1 = datetime(2021, 1, 1) + timedelta(days=1,
#                                        seconds=1_000)  # use key word for clarity
# dt2 = datetime.now()

# # parse string to datetime object; search python3 strptime
# dt = datetime.strptime("2021/01/01", "%Y/%m/%d")
# dt = datetime.fromtimestamp(time.time())  # convert to a datetime object

# print(f"{dt.year}/{dt.month}")
# print(dt.strftime("%Y/%m"))  # convert datetime object to a string

# print(dt2 > dt1)  # you can compare datetime objects as well

# duration = dt2 - dt1
# print(duration)
# print("days", duration.days)
# print("seconds", duration.seconds)
# print("total_seconds", duration.total_seconds())

# Generating random values
# import random
# import string

# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([1, 2, 3, 4]))
# print(random.choices([1, 2, 3, 4], k=2))


# # print in both lower and upper cases for 26 letters
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.digits)

# # generate a password from the string
# # "" is to print it as no array brackets
# print(",".join(random.choices("abcedfghi", k=4)))
# print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

# # shuffling an array
# numbers = [1, 2, 3, 4]
# random.shuffle(numbers)
# print(numbers)  # gets different combinations each time


# open a browser
# import webbrowser

# print("Deployment completed")
# webbrowser.open("http://google.com")


# Sending emails
# Templates

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# import smtplib
# from string import Template

# template = Template(Path("template.html").read_text())
# message = MIMEMultipart()
# message["from"] = "Renee Thomsen"
# message["to"] = "testuser@codewithmosh.com"
# message["subject"] = "This is a test"
# body = template.substitute({"name": "John"}) ## pass keyword arguments
# message.attach(MIMEText(body, "html"))
# message.attach(MIMEImage(Path("renee.png")))
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("testuser@codewithmosh.com", "todayskyisblue")
#     smtp.send_message(message)
#     print("Sent...")


# Command line arguments
# import sys
# if len(sys.argv) == 1:
#     print("USAGE: python3 app3.py <password>")
# else:
#     password = sys.argv[1]
#     print("Password", password)
# print(sys.argv)

# running external program
import subprocess

# completed = subprocess.run(["ls", "-l"],
#                           capture_output=True,
#                           text=True)
completed = subprocess.run(["python3", "other.py"],
                          capture_output=True,
                          text=True)
print("args", completed.args)
print("returncode", completed.returncode)  # return code 0 means success, 1 means error, do a try except to fix it
print("stderr", completed.stderr)
print("stdout", completed.stdout)
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen