# Check if Item Exists 
tuple1 = ('Apple', 'cat', 'banana', 'bed')
if 'cat' in tuple1:
    print('its there')

# Repeat Item 
tuple2 = ('A',)* 3
print(tuple2)

# + Operator in Tuple 
tuple3 = ('app', 'android')
tuple4 = ('bed', 'car')
print(tuple3 + tuple4)

x = (3, 4, 5, 6)
x = x + (1, 2, 3)
print(x)

# Tuple Length
tuple5 = ('apple', 'android', 'galaxy', 'samsung', 'nokia')
print(len(tuple5))

# create tuble using tuble()
tuple6 = tuple(('a','b', 'c'))
print(tuple6)

#from list to tuple
list = ['apple', 'android', 'galaxy', 'samsung', 'nokia']
tuple7 = tuple((list))
print(tuple7)