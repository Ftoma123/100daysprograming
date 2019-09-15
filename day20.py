set1 = {1,2,"Ahmed",2}
#items not repeated in the set
print(set1)

#print item using for
for x in set1:
    print(x)

#check if item exsit (true or false)
print(5 in set1)

#Add one item
set1.add('Nasser')
print(set1)

#add multiple items
set1.update(['Fahad','ww',5])
print(set1)