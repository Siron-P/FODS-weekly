#Write a program to find the simple interest when the value of principle, 
#rate of interest and time period is provided by the user.

#Taking user input for principle, interest, and time period
print("Calculating The Simple Interest\n")
P = int(input("Value of Principle: "))
T = int(input("\n Time Period: "))
R = int(input("\n Rate of Interest: "))

#Calculating simple interest
Simple_Interest= (P*T*R)/100

#Displaying Output
print("The simple interest is ",Simple_Interest)