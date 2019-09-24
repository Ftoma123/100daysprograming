#Loop through string
for x in "banana":
    print(x)

#Loop with breack
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x =='banana':
        break
#Loop with breack (cahnge order)
for x in fruits:
    if x =='banana':
        break
    print(x)

#Loop with continue
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x =='banana':
        continue
    print(x)