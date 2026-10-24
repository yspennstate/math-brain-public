from fractions import Fraction as F
from itertools import combinations

# Current live candidate / imported rigorous central prime reserve.
C = F(6521851214, 10**9)      # C^dagger
DELTA0 = F(49065, 10**7)      # weakened exact floor 0.0049065
EPS = F(294, 10**7)           # 2.94e-5

# Exact Boolean stress witness: bit x=1 means output -1.
NEG_MASK = 0xE72B10D4
N = 5
PIVOT = 4

def vals_from_mask(mask, n):
    return [-1 if (mask >> x) & 1 else 1 for x in range(1 << n)]

def influences(vals, n):
    ans = []
    den = 1 << (n - 1)
    for i in range(n):
        cnt = 0
        for x in range(1 << n):
            if (x >> i) & 1:
                continue
            if vals[x] != vals[x ^ (1 << i)]:
                cnt += 1
        ans.append(F(cnt, den))
    return ans

def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def response_pattern_count(vals, n, block):
    block = tuple(block)
    comp = tuple(i for i in range(n) if i not in block)
    pats = set()
    for xb in range(1 << len(block)):
        row = []
        for yc in range(1 << len(comp)):
            x = 0
            for j, i in enumerate(block):
                if (xb >> j) & 1:
                    x |= 1 << i
            for j, i in enumerate(comp):
                if (yc >> j) & 1:
                    x |= 1 << i
            row.append(vals[x])
        pats.add(tuple(row))
    return len(pats)

vals = vals_from_mask(NEG_MASK, N)
assert sum(v == -1 for v in vals) == 15

# Essential: every coordinate is genuinely used.
parent_inf = influences(vals, N)
assert all(x > 0 for x in parent_inf)

# Exact composition-primality test for disjoint Boolean substitution:
# any nontrivial proper child block of size >=2 would induce <=2 response rows.
counts = []
for r in range(2, N):
    for block in combinations(range(N), r):
        counts.append((block, response_pattern_count(vals, N, block)))
assert min(c for _, c in counts) >= 3

# Pivot restrictions (pivot is top truth-table layer bit x_4).
g0 = vals[:16]
g1 = vals[16:]
disagree = sum(a != b for a, b in zip(g0, g1))
assert disagree == 15
d = F(disagree, 16)
I0 = sum(influences(g0, 4), F(0))
I1 = sum(influences(g1, 4), F(0))
assert I0 == F(3, 2)
assert I1 == F(2, 1)
assert abs(I1 - I0) == F(1, 2)
# This exactly saturates |I1-I0| <= 8 min(d,1-d) at d=15/16.
assert abs(I1-I0) == 8 * min(d, 1-d)

# Uniform Walsh data: c_A is the no-pivot coefficient, d_A the pivot coefficient.
raw = fwht(vals)
c = [F(raw[A], 32) for A in range(16)]
e = [F(raw[A | 16], 32) for A in range(16)]
assert sum(x*x for x in e) == F(15, 16)
assert sum(x*x for x in c) == F(1, 16)
assert sum(abs(x*y) for x, y in zip(c, e)) == F(15, 64)
# Cauchy upper bound is sqrt(15)/16, so squared saturation ratio is 15/16.
ratio_sq = (sum(abs(x*y) for x, y in zip(c, e)) ** 2) / (F(15, 256))
assert ratio_sq == F(15, 16)

# Improved universal Boolean-axis envelope.
# For d=k/16 (k=1,...,15):
#   |I1-I0| <= 8 min(d,1-d),
#   two potential motions cost <=170 d eps,
#   old-support entropy linear term <=16 eps sqrt(d(1-d)).
# The coefficient is therefore
#   L_k = C*min(k,16-k)/2 + 85*k/8 + sqrt(k(16-k)).
# We certify its maximum at k=15 without floating point.
L15_UP = C/F(2) + F(1275,8) + F(3873,1000)
# sqrt(15) < 3.873 exactly.
assert 3873**2 > 15 * 1000**2
# k<=8: sqrt(k(16-k))<=8 and the crude maximum is at k=8.
L_LOW = 4*C + F(85) + F(8)
assert L_LOW < L15_UP
# 9<=k<=14: use sqrt<=8; this affine upper bound increases with k,
# and its k=14 endpoint is below the k=15 certificate.
assert F(85,8) - C/F(2) > 0
L14_CRUDE = C + F(85*14,8) + F(8)
assert L14_CRUDE < L15_UP

# Refined entropy transport also gives quadratic term <=48*d eps^2 <=45 eps^2.
# Leakage h2(zeta) <= h2(4 eps^2) < 31*(4 eps^2):
# h2(z)<=z log2(e/z), e<3, and 3 < 2^31 z.
z = 4*EPS*EPS
assert F(3) < (2**31) * z
H_LEAK_UP = 31*z
LOSS_UP = L15_UP*EPS + 45*EPS*EPS + H_LEAK_UP
MARGIN = DELTA0 - LOSS_UP
assert MARGIN > 0

# The same refined envelope no longer certifies 2.95e-5; this is an envelope
# boundary only, not a Boolean counterexample to the gate inequality.
EPS_BAD = F(295, 10**7)
z_bad = 4*EPS_BAD*EPS_BAD
assert F(3) < (2**31)*z_bad
LOSS_BAD = L15_UP*EPS_BAD + 45*EPS_BAD*EPS_BAD + 31*z_bad
MARGIN_BAD = DELTA0 - LOSS_BAD
assert MARGIN_BAD < 0

print('PASS')
print('candidate_C', float(C))
print('certified_axis_radius', float(EPS))
print('radius_factor_vs_2e-5', float(EPS / F(2,100000)))
print('linear_coefficient_upper', float(L15_UP))
print('quadratic_plus_leak_loss_upper', float(45*EPS*EPS + H_LEAK_UP))
print('total_loss_upper', float(LOSS_UP))
print('reserve_lower', float(MARGIN))
print('envelope_reserve_at_2.95e-5', float(MARGIN_BAD))
print('stress_mask', hex(NEG_MASK))
print('stress_output_negative_count', sum(v == -1 for v in vals))
print('stress_min_response_patterns_over_proper_blocks', min(c for _,c in counts))
print('stress_pivot_disagreement', f'{disagree}/16')
print('stress_child_influences', str(I0), str(I1))
print('stress_abs_child_influence_gap', str(abs(I1-I0)))
print('stress_sum_abs_c_d', str(sum(abs(x*y) for x,y in zip(c,e))))
print('stress_cauchy_ratio_squared', str(ratio_sq))
print('stress_parent_influences', ','.join(str(x) for x in parent_inf))
