'''Write a program to copy the contents of one file to another'''

with open("program1.txt",'r') as firstfile, open("program2.txt",'w') as secondfile:

    for line in firstfile:
        secondfile.write(line)