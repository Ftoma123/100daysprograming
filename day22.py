#creating Dictionary
dict1 = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1934
}
print(dict1)

#access item
model = dict1["model"]
print(model)

#access item using get()
model = dict1.get('model')
print(model)

#change value
dict1['brand'] = "Ferari"
print(dict1)

#loop to print keys
for x in dict1:
    print(x)

#loop to print values
for x in dict1:
    print(dict1[x])

#loop to print value using values()
for x in dict1.values():
    print(x)

#loop to print keys and values
for x, y in dict1.items():
    print(x,y)

#print all keys and values withou loop using items()
print(dict1.items())