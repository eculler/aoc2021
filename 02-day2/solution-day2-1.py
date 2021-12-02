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

import pandas as pd

# Read in the data
directions = pd.read_csv(
	os.path.join('..', 'input', 'directions.txt'),
	sep=' ',
	names=['direction', 'amount'])

# Set quantities as negative for down
directions.loc[directions.direction=='up', 'amount'] *= -1
# Group into horizontal and depth
directions.direction.replace('forward', 'horizontal', inplace=True)
directions.direction.replace(['up', 'down'], 'depth', inplace=True)

# Add up
final_location = directions.groupby('direction').sum()

# Print product
print(final_location.product())