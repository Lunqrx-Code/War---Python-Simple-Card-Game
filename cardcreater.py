c=1
x=1
y=0
list=[]
for i in range (52):
    if c <=4:
        y+=1
    if c > 4:
        y=1
        x+=1
        c=1
    array=[x,y]
    list.append(array)
    c+=1

print(list)
