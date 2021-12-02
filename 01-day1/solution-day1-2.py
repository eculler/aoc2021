"""
Day 2 Puzzle 2

Considering every single measurement isn't as useful as you 
expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window.

Start by comparing the first and second three-measurement 
windows. The measurements in the first window are marked 
A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The 
second window is marked B (200, 208, 210); its sum is 618. 
The sum of measurements in the second window is larger than 
the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of 
measurements in this sliding window increases from the 
previous sum. So, compare A with B, then compare B with C, 
then C with D, and so on. Stop when there aren't enough 
measurements left to create a new three-measurement sum.
"""
import os

import numpy as np

# Read in the data
sonar = np.loadtxt(os.path.join('..', 'input', 'sonar.txt'))

# Compute differences
sonar_diff = (sonar[3:] - sonar[:-3]) > 0

# Compute number of increases
increases = sonar_diff.sum()

# Print answer
print(increases)
