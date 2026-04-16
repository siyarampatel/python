# inut list and print larget elemet
l = list(map(int, input().split()))
m=l[0]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
print("The max element is:",m)