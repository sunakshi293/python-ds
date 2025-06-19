# Question number 1
l1=[1,2,3,4,5,6,7,8,9,10]
print(l1)

# Question number 2
print("__________________________________________")
l1=[1,10,100,3,6,8]
print(l1)
print("length=",len(l1))
l1.insert(59,3)
l1.append(5)
print("New list= ",l1)
print("New lengths=" ,len(l1))

# Question number 3
print("____________________________________________")
l1=[1,4,2,42,4,6,2,56,4,56,2]
print(l1[::2])

# Question number 4
print("______________________________________________")
l1=["Guarav",12,23,33.33,"Sharma",True]
l2=[]
for i in l1:
  if type(i)==str:
    l2.append(i)
print("New list= ",l2)

# Question number 5
print("______________________________________________")
l1=("Gaurav",12,23,33.33,"Sharma",True)
sum=0
for i in l1:
    if type(i)==int:
        if type(i)==int:
          sum=sum+i
print("sum of all number= ",sum)

# Question number 6
print("__________________________________________")
l1=["Isha","Tannu","neelakshi","Anjali","palak"]
print(l1)
frnd1=input("Enter a friend: ")
l1.append(frnd1)
print(l1)
frnd2=input("Enter the most important freind: ")
ind=int(input("Enter the location: "))
l1.insert(ind,frnd2)
print("New list: ",l1)