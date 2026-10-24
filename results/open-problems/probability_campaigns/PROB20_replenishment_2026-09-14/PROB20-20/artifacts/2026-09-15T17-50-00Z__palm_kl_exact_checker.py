from fractions import Fraction
from itertools import product, permutations
from math import log

# Exact finite-support checker for the Palm identities in the 2026-09-15
# PROB20-20 report.  The finite example is only a bookkeeping certificate;
# it is not evidence for the asymptotic conjecture.

pi = [Fraction(2, 5), Fraction(3, 10), Fraction(1, 5), Fraction(1, 10)]
nu = sum(Fraction(k) * p for k, p in enumerate(pi))
n = 5
m = 7


def falling(a, r):
    z = 1
    for j in range(r):
        z *= a - j
    return z


states = []
p_m = Fraction(0)
for x in product(range(len(pi)), repeat=n):
    px = Fraction(1)
    for v in x:
        px *= pi[v]
    if sum(x) == m:
        states.append((x, px))
        p_m += px

b = -log(float(p_m))

# One-ball Palm measures.
Ptilde = {}
Qtilde = {}
for x in product(range(len(pi)), repeat=n):
    px = Fraction(1)
    for v in x:
        px *= pi[v]
    for i in range(n):
        if x[i]:
            Ptilde[(x, i)] = px * Fraction(x[i], 1) / (n * nu)

for x, px in states:
    qx = px / p_m
    for i in range(n):
        if x[i]:
            Qtilde[(x, i)] = qx * Fraction(x[i], m)

assert sum(Ptilde.values()) == 1
assert sum(Qtilde.values()) == 1

kl1 = 0.0
for key, q in Qtilde.items():
    p = Ptilde[key]
    kl1 += float(q) * log(float(q / p))
formula1 = b + log(float(n * nu / Fraction(m)))
assert abs(kl1 - formula1) < 1e-12

# Boundary size-biased law.
pistar = [Fraction(0)] * len(pi)
for k in range(1, len(pi)):
    pistar[k] = Fraction(k) * pi[k] / nu
assert sum(pistar) == 1


def conv_prob_A(r):
    total = Fraction(0)
    for ordinary in product(range(len(pi)), repeat=n - r):
        po = Fraction(1)
        for v in ordinary:
            po *= pi[v]
        for stars in product(range(1, len(pi)), repeat=r):
            ps = Fraction(1)
            for v in stars:
                ps *= pistar[v]
            if sum(ordinary) + sum(stars) == m:
                total += po * ps
    return total


def D_r_direct(r):
    ans = Fraction(0)
    for x, px in states:
        qx = px / p_m
        numerator = 0
        for inds in permutations(range(n), r):
            term = 1
            for i in inds:
                term *= x[i]
            numerator += term
        ans += qx * Fraction(numerator, falling(m, r))
    return ans


print("finite model: n=", n, "m=", m, "nu=", float(nu))
print("P(S_n=m)=", float(p_m), "b=", b)
print("one-ball Palm KL direct=", kl1)
print("one-ball Palm KL formula=", formula1)

for r in (1, 2, 3):
    D = D_r_direct(r)
    A = conv_prob_A(r)
    rhs = Fraction(falling(n, r), falling(m, r)) * (nu ** r) * A / p_m
    assert D == rhs
    kl_formula = (
        b
        + log(float(Fraction(falling(n, r), falling(m, r)) * (nu ** r)))
        - log(float(D))
    )
    assert abs(kl_formula + log(float(A))) < 1e-12
    print("r=", r)
    print("  D_r direct=", float(D))
    print("  D_r size-biased identity=", float(rhs))
    print("  A_{n,r}=", float(A))
    print("  Palm KL formula=", kl_formula)
    print("  -log A_{n,r}=", -log(float(A)))

print("ALL EXACT PALM / SIZE-BIASED CHECKS PASSED")
