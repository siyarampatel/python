l=[1,2,3,4,5,6,7,8,9]
l1=[i*i for i in l if i%2==0]
l2=[i*i for i in l if i%2!=0]
print("even=",l1,"odd=",l2)