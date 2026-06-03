# If you are coming from JS background, you know that there are a few in build functions for arrays like "map()", "filter()", "reduce()", "some()", "every()", "find()", "findIndex()", "sort()"

# map()
# JavaScript
'''
const nums = [1, 2, 3];
const doubled = nums.map(x => x * 2);

console.log(doubled); // [2, 4, 6]
'''

# Python
nums = [1, 2, 3]
doubled1 = list(map(lambda x: x * 2, nums))

print(doubled1)  # [2, 4, 6]

# More Pythonic
doubled2 = [x * 2 for x in nums]
print(doubled2)


# filter()
# JavaScript
'''
const nums = [1, 2, 3, 4];
const evens = nums.filter(x => x % 2 === 0);

console.log(evens); // [2, 4]
'''

# Python
nums = [1, 2, 3, 4]
evens1 = list(filter(lambda x: x % 2 == 0, nums))

print(evens1)

# More Pythonic
evens2 = [x for x in nums if x % 2 == 0]
print(evens2)


# reduce()
# JavaScript
'''
const nums = [1, 2, 3, 4];
const sum = nums.reduce((acc, curr) => acc + curr, 0);

console.log(sum); // 10
'''

# Python
from functools import reduce

nums = [1, 2, 3, 4]
total1 = reduce(lambda acc, curr: acc + curr, nums, 0)

print(total1)

# or

total2 = sum(nums)

print(total2)


# some()
# Checks if at least one element matches.\
# JavaScript
'''
nums.some(x => x > 3)
'''

# Python
print(any(x > 3 for x in nums))

# every()
# Checks if all elements match.
# JavaScript
'''
nums.every(x => x > 0)
'''

# Python
print(all(x > 0 for x in nums))


# find()
# JavaScript
'''
const result = nums.find(x => x > 2);
'''

# Python
result = next((x for x in nums if x > 2), None)
print(result)
