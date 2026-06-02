# string objects in Python are recognised when anything is enclosed in quotes, be it single, double or even triple quotes

mystr = "CodingIsFun"
print(mystr)

# triple quotes are used for multi-line string

multi_line_str = '''hi
my name is pranaav
how are you?
'''

# in built string fuynctions

# Case Changing functions
# upper()
str1 = "pranaav in lower to upper"
print(str1.upper())
# lower()
str2 = "PRANAAV IN UPPER TO LOWER"
print(str2.lower())
# capitalize()
str3 = "capitalize first letter in the string"
print(str3.capitalize())
# title()
str4 = "make this a title"
print(str4.title())

# Checking properties
str_alpha = "abcDEF"
str_dig = "100"
str_al_num = "pran28"
# isalpha()
print(str_alpha.isalpha())
print(str_dig.isalpha())
print(str_al_num.isalpha())
# isdigit()
print(str_alpha.isdigit())
print(str_dig.isdigit())
print(str_al_num.isdigit())
# isalnum()
print(str_alpha.isalnum())
print(str_dig.isalnum())
print(str_al_num.isalnum())

# Search and Replace
# find(substring)
print(str1.find("a"))
# replace(old, new)
print(str1.replace("in", "from"))

# Splitting and Joining
text = "apple,banana,orange"
# split()
fruits = text.split(",")
print(fruits)
# join() -> we need the joining string and then the array
print(", ".join(fruits))


# Trimming
# trim() -> trims from both sides
# lstrip() -> only from the left side
# rstrip() -> only from the right side

# String slicing
text2 = "Hellow World"
# from starting to specific index
print(text2[0:5])
# from specific index to end
print(text2[7:])
# using negative indices
print(text2[-6:])

# string is immutable
# so if we have a string, "Prnanaav" and we do str.upper(), the str remains "Pranaav", we can still get "PRANAAV", and we can get this only if we save it to another variable

# Checking substring
text3 = "Hello, world"
sub_string = "world"
# in()
print(sub_string in text3)
