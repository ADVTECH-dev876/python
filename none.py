Python None
Python None
None is a special constant in Python that represents the absence of a value.

Its data type is NoneType, and None is the only instance of a NoneType object.

NoneType
Variables can be assigned None to indicate "no value" or "not set".

ExampleGet your own Python Server
Assign and display a None value:

x = None
print(x)
Use type() to see the type of a None value.

Example
Assign and print the data type of a None value:

x = None
print(type(x))
Comparing to None
To compare a value to None, use the identity operator is or is not

Example
Use the identity operator is for comparisons with None:

result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")
Example
Similar example, but using is not instead:

result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")
True or False
None evaluates to False in a boolean context.

Example
Check truthiness:

print(bool(None))
Functions returning None
Functions that do not explicitly return a value return None by default.

Example
A function without a return statement returns None:

def myfunc():
  x = 5

x = myfunc()
print(x)
