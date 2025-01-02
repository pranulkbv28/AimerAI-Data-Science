# In Python, a namespace is a container that holds a set of identifiers (names) and their corresponding objects.
# Namespaces are used to ensure that names are unique and won't lead to naming conflicts.

# There are four types of namespaces in Python:

# 1. Built-in Namespace:
#    This namespace contains the names of all built-in functions and objects in Python.
#    These names are always available in any Python program.

print(len("Hello"))  # 'len' is a built-in function

# 2. Global Namespace:
#    This namespace contains names defined at the top level of a module or script.
#    These names are available throughout tifhe module.

global_var = "I am a global variable"

def global_scope_example():
    print(global_var)  # Accessing the global variable

global_scope_example()

# 3. Enclosing Namespace:
#    This namespace contains names defined in a nested function.
#    These names are available to the nested function and any functions defined within it.

def outer_function():
    enclosing_var = "I am an enclosing variable"
    
    def inner_function():
        print(enclosing_var)  # Accessing the enclosing variable
    
    inner_function()

outer_function()

# 4. Local Namespace:
#    This namespace contains names defined within a function.
#    These names are only available within the function where they are defined.

def local_scope_example():
    local_var = "I am a local variable"
    print(local_var)

local_scope_example()

# The LEGB rule:
# Python resolves names by searching in the following order:
# 1. Local Namespace
# 2. Enclosing Namespace
# 3. Global Namespace
# 4. Built-in Namespace

# Example demonstrating the LEGB rule:

def legb_example():
    local_var = "I am a local variable"
    
    def inner_function():
        enclosing_var = "I am an enclosing variable"
        
        def innermost_function():
            print(local_var)  # Local scope
            print(enclosing_var)  # Enclosing scope
            print(global_var)  # Global scope
            print(len)  # Built-in scope
        
        innermost_function()
    
    inner_function()

legb_example()