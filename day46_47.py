#Library Class
class Library:
    def __init__(self, book, shelf):
        self.book = book
        self.shelf = shelf

    def print_info(self):
        print('Books is ',lib.book, 'Shelfs is ',lib.shelf)

class Sience_section(Library):
    def __init__(self, book, shelf):
        super().__init__(book, shelf)
        self.name ='Physics books'
#Q1
lib = Library(300, 45)
lib.print_info()
#Q2
sience =Sience_section(300, 45)
print(sience.name)
#Q3
lib.book = 20
lib.shelf = 4
lib.print_info()