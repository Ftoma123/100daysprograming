#using range() in Loop
for x in range(6):
    print(x)

print('____________________')
#using range() with parameter
for x in range(2,6):
    print(x)

print('____________________')
#using range() with specific increment
for x in range(2,20,3): #(start, ende, increment)
    print(x)

print('____________________')
#else
for x in range(0,6):
    print(x)
else:
    print('finished')

print('____________________')
#nested loop
adj = ['red', 'big', 'tasty']
fruits = ['Apple', 'Banana', 'Cherry']

for x in adj:
    for y in fruits:
        print(x, y)