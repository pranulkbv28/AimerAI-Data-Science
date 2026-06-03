# In python, a list is a built in data structure that is used to store muiltiple items in a single variable
# they are mutable, ordered and can contain elements of different data types
# You can also make a nested list

# Properties
# Ordered
# Mutable
# Heterogeneous
# Indexing
# Slicing
# Duplicates
# Built-in Methods

my_list = [1,2,3,4,5]
fruits = ["apple", "banana", "oranges"]
nested_list = [my_list, fruits]

print(my_list)
print(fruits)
print(nested_list)

# converting string to a list
str_list = list("hello")

# converting tuple into a list
tuple_list = list((1,2,3))

# creating a list from a range
range_list = list(range(5))

print(str_list)
print(tuple_list)
print(range_list)

# Appending and Extending lists
# append adds one element to the end of the list
fruits.append("mango")
# extend adds multiple elements to the list in the same order
my_list.extend([6,7])

print(my_list)
print(fruits)

# inserting elements at a specified index
# index(pos, new_element)
fruits.insert(1, "jackfruit")

print(fruits)

# Removing elements
# remove(item) -> this removes the element
fruits.remove("jackfruit")
print(fruits)
# pop(index) -> this removes the element at the index
fruits.pop(len(fruits) - 1)
print(fruits)

# List Slicing
# list[start:end+1]
sliced_list = my_list[1:4]
print(sliced_list)

# List Sorting
# sort() -> this sorts the list in place. If we pass a param called reverse=True, it gives us descending order
numbers = [5,1,3,2,4]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
# sorted(list) -> returns a new sorted list
numbers2 = [5,1,3,2,4]
new_numbers_asc = sorted(numbers2)
new_numbers_desc = sorted(numbers2, reverse=True)
print(new_numbers_asc)
print(new_numbers_desc)

# List Membership
# using "in", we can check the presence of a member in a list
print(2 in my_list) # -> returns Boolean

# Copying a list
copied_list = my_list.copy()
print(copied_list)

# Clearing a list
number_new = [5,1,3,2,4]
print(number_new)
number_new.clear()
print(number_new)
