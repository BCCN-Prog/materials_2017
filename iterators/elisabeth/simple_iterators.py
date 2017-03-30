
x = iter([22,23,'dd',4,5])
y = x.__iter__()
z = x

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
