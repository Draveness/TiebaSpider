f = open('items.json','r')
line = f.readline()
while line:
    print line,
    line = f.readline()

f.close()
