from fractions import Fraction
from itertools import product

# Exact test symbol:
# f(t) = 1/2 + (1/4) cos(2*pi*t) + (1/4) cos(4*pi*t).
# Hence fhat(0)=1/2 and fhat(+-1)=fhat(+-2)=1/8.
# Triangle inequality gives 0 <= f <= 1.

def det_fraction(mat):
    n = len(mat)
    if n == 0:
        return Fraction(1)
    a = [list(map(Fraction, row)) for row in mat]
    sign = 1
    prev = Fraction(1)
    for k in range(n - 1):
        if a[k][k] == 0:
            r = next((r for r in range(k + 1, n) if a[r][k] != 0), None)
            if r is None:
                return Fraction(0)
            a[k], a[r] = a[r], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) / prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = Fraction(0)
    return sign * a[n - 1][n - 1]

def exact_pattern_probabilities(n=6):
    coeff = {
        0: Fraction(1, 2),
        1: Fraction(1, 8),
        -1: Fraction(1, 8),
        2: Fraction(1, 8),
        -2: Fraction(1, 8),
    }
    K = [[coeff.get(i-j, Fraction(0)) for j in range(n)] for i in range(n)]
    cache = {}
    def det_sub(indices):
        key = tuple(sorted(indices))
        if key not in cache:
            cache[key] = det_fraction([[K[i][j] for j in key] for i in key])
        return cache[key]

    out = {}
    for bits in product((0, 1), repeat=n):
        ones = [i for i, b in enumerate(bits) if b]
        zeros = [i for i, b in enumerate(bits) if not b]
        p = Fraction(0)
        for mask in range(1 << len(zeros)):
            add = [zeros[j] for j in range(len(zeros)) if (mask >> j) & 1]
            p += (-1) ** len(add) * det_sub(ones + add)
        out[bits] = p
    assert sum(out.values()) == 1
    assert min(out.values()) >= 0
    return out

patterns = exact_pattern_probabilities()
words = list(product((0, 1), repeat=3))
index = {w: i for i, w in enumerate(words)}

# Pair law of consecutive nonoverlapping 3-bit output blocks.
P = [[Fraction(0) for _ in range(8)] for _ in range(8)]
for bits, pr in patterns.items():
    P[index[bits[:3]]][index[bits[3:]]] += pr

# Matus 1996 theorem for any 5-state two-block factor:
# [13] + sqrt([24]) + sqrt([32]) + [41] + [51] + [52] + [55]
# >= (1/4) [5]^2 [11][12][23].
#
# To certify the inequality for this test symbol for EVERY surjective coarsening
# phi:{0,1}^3 -> {1,...,5}, it is enough to drop the two nonnegative square-root
# terms and verify the remaining rational LHS is still >= RHS.

best_gap = None
best_phi = None
best_l0 = None
best_rhs = None
count = 0

for phi0 in product(range(5), repeat=8):
    if len(set(phi0)) < 5:
        continue
    Q = [[Fraction(0) for _ in range(5)] for _ in range(5)]
    for i in range(8):
        for j in range(8):
            Q[phi0[i]][phi0[j]] += P[i][j]
    marginal = [sum(Q[r]) for r in range(5)]

    # 0-based labels correspond to Matus labels 1,...,5.
    L0 = Q[0][2] + Q[3][0] + Q[4][0] + Q[4][1] + Q[4][4]
    RHS = Fraction(1, 4) * marginal[4]**2 * Q[0][0] * Q[0][1] * Q[1][2]
    gap = L0 - RHS
    if best_gap is None or gap < best_gap:
        best_gap = gap
        best_phi = phi0
        best_l0 = L0
        best_rhs = RHS
    count += 1

assert count == 126000
assert best_gap > 0

print(f"surjective coarsenings checked = {count}")
print("test symbol = 1/2 + (1/4) cos(2*pi*t) + (1/4) cos(4*pi*t)")
print(f"minimum rational lower-bound gap = {best_gap}")
print(f"minimum gap decimal > {float(best_gap):.12f}")
print(f"attaining label tuple on words 000,001,...,111 = {best_phi}")
print(f"L0 = {best_l0}")
print(f"RHS = {best_rhs}")
print("PASS: for this exact mixed degree-two symbol, every 5-state coarsening of consecutive 3-bit blocks satisfies Matus's inequality even after the two sqrt terms are dropped.")
