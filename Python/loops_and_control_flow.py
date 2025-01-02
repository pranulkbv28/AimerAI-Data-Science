# Introduction to Loops and Control Flow in Python

# Loops and control flow are fundamental concepts in programming that allow you to execute code repeatedly 
# and make decisions based on certain conditions.

# 1. For Loop
# The 'for' loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string).
# It allows you to execute a block of code multiple times.

# Example of a for loop:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # This will print each fruit in the list

# 2. While Loop
# The 'while' loop in Python is used to repeatedly execute a block of code as long as a condition is true.

# Example of a while loop:
count = 0
while count < 5:
    print(count)  # This will print numbers from 0 to 4
    count += 1

# 3. If Statement
# The 'if' statement is used to execute a block of code only if a specified condition is true.

# Example of an if statement:
x = 10
if x > 5:
    print("x is greater than 5")  # This will print because the condition is true

# 4. If-Else Statement
# The 'if-else' statement is used to execute one block of code if a condition is true, and another block of code if it is false.

# Example of an if-else statement:
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")  # This will print because the condition is false

# 5. Elif Statement
# The 'elif' (short for else if) statement is used to check multiple conditions.

# Example of an elif statement:
z = 7
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but less than or equal to 10")  # This will print because the condition is true
else:
    print("z is 5 or less")

# 6. Break Statement
# The 'break' statement is used to exit a loop prematurely when a certain condition is met.

# Example of a break statement:
for i in range(10):
    if i == 5:
        break  # This will exit the loop when i is 5
    print(i)

# 7. Continue Statement
# The 'continue' statement is used to skip the rest of the code inside a loop for the current iteration and continue with the next iteration.

# Example of a continue statement:
for i in range(10):
    if i % 2 == 0:
        continue  # This will skip the even numbers
    print(i)  # This will print only odd numbers

# 8. Nested Loops
# You can use loops inside other loops. This is called nesting.

# Example of nested loops:
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")  # This will print the combination of i and j values

# These are the basic concepts of loops and control flow in Python. Understanding these will help you write more efficient and effective code.