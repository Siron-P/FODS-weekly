'''Create a function called word_intersection that prompts
 the user for two English words, and displays 
 which letters the two words have in common. '''

#Creating a funciton
def Word_intersection():
    print("Enter any two English words: ")
    a = input("First word: ")
    b= input("Second Word: ")
    #Asking user for input

    #storing outcome in new variable
    common_letters = set(a) & set(b)
    #finding common letters by converting both variables into set
    
    #if...else condition to print common letter if there is
    if common_letters:
        print("The common letters are :",common_letters)
    else:
        print("The two words doesn't have any word in common")

Word_intersection() #calling function
