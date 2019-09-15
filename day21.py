set1 = {"Ahmed","Noura","Nada","Fatimah"}

#length of the set
print(len(set1))

#remove specific item using remove() (if item not exsit error will shown)
set1.remove("Noura")
print(set1)

#remove specifi item using remove() (if item not exsit NO error will shown)
set1.discard("Ahmed")
print(set1)

#remove random item using pop()
x = set1.pop()
print(x)
print(set1)

#remove all items using clear()
set1.clear()
print(set1)

#remove the set using del
del set1
print(set1)

#set() to create a new set
set2 = set(('red','green','blue'))
print(set2)