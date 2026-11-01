#!/usr/bin/env python3
"""High-precision check of the two-bit AND endpoint formulas.

This is a validation aid.  The all-p asymptotic is proved symbolically in REPORT.md.
"""

from decimal import Decimal, getcontext

getcontext().prec = 100
D0 = Decimal(0)
D1 = Decimal(1)
D2 = Decimal(2)
LN2 = D2.ln()


def h2(x):
    x = Decimal(x)
    if x == 0 or x == 1:
        return D0
    return (-x * x.ln() - (D1 - x) * (D1 - x).ln()) / LN2


def masses(p, q):
    return (
        (1 - 2 * p * q) ** 2,
        4 * q**2 * p * (1 - p),
        4 * p**2 * q * (1 - q),
        4 * p * (1 - p) * q * (1 - q),
    )


def entropy(probs):
    return sum((-x * x.ln() / LN2 for x in probs if x), D0)


def ledger(p, q):
    r = masses(p, q)
    t = r[2] + r[3]
    s = 4 * q * (1 - q)
    M = entropy(r) - h2(t)
    J = h2(t) - p * h2(s)
    u = r[1] / (1 - t)
    M_conditional = (1 - t) * h2(u) + t * h2(p)
    return r, M, J, J - M, M_conditional


def nstr(x, n):
    return format(x, f".{n}g")


q = D1 / 4
kappa = -D1 + D1 / (2 * LN2)
print("q = 1/4")
print("predicted D(p) = (1/2) p log2(1/p) + kappa p + O(p^2 log(1/p))")
print("kappa =", nstr(kappa, 40))
print("k p mass_sum_error M_chain_error D/(p log2(1/p)) normalized_remainder")
for k in (3, 6, 9, 12, 18, 24, 36, 48):
    p = D2 ** (-k)
    r, M, J, D, Mc = ledger(p, q)
    logp = (D1 / p).ln() / LN2
    lead = Decimal("0.5") * p * logp
    rem = (D - lead - kappa * p) / (p**2 * logp)
    print(
        k,
        nstr(p, 8),
        nstr(sum(r) - 1, 5),
        nstr(M - Mc, 5),
        nstr(D / (p * logp), 30),
        nstr(rem, 30),
    )

p = D1 / 8
r, M, J, D, Mc = ledger(p, q)
print("\ncertificate-point cross-check p=1/8,q=1/4")
print("masses =", [nstr(x, 40) for x in r])
print("M =", nstr(M, 60))
print("J =", nstr(J, 60))
print("J-M =", nstr(D, 60))
