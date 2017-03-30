

def deprecated_decorator(*args):
    print ('before wrap()')
    print ('Deprecation warning')
    outside= 1
    def wrap (func):
        func.inside_wrap =1
        print("Inside wrap()", outside)
        def wrapped_func(*args)
            print(func.inside_wrap)
            func.inside_wrap +=1
            print ("inside wrapped_func",outside)
            func(*args)
            print('ending wrapped_func',outside)
        return wrapped_func
        print("ending wrap()")
    return wrap



@deprecated_decorator()
def main_function(*args):
    print("In main_function")

@deprecated_decorator('b')
def deprecate_dd(*args):
    print("another function")






def decorator_function_with_arguments(arg1, arg2, arg3):
    print ('Before wrap')
    def wrap(f):
        #how many times does this print
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f
        print ("After Wrapping")
    return wrap

@decorator_function_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")
