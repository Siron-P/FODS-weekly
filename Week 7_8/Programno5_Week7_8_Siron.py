#5. Create a 5x5 matrix with row values ranging from 0 to 4

import numpy as np

matrix = np.arange(25).reshape(5,5) #making (5,5) matrix
matrix = matrix % 5 #keeping the remainder in matrix 
print (f"The 5x5 matrix 0-4 is \n {matrix}")