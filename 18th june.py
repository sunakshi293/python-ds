#  Question number 1
t1=(10,20,10,22,10 ,25,50)
print(t1)
t1=set(t1)
t1=tuple(t1)
print("After removing duplicate elements: ",t1)

# Question number 2
print("__________________________________________________")
l1=[[1,2],[3,4],[5,6]]
print("oringinal list: ",l1)
l2=[j for i in  l1 for j in i ]
print("flattened list: ",l2)

# Question number 3
print("____________________________________________________")
tup=(3,5,1,8,2)
print("original Tuple: ",tup)
tup=list(tup)
tup.sort()
print("Min= ",tup[0])
print("Max= ",tup[-1])

# Question number 4
print("_________________________________________________")
l1=[(i,i**3) for i in range(1,6)]
print("list :",l1)
