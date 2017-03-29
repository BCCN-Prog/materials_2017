#tasks: deprecated, memorizer: write fibonacci function, decorator should see if a value was already calculated.

def deprecated(f):
    print(f.__name__, 'is deprecated')
    def f_new(*args):
        
#        def wrapped_f(*args):
#            print("Inside wrapped_f()")
#            print("Decorator arguments:", arg1)
#            f(*args)
#            print("After f(*args)")
#        return wrapped_f
        return f(*args)
    return f_new


@deprecated
def func_old(arg1, arg2):
    print('I am too old for this shit!')
    print('but I still got cool arguments: ', arg1, arg2)


def miao():
    print('miao')
    

miao()
print('first call to func_old')   
func_old('1st arg', '2nd arg')

print('second call to func_old')   
func_old('new arg', 'other new arg')


