
def first_decorator (g):
    print("Oliver loves Taylor Swift")
    return g

@first_decorator
def func_alex():
    print("No seriously he loves her (he thinks she looks hot)")

def entry_exit(f):
    def new_f(x):
        print('once here')
        print("Entering", f.__name__)
        f(x)
        print("Exited", f.__name__)
        print('running here just once')
        new_f.__name__ = f.__name__
    return new_f

@entry_exit
def func1(temp):
    print(temp)
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")

func1()
func2()
print(func1.__name__)
