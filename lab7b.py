# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date: 11/13/2026
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab7b.py
import numpy as np
array1 = np.array([20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
array2 = np.array(range(20,50))
# TO DO 2: Reshape array1 reshapes array2 according to instructions given in readme.md file.
array1 = np.reshape(array1, (5,6))
array2 = np.reshape(array2, (2,3,5))
print(array1)
print(array2)
# TO DO 3: Create array5 according to instructions given in readme.md file.
array5 = np.eye(5)
array5 = np.diag([45,7,61,8,9])
print(array5)
# TO DO 4: Create array6 according to instructions given in readme.md file.
array6 = np.random.randint(0, 100, size=(7, 7))
print(array6)
# TO DO 5: Run the script.

