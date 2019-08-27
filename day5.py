x = "Apple"
y = "Orange"
z = "Limon"
print(x+' '+y+' '+z)

line = "Apple Orange Limon"
n = 6
c = [line[i:i+n] for i in range(0, len(line), n)]
print(c)