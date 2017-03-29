class entry_exit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)

print('Nothing has happened yet!')

@entry_exit
def func1():
    print("inside func1()")

print('in between the two function definitions')

@entry_exit
def func2():
    print("inside func2()")

print('calling the two functions')

func1()
func2()
