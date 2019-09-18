# if, elif, else
a = 33
b = 200
if a > b:
    print('a greater than b')
elif a == b:
    print("a equal b")
else:
    print('b greater than a')

# if in one line
if a > b : print('a greater than b')

#if & else in one line (not work)
# print("A") if a > b else print("=") if a = b else print('"B')

#And
a = 1
b = 2
c = 3
if a < b and b < c:
    print('a is the smallest ')

#Or
if a < b or b > c:
    print('a is the smallest ')

#Nested if
x = 12
if x > 10:
    print('x greter than 10')
    if x > 20:
        print('x greater than 20')
    else:
        print('x smaller than 20')