# Question number 1
print("*******************************")
name=input("Enter student's name: ")
std=input("Enter student's class: ")
section=input("Enter student's section: ")
english=int(input("Enter marks in ENGLISH: "))
os=int(input("Enter marks in OS: "))
maths=int(input("Enter marks in MATHS: "))
de=int(input("Enter marks in DE: "))
oops=int(input("Enter marks in OOPS: "))
total=english+os+maths+de+oops
av=total/5
print("-------------------------------------------")
print("\t\tRESULT")
print("-------------------------------------------")
print("Name- ",name)
print("Class- ",std)
print("Section- ",section)
print("Percentage scored- ",av,"%")

# Question number 2
print("*******************************")
a=int(input("Enter a number "))
b=int(input("Enter a number "))
c=int(input("Enter a number "))
sum=a+b+c
print("Sum ",sum)

# Question number 3
print("*******************************")
a=int(input("Enter a number "))
print("Square= ",a*a)

# Question number 4
print("*******************************")
temp=input("Enter the temperature in Celsius- ")
tempc=float(temp)
tempf=(tempc*(9/5))+32
print("Temperature in Celsius= ",tempc)
print("Temperature in Fahrenheit= ",tempf)

# Question number 5
print("***************************")
a=int(input("Enter a number  "))
b=int(input("Enter a number  "))
quotient=a//b
remainder=a%b
print("Quotient= ",quotient)
print("Remainder= ",remainder)