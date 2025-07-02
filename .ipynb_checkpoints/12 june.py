#Question number 1
print("***************************")
name=input("Enter student names:")
std=input("Enter student class:")
section=input("Enter student setion:")
english=int(input("Enter marks in ENGLISH:"))
maths=int(input("Enter marks in MATHS:"))
de=int(input("Enter marks in DE:"))
oops=int(input("Enter marks in OOPS:"))
daa=int(input("Enter marks in DAA:"))
total=english+maths+de+oops+daa
av=total/5
print("-----------------------------------")
print("\t\RESULT")
print("-----------------------------------")
print("Name-",name)
print("Class-",std)
print("Section-",section)
print("percentage scored-",av,"%")

#Question number 2
print("*********************************")
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter  a number:"))
sum=a+b+c
print("sum",sum)

#Question number 3
print("**********************************")
a=int(input("Enter a number:"))
print("Square=",a*a)

#Question number 4
print("***********************************")
temp=input("Enter the temperature in celsius-")
tempc=float(temp)
tempf=(tempc*(9/5))+32
print("Temperature in celsius=",tempc)
print("Temperature in fahrenheit=",tempf)

#Question number 5
print("************************************")
a=int(input("Entera number"))
b=int(input("Enter a number"))
quotient=a//b
remainder=a%b
print("Quotient=",quotient)
print("Remainder=",remainder)