#Write a function to accept a list of names 
#and return the sorted order of names back.

def List_of_names():
    #taking input and storing in listinput variable
    listinput = input("Enter some words separated by space; ").split()

    #Sorting orders of list with ".sort()"
    listinput.sort()
    return listinput

#Calling the function and storing it to another variable
Sorted_order = List_of_names()

#displaying the sorted order
print("The sorted order of names are \n",Sorted_order)

