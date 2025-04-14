#Write a Python program that accepts a string 
#and calculates the number of digits and letters.

#taling input from user
string = (input("Enter a string: \n")) #storing input in variable "string"

#creating a function
def counting(string):

    count_letter = 0 
    count_digits = 0
    #initializing count of letter and digit as zero

    for char in string: #for loop to check
        if char.isalpha(): #to find if the string are letters
            count_letter += 1
            #increasing count value

        elif char.isdigit():#to find if the string are letters
            count_digits += 1
            #increasing count value

        else:
            print("Invalid Input!!!") #if wrong input is given
        
    print("Number of Letters: ",count_letter)
    print("Number of digits: ",count_digits)
    #printing the final count of letters and digits

counting(string)#calling the function
