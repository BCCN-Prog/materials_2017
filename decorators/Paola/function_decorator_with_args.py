# For modifying functions with arguments

def decorator_function_with_arguments(arg1, arg2, arg3):
    #print("outside wrap()")
    # x=2 this is not saved in the global environment
    def wrap(f):
        print("Inside wrap()")
        f.has_run = False
        def wrapped_f(*args):
            if not f.has_run:
                print("The function %s is deprecated, will be erase in future versions" %f.__name__)
                f.has_run = True
            #print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            #print("After f(*args)")
        #print("After wrapped_f")
        return wrapped_f
    #print("After wrap")
    return wrap

@decorator_function_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

print("        After decoration")
print("\n")
# print(x) raises a NameError
#print("        Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("        after first sayHello() call")
print("\n")
sayHello("a", "different", "set of", "arguments")
print("        after second sayHello() call")

# Deprecated print statement
#def deprecated(arg1, arg2):
#    print("This fucntion is deprecated, will be erase in future version.")
#    print("")
#    def wrap(f):


#@deprecated

# Memorize - Fibonacci function
