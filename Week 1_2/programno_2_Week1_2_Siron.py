#Write a program that prompts the user for two integer values
#and displays the results of the first number divided by the second, 
#with exactly two decimal places displayed. 

#Prompt the user for 2 integer values
print("\n Enter any 2 numbers for their division: ")
num1 = int(input("\n The First Number : ")) #taking 1st number input
num2 = int(input("\n The Second Number : ")) #taking 2nd number input

#program to calculate division
div = num1/num2

#printing the result of the user input with exactly two decimal places displayed.
print(f"The result of {num1} divided by {num2} is {div:.2f}")