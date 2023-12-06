list=["apple","orange","pappaya","banana"]
max_length=0
for word in list:
    current_length=0
    for char in word:
        current_length+=1
    if current_length>max_length:
        max_length=current_length
print("length of longest word:",max_length)        
