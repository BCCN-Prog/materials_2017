def funny_func(p,o):
    def no_fun(f):
        print ("this is no fun")
        def fun_fun_fun(*args):
            print ("shall we have fun?")
            print ("we will have fun", p,o)
            f(*args)
            print ("we had fun")
        return fun_fun_fun
    return no_fun

@funny_func("fun", "fun")
def fun_fun(a,b):
    print ("we are having", a, b)


fun_fun("fun", "fun")
