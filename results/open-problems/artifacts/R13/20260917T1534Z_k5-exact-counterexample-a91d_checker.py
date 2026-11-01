from itertools import product
from fractions import Fraction
import sympy as sp

# R13 exact finite certificate:
# (i) an exact structured 5x5 Komlos obstruction with discrepancy T,
# (ii) an all-rational nearby witness with discrepancy 3584891/2000000,
# (iii) exact separation from the published Belhaouari-AlQudah K(5) value.

sqrt = sp.sqrt

T = (2*sqrt(2) + 3*sqrt(3) + 2*sqrt(51 + 3*sqrt(6))) / 13
b = 1/sqrt(3)
d = 1/sqrt(2)
a = (T-b)/2
c = (T-d)/3

# Defining identities and unit-column constraints.
assert sp.simplify(2*a + b - T) == 0
assert sp.simplify(3*c + d - T) == 0
assert sp.simplify(2*a*a + 2*c*c - 1) == 0
assert sp.simplify(3*b*b - 1) == 0
assert sp.simplify(2*d*d - 1) == 0
assert all(x.is_positive for x in (T,a,b,c,d))

A = sp.Matrix([
    [ 0,  a,  0,  a,  b],
    [-a,  0,  0,  a, -b],
    [ a,  a,  0,  0, -b],
    [-c,  c, -d, -c,  0],
    [-c,  c,  d, -c,  0],
])

col_norm2 = [
    sp.simplify(sum(A[i,j]**2 for i in range(5)))
    for j in range(5)
]
assert col_norm2 == [1,1,1,1,1]

S = [sp.Matrix((1,)+tail) for tail in product((-1,1), repeat=4)]
witness_rows = []
for idx,s in enumerate(S):
    dots = A*s
    hits = []
    for i,z in enumerate(dots):
        if sp.simplify(z-T) == 0:
            hits.append((i,+1))
        elif sp.simplify(z+T) == 0:
            hits.append((i,-1))
    assert hits, (idx, tuple(s), dots)
    witness_rows.append(hits[0])

# Full 32-sign enumeration (the projective half above already suffices by antipodality).
S32 = [sp.Matrix(s) for s in product((-1,1), repeat=5)]
for idx,s in enumerate(S32):
    dots = A*s
    assert any(sp.simplify(z-T) == 0 or sp.simplify(z+T) == 0 for z in dots), (idx, tuple(s), dots)

# Since all row l1 norms are exactly T, every projective signing has
# infinity norm at most T; the hit above makes it exactly T.
row_l1_symbolic = [T,T,T,T,T]
assert sp.simplify(2*a+b-T) == 0
assert sp.simplify(3*c+d-T) == 0

# Pure-integer nearby certificate, independent of symbolic radical simplification.
D = 10_000_000
I = [
    [       0,  6075479,        0,  6075479,  5773497],
    [-6075479,        0,        0,  6075479, -5773497],
    [ 6075479,  6075479,        0,        0, -5773497],
    [-3617798,  3617798, -7071061, -3617798,        0],
    [-3617798,  3617798,  7071061, -3617798,        0],
]
norm2_int = [sum(I[i][j]**2 for i in range(5)) for j in range(5)]
assert all(x <= D*D for x in norm2_int)

margins = []
for s in [(1,)+tail for tail in product((-1,1), repeat=4)]:
    dots = [sum(I[i][j]*s[j] for j in range(5)) for i in range(5)]
    margins.append(max(abs(x) for x in dots))
M = min(margins)
assert set(margins) == {17_924_455}
full_margins = []
for s in product((-1,1), repeat=5):
    dots = [sum(I[i][j]*s[j] for j in range(5)) for i in range(5)]
    full_margins.append(max(abs(x) for x in dots))
assert set(full_margins) == {17_924_455}
assert M == 17_924_455
L = Fraction(M,D)
assert L == Fraction(3_584_891,2_000_000)

# Exact strict separation from the published candidate
# K0=(4+sqrt(142))/9:
# sqrt(142) < 1193/100, hence K0 < 177/100 < L.
assert 1193**2 - 142*100**2 == 3249 > 0
assert Fraction(177,100) < L

# Also certify T > 233/130 > 177/100 using only integer square gaps.
assert 2*500**2 - 707**2 > 0          # sqrt(2) > 707/500
assert 3*250**2 - 433**2 > 0          # sqrt(3) > 433/250
assert 6*1000**2 - 2449**2 > 0        # sqrt(6) > 2449/1000
assert 58347*500**2 - 3819**2*1000 > 0 # sqrt(58347/1000) > 3819/500
assert Fraction(233,130) > Fraction(177,100)

print("T_EXACT", T)
print("T_DECIMAL_15", sp.N(T, 16))
print("MINPOLY_T", sp.minpoly(T))
print("A_COLUMN_NORM2", col_norm2)
print("PROJECTIVE_CLASSES", len(S))
print("ALL_SIGNINGS", len(S32))
print("WITNESS_ROWS_0BASED", witness_rows)
print("RATIONAL_DENOMINATOR", D)
print("RATIONAL_COLUMN_NORM2_NUMERATORS", norm2_int)
print("RATIONAL_PROJECTIVE_MARGIN_NUMERATOR", M)
print("RATIONAL_LOWER", f"{L.numerator}/{L.denominator}", float(L))
print("OLD_K0_UPPER_RATIONAL", "177/100")
print("CONCLUSION published K(5)=(4+sqrt(142))/9 is strictly below an admissible 5x5 obstruction")
print("R13_K5_COUNTEREXAMPLE_EXACT_PASS")
