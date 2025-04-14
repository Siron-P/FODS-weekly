'''
Create a program called calculator with functions to perform the following 
arithmetic calculations, each should take two decimal parameters and 
return the result of the arithmetic calculation in question.[7]
A. Addition
B. Subtraction
C. Multiplication
D. Division
E. Truncated division
F. Modulus
G. Exponentiation
'''

#Creating function for Addition 
def Addition(n1,n2):
    return n1+n2

#Creating function for Subtraction
def Subtraction(n1,n2):
    return n1-n2

#Creating function for Multiplication
def Multiplication(n1,n2):
    return n1*n2

#Creating function for Division
def Division(n1,n2):
    return n1/n2

#Creating function for Truncated Division
def Truncated_division(n1,n2):
    return n1//n2

#Creating function for Modulus
def Modulus(n1,n2):
    return n1%n2

#Creating function for Exponentiation
def Exponentiation(n1,n2):
    return n1**n2

#Creating function for the main code
def main():
    #asking user for 2 input
    print("\n \n \n--------CALCULATOR--------")
    print("Enter any two numbers for its calculations \n \n")
    n1 = float(input("The first decimal number: "))
    n2 = float(input("The second decimal number: "))

    #printing all the values
    print("Addition : ",Addition(n1,n2))
    print("Subtraction : ",Subtraction(n1,n2))
    print("Multiplication : ",Multiplication(n1,n2))
    print("Division : ",Division(n1,n2))
    print("Truncated Division : ",Truncated_division(n1,n2))
    print("Modulus : ",Modulus(n1,n2))
    print("Exponentiation : ",Exponentiation(n1,n2))

#Calling the main function to run the code
main()

