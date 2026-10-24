from fractions import Fraction as F

# P19 independent exact audit of P20-D0010-THREE-PIECE-IFF-01.
# All checks are rational. The external sufficiency theorem (Wang-Wang 2011)
# is not re-proved here; the report separately checks its hypotheses.

lo = F(1,4)
mid = F(1,3)
hi = F(2,5)

def h1(c): return 15*c - 3
def h2(c): return 9 - 21*c
def h3(c): return F(3,2)*c

# Affine functions a*c+b.
H1 = (F(15), F(-3))
H2 = (F(-21), F(9))
H3 = (F(3,2), F(0))

def add(x,y): return (x[0]+y[0], x[1]+y[1])
def mul(r,x): return (r*x[0], r*x[1])

norm = add(add(mul(F(1,6),H1), mul(F(1,6),H2)), mul(F(2,3),H3))
mean = add(add(mul(F(1,72),H1), mul(F(1,24),H2)), mul(F(4,9),H3))
tail = mul(F(2,3),H3)

assert norm == (F(0), F(1))
assert mean == (F(0), F(1,3))
assert tail == (F(1), F(0))  # P(X>1/3)=c.

# Strict positivity on the full parameter interval follows from affine endpoint minima.
assert h1(lo) == F(3,4) > 0
assert h2(hi) == F(3,5) > 0
assert h3(lo) == F(3,8) > 0

# Unimodality inequalities; affine differences attain minima at endpoints.
assert h2(lo) - h1(lo) > 0
assert h2(mid) - h1(mid) == 0
assert h2(hi) - h3(hi) == 0
assert h2(mid) - h3(mid) > 0
assert h1(hi) - h2(hi) > 0

# The count obstruction is 1 <= E[N] = 3c, with sharp threshold c=1/3.
assert 3*lo < 1
assert 3*mid == 1
assert 3*hi > 1

print("normalization_affine =", norm)
print("mean_affine =", mean)
print("tail_mass_affine =", tail)
print("positive_endpoint_minima =", h1(lo), h2(hi), h3(lo))
print("threshold =", mid)
print("P19-AUDIT-P20-D0010-THREEPIECE-IFF-21 PASS")
