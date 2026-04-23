l=[0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4]
l1=[]
temp=[l[0]]
for i in range(1,len(l)):
    if l[i]==l[i-1]:
        temp.append(l[i])
    else:
        l1.append(temp)
        temp=[l[i]]

print(l1)