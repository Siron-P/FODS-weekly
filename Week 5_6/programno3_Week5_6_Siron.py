'''Write a program to find and replace 
a specific word in a file with another word'''

find_word = "Python"
replace_word = "It"

with open("program3.txt",'r') as f:
    data = f.read()
    data = data.replace(find_word,replace_word)

with open("program3.txt",'w') as f:
    f.write(data)

print("Word Replaced!")
