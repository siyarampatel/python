n=int(input("give n"))
def oe (n):
    even=1
    odd=1
    if(n%2==0):
        print("no is even")
        for i in range(1,n+1):
            if n%i==0 and i%2!=0:
                even*=i
        print("product of odd factors->",even)
    else:
        print("number is odd")
        for i in range(1,n+1):
            if n%i==0 and i%2==0:
                odd*=i
                print("product of even factors->",odd)


oe(n)
      

