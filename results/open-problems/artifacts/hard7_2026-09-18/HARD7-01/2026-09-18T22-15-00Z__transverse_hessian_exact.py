#!/usr/bin/env python3
from fractions import Fraction as F

# Uniform centered boxes with half-widths:
# K=(3/4,1,1), L=(1/5,1/4,1/4), M=(K+L)/2=(19/40,5/8,5/8).
# W=x1*x2+x2*x3+x3*x1.
pK, pL, pM = F(3,4), F(1,80), F(95,512)
SK, SL, SM = F(17,72), F(19,19200), F(449,12288)

# Certified rational enclosures for cube roots.
loK, hiK = F(908560296416069829,10**18), F(90856029641606983,10**17)
loL, hiL = F(7252482552519967,31250000000000000), F(46415888336127789,200000000000000000)
loM, hiM = F(14259070735584271,25000000000000000), F(570362829423370841,10**18)

data = [
    ("K", pK, loK, hiK),
    ("L", pL, loL, hiL),
    ("M", pM, loM, hiM),
]
for name,p,lo,hi in data:
    assert lo**3 < p < hi**3, (name, p, lo**3, hi**3)

# DBM margin at epsilon=0 (common volume factor 8^(1/3) omitted).
g_lower = loM - (hiK + hiL)/2
g_upper = hiM - (loK + loL)/2
assert g_lower > 0

# Transverse second-variation numerator
# q = pM^(1/3) SM - (pK^(1/3) SK + pL^(1/3) SL)/2.
# Upper bound uses positive coefficient on M and negative coefficients on K,L.
q_upper = SM*hiM - (SK*loK + SL*loL)/2
q_lower = SM*loM - (SK*hiK + SL*hiL)/2
assert q_upper < 0

print("pK =", pK, "SK =", SK)
print("pL =", pL, "SL =", SL)
print("pM =", pM, "SM =", SM)
for name,p,lo,hi in data:
    print(f"cuberoot_{name}_bracket =", lo, hi)
print("g_bracket =", g_lower, g_upper)
print("q_bracket =", q_lower, q_upper)
print("half_D2_upper = q_upper/3 =", q_upper/F(3))
print("ALL_EXACT_CHECKS_PASS")
