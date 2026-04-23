l=[0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4]
l.sort();
l1=[]
for i in range(0,len(l)):
    if l[i]!=l[i-1]:
        l1.append(l[i])
print(l1)
    