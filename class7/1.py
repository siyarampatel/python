l1=["red","orange","green","blue","white"]
l2=["black","yellow","green","blue"]
l2l1=[]
l1l2=[]
for i in l1:
    if i not in l2:
        l1l2.append(i)

print("L1-L2",l1l2)

for i in l2:
    if i not in l1:
        l2l1.append(i)

print("L2-L1",l2l1)