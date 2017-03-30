def deprecated1():
    print("The function that is gonna be deprecated has just been defined")
    def wrap(f):
        has_run = [False]
        def wrapped_f(*args):
            print("we now call the function")
            if has_run[0] == False:
                print("The function %s is gonna be deprecated soon."%(f.__name__))
                has_run[0] = True
            f(*args)        
        return wrapped_f
    return wrap

def deprecated2():
    print("The function that is gonna be deprecated has just been defined")
    def wrap(f):
        f.has_run = False
        def wrapped_f(*args):
            print("we now call the function")
            if not f.has_run:
                print("The function %s is gonna be deprecated soon."%(f.__name__))
                f.has_run = True
            f(*args)        
        return wrapped_f
    return wrap
    
def decorator_function_with_arguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap

#@decorator_function_with_arguments("hello", "world", 42)
@deprecated2()
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

#print("After decoration")

#print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
sayHello("say", "hello", "argument", "list")
#print("after first sayHello() call")
#sayHello("a", "different", "set of", "arguments")
#print("after second sayHello() call")
