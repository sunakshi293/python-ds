# Question number 1
print("welcome to coderail ticket booking system")
name=input("Enter the name: ")
age=int(input("Enter the age: "))
print("choose your travel class")
print("1. first class -Rs.1500")
print("2. second class -Rs.1000")
print("3. sleeper class -Rs.500")
choice=int(input("choice- "))
if choice==1:
    clss="First class"
    price=1500
elif choice==2:
    clss="Second class"
    price=1000
elif choice==3:
    clss="Third class"
    price=500
else:
    print("invalid choice") 
    exit()
    
if age<=5:
    print("Ticket is free: ")
    price=0
elif age>=60:
    print("20% discount") 
    price=price-(price/5)
print("Do you want to include the meal?(Y/N:")
meal=input("Enter your choice: ")
if meal=='y' or meal=='Y':
    price=price+200
    print("Rs. 200 extra")
    m='Yes'
elif meal=='n' or meal=='N':
    print("No extra charges")
    m='No'
else:
    print("invalid choice")
    m='no'
    
# Question number 2
print("********************************************")
print("welcome to burger king")
print("\tMenu")
print("\t Item          \t price(Rs)")
print("\t1.whopper burger  \tRs.150")
print("\t2.crispy veg       \tRs.100")
print("\t3.chicken wings     \tRs.120 ")
choice=int(input("Enter the item number(1\2\3):"))
print()
if choice==1:
    price=150
elif choice==2:
    price=100
elif choice==3:
    price=120
else:
    print("invalid choice: ")
    exit()
    
qt=int(input("Enter quantity: "))
price=qt*price
print()

coup=input("Do you have coupon code?(yes\no): ")
print()
if coup.lower()=="yes":
    code=input("Enter your coupon code: ")
    print("Applying coupon code.....")
    price=price-(price*0.5)
if code=='kING50':
    print("Original price- ",price)
    print("Discount applied: 50%")
    price=price-(price*0.5)
if code=='BK20':
    print("original price-",price) 
    print("Discount applied: Rs20")
    price=price-20
else:
    print("Invalid coupon code")
    print("No coupon applied")
    
print("Final price:", price)
print("Thank you for ordering at burger king!")

             