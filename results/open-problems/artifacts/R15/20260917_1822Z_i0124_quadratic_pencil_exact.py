from fractions import Fraction
from itertools import product
from math import comb, ceil, floor

N = 285
D2 = 180690
D3 = -2502870
NDIR = 1093
BASE4 = 40*comb(N,4)

def category(t):
    rs = sorted(z % 3 for z in t)
    if rs == [0,0,0]: return "A"
    if rs == [1,1,1]: return "B"
    if rs == [2,2,2]: return "C"
    if rs == [0,1,2]: return "D"
    raise AssertionError((t,rs))

types = []
for a in range(N+1):
    for b in range(a,N+1):
        c = N-a-b
        if c < b or c > 109:
            continue
        q2 = sum((z-95)**2 for z in (a,b,c))
        q3 = sum((z-95)**3 for z in (a,b,c))
        s4 = sum(comb(z,4) for z in (a,b,c))
        types.append((a,b,c,q2,q3,s4,category((a,b,c))))
assert len(types) == 169
assert {k:sum(t[-1]==k for t in types) for k in "ABCD"} == {"A":21,"B":24,"C":19,"D":105}

# Two exact pointwise lower supports for q3.  These finite inequalities
# eliminate every projective quadratic-form value distribution except one.
q3_supports = [
    (Fraction(-27,2), Fraction(75), Fraction(-588), Fraction(0), Fraction(27)),
    (Fraction(-183,13), Fraction(1020,13), Fraction(1176,13), Fraction(0), Fraction(366,13)),
]
q3_equalities = []
for co in q3_supports:
    eq = []
    for t in types:
        idx = "ABCD".index(t[-1])
        rhs = co[0]*t[3] + co[1+idx]
        slack = Fraction(t[4]) - rhs
        assert slack >= 0
        if slack == 0:
            eq.append((t[0],t[1],t[2],t[-1]))
    q3_equalities.append(eq)

# Exact projective value counts for canonical quadratic forms over F_3^n.
# A=q=0, B=q=2, C=q=1.  Over odd characteristic every quadratic form
# diagonalizes; at each rank the two discriminant representatives are enough.
def projective_q_patterns(n):
    patterns = set()
    witness = {}
    for r in range(n+1):
        reps = [0] if r == 0 else [0,1]
        for twist in reps:
            coeff = [1]*r
            if r and twist:
                coeff[-1] = 2
            counts = [0,0,0]
            for x in product(range(3), repeat=n):
                q = sum(coeff[i]*x[i]*x[i] for i in range(r)) % 3
                counts[q] += 1
            pat = ((counts[0]-1)//2, counts[2]//2, counts[1]//2)
            patterns.add(pat)
            witness.setdefault(pat, (r,twist,tuple(counts)))
    return tuple(sorted(patterns)), witness

p6,w6 = projective_q_patterns(6)
p7,w7 = projective_q_patterns(7)
assert p6 == (
    (40,162,162),(94,135,135),(112,126,126),
    (121,0,243),(121,81,162),(121,108,135),
    (121,135,108),(121,162,81),(121,243,0),
    (130,117,117),(148,108,108),(202,81,81),(364,0,0)
)
assert p7 == (
    (121,486,486),(283,405,405),(337,378,378),
    (364,0,729),(364,243,486),(364,324,405),
    (364,351,378),(364,378,351),(364,405,324),
    (364,486,243),(364,729,0),(391,351,351),
    (445,324,324),(607,243,243),(1093,0,0)
)

def support_global(co, counts):
    a,b,c,d = counts
    return co[0]*D2 + co[1]*a + co[2]*b + co[3]*c + co[4]*d

survivors = []
elimination_gaps = {}
for abc in p7:
    counts = (*abc,0)
    bounds = [support_global(co,counts) for co in q3_supports]
    best = max(bounds)
    elimination_gaps[("s0",counts)] = best - D3
    if all(Fraction(D3) >= z for z in bounds):
        survivors.append(("s0",counts))
for abc in p6:
    counts = (*abc,729)
    bounds = [support_global(co,counts) for co in q3_supports]
    best = max(bounds)
    elimination_gaps[("s1",counts)] = best - D3
    if all(Fraction(D3) >= z for z in bounds):
        survivors.append(("s1",counts))
assert survivors == [("s1",(40,162,162,729))]
assert min(g for k,g in elimination_gaps.items() if k != ("s1",(40,162,162,729))) > 0
assert w6[(40,162,162)][0] == 2
assert (3**4-1)//2 == 40

# The previous ordinary-MacWilliams formal witness is incompatible with the
# cross-direction residue invariant: D-directions must number 0 or 729.
old_hist = {
    (67,109,109):152,(87,99,99):1,(91,95,99):46,
    (92,95,98):8,(93,93,99):1,(93,95,97):2,
    (93,96,96):1,(94,95,96):90,(95,95,95):792,
}
old_cats = {k:0 for k in "ABCD"}
for t,m in old_hist.items():
    old_cats[category(t)] += m
assert old_cats == {"A":3,"B":152,"C":800,"D":138}
assert old_cats["D"] not in (0,729)

# Exact fourth-moment lower/upper supports after category counts are forced.
# Coordinates: constant,q2,q3,1_A,1_B,1_C,1_D.
lower4 = (
    Fraction(582598290,61), Fraction(12977,6), Fraction(4475,366),
    Fraction(-2457,61), Fraction(0), Fraction(-9555,61), Fraction(-20369,183)
)
upper4 = (
    Fraction(47752832,5), Fraction(131873,60), Fraction(883,60),
    Fraction(-52,5), Fraction(0), Fraction(343,5), Fraction(263,6)
)
def eval4(co,t):
    idx = "ABCD".index(t[-1])
    return co[0] + co[1]*t[3] + co[2]*t[4] + co[3+idx]

eq_lo,eq_hi = [],[]
for t in types:
    lo = eval4(lower4,t)
    hi = eval4(upper4,t)
    assert lo <= t[5] <= hi
    if lo == t[5]: eq_lo.append((t[0],t[1],t[2],t[-1]))
    if hi == t[5]: eq_hi.append((t[0],t[1],t[2],t[-1]))

forced = (40,162,162,729)
beq = (NDIR,D2,D3,*forced)
lo_total = sum(c*b for c,b in zip(lower4,beq))
hi_total = sum(c*b for c,b in zip(upper4,beq))
q_lo = (lo_total-BASE4)/81
q_hi = (hi_total-BASE4)/81
assert q_lo == Fraction(25061253,61)
assert q_hi == Fraction(36982181,90)
assert ceil(q_lo) == 410841
assert floor(q_hi) == 410913
assert 410841 > 410508 and 410913 < 411179

# Midpoint-defect consequences.
assert 410913-410508 == 405
assert 29*28//2 == 406  # so r_m-21 cannot reach 29; hence r_m <=49
assert 1902-405 == 1497 # at least this many have r_m in {21,22}

print("PASS R15 I0124 exact quadratic-pencil / midpoint certificate")
print(f"types={len(types)} categories={{A:21,B:24,C:19,D:105}}")
print(f"q3_support1_equalities={q3_equalities[0]}")
print(f"q3_support2_equalities={q3_equalities[1]}")
print(f"quadratic_patterns_dim7={p7}")
print(f"quadratic_patterns_dim6={p6}")
print(f"unique_survivor={survivors[0]}; rank={w6[(40,162,162)][0]}; radical_dim=4")
print(f"old_formal_hist_categories={old_cats} -> impossible because D must be 0 or 729")
print(f"fourth_lower_equalities={eq_lo}")
print(f"fourth_upper_equalities={eq_hi}")
print(f"Q_exact_rational_range=[{q_lo},{q_hi}]")
print(f"Q_integer_range=[{ceil(q_lo)},{floor(q_hi)}]")
print("midpoint_consequences: defect<=405; every r_m<=49; at least1497/1902 centers have r_m in {21,22}")
