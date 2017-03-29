
def no_unneccessary_recursiveness(f):
        cache = {}
        def wrapped_f(*args):
            if args[0] in cache:
                print('found arg in cache')
                return cache[args[0]]
            else:
                print('calculating')
                val = f(*args)
                cache[args[0]] = val
                print(val)
                return val
        return wrapped_f




@no_unneccessary_recursiveness
def fibonacci(n):
    if n == 1: 
        return 1
    elif n == 2: 
        return 1
    else: 
        return fibonacci(n-2)+fibonacci(n-1)
        

fibonacci(3)
