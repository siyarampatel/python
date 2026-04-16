# inut list and print second larget elemet
print("Input elements")
l = list(map(int, input().split()))
m=l[0]
s=l[0]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
for i in range(len(l)):
    if l[i]<m and l[i]>s:
        s=l[i]
print("The second largest element is:",s)