#Object Methods 
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print('my age is '+self.age)

p1 = person('Jhon', 40)
print(p1.age)

#Modify Object Properties 
p1 = person('Jhon', 40)
p1.age = 10
print(p1.age)

#Delete Object Properties 
p1 = person('Jhon', 40)
del p1.age
print(p1.age)

#Delete Objects 
p1 = person('Jhon', 40)
del p1
print(p1)

