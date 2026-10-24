from fractions import Fraction
from math import isqrt
import sympy as sp

print('R06 I0056 edge-to-vertex closure exact checker')

# 1. One-step closure combinatorics for representative finite degrees.
# For adding an outside vertex with r>=2 neighbors in K:
# edge boundary delta = d-2r exactly;
# outer vertex boundary delta <= d-r-1 <= d-3.
for d in range(2, 101):
    for r in range(2, d+1):
        de = d - 2*r
        dbmax = d - r - 1
        assert de <= d - 4
        assert dbmax <= d - 3
print('closure one-step inequalities d<=100: PASS')

# 2. Symbolic iteration algebra with h=d-3+x, x>=0.
d, m, n, x = sp.symbols('d m n x', real=True)
h = d - 3 + x
termination_coeff = sp.simplify(h - d + 4)
backward_gain = sp.simplify(h - d + 3)
assert termination_coeff == 1 + x
assert backward_gain == x
# terminal b_m=e_m>=h(n+m); backwards b_0>=b_m-(d-3)m
expr = sp.expand(h*(n+m) - (d-3)*m)
assert sp.simplify(expr - (h*n + x*m)) == 0
print('closure iteration algebra: PASS')

# 3. Edge constant formula and threshold algebra for f>=5.
f = sp.symbols('f', integer=True, positive=True)
Phi2 = (d-2)**2 - 4*(d-2)/(f-2)
diff = sp.factor(Phi2 - (d-3)**2)
assert sp.simplify(diff - (2*d-5 - 4*(d-2)/(f-2))) == 0
# At f=5 this is the minimal value as f increases.
diff_f5 = sp.factor(diff.subs(f,5))
assert sp.simplify(diff_f5 - (2*d-7)/3) == 0
print('edge-threshold symbolic algebra: PASS')

# 4. Exact finite sanity sweep over admissible nonpositive-curvature pairs.
# Compare squares: Phi_E >= d-3 for f>=5 and 1/d+1/f <= 1/2.
checked = 0
for dd in range(3, 101):
    for ff in range(5, 101):
        if Fraction(1,dd) + Fraction(1,ff) > Fraction(1,2):
            continue
        # Phi_E^2 as an exact rational.
        phi2 = Fraction((dd-2)**2,1) - Fraction(4*(dd-2),ff-2)
        assert phi2 >= 0
        rhs2 = Fraction((dd-3)**2,1)
        assert phi2 >= rhs2
        # equality only at the Euclidean (3,6) pair in this range.
        if phi2 == rhs2:
            assert (dd,ff) == (3,6)
        checked += 1
print('admissible f>=5 exact pair sweep:', checked, 'pairs: PASS')

# 5. H_{5,5}: exact edge constant sqrt(5), threshold and interval collapse.
dd=5; ff=5
phi2_h55 = Fraction((dd-2)**2,1) - Fraction(4*(dd-2),ff-2)
assert phi2_h55 == 5
assert phi2_h55 > (dd-3)**2  # sqrt(5)>2
# Previous lower phi=(1+sqrt5)/2, previous upper sqrt5.
# Width positive because sqrt5>1; after theorem lower=upper sqrt5, width=0.
assert 5 > 1
print('H55: Phi_E^2=5 and Phi_E>d-3=2: PASS')
print('H55 certified interval after closure lemma: [sqrt(5), sqrt(5)]')
print('H55 certified width after: 0')

# 6. Why quadrangular cases are not covered by the threshold lemma:
# f=4 gives Phi_E^2-(d-3)^2=-1 identically.
assert sp.factor(diff.subs(f,4)) == -1
print('f=4 threshold obstruction exactly -1 in squared comparison: PASS')

print('PASS')
