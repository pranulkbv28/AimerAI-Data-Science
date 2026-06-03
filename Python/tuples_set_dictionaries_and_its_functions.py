# Tuples
# it is very similar to lists but with some differences
# it is created using parenthesis, ()
# it is an immutable object
# similar operations as for list
my_tuple = (1,2,3)
mixed_tuple = (1, "apple", 3.14, True)
print(my_tuple[0])
print(my_tuple+mixed_tuple) # -> concats both of them
print(len(my_tuple))

# Set
# It supports operations like union, Intersection and such
# It cannot have duplicate properties. Even if we do define it with repeated elements, the duplicates are removed
# It is created using curly brackets, {}
my_set = {1,2,3,4}
my_set2 = {7,8,9,0}
# Similar Operations like in lists and tuples
# add()
my_set.add(5)
print(my_set)
# remove()
my_set.remove(3)
print(my_set)
# set1.union(set2) -> returns the union set
print(my_set.union(my_set2))
# set1.intersection(set2) -> returns the intersection set
print(my_set.intersection(my_set2))
# set1.difference(set2) -> returns the difference set
print(my_set.difference(my_set2))
# set1.symmetric_difference(set2) -> returns the symmetric_difference set
print(my_set.symmetric_difference(my_set2))
# element in set1 -> returns boolean
print(1 in my_set)


# Dictionaries
# It helps us store key value pairs
# Values are mutable, although keys are immutable
# Unordered
# They have unique keys
# created like: {"key1":"value1", "key2":"value2"}
my_dict = {
    "name":"Alice",
    "age":30,
    "city":"New York",
    "is_elligible_to_vote":True
}
my_dict2 = {
    "name":"Graham",
    "age":16,
    "city":"Chicago",
    "is_elligible_to_vote":False
}
mixed_dict = {
    1:"one",
    2:[1,2,3],
    3.14:(3,14),
    "is_active":True
}
# Operations
# clear()
mixed_dict.clear()
# copy()
new_dict = my_dict.copy()
# pop()
my_dict2.pop("is_elligible_to_vote")
print(my_dict2)
# update()
my_dict2.update({"age":24, "is_elligible_to_vote":True})
print(my_dict2)
# dict.get()
print(my_dict.get("name"))
# items() -> gives us all the key value pairs
print(my_dict.items())
# values() -> gives us all the values
print(my_dict.values())
# keys() -> gives us all the keys
print(my_dict.keys())