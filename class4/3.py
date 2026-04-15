n=int(input("give n"))
r=int(input("give r"))
def ncr(n,r):
    factr=1
    factn=1
    factnr=1
    for i in range(1,n+1):
        factn*=i;
    for i in range(1,r+1):
        factr*=i;
    nr=n-r
    for i in range(1,nr+1):
        factnr*=i;
    return factn//(factr*factnr)

result = ncr(n,r)
print("ncr->",result)


