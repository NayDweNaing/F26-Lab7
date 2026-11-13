# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date: 11/13/2026
# Purpose: Create Series.
# Usage: ./lab7d.py
import numpy as np
# Creating a 2D NumPy array
arr_2d = np.array([[10, 20, 30, 40, 50],[60, 70, 80, 90, 100],[110, 120, 130, 140, 150],[160, 170, 180, 190, 200]])
print("original:\n",arr_2d)
arr_2d = arr_2d[:2, 2:]
print("sliced:\n",arr_2d)
middle = arr_2d[1:3, 1:3]
print("middle:\n",middle)
everyother = arr_2d[::2, ::2]
print("every other:\n",everyother)