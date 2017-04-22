# use a generator expression if all you're doing is iterating once. 
# If you want to store and use the generated results, use a list comprehension.

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
sqList = [x**2 for x in my_list]
print(sum(sqList))

# now using generator expression
sqGE =(x**2 for x in my_list)
print(sum(sqGE))
