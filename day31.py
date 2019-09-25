#calling function
def my_function():
    print('Hello, you are in the function')

my_function()

print('___________________')
#function with parameter
def my_function2(name):
    print('Hello ' + name )

my_function2('Fatima')
my_function2('Noura')

print('___________________')
#function with default parameter
def my_function3(name = "Hessah"):
    print('Hello '+ name)

my_function3('norah')
my_function3('sara')
my_function3()
