#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
x = int(input("Enter an integer=>"))
y = int(input("Enter an integer=>"))
z = int(input("Enter an integer=>"))

if z == x == y:
    hyp = x
    side1 = y
    side2 = z
    print("{},{},{} do not form a pythagoran triple".format(side1, side2, hyp))
elif x > y and x > z:
    hyp = x
    side1 = y
    side2 = z
elif y > x and y > z:
    hyp = y
    side1 = x
    side2 = z
elif z > x and z > y:
    hyp = z
    side1 = x
    side2 = y
if hyp != side1:
    if hyp**2 == (side1**2)+(side2**2):
        print("{},{},{} form a Pythagorean triple".format(side1,side2,hyp))
    else:
        print("{},{},{} do not form a pythagoran triple".format(side1, side2, hyp))