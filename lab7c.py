# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date: 11/13/2026
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py
import numpy as np
# TO DO 1: Create numArray according to instructions given in readme.md file.
slice1 = np.array(range(1,101))
print("slice1[0:10]:\n", slice1[0:10])
print("slice1[-1:-11:-1]:\n", slice1[-1:-11:-1])
print("slice1[21:(21+30)]:\n", slice1[21:(21+30)])
# TO DO 2: Perform the operations on numArray given in readme.md file.
slice1[50:65] = 101
print("slice1[50:65] = 101:\n", slice1)
# TO DO 3: Run the script.

