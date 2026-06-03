# They are a block of reusable code that is used to perform a certain task
# there three types in Python
# Inbuilt: len(), print()....
# User defined function: starts with the keyword "def"
# Lambda functions: One liner functions


# UDF
def my_sum(a,b,c=10):
    return a+b+c

def greet(name="Guest"):
    return f"Hello, {name}!"

def describe_person(name, age):
    return f"{name} is {age} years old."

def add_all(*args):
    return sum(args)

print(my_sum(2,3))
print(greet())
print(greet("Pranaav"))
print(describe_person(age=24, name="Pranaav"))
print(add_all(1,2,3,4,5))

# lambda
add = lambda a,b: a+b
result = add(3,5)
print(result)

numbers = [1,2,3,4]
squared = list(map(lambda x:x^2, numbers))
even_numbers = list(filter(lambda x:x%2==0, numbers))

from functools import reduce
product = reduce(lambda x,y:x*y, numbers)

print(squared)
print(even_numbers)
print(product)