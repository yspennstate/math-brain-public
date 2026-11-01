from fractions import Fraction as F
from math import isqrt
from itertools import combinations, product
from collections import Counter

# R13 exact checker: (i) why the equal-triple fully-aligned cover route cannot
# pass alpha<1/3, and (ii) an exact algebraic mixed-support six-column
# obstruction strictly above the preceding rational 1.84535465 certificate.
# All acceptance tests use integer/Fraction arithmetic.

N = 6

# ---------------------------------------------------------------------------
# Part I. Exact failure of the natural equal-triple fully-aligned cover.
# ---------------------------------------------------------------------------
classes = [x for x in range(1 << N) if (x & 1) == 0]
class_index = {x:i for i,x in enumerate(classes)}
triples = list(combinations(range(N), 3))
atoms = []
for T in triples:
    for b1,b2 in product((0,1), repeat=2):
        pat = {T[0]:0, T[1]:b1, T[2]:b2}
        mask = 0
        for x in classes:
            vals = [((x >> j) & 1) ^ pat[j] for j in T]
            if vals[0] == vals[1] == vals[2]:
                mask |= 1 << class_index[x]
        atoms.append((T,mask))

assert len(classes) == 32
assert len(atoms) == 80
assert all(mask.bit_count() == 8 for _,mask in atoms)

q4_count = 0
q4_dist = Counter()
q4_max = 0
for inds in combinations(range(80),4):
    Ts = [atoms[i][0] for i in inds]
    deg = [sum(j in T for T in Ts) for j in range(N)]
    if max(deg) > 2:
        continue
    q4_count += 1
    union = 0
    for i in inds:
        union |= atoms[i][1]
    u = union.bit_count()
    q4_dist[u] += 1
    q4_max = max(q4_max,u)

assert q4_count == 19560
assert q4_dist == Counter({19:1440,20:2400,22:11520,23:960,24:3240})
assert q4_max == 24
# If strict equal-triple rows have normalized amplitude >1/3 and every
# coordinate squared load is alpha<1/3, every coordinate can occur in at
# most two supports; hence q<=4.  q<=3 covers at most 24 classes, while the
# exact q=4 enumeration above also covers at most 24.  So this restricted
# route cannot cover all 32 projective classes.

# ---------------------------------------------------------------------------
# Part II. Exact algebraic mixed-support obstruction.
# ---------------------------------------------------------------------------
# P has a unique root r_* in [LO,HI].
LO = F(6064574866229, 10**13)
HI = F(6064574866230, 10**13)
Q_OLD = F(36907093, 20000000)              # 1.84535465
Q_NEW = F(23066933137, 12500000000)       # 1.84535465096
P_COEFF = [64,-256,288,-192,340,-192,60,-40,7]

def peval(coeff, x):
    y = F(0)
    for a in coeff:
        y = y*x + a
    return y

p_lo = peval(P_COEFF, LO)
p_hi = peval(P_COEFF, HI)
assert p_lo < 0 < p_hi

# P'(r)>0 throughout I.  For a rigorous interval lower bound, positive
# monomials are evaluated at LO and negative monomials at HI.
dp_lower = (
    512*LO**7 - 1792*HI**6 + 1728*LO**5 - 960*HI**4
    + 1360*LO**3 - 576*HI**2 + 120*LO - 40
)
assert dp_lower > 0

# On I the two squarings used to derive P are reversible.  In particular,
# 1/2<r<3/4 gives 2r-1>0 and
# (2-r)/sqrt(1+r^2)-1>0 because (2-r)^2-(1+r^2)=3-4r>0.
# The intermediate H is >1/2 since 0<2r-1<1/2.
assert LO > F(1,2)
assert HI < F(3,4)
assert 3 - 4*HI > 0

# The mixed-support sign pattern.  For every projective Boolean signing,
# exactly one row has all its nonzero coefficient signs aligned (or all
# anti-aligned).  This property is independent of coefficient magnitudes.
rows = [
    {0:-1,1:+1,3:-1,5:-1},
    {0:+1,2:+1,4:+1,5:-1},
    {2:-1,3:+1,5:-1},
    {0:+1,1:+1,3:+1,5:+1},
    {0:-1,2:-1,4:+1,5:+1},
    {0:-1,2:+1,3:+1},
]
projective = [eps for eps in product((-1,1), repeat=6) if eps[0] == 1]
row_hits = [0]*6
cover_mult = []
for eps in projective:
    hit = []
    for i,row in enumerate(rows):
        vals = [row[j]*eps[j] for j in row]
        if all(v == vals[0] for v in vals):
            hit.append(i)
            row_hits[i] += 1
    cover_mult.append(len(hit))
assert len(projective) == 32
assert cover_mult == [1]*32
assert row_hits == [4,4,8,4,4,8]

# For r=r_* define
#   g=(1+4r^2)^(-1/2), a=r g,
#   f=(2(1+r^2))^(-1/2), e=r f, d=1/sqrt(2).
# Then every column has norm exactly one.  The reversible root equation is
#   (2-r)/sqrt(1+r^2)-1 = sqrt(2)(2r-1)/sqrt(1+4r^2),
# which is exactly equivalent to 2a+d+e = 2f+g =: T_6.
# Thus each of the six rows has l1 norm T_6, and the cover check above
# implies ||A epsilon||_infty=T_6 for every Boolean epsilon.

# Certify T_6 strictly exceeds a new rational floor.  Since
# T(r)=sqrt(2/(1+r^2))+sqrt(1/(1+4r^2)) is strictly decreasing for r>0
# and r_*<HI, it suffices to bound T(HI) from below by exact rationals.
def sqrt_lower(x, digits=18):
    scale = 10**digits
    n = (x.numerator * scale * scale) // x.denominator
    y = isqrt(n)
    q = F(y, scale)
    assert q*q <= x
    assert (q + F(1,scale))**2 > x
    return q

term1_sq = F(2,1) / (1 + HI*HI)
term2_sq = F(1,1) / (1 + 4*HI*HI)
term1_lb = sqrt_lower(term1_sq)
term2_lb = sqrt_lower(term2_sq)
T_lb = term1_lb + term2_lb
assert T_lb > Q_NEW > Q_OLD
improvement = Q_NEW - Q_OLD
assert improvement == F(3,3125000000)  # 9.6e-10

print('R13_ALGEBRAIC_N6_TEMPLATE_EXACT_PASS')
print('equal_triple_q4_families =', q4_count)
print('equal_triple_q4_union_distribution =', dict(sorted(q4_dist.items())))
print('equal_triple_q4_max_union =', q4_max)
print('equal_triple_min_uncovered =', 32-q4_max)
print('P_at_LO_sign = negative')
print('P_at_HI_sign = positive')
print('Pprime_interval_lower =', float(dp_lower))
print('root_interval =', float(LO), float(HI))
print('mixed_projective_classes =', len(projective))
print('mixed_cover_multiplicity_distribution = {1: 32}')
print('mixed_row_projective_hits =', row_hits)
print('term1_lower =', float(term1_lb))
print('term2_lower =', float(term2_lb))
print('T6_rational_lower =', float(T_lb))
print('old_obstruction =', float(Q_OLD))
print('new_certified_floor =', float(Q_NEW))
print('certified_floor_improvement =', float(improvement))
