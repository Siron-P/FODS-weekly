'''Write a function that accepts a string
and calculate the number of upper case 
letters and lower case letters.''' 

a=input("Enter Some Words: \n")

#initializing upper and lower count as zero
ucount=0
lcount=0

#for loop to check upper case and lower case letters
for i in a:
    if i.islower():
        lcount+=1
    elif i.isupper():
        ucount+=1

print("The number of upper case letters is",ucount)
print("The number of lower case letters is",lcount)
