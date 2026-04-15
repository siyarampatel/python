# list
# mutable
# dynamic in size
# mixed data types values can be stored
# can be created using[]
# sequence data structure can be acessed using index

#creation 
l=[];
l=[1,2,3,4]
l=[1,"hello",4.6]
l=list((1,2,3,4,5,6))
l=list("abcd")
print(list)

# Forward index:   0   1   2   3
# List:           [10, 20, 30, 40]
# Backward index: -4  -3  -2  -1
for x in l:
    print(x)

for i in range(len(l)):
    print(l[i])

for i, val in enumerate(l):
    print(i, val)



a = [i for i in range(5)]              # [0,1,2,3,4]
a = [i*i for i in range(5)]            # squares
a = [i for i in range(10) if i%2==0]   # even numbers

a = [[1,2], [3,4]]

a[0]        # [1,2]
a[0][1]     # 2



# reverse
a[::-1]

# max element
max(a)

# remove duplicates
list(set(a))

# flatten list
[x for sub in a for x in sub]