# This is a basic Python script to demonstrate some fundamental concepts

# Print a message to the console
print("Hello, World!")

# Variables and data types
integer_var = 10  # Integer
float_var = 20.5  # Float
string_var = "Python is fun!"  # String
boolean_var = True  # Boolean

# Print variables
print(integer_var)
print(float_var)
print(string_var)
print(boolean_var)

# Lists - ordered, mutable collection of items
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Tuples - ordered, immutable collection of items
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Dictionaries - unordered, mutable collection of key-value pairs
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)

# Conditional statements
if integer_var > 5:
    print("integer_var is greater than 5")
else:
    print("integer_var is not greater than 5")

# Loops
# For loop
for i in range(5):
    print("For loop iteration:", i)

# While loop
count = 0
while count < 5:
    print("While loop iteration:", count)
    count += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))