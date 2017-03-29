def first_decorator(g):
    print('this is my first decorator')
    return g

@first_decorator
def func_david():
    print(' inside davids function')


def entry_exit(f):
    # this only gets run once
    print('once here')
    def new_f(test):
        print("Entering", f.__name__)
        f(test)
        print("Exited", f.__name__)
    # this only gets run once
    print('running here just once')
    new_f.__name__ = f.__name__
    return new_f

@entry_exit
def func1(temp):
    print(temp)
    print("    inside func1()")


func1()

@entry_exit
def func2():
    print("     inside func2()")

func1()
func2()
print(func1.__name__)
