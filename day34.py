#passing list to function
def my_function(food):
    for x in food:
        print(x)

fruits = ['Apple', 'Banana', 'Cherry']
my_function(fruits)
print('____________')

#function with return 
def my_function1(x):
    return 5 * x

print(my_function1(2))
print(my_function1(3))
print(my_function1(4))
print('____________')

#keyword arguments (kwargs)
def my_function2(child1, child2, child3):
    print('the bigger child is '+ child1)

my_function2(child3 = 'Nada', child2 = 'Hessah', child1 = 'Nourah')
print('____________')

#arbitary argument
def my_function3(*childs): #(unknown atributes number)
    print('the bigger child is '+childs[0])
    print('the smaller child is '+childs[2])

my_function3('Noura1','Hessah2','Nada3')
print('____________')

#recursint
def my_function_rec(k):
    if (k>0):
        res = k + my_function_rec(k-1)
        print(res)
    else:
        res = 0
    return res

my_function_rec(6)