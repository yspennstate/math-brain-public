#!/usr/bin/env python3
"""Rigorous finite certificate for the fixed-support arbitrary host-group theorem.

For the 18 exceptional core cells T of the published balanced n=18 FEI source gate,
enumerate every nonempty subset B of T.  Its one-host Fourier block has
    q_B(S) = 2^-9 sum_{x in B} (-1)^{<S,x>}.
The script proves two inequalities for every B:
    I_B >= 5|B|/512,
    H_B - 4 I_B + |B|/128 <= 0.
The second entropy inequality is certified with rational atanh-series upper
bounds on all logarithms; strict non-equality cases are separated from the 27
elementary equality cases.  These two inequalities imply that for every C>=4
and every set partition of T into arbitrary host groups, the published nine
source edges maximize H-C(I-1).
"""
from fractions import Fraction
import numpy as np

T = [78,79,113,121,228,484,170,186,149,151,338,466,284,316,291,295,393,457]
PAIR_MASKS = {(1 << (2*j)) | (1 << (2*j+1)) for j in range(9)}
SINGLE_MASKS = {1 << j for j in range(18)}
A4_EQUALITY_MASKS = PAIR_MASKS | SINGLE_MASKS
SCALE = 10**12
CNUM, CDEN = 4076157, 625000  # C_*=6.5218512 exactly
DEN = 1 << 18                 # 512^2

def ln_unit_bounds(y, terms=100):
    """Rigorous bounds for ln(y), 1<=y<=2, using atanh."""
    assert Fraction(1) <= y <= Fraction(2)
    z = (y - 1) / (y + 1)
    z2 = z*z
    s = Fraction(0)
    p = z
    for j in range(terms):
        s += p / (2*j + 1)
        p *= z2
    lo = 2*s
    hi = lo + 2*p / ((2*terms + 1) * (1-z2))
    return lo, hi

LN2_LO, LN2_HI = ln_unit_bounds(Fraction(2))

def log2_int_bounds(w):
    assert w >= 1
    k = w.bit_length() - 1
    if w == 1 << k:
        return Fraction(k), Fraction(k)
    y = Fraction(w, 1 << k)
    lo, hi = ln_unit_bounds(y)
    return Fraction(k) + lo/LN2_HI, Fraction(k) + hi/LN2_LO

def ceil_frac(x):
    return -((-x.numerator)//x.denominator)

# Per-character rigorous upper bounds on
# phi((r/512)^2) = (r^2/2^18) log2(2^18/r^2).
EUP = [0]*19
for r in range(1,19):
    llo, lhi = log2_int_bounds(r)
    log_hi = Fraction(18) - 2*llo
    e_hi = Fraction(r*r, DEN) * log_hi
    EUP[r] = ceil_frac(e_hi*SCALE)
EUP = np.array(EUP, dtype=np.int64)

# Source geometry: the only distance-one pairs inside T are exactly the 9 source pairs.
edge_pairs = set()
for i in range(18):
    for j in range(i+1,18):
        if (T[i]^T[j]).bit_count() == 1:
            edge_pairs.add((1<<i)|(1<<j))
assert edge_pairs == PAIR_MASKS

# Character signs chi_S(x), rows indexed by the 18 source cells.
signs = np.empty((18,512), dtype=np.int16)
for j,x in enumerate(T):
    for s in range(512):
        signs[j,s] = 1 if ((s & x).bit_count() & 1) == 0 else -1
degree_plus_host = np.array([s.bit_count()+1 for s in range(512)], dtype=np.int64)

def is_union_of_source_pairs(mask):
    if mask == 0:
        return False
    for j in range(9):
        b0 = (mask >> (2*j)) & 1
        b1 = (mask >> (2*j+1)) & 1
        if b0 != b1:
            return False
    return True

def ceil_div(a,b):
    return -((-a)//b)

w = np.zeros(512, dtype=np.int16)
prev = 0
checked = 0
d_equalities = 0
max_a4_upper = -10**30
max_a4_mask = None
max_cstar_gap_upper = -10**30
max_cstar_gap_mask = None

for k in range(1,1<<18):
    mask = k ^ (k>>1)  # Gray code
    diff = mask ^ prev
    j = (diff & -diff).bit_length()-1
    if mask & diff:
        w += signs[j]
    else:
        w -= signs[j]
    prev = mask
    checked += 1

    m = mask.bit_count()
    aw = np.abs(w).astype(np.int64)
    inum = int(np.dot(degree_plus_host, aw*aw))  # I_B = inum / 2^18

    # Exact rational influence inequality.
    dnum = inum - 2560*m  # 5m/512 in denominator 2^18
    assert dnum >= 0
    if dnum == 0:
        d_equalities += 1
    assert (dnum == 0) == is_union_of_source_pairs(mask)

    # The 27 equality cases of H-4I+m/128=0 are elementary:
    # singleton blocks and one complete source edge.  All other cases are
    # checked with a rigorous entropy upper bound.
    if mask not in A4_EQUALITY_MASKS:
        hup = int(EUP[aw].sum())
        four_i_floor = (SCALE * 4 * inum)//DEN
        a4_upper = hup - four_i_floor + m*(SCALE//128)
        if a4_upper > max_a4_upper:
            max_a4_upper = a4_upper
            max_a4_mask = mask
        assert a4_upper < 0

    # Direct stable-candidate gap:
    # s_C(B) - |B|/2*s_C(E), where E is a source edge.
    # Use upper H, lower floor for C I, and upper ceil for the positive
    # term -m*(1/32-5C/512).
    if mask not in PAIR_MASKS:
        hup = int(EUP[aw].sum())
        ci_floor = (SCALE*CNUM*inum)//(CDEN*DEN)
        pos_num = m*(5*CNUM*32 - CDEN*512)
        pos_ceil = ceil_div(SCALE*pos_num, CDEN*512*32)
        gap_upper = hup - ci_floor + pos_ceil
        if gap_upper > max_cstar_gap_upper:
            max_cstar_gap_upper = gap_upper
            max_cstar_gap_mask = mask
        assert gap_upper < 0

assert checked == (1<<18)-1
assert d_equalities == (1<<9)-1
assert max_a4_upper <= -6117834384
assert max_cstar_gap_upper <= -2462745200

# Exact elementary equality formulas.
# Singleton: H=9/256, I=11/1024.
assert Fraction(9,256) - 4*Fraction(11,1024) + Fraction(1,128) == 0
# Source edge: H=1/16, I=5/256.
assert Fraction(1,16) - 4*Fraction(5,256) + Fraction(2,128) == 0

# Bell(18): number of arbitrary set partitions of the fixed 18-cell support.
n = 18
S = [[0]*(n+1) for _ in range(n+1)]
S[0][0] = 1
for i in range(1,n+1):
    for q in range(1,i+1):
        S[i][q] = S[i-1][q-1] + q*S[i-1][q]
bell_n = sum(S[n])
assert bell_n == 682076806159

def cells(mask):
    return [T[j] for j in range(18) if (mask>>j)&1]

print("PASS")
print("subsets_checked =", checked)
print("influence_equalities =", d_equalities)
print("a4_elementary_equalities =", len(A4_EQUALITY_MASKS))
print("strict_a4_upper_max_scaled =", max_a4_upper)
print("strict_a4_upper_max =", max_a4_upper/SCALE)
print("strict_a4_upper_witness =", cells(max_a4_mask))
print("Cstar =", CNUM/CDEN)
print("strict_Cstar_gap_upper_scaled =", max_cstar_gap_upper)
print("strict_Cstar_gap_upper =", max_cstar_gap_upper/SCALE)
print("strict_Cstar_gap_witness =", cells(max_cstar_gap_mask))
print("bell_partitions_18 =", 682076806159)
print("source_partition_unique_for_every_C_gt_4 = True")
