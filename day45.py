#itrator of list
mytuple = ['apple', 'banana', 'mango']
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
#______________
print('__________')

#itrator of string
mystr = 'banana'
myit1 = iter(mystr)
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
#______________
print('__________')

#Create an Iterator 
class Mynumbers:
    def __iter__(self):
        self.a =1
        return self

    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

Myclass = Mynumbers()
Myiter = iter(Myclass)

print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))

