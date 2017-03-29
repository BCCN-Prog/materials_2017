# For modifying funcitons without arguments

def entry_exit(f):
    """
    f is a function that will be modified using a decorator.
    outputs the new_f, the wrap function
    """
    # It only prints one time.
    print("This is the first call to the decorator", f.__name__)
    def new_f():
        """
        nested function inside the decorator, this is the wrap fucntion.
        This wrap function will print a string, call f() and
        print another string.
        This is the modification of the fucntion.
        """
        print("The decorator enters the 'wrap' function", f.__name__)
        f()
        print("This is the added text", f.__name__)
    print("Depricate function")
    # new_f.__name__ = f.__name__
    return new_f


# @ syntax says the first time you run the function below,
# first enter @entry_exit using func1 as argument.
@entry_exit
def func1():
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")

func1()
func2()
print(func1.__name__)

func1()
func2()
