# T084, agent B: (a) extension v=6 of the unbalanced 8-element matroid (its own bases balanced) at pair (0,4) with random weights,
# (b) AG(3,2) all pairs.
import numpy as np, sys, re
exec(re.split(r"\nK4 = ", open('weighted_regular.py').read())[0])
A8 = [(13726 >> (4 * c)) & 15 for c in range(4)]; cols9 = [1, 2, 4, 8] + A8 + [6]; rk9 = ranks(cols9, 9)
test('ext v=6, pair (0,4), all weights random', rk9, 9, pair=(0, 4))
test('AG(3,2)', ranks([1, 2, 4, 8, 14, 13, 11, 7], 8), 8)
