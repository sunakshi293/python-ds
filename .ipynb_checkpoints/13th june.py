# Question number 1
print("*************************************")
num=int(input("Enter a number:"))
if num==1:
    print("January")
elif num==2:
    print("February")
elif num==3:
    print("March")
elif num==4:
    print("April")
elif num==5:
    print("May")
elif num==6:
    print("June")
elif num==7:
    print("July")
elif num==8:
    print("August")
elif num==9:
    print("September")
elif num==10:
    print("October")
elif num==11:
    print("November")
elif num==12:
     print("December") 
else:
    print("invalid") 
    
# Question number 2
print("**********************************")
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
fname=input("Enter your first name:")
lname=input("Enter your last name:")
name=fname+ "   "+lname
print("a= ",a)
print("b= ",b)
print("name= ",name) 
if a>b:
    print(a, " is greater than ",a)
    for i in range(5):
        print(fname)
elif b>a:
    print(b, " is greater than ",a)
    for i in range(3):
        print(lname)
else:
    print(a, "is equal to ",b)
    
# Question number 3
print("************************************")
str1=input("Enter first string: ")
str2=input("Enter second string: ")
if str1==str2:
    print("string 1 is equal to string 2")
else:
    print("string are not equal")
if str1 is str2:
    print("string 1 and string 2 are equal(ID)")
else:
    print("stringare not equal(ID)")
    
# Question number 4
print("**************************************")
str1=input("Enter first string: ")  
str2=input("Enter second string:") 
# strimgs cannot be converted into numbers 
if str1 is str2:
    print("string 1 and string 2 are equal")
else:
    print("strings are not equal(ID)" ) 
    
# Question number 5
print("***************************************")
num=int(input("Enter a number: "))
sum=0
for i in range(num+1):
    sum=sum+i
print("sum from 0 to ",num,"=",sum)
 
# Question number 6
print("*****************************************")
num=int(input("Enter a number:"))
print("Even numbers are ")   
for i in range(num+1)
    if i%2==0:
        print(i,end="  ")
        
# Question number 7
print("**************************************")
