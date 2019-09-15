#copy dictionary using copy()
dict1 = {
    'brand':'Ford',
    'model':'Mustang',
    'year':1934
}

new_dict = dict1.copy()
print(new_dict)

#copy dictionary using dict()
new_dict1 = dict(dict1)
print(new_dict1)

#Nested Dictionaries 
family_dict = {
    'child1':{
        'name':'Noura',
        'year':2000
    },
    'child2':{
        'name':'Nada',
        'year':2006
    },
    'child3':{
        'name':'Nasser',
        'year':2012
    }
}
print(family_dict)

#Nested Dictionaries by creating 3 indivisual dict then incluse them in other dict
child1 = {
    'name':'Abodi',
    'year': 2008
}
child2 = {
    'name':'Ftoma',
    'year': 2005
}
child3 = {
    'name':'Monera',
    'year': 2019
}

family_dic1 ={
    'child1': child1,
    'child2': child2,
    'child3': child3
}

print(family_dic1)

#creat dictionay using dict()
dict2 = dict(brand='Ford', model='Mustang', year=1934)
print(dict2)