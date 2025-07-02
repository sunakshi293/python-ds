# Question 1
l1=[20,25,19,10,77,82,11,15,10,64]
print(l1)

# Question number 2
print("***************************************")
l1=[1,10,100,3,6,8]
print(l1)
print("length= ",len(l1))
l1.insert(59,3)
l1.append(5)
print("New list= ",l1)
print("New length= ",len(l1))

# Question number 3
print("******************************************")
l1=[1,4,2,42,4,6,2,56,4,56,2]
print(l1[::2])

# Question number 4
print("*********************************")
l1=["Gaurav",12,23,33.33,"Sharma",True]
l2=[]
for i in l1:
    if type(i)==str:
        l2.append(i)
print("New list= ",l2)

# Question number 5
print("*******************************************")
l1=["Gaurav",12,23,33.33,"Sharma",True]
sum=0
for i in l1:
    if type(i)==int:
        sum=sum+i
print("Sum of all numbers= ",sum)

# Question number 6
print("***************************************")
l1=["Isha","Tannu","Neelakshi","Anjali","palak"]
print(l1)
frnd1=input("Enter a friend: ")
l1.append(frnd1)
print(l1)
frnd2=input("Enter the most important friend: ")
ind=int(input("Enter the location: "))
l1.insert(ind,frnd2)
print("New list: ",l1)