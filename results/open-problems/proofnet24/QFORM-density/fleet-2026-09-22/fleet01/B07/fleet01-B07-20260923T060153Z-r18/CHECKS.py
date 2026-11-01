import itertools
import math
import numpy as np


def H_anchor(M, q, i, j):
    m, n = M.shape
    ans = 0.0
    for R in itertools.combinations(range(m), q):
        if i not in R:
            continue
        for C in itertools.combinations(range(n), q):
            if j not in C:
                continue
            d = np.linalg.det(M[np.ix_(R, C)])
            ans += d * d
    return ans


def Tq(M, q):
    s = np.linalg.svd(M, compute_uv=False)
    return float(np.sum(s[q:] ** 2))

rng = np.random.default_rng(20260923)
ratios = []
violations = []
for m, n in [(4, 4), (5, 6), (6, 5), (7, 7)]:
    for sample in range(10):
        M = rng.integers(-4, 5, size=(m, n)).astype(float)
        for i, j in [(0, 0), (m - 1, n - 1)]:
            for q in range(1, min(4, m, n)):
                hq = H_anchor(M, q, i, j)
                hp = H_anchor(M, q + 1, i, j)
                if hq <= 1e-10:
                    continue
                lhs = Tq(M, q) * hq
                rhs = q * q * hp
                if hp > 1e-9:
                    ratios.append(lhs / rhs)
                if lhs > rhs * (1 + 1e-8) + 1e-7:
                    violations.append((m, n, sample, i, j, q, lhs, rhs))

assert not violations
assert len(ratios) == 226

theta = 1 / 16
kappa = 1 / (256 * math.sqrt(3))
eta = theta ** 2 / (2304 * math.sqrt(10))
balanced_sq = theta ** 2 / (256 * math.sqrt(10))
tube = math.sqrt(balanced_sq)
a = theta / math.sqrt(12)
partner_cap = 3 * math.e * (6 / theta ** 2) ** (1 / 6) / kappa

print('nontrivial_ratio_tests=', len(ratios))
print('max_finite_ratio=', max(ratios))
print('violations=', len(violations))
print('eta=', eta)
print('balanced_squared_tail=', balanced_sq)
print('relative_tube=', tube)
print('tube_over_a=', tube / a)
print('rank3_partner_cap=', partner_cap)
print('STATUS=QFORM_ANCHORED_VOLUME_RANKTAIL_CHECK_PASS')
