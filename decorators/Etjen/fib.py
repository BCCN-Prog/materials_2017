# Fib function definition
#	def fib(n):
#   	return n if n < 2 else fib(n-2) + fib(n-1)

# decorator takes a function as an argument and returns a replacement function
def memoize(f):
    cache = {} 						# define a dictionary cache to store the fib numbers
    def decorated_function(*args):  # * means that arguments should be extracted
        if args in cache: 			# check if the argument already exists in the cache
            return cache[args] 		# if yes return it
        else:
            cache[args] = f(*args)	# otherwise assign the function with arguments to the dictionary say f(2) which will be calculated on its own
            return cache[args]		# return the dictionary
    return decorated_function		# return the decorated function 

@memoize
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)

fib = memoize(fib) # this assings the f(*args) to the fib function because it points to the body of the decorated function 
print(fib(10))

