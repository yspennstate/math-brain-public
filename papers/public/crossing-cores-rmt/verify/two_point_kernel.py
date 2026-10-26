import os
"""The missing ingredient for gluing is a two-point kernel: the section
volume with BOTH the base point x and an interior state u held fixed.
For the square abab the walk visits x, u_1, u_2, u_2-u_1+x, so holding
x and u = u_1 fixed and integrating u_2 gives

    K(x,u) = length{u_2 : u_2 in [0,1], u_2-u+x in [0,1]} = (1-|u-x|)_+ .

Check: integrating out u must return the square's profile."""
from fractions import Fraction as Fr
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import tk_core
from exact_volume import volume_from_halfspaces

def K(x, u):
    d = abs(Fr(u) - Fr(x))
    return max(Fr(0), 1 - d)

# integral of K(x,u) du over [0,1], exactly, as a function of x
def prof_from_K(x):
    x = Fr(x)
    # int_0^1 (1-|u-x|) du = 1 - x^2/2 - (1-x)^2/2
    return 1 - x*x/2 - (1-x)*(1-x)/2

def section_square(x):
    pm = (2,3,0,1)   # abab
    rows = tk_core.dedupe_rows(tk_core.toeplitz_forms(pm))
    hs = []
    for r in rows:
        c = tuple(r[1:])
        hs.append((c, Fr(x)))
        hs.append((tuple(-v for v in c), 1 - Fr(x)))
    return volume_from_halfspaces(hs, [(-1,1)]*2)

print("x      int K(x,u) du     engine f_abab(x)")
for x in (Fr(0), Fr(1,4), Fr(1,3), Fr(1,2), Fr(3,4), Fr(1)):
    a, b = prof_from_K(x), section_square(x)
    print(f"{str(x):<6} {str(a):<16} {str(b):<12} {'OK' if a == b else 'MISMATCH'}")
print()
print("volume of the square from the kernel: int int K =", 
      sum(prof_from_K(Fr(i,6))*w for i, w in
          zip(range(7), [Fr(41,840),Fr(216,840),Fr(27,840),Fr(272,840),Fr(27,840),Fr(216,840),Fr(41,840)])),
      " (exact p_T(abab) = 2/3)")
