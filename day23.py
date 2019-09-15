dict1 ={
    "brand":"Ford",
    "model":"mustang",
    "year":1934
}

#check if key exsit
if "brand" in dict1:
    print("true, brand exsit")

#Dictionary length
print(len(dict1))

#adding item
dict1["color"] = "red"
print(dict1)

#remove specifi item using pop()
dict1.pop('model')
print(dict1)

#remove last item using popitem()
#dict1.popitem()
print(dict1)

#remove specific item using del
del dict1['brand']
print(dict1)

#clear the dictionary using clear()
dict1.clear()
print(dict1)

#remove the dictionaty copletly using del
del dict1
print(dict1)
