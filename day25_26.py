#Q1 
set1 = {1,3,5,7,8}
print(set1)

#add to the set (4,8,12)
set1.update([4,8,12])
print(set1)

#remove 8 element
set1.remove(8)
print(set1)

#remove all item
set1.clear()
print(set1)


#Q2
#create dictionary
dict1 = {
    'type':'Bird',
    'skin cover':'Feathers'
}
print(dict1)

#print value of type
type = dict1['type']
print(type)

#change skin cober value
dict1['skin cover'] = 'New Feathers'

print(dict1)
