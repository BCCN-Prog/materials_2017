
def yrange(n):
    i = 0
    while i < n:
        yield i
        # yield 22 + i
        i += 1

y = yrange(3)

print(y)

while True:
    try:
        print(next(y))
    except StopIteration:
        print('you reached the end of the generator created iterator... exiting gracefully')
        break
