list=[23,56,78,90]
x=max(list)
y=list.index(x)
print("the largest no.",x,"is position",y)
num=11
if num>1:
    for i in range(2,num):
        if (num%i==0):
            print("number",num," is not prime")
            break;
    else:
       print("number",num, "is prime")
else:
    print("number",num," is prime")

               
               

        
                      

