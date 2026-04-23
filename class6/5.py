l=[1,2,3,4,5,6,7,8,9]
for i in range(0,len(l)):
    if l[i]%2==0:
        l[i]="even"
    else:
        l[i]="odd"
print(l)