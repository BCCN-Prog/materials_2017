def f(x):
    long = range(10**x)
    y = []
    for idx in long:
        y.extend([idx*2])
        #y = [idx]
    return y

def g(y):
    z = []
    for idx in f(y):
        z.append(idx/2)
    return z

pow = 7

a = g(pow)
print(a)
