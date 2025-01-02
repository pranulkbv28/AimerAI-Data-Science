# Introduction to Type Conversions and Conditions in Python

# Type Conversions
# Type conversion is the process of converting one data type to another.
# Python provides several built-in functions to perform type conversions.

# Example of type conversion functions:
# int() - converts a value to an integer
# float() - converts a value to a float
# str() - converts a value to a string
# bool() - converts a value to a boolean

# Converting a float to an integer
float_value = 3.14
int_value = int(float_value)  # int_value will be 3

# Converting an integer to a string
int_value = 10
str_value = str(int_value)  # str_value will be '10'

# Converting a string to a float
str_value = "3.14"
float_value = float(str_value)  # float_value will be 3.14

# Converting a value to a boolean
# Any non-zero number or non-empty string is considered True
bool_value = bool(1)  # bool_value will be True
bool_value = bool(0)  # bool_value will be False
bool_value = bool("Hello")  # bool_value will be True
bool_value = bool("")  # bool_value will be False

# Conditions
# Conditions are used to execute code based on whether a statement is true or false.
# The most common conditional statements are if, elif, and else.

# Example of conditional statements:
x = 10
y = 20

# if statement
if x < y:
    print("x is less than y")

# elif statement (else if)
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

# else statement
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# Combining conditions using logical operators
# and - returns True if both statements are true
# or - returns True if at least one statement is true
# not - reverses the result, returns False if the result is true

a = 5
b = 10
c = 15

if a < b and b < c:
    print("Both conditions are true")

if a > b or b < c:
    print("At least one condition is true")

if not a > b:
    print("a is not greater than b")