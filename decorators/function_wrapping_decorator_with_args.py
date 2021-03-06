def deprecated(blank):
    print('before wrap()')
    print('DeprecationWarning 1: this runs when we define the function')
    outside = 1
    def wrap(func):
        func.inside_wrap = 1
        print('  inside wrap()', outside)
        print('DeprecationWarning 2: how many function declarations does this run on?')
        def wrapped_func(*args):
            if func.inside_wrap < 2:
                print('DeprecationWarning 3: how many times?')
            print(func.inside_wrap)
            func.inside_wrap += 1
            print(func.inside_wrap)
            print('    inside wrapped_func()', outside)
            func(*args)
            print('    ending wrapped_func()')
        return wrapped_func
    print('ending wrap()')
    outside += 1
    return wrap

@deprecated('b')
def deprecate_me(*args):
    print('      inside deprecated function')

@deprecated('b')
def deprecate_dd(*args):
    print('      another deprecated function')

@deprecated('b')
def deprecate_ee(*args):
    print('      another deprecated function')

# @deprecated
# # stuff that is deprecated

# @memorize
# def fibonacci():
#     # do it

def decorator_function_with_arguments(arg1, arg2, arg3):
    print('Before wrap()')
    # print(f)
    # Decorators use Classes under the hood. And a class
    #   always receives an implicit reference to the
    #   'self' as its first argument. We are giving it
    #   an explicit name as 'f' (or 'g') in order to access
    #   it inside the function. This is also why we need
    #   the double wrapping.
    def wrap(g): # see I can also call it g (or anything else!)
        # how many times does this print?
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            g(*args)
            print("After f(*args)")
        return wrapped_f
    print('After wrap()')
    return wrap

@decorator_function_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('     sayHello arguments:', a1, a2, a3, a4)

@decorator_function_with_arguments("these", "are", "different")
def sayGoodbye(a1, a2):
    print('     sayGoodbye arguments:', a1, a2)



print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")
