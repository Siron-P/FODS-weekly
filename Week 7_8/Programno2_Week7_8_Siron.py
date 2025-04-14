#2. Ask user to input two numbers a, b. 
#Write a program to generate a random array of shape (a, b) and
#print the array and avg of the array

import numpy as np

a = int(input("Enter the row of the array : "))
b = int(input("Enter the column of the array : "))
#generating the random array
rand_array = np.random.randint(0,100, size=(a,b)) #random number from 0-1, array shape user input
print(rand_array)

average = np.mean(rand_array) #for finding the average
print (f"THe average of the array is {average}")