#example 1
x= 1
y= 1.1
z= 1j

print(x)
print(y)
print(z)
print( type(x))
print( type(y))
print( type(z))

print('______________')
#example 2 type convesion
x = 10
y = 10.5
z = 10j
#convert int to float
intToFloat = float(x)
#convert float to int
floatToInt = int(y)
#convert int to complex
intToComplex = complex(x)

print(intToFloat)
print(floatToInt)
print(intToComplex)

print(type(intToFloat))
print(type(floatToInt))
print(type(intToComplex))

print('______________')
#example 3 Random number

import random
print(random.randrange(1,10))