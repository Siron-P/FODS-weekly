#7. Create an array of random integer numbers as a numpy array, 
#sort them and perform operations such as reshaping of the array into matrix of feasible dimensions.
#(e.g., if we have an array of 1 * 10, then we can reshape it into 2 * 5 or 5 * 2 matrix.)
#[Hint: Use the array of reshape (row * column)] 

import numpy as np

array = np.random.randint(0,100,size=10)
sorted_array=np.sort(array)
matrix_2_5=sorted_array.reshape(2,5)
matrix_5_2=sorted_array.reshape(5,2)

print("original array: ")
print(array)
print("\nsorted array: ")
print(sorted_array )
print("\nreshaed matrix (2x5): ")
print(matrix_2_5)
print("\nreshaped matrix (5x2): ")
print(matrix_5_2)