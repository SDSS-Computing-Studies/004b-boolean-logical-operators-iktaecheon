#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
x = input("Enter a number: ")
dot = "."
negative = "-"
if dot in x:
    print(x + " is not a positive integer")
elif negative in x:
    print(x + " is not a positive integer")
else:
    print(x + " is a positive integer.")