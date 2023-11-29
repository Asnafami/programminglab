list1=[]
list2=[]
a=int(input("enter the limit of 1st list:"))
b=int(input("enter the limit of 2nd list:"))
for i in range(0,a):
    print("enter 1st element in list1)
    x=int(input())
    list.append(x)
print(list1)
for i in range(0,b):
    y=int(input())
    list.append(y)
print(list2)
if len(list1)==len(list2):
    print("list are same length")
else:
    print("list are different length")
