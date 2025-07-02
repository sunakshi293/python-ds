# Question number 1
str1=input("Enter a string: ")
l=len(str1)
if l<2:
    print("invali string")
else:
    str2=str1[:2]+str1[1-2:1]
    print("new string-",str2)
    
# Question number 2
print("****************************************")
str1=input("Enter first string- ")
str2=input("Enter second string-")
a=str1[:1]
b=str2[:1]
str1=str1.replace(a,b)
str2=str2.replace(b,a)
print("new strings= ",str1," ",str2)

# Question number 3
str1=input("enter a string: ")
l=len(str1)
if l<3:
    print("string- ",str1)
elif str1.endswith("ing"): 
    print("New string- ",str1+"ly") 
else:
    print("New string- ",str1+"ing")
    
# Question number 4
print("******************************************")
str1=input("Enter a string: ")
if len(str1)==0:
    print("string is empty")
else:
    a=int(input("Enter the index: "))
    if a>len(str1):
        print("Enter index is greater than the length of string")
    else:
        print("string= ",str1)
        print("New string= ",str1[:a]+str1[a+1:]) 
