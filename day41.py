#create object
class MyClass:
    x = 5

p1 = MyClass() #تعريف لل opject
print(p1.x)
print('_______________')
#___________

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person('Jhon', 13)
print(p1.name)
print(p1.age)
print('_______________')
#___________

class person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfun(abc):
        print('my name is ', abc.name)

p1 = person('Jhon', 12)
p1.myfun()
