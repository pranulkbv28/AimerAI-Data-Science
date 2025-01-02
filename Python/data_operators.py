# data_operators.py

"""
This module provides an introduction to data operators in Python.
Data operators are used to perform operations on variables and values.
Python supports a variety of operators, including arithmetic, comparison, logical, bitwise, assignment, and identity operators.
"""

# Arithmetic Operators
# These operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.
a = 10
b = 5

print("Addition:", a + b)        # Output: 15
print("Subtraction:", a - b)     # Output: 5
print("Multiplication:", a * b)  # Output: 50
print("Division:", a / b)        # Output: 2.0
print("Modulus:", a % b)         # Output: 0
print("Exponentiation:", a ** b) # Output: 100000
print("Floor Division:", a // b) # Output: 2

# Comparison Operators
# These operators compare two values and return a boolean result.
print("Equal:", a == b)          # Output: False
print("Not Equal:", a != b)      # Output: True
print("Greater than:", a > b)    # Output: True
print("Less than:", a < b)       # Output: False
print("Greater than or equal to:", a >= b) # Output: True
print("Less than or equal to:", a <= b)    # Output: False

# Logical Operators
# These operators are used to combine conditional statements.
x = True
y = False

print("AND:", x and y)           # Output: False
print("OR:", x or y)             # Output: True
print("NOT:", not x)             # Output: False

# Bitwise Operators
# These operators are used to perform bit-level operations.
c = 6  # Binary: 110
d = 2  # Binary: 010

print("Bitwise AND:", c & d)     # Output: 2 (Binary: 010)
print("Bitwise OR:", c | d)      # Output: 6 (Binary: 110)
print("Bitwise XOR:", c ^ d)     # Output: 4 (Binary: 100)
print("Bitwise NOT:", ~c)        # Output: -7 (Binary: -111)
print("Bitwise Left Shift:", c << 1) # Output: 12 (Binary: 1100)
print("Bitwise Right Shift:", c >> 1) # Output: 3 (Binary: 011)

# Assignment Operators
# These operators are used to assign values to variables.
e = 10
e += 5  # Equivalent to e = e + 5
print("Assignment (+=):", e)     # Output: 15

e -= 3  # Equivalent to e = e - 3
print("Assignment (-=):", e)     # Output: 12

e *= 2  # Equivalent to e = e * 2
print("Assignment (*=):", e)     # Output: 24

e /= 4  # Equivalent to e = e / 4
print("Assignment (/=):", e)     # Output: 6.0

e %= 5  # Equivalent to e = e % 5
print("Assignment (%=):", e)     # Output: 1.0

e **= 3  # Equivalent to e = e ** 3
print("Assignment (**=):", e)    # Output: 1.0

e //= 2  # Equivalent to e = e // 2
print("Assignment (//=):", e)    # Output: 0.0

# Identity Operators
# These operators are used to compare the memory locations of two objects.
f = [1, 2, 3]
g = [1, 2, 3]
h = f

print("Is:", f is h)             # Output: True
print("Is Not:", f is not g)     # Output: True

# Membership Operators
# These operators are used to test if a sequence is presented in an object.
print("In:", 2 in f)             # Output: True
print("Not In:", 4 not in f)     # Output: True