#!/usr/bin/env python3
# R15 / I0124 exact certificate for the N=285 no-110 structural corridor
# and for feasibility of the ordinary ternary MacWilliams weight-enumerator
# relaxation.  Integer/Fraction arithmetic only.

from fractions import Fraction
from math import comb

N = 285
QFIELD = 3
AFF_DIM = 7
CODE_DIM = 8
N_DIR = (3**AFF_DIM - 1)//2       # 1093 projective hyperplane directions
N_AFF_HYP = 3*N_DIR               # 3279 affine hyperplanes
MU = N//3                         # 95
assert 3*MU == N

# A hypothetical cap has no three collinear points, hence every triple is
# affinely independent.  Point/pair/triple hyperplane-incidence counts yield
# the centered second and third moments below.
D2 = 180690
D3 = -2502870

# All sorted parallel-slice types under the branch h <= 109 everywhere.
types = []
for a in range(N + 1):
    for b in range(a, N + 1):
        c = N-a-b
        if b <= c <= 109:
            types.append((a,b,c))
assert len(types) == 169


def q2(t):
    return sum((z-MU)**2 for z in t)


def q3(t):
    return sum((z-MU)**3 for z in t)


def s4(t):
    return sum(comb(z,4) for z in t)

# Exact supporting inequality on all 169 no-110 direction types:
#   s4 <= 9550635 + (52745/24) q2 + (353/24) q3.
# Multiplication by 24 keeps the finite check integral.
inequalities = []
inequalities_eq = []
for t in types:
    gap24 = 24*9550635 + 52745*q2(t) + 353*q3(t) - 24*s4(t)
    assert gap24 >= 0, (t, gap24)
    inequalities.append(gap24)
    if gap24 == 0:
        inequalities_eq.append(t)
assert inequalities_eq == [(67,109,109),(88,88,109),(95,95,95)]

S4_upper = (
    N_DIR*9550635
    + Fraction(52745,24)*D2
    + Fraction(353,24)*D3
)
assert S4_upper == Fraction(21598269855,2)

# Planar-four-cap / midpoint-energy identity:
#   sum_K C(h_K,4) = 40*C(N,4) + 81 Q,
# where Q = sum_{m notin C} C(r_m,2).
Q_upper_exact = (S4_upper - 40*comb(N,4))/81
assert Q_upper_exact == Fraction(22203685,54)
Q_upper_int = Q_upper_exact.numerator // Q_upper_exact.denominator
assert Q_upper_int == 411179

# Convex lower bound for pair-midpoint energy.
PAIR_TOTAL = comb(N,2)
EXTERIOR_CENTERS = 3**AFF_DIM - N
base, rem = divmod(PAIR_TOTAL, EXTERIOR_CENTERS)
assert (PAIR_TOTAL, EXTERIOR_CENTERS, base, rem) == (40470,1902,21,528)
Q_lower = ((EXTERIOR_CENTERS-rem)*comb(base,2) + rem*comb(base+1,2))
assert Q_lower == 410508
assert Q_lower <= Q_upper_int
DEFECT_MAX = Q_upper_int - Q_lower
assert DEFECT_MAX == 671

# If s_m = r_m - 21, then sum s_m = 528 and exactly
#   Q - 410508 = sum_m C(s_m,2).
# Since C(s,2) >= 0 for every integer s, the corridor gives sharp elementary
# concentration consequences.
assert comb(38,2) == 703 > DEFECT_MAX   # r_m >= 59 impossible
assert 2*comb(33,2) == 1056 > DEFECT_MAX  # at most one r_m >= 54
MIN_STANDARD_CENTERS = EXTERIOR_CENTERS - DEFECT_MAX
assert MIN_STANDARD_CENTERS == 1231     # at least this many r_m in {21,22}

# An exact *formal* parallel-slice histogram satisfying the first three
# hyperplane moment constraints, entirely in the no-110 branch.
formal_hist = {
    (67,109,109): 152,
    (87,99,99): 1,
    (91,95,99): 46,
    (92,95,98): 8,
    (93,93,99): 1,
    (93,95,97): 2,
    (93,96,96): 1,
    (94,95,96): 90,
    (95,95,95): 792,
}
assert sum(formal_hist.values()) == N_DIR
assert all(t in types for t in formal_hist)
assert sum(w*q2(t) for t,w in formal_hist.items()) == D2
assert sum(w*q3(t) for t,w in formal_hist.items()) == D3

formal_S4 = sum(w*s4(t) for t,w in formal_hist.items())
formal_Q = Fraction(formal_S4 - 40*comb(N,4),81)
assert formal_Q == 410898
assert Q_lower <= formal_Q <= Q_upper_int

# Change category: augment x in F_3^7 to (1,x).  A spanning 285-cap would
# yield a ternary [285,8,>=176] linear code containing the all-ones word.
# Every direction type contributes two scalar multiples of each of its three
# nonconstant affine-function words.  Build the corresponding formal primal
# weight enumerator from the histogram.
A = [0]*(N+1)
A[0] = 1
A[N] = 2  # two nonzero constants
for t,w in formal_hist.items():
    for h in t:
        A[N-h] += 2*w

expected_A = {
    0:1,
    176:608,
    186:98,
    187:16,
    188:4,
    189:184,
    190:5044,
    191:180,
    192:10,
    193:16,
    194:92,
    198:2,
    218:304,
    285:2,
}
assert {i:a for i,a in enumerate(A) if a} == expected_A
assert sum(A) == 3**CODE_DIM
assert min(i for i,a in enumerate(A) if a and i>0) == 176

# q=3 Krawtchouk polynomial and exact MacWilliams transform.  This verifies
# that *every* ordinary dual weight-enumerator coefficient is a nonnegative
# integer; for j>0 it is even, as required by ternary scalar pairing.
def Kraw(j,i):
    lo = max(0, j-(N-i))
    hi = min(j, i)
    return sum(
        (-1)**ell * 2**(j-ell) * comb(i,ell) * comb(N-i,j-ell)
        for ell in range(lo,hi+1)
    )

B = []
for j in range(N+1):
    numerator = sum(A[i]*Kraw(j,i) for i in range(N+1) if A[i])
    assert numerator % (3**CODE_DIM) == 0, (j,numerator)
    bj = numerator // (3**CODE_DIM)
    assert bj >= 0, (j,bj)
    if j > 0:
        assert bj % 2 == 0, (j,bj)
    B.append(bj)

assert B[0] == 1
assert B[1] == B[2] == B[3] == 0
assert B[4] == 2*formal_Q == 821796
assert B[5] == 68461894
assert B[6] == 7101562806
assert B[7] == 540318154200
assert B[8] == 38445056580988
assert all(b > 0 for b in B[4:])
assert sum(B) == 3**(N-CODE_DIM)

# In any actual cap code, each planar 4-cap support contributes the two
# nonzero scalar multiples of its unique dependency, so B4 = 2Q.  Therefore
# the midpoint corridor is equivalently the dual-weight-four corridor below.
assert 2*Q_lower == 821016
assert 2*Q_upper_int == 822358

print("PASS R15 I0124 exact N=285 no-110 structural certificate")
print(f"types={len(types)}; D2={D2}; D3={D3}")
print(f"fourth_support_equalities={inequalities_eq}")
print(f"Q_range=[{Q_lower},{Q_upper_int}]; Q_upper_exact={Q_upper_exact}; defect_max={DEFECT_MAX}")
print("midpoint_consequences: r_m<=58; at_most_one_r_m>=54; "
      f"at_least_{MIN_STANDARD_CENTERS}_centers_have_r_m_in_{{21,22}}")
print(f"formal_hist_Q={formal_Q}; formal_hist={list(formal_hist.items())}")
print(f"formal_A={[(i,a) for i,a in enumerate(A) if a]}")
print("MacWilliams: B1=B2=B3=0; "
      f"B4={B[4]}; B5={B[5]}; B6={B[6]}; B7={B[7]}; B8={B[8]}; "
      "all_Bj_nonnegative_integral_even_for_j>0=True")
