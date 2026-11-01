from fractions import Fraction
from math import factorial
from itertools import product

pi = [Fraction(2,5), Fraction(1,4), Fraction(1,5), Fraction(1,10), Fraction(1,20)]
assert sum(pi) == 1
nu = sum(Fraction(k) * pi[k] for k in range(len(pi)))


def falling(x, r):
    out = 1
    for j in range(r):
        out *= x - j
    return out


def elementary_symmetric(z, h):
    dp = [Fraction(0)] * (h + 1)
    dp[0] = 1
    for x in z:
        for j in range(h, 0, -1):
            dp[j] += dp[j - 1] * x
    return dp[h]


def convolve_laws(laws, target):
    dp = [Fraction(0)] * (target + 1)
    dp[0] = 1
    for law in laws:
        nd = [Fraction(0)] * (target + 1)
        for s, ps in enumerate(dp):
            if not ps:
                continue
            for k, pk in enumerate(law):
                if s + k <= target:
                    nd[s + k] += ps * pk
        dp = nd
    return dp[target]


# Lemma 4.1: exact fixed-configuration Maclaurin bound.
z = [5, 7, 9, 11]
T = sum(z)
N = len(z)
for h in range(1, N + 1):
    exact = Fraction(factorial(h)) * elementary_symmetric(z, h) / Fraction(falling(T, h))
    bound = Fraction(falling(N, h), N ** h) * Fraction(T ** h, falling(T, h))
    assert exact <= bound
    print("TAIL", h, float(exact), float(bound), exact <= bound)


# Lemma 7.1: exact all-orders size-biased convolution identity.
n = 6
m = 11
pn = convolve_laws([pi] * n, m)
assert pn > 0

pi_star = [Fraction(0)] * len(pi)
for k in range(1, len(pi)):
    pi_star[k] = Fraction(k) * pi[k] / nu
assert sum(pi_star) == 1

allocs = []
for y in product(range(len(pi)), repeat=n):
    if sum(y) != m:
        continue
    w = Fraction(1)
    for v in y:
        w *= pi[v]
    allocs.append((y, w))
assert sum(w for _, w in allocs) == pn

for r in (1, 2, 3):
    direct_num = Fraction(0)
    for y, w in allocs:
        distinct_mass = Fraction(0)
        for inds in product(range(n), repeat=r):
            if len(set(inds)) != r:
                continue
            prod_occ = 1
            for i in inds:
                prod_occ *= y[i]
            distinct_mass += prod_occ
        direct_num += w * distinct_mass / Fraction(falling(m, r))
    D = direct_num / pn

    conv = convolve_laws([pi] * (n - r) + [pi_star] * r, m)
    rhs = Fraction(falling(n, r)) * nu ** r / Fraction(falling(m, r)) * conv / pn
    assert D == rhs
    print("IDENTITY", r, float(D), D == rhs)

print("ALL EXACT CHECKS PASSED")
