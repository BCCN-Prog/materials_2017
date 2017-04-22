# refer to this link for explanations between different concepts on generators and iterators 
# http://nvie.com/posts/iterators-vs-generators/

x = [1, 2, 3] 	# x the iterable which returns an iterator, x is a container a list in this case
y = iter(x) 	# instances of x 
z = x.__iter__()# can define this way as well

print(next(y)) #1
 
print(next(y)) #2

print(next(z)) #1
