# T084, agent B: adversarial weights (as adversarial_weights.py) on binary matroids outside the sixth-root-of-unity class:
# F7, F7*, AG(3,2) (all transitive on pairs up to symmetry, so a few pairs suffice), and AG(3,2)'s relaxation S8 as control.
import numpy as np, re, sys
src = open('adversarial_weights.py').read(); exec(src.split("\nK5 = ")[0])
F7 = [1, 2, 4, 3, 5, 6, 7]; rkF = ranks(F7, 7)
search('F7', rkF, 7, starts=20, pairs=[(0, 1), (0, 3)])
search('F7*', dual_rank(rkF, 7), 7, starts=20, pairs=[(0, 1), (0, 3)])
search('AG(3,2)', ranks([1, 2, 4, 8, 14, 13, 11, 7], 8), 8, starts=12)
