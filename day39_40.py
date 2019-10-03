#Q1 usine recursion to calculate 5^3 and print the result
def myfunc(k):
    if (k>0):
        res = k ** myfunc(k-2)
    else:
        res = 1
    return(res)    

print(myfunc(5))
print('_______')
#Q2
list1 = [4, -6, -5, -1, 2, 3, 7, 9, 88]
pos_nos = list(filter(lambda x: (x >= 0), list1)) 

for x in pos_nos:
    print(x)
    
