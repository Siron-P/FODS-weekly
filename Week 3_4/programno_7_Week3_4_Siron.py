'''
Write a program that prompts the user to enter integer values
to populate two lists, then prints messages to determine the following:
(a) Whether the lists are of the same length. 
(b) Whether the elements in each list sum to the same value. 
(c) Whether there are any values that occur in both lists
'''

#Asking user for 2 inputs
print("enter integer values to populate two lists \n")
#storing inputs in 2 variable as list
list1 = list(map(int, input("1st list of integers separated by spaces : ").split()))
list2 = list(map(int, input("2nd list of integers separated by spaces : ").split()))

#displaying list 1 and list 2
print("\n \n")
print("The list 1 is",list1)
print("The list 2 is ",list2)
print("\n \n")

#Checking Whether the lists are of the same length
if len(list1) == len(list2):
    print("The list are of same length")
else:
    print("The list are of different length")

#Checking Whether the elements in each list sum to the same value. 
if sum(list1)==sum(list2):
    print("The elements in each list sum to same value")
else:
    print("The elements in each list doesn't sum to same value")

#Checking Whether there are any values that occur in both lists
values = set(list1) & set(list2)
if values:
    print("Value that occur in both list are ", values)
else:
    print("there are no values that occur in both lists")


