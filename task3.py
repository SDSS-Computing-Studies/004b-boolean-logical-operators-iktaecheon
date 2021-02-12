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
x = float(input("Enter a number: "))
y = int(x)


if x - y != 0:
    print(str(x) + " is not a positive integer")
elif x < 0:
    print(str(x) + " is not a positive integer")
else:
    print(str(x) + " is a positive integer.")