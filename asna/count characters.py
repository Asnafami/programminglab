string="hello world"
char_frequency={}
for char in string:
    if char in char_frequency:
        char_frequency[char]+=1
    else:
        char_frequency[char]=1
print(char_frequency)
