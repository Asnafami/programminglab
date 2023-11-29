list=[]
n=int(input("enter number of element:"))
for i in range(0,n):
    x=int(input())
    if x>=100:
        x='over'
    list.append(x)
print(list)
    
