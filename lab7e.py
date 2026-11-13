# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Nay Dwe Naing
# Date:11/13/2026
# Purpose: Create Series.
# Usage: ./lab7e.py

# TO DO 1: Import pandas module.
import pandas as pd

# TO DO 2: Create a series according to instructions given in readme.md file.
grades = ["<50", "50-59", "60-69", "70-79", "80-89", "90-100"]
gradeseries = pd.Series(grades, index=["F", "D", "C", "B", "A", "A+"])
print(gradeseries)

# TO DO 3: Perform the operations on this series given in readme.md file.
print(gradeseries.loc[["C"]])

# TO DO 4: Run the script.