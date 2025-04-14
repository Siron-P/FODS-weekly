#Write a program to take a number input from the user 
#and display whether the number is even or odd.

#Asking user to give input
print("\n Enter a number to find out it is odd or even? \n")
num = int(input("Insert any number: ")) #taking input and storing in 'num'

#checking odd or even
if(num%2==0): #to determine even number
    print("\n The number {num} is even number!!") 
else: #if not even number the program will display it as odd through else condition
    print("\n The number", num, " is odd number!!")