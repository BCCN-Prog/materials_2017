def entry_exit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    # new_f.__name__ = f.__name__
    return new_f

@entry_exit
def func1():
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")

#func1()
#func2()
#print(func1.__name__)

def fancy_decorator(x):
    print("The wonderful function elichan has been born")
    def new_x()
    return x
    
    

@fancy_decorator
def elichan(step):
    return [x for x in range(0,8,step)]
    
print(elichan())
