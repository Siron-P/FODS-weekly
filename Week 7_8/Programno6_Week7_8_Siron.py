#6.Write a program to input an array of numbers from the user (at least 10 elements in list), 
# sort them and perform slicing operations to get elements between indexes such as 2-5, 5-8, 2-9. 

import numpy as np
number = []
for i in range (0,10) :
  num = int (input(f"Enter the number {i+1} : "))
  number.append(num) #appending the number in empty list

number_array =np.array(number) #converting into array
print (f"Original array: {number_array}")

sort_arr = np.sort(number_array)
print (f"The sorted number: {sort_arr}")

slicing1 = sort_arr[2:6] #displays elements from 2-5 index
slicing2 = sort_arr[5:9]
slicing3 = sort_arr[2:10]

print (f"The elements between 2-5: {slicing1}")
print (f"The elements between 5-8: {slicing2}")
print (f"The elements between 2-9: {slicing3}")