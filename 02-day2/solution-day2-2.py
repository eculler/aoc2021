"""
Day 2 Puzzle 2

Based on your calculations, the planned course doesn't 
seem to make any sense. You find the submarine manual and 
discover that the process is actually slightly more complicated.

In addition to horizontal position and depth, you'll also need 
to track a third value, aim, which also starts at 0. The 
commands also mean something entirely different than you first 
thought:

	down X increases your aim by X units.
	up X decreases your aim by X units.
	forward X does two things:
		It increases your horizontal position by X units.
		It increases your depth by your aim multiplied by X.

Again note that since you're on a submarine, down and up do the 
opposite of what you might expect: "down" means aiming in the 
positive direction.

Using this new interpretation of the commands, calculate the 
horizontal position and depth you would have after following the 
planned course. What do you get if you multiply your final 
horizontal position by your final depth?
"""
import pandas as pd

# Read in the data
directions = pd.read_csv(
	'directions.txt',
	sep=' ',
	names=['command', 'amount'])

# Set quantities as negative for up
directions.loc[directions.command=='up', 'amount'] *= -1

# Compute aim
directions['aim'] = directions.amount.mask(
	directions.command=='forward', 0
    ).cumsum(skipna=True)

# Compute horizontal and depth increments
directions['horizontal'] = directions.amount.where(
	directions.command=='forward', 0)
directions['depth'] = directions.horizontal * directions.aim

# Sum and then multiply the result
print(directions[['horizontal', 'depth']].sum().product())