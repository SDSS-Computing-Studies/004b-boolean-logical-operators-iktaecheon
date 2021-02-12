#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a > b:
    factor = b
    largenum = a
elif b > a:
    factor = a
    largenum = b

if largenum%factor == 0:
    print(str(factor) + " is a factor of " + str(largenum))
else:
    print(str(factor) + " is not a factor of " + str(largenum))