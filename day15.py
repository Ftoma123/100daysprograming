# List Length
list1 = ['A','B','C','D']
print(len(list1))

# Add Items
list2 = ['A','B','C','D']
list2.append('E')
print(list2)

# add an item at the specified index
list3 = ['A','B','C','D']
list3.insert(1,'E')
print(list3)

# Remove Specific Item
list4 = ['A','B','C','D']
list4.remove('A')
print(list4)

# pop() removes the specified index 
list5 = ['A','B','C','D']
list5.pop(1)
print(list5)
# or last index.
list6 = ['A','B','C','D']
list6.pop()
print(list6)

# clear() empties the list
list7 = ['A','B','C','D']
list7.clear()
print(list7)

# Copy a List 
list8 = ['A','B','C','D']
new_list = list8.copy()
list8.pop()
print(list8)
print(new_list)

# Another way to make a copy is to use the list()
list9 = ['A','B','C','D']
new_list = list(list9)
list9.pop()
print(list9)
print(new_list)

# list() for creating new list
list11 = list(('app', 'ddd', 'eee'))
print(list11)