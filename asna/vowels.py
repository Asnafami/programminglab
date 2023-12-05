list=["apple","orange","grape","banana"]
vowel='a e i o u'
list1=[x for x in list for x in x if x in vowel]
n=len(list1)
print("no.of vowel:",n)
for i in list:
    w=len(i)
    print("length of",i,":",w)
    if(w>=18):
        print(i,"word length is:",w)
