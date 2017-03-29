

print('List comprehension:')
S = [x**2 for x in range(10)]
print(S)
print(sum(S))

# The only difference is the round brackets.
# This is optimize in time and memory, because you create the
# things on the fly.
print('Generator comprehension:')
a = (x**2 for x in range(10))
print(a)
print(sum(a))
