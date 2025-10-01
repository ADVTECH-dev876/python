Validate Input
It is a good practice to validate any input from the user. In the example above, an error will occur if the user inputs something other than a number.

To avoid getting an error, we can test the input, and if it is not a number, the user could get a message like "Wrong input, please try again", and allowed to make a new input:

Example
Keep asking until you get a number:

y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")
