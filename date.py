Python Modules
What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

Create a Module
To create a module just save the code you want in a file with the file extension .py:


//code
def greeting(name):
  print("Hello, " + name)
Use a Module
Now we can use the module we just created, by using the import statement:

Example
Import the module named mymodule, and call the greeting function:

import mymodule

mymodule.greeting("Jonathan")
Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

Example
Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
Example
Import the module named mymodule, and access the person1 dictionary:

import mymodule

a = mymodule.person1["age"]
print(a)

Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

ExampleGet your own Python Server
Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)
Date Output
When we execute the code from the example above the result will be:

2025-09-30 17:23:22.582377
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter:

Example
Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
Creating Date Objects
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.

Example
Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)
