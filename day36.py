#lambda with function
def myfunc_double(n):
    return lambda a : a*n

def myfunc_triple(n):
    return lambda a : a*n

my_double = myfunc_double(2)
my_triple = myfunc_triple(3)
print(my_double(10))
print(my_triple(10))
print('________________')


#lambda with function shorten the above
def myfunc(n):
    return lambda a : a*n

my_double = myfunc(2)
my_triple = myfunc(3)
print(my_double(10))
print(my_triple(10))
print('________________')