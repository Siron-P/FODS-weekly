#3. Create a vector of size 10 with values ranging from 0 to 1, both excluded.

import numpy as np
#vector from 0-1 of size 10
vector = np.linspace (0,1,10)[1:-1] #selects elemts from index one to second last element
print (f"The vector of 0-10 is {vector}")