
x = iter([1,2,3,4,5])
y = x.__iter__()

print(x)
print(y)

print(next(x))
print(next(y))
print(next(y))
print(next(x))
print(next(x))
print('The next one will break')
print(next(x))
print(next(y))

for letter in 'python':
    print(letter)
