"""The free conditional-positivity tests for gamma_T once m_28 is known.

With m_28 = 1141293103886559392/225225 (lattice_counts_reduced.py, k = 14)
the order-28 test of order28_threshold.py is decided: the even block
indexed by {2,4,...,14} has positive Schur slack.  The next test enlarges
the odd block indexed by {1,3,...,13} by index 15, whose new diagonal
entry is r_30; this script prints the order-28 slack and the exact
threshold that test puts on m_30.

Run:  python -u order30_threshold.py
"""
from fractions import Fraction as Fr
from order24_threshold import free_cumulants, solve, det, mT as mT22

mT = dict(mT22)
mT[24] = Fr(1112571762134554, 75075)
mT[26] = Fr(2032842751996209, 7700)
mT[28] = Fr(1141293103886559392, 225225)
TOP = 30

r0 = free_cumulants(mT, TOP, m_top_zero=True)
C = r0[TOP]
r = dict(r0)
print(f"r_30 = m_30 - {-C}")

blocks = (("odd", [1, 3, 5, 7, 9, 11, 13, 15]), ("even", [2, 4, 6, 8, 10, 12, 14]))
for name, idx in blocks:
    core, last = idx[:-1], idx[-1]
    A = [[r[i + j] for j in core] for i in core]
    v = [r[i + last] for i in core]
    x = solve([row[:] for row in A], v[:])
    q = sum(a * b for a, b in zip(v, x))
    print(f"\n{name} block indexed by {idx}: leading determinant positive: {det(A) > 0}")
    if 2 * last < TOP:
        slack = r[2 * last] - q
        print(f"   Schur slack at r_{2*last} = {slack}")
        print(f"   = {float(slack):.6g}  {'PASSES' if slack >= 0 else 'FAILS'}")
        print(f"   relative to r_{2*last}: {float(slack / r[2*last]):.3e}")
    else:
        thresh = q - C
        print(f"   condition r_30 >= v^T A^-1 v becomes m_30 >= {thresh}")
        print(f"   = {float(thresh):.10e}")
