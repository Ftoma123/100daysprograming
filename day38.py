#looping in array
cars = ['Ford', 'Ferrai', 'BMW', 'GMC']
for x in cars:
    print(x)

#add element
cars.append('new brand')
print(cars)

#removing element
cars.pop(2)
print(cars)

#remove element using its value
cars.remove('Ford')
print(cars)