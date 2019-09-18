#Loop (While)
#simple while
i = 1
while(i < 6):
    print(i)
    i +=1

print("__________")

# While with break
i = 1
while(i < 6):
    print(i)
    if i == 3:
        break
    i += 1

print("__________")

#While with continue
i = 0
while (i < 6):
    i += 1
    if i == 3:
        continue
    print(i)
    
print("__________")

#While with else
i = 1
while (i < 6):
    print(i)
    i += 1
else:
    print('i >= 6')
    