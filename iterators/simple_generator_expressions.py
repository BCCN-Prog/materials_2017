

print('List comprehension:')
S = [x**2 for x in range(10)]
print(S)
print(S[0:5])
print(sum(S))


print('Generator comprehension:')
a = (x**2 for x in range(10))
print(a)
print(sum(a))
