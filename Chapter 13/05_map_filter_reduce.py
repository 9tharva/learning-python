from functools import reduce  # Needed for reduce()

# Map Example
l = [1, 2, 3, 4, 5]

square = lambda x: x * x
sqList = map(square, l)
print(list(sqList))

# Filter Example 
def even(n):
    return n % 2 == 0

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Example
def add(a, b):
    return a + b

mul = lambda x, y: x * y

print(reduce(add, l))
print(reduce(mul, l))
