dict={}
x=int(input("enter the limit of students:"))
for i in range(0,x):
    key=input("enter the student roll no:")
    value1=int(input("enter the mark of 1st subject"))
    value2=int(input("enter the mark of 2nd subject"))
    value3=int(input("enter the mark of 3rd subject"))
    value4=int(input("enter the mark of 4th subject"))
    value5=int(input("enter the mark of 5th subject"))
    dict[key]=value1,value2,value3,value4,value5
    total=value1+value2+value3+value4+value5
    percentage=(total/100)*100
    print("percentage of roll no.",key,"is:",percentage,"%")
print(dict)
