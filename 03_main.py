"""
Homework Assignment #3: "If" Statements

Details:
Create a function that accepts 3 parameters and checks for equality between any two of them.

Your function should return True if 2 or more of the parameters are equal,
 and false is none of them are equal to any of the others.

Extra Credit:
Modify your function so that strings can be compared to integers if they are equivalent.
For example, if the following values are passed to your function:

6,5,"5"

You should modify it so that it returns true instead of false.

Hint: there's a built in Python function called "int" that will help you convert strings to Integers.
"""


def equalCheck(a, b, c):
    # convert arguments to ints
    a = int(a)
    b = int(b)
    c = int(c)

    # compare all pairs
    if a == b or a == c or b == c:
        return True
    else:
      return False


# Testing
print(equalCheck(1, 2, 3), "Result: False")
print(equalCheck(1, 1, 3), "Result: True")
print(equalCheck(1, 2, 1), "Result: True")
print(equalCheck(1, 2, 2), "Result: True")

print(equalCheck('1', '2', '3'))
print(equalCheck(1, '1', 3))
print(equalCheck(1, 2, '1'))
print(equalCheck(1, '2', 2))

