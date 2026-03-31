# name = input("Enter your name:")
# print("your name is",name)

# def greet(name):
#  print("ram ram",name)

# greet("abhijeet")

# prime number code


number = int(input("Enter your number"))
if number>1:
    for i in range(2,number//2):
     if number%i==0:
      print("It's not an prime number")
      break
    else:
     print("It's an prime number")

else:
    print("Tt's not an prime nunber")
