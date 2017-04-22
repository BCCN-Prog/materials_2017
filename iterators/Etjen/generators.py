# Generators are iterators, but you can only iterate over them once. It's because they do not store all the values in memory
# they generate the values on the fly:
# yield is a keyword that is used like return, except the function will return a generator and not a single value


def myGen(n):
	yield n
	yield n + 1

g = myGen(6)
print(next(g))
print(next(g))
print(next(g))

while True:
    try:
        print(next(y))
    except StopIteration:
        print('you reached the end of the generator created iterator... exiting gracefully')
        break