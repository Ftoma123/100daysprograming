#Use the super() Function for inheritance
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student('Noura', 'Almulhim')
x.printname()
print('_________')
#_________

#Add Properties (value) to child class
class Person1:
    def __init__(self,fname1, lname1):
        self.firstname1 = fname1
        self.lastname1 = lname1
    def printname1(self):
        print(self.firstname1, self.lastname1)

class Student1(Person1):
    def __init__(self, fname1, lname1):
        super().__init__(fname1, lname1)
        self.graduationyear =2019
x1 = Student1('Jhon', 'Doe')
print(x1.graduationyear)
print('_________')

#Add Properties (variable) to child class
class Person2:
    def __init__(self,fname2, lname2):
        self.firstname2 = fname2
        self.lastname2 = lname2
    def printname2(self):
        print(self.firstname2, self.lastname2)

class Student2(Person2):
    def __init__(self, fname2, lname2, year):
        super().__init__(fname2, lname2)
        self.garduationyear = year

x2 = Student2('Fatima', 'Almulhim', 2016)
print(x2.garduationyear)
print('_______')
#____________

#Add Methods to the child class
class Person3:
    def __init__(self,fname3, lname3):
        self.firstname3 = fname3
        self.lastname3 = lname3
    def printname3(self):
        print(self.firstname3, self.lastname3)
class Student3(Person3):
    def __init__(self, fname3, lname3, year):
        super().__init__(fname3, lname3)
        self.graduationyear = year

    def welcome(self):
        print('Welcome ', self.firstname3, self.lastname3, 'in the class of', self.graduationyear)

x3 = Student3('Fatima', 'Almulhim', '2016')
x3.welcome()

