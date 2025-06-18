# Question number 1
list1=["Hello","Dsuya","Hey","Here","Mukerian","hii"]
result=[i for i in list1 if len(i)<=4]
print("strings wuth less than fourlatters:" ,result)

# Question number 2
print("-----------------------------------")
list1=[i for i in range(20)]
print(list1)
list2=["even" if i%2==0 else "odd" for i in list1]
print("New list:" ,list2)

# Question number 3
print("--------------------------------------")
l1=[i for i in range(1,1000) if i%7==0]
print("numbers divisible by 7: ",l1)

# Question number 4
print("---------------------------------------")
str1="Hey! How are you? I hope you are doing great."
count=0
for i in str1:
    if i==" ":
        count+=1
print("Total number of spaces:", count)

# Question number 5
print("------------------------------------")
list_a=[1,2,3,4]
list_b=[2,3,4,5]
l=[i for i in list_a for j in list_b if i==j]
print("New list:" ,l)