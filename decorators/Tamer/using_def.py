def trial_decor(a):
    print ("Hello, look at me, I'm Mr. Decorator")
    def inside_decor():
        print ("entering the insider")
        a()
        print ("out of insider")
    inside_decor.__name__ = a.__name__
    return inside_decor

@trial_decor
def first_func():
    print ("enter first func")


@trial_decor
def second_func():
    print ("enter second func")

first_func()
second_func()
print (first_func.__name__)
'''
def entry_exit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    new_f.__name__ = f.__name__
    return new_f


@entry_exit
def func1():
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")

func1()
func2()
print(func1.__name__)
'''
