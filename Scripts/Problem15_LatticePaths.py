"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

# the paths will look like a sequence of 'R' and 'D' letters (R for moving 1 step to right, D for down).
# there are 20 Rs and 20 Ds, for a total sequence length of 40. The Rs and Ds are indistinguishable
# so the total number of paths is 40!/(20!)^2

import math
print( math.comb(40,20) ) # 40 Choose 20 is the same as 40!/(20!)^2



