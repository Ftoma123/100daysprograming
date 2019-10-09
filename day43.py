 #inheretance
 #parent class
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

x = person('Jhon', 'Doe')
x.printname()

# Create a Child Class
class student(person):
    pass
s = student('Noura','Almulhim')
s.printname()

class student1(person):
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname) #for not overridde init() from parent
s1 =student1('Nasser', 'Almulhim')
s1.printname()