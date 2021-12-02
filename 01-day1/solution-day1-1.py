"""
Advent of Code Day 1 Puzzle 1

This report indicates that, scanning outward from the submarine, 
the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the 
depth increases, just so you know what you're dealing with - 
you never know if the keys will get carried into deeper water 
by an ocean current or a fish or something.

To do this, count the number of times a depth measurement 
increases from the previous measurement. (There is no 
measurement before the first measurement.)
"""
import os

# Initialize increase count
increases = 0

# Open input file
with open(os.path.join('..', 'input', 'sonar.txt'), 'r') as sonar:
	# Get the first line
	previous_depth = sonar.readline()
	
	# Continue with the rest of the lines
	for depth in sonar:
		# Note if there was an increase
		increases += (int(depth) - int(previous_depth)) > 0
		# Prepare for next round
		previous_depth = depth

		
print(increases)
