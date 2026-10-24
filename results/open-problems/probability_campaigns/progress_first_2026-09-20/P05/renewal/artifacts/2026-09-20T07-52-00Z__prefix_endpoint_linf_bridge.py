#!/usr/bin/env python3
"""
P05 binary LCS renewal route: exact sanity checks for the prefix-endpoint
L_infinity stability lemma and deterministic high-precision diagnostics for the
sharpened phase-randomized renewal bridge.

The exhaustive portion is a self-check, not the proof. The proof is written in
the accompanying immutable report. The benchmark decimals are diagnostics:
the theorem itself is the symbolic inequality in the report.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product
from math import comb

getcontext().prec = 80
MAX_WORD = 4


def lcs(x, y):
    row = [0] * (len(y) + 1)
    for a in x:
        prev = 0
        for j, b in enumerate(y, 1):
            old = row[j]
            if a == b:
                row[j] = prev + 1
            elif row[j - 1] > row[j]:
                row[j] = row[j - 1]
            prev = old
    return row[-1]


# Exhaustively self-check
# |LCS(X[:m],Y[:n])-LCS(X[:m'],Y[:n'])|
# <= max(|m-m'|,|n-n'|)
# on all binary words of lengths <= MAX_WORD and all prefix endpoint pairs.
cases = 0
for lx in range(MAX_WORD + 1):
    for ly in range(MAX_WORD + 1):
        for xb in product("01", repeat=lx):
            x = "".join(xb)
            for yb in product("01", repeat=ly):
                y = "".join(yb)
                val = {}
                pts = []
                for m in range(lx + 1):
                    for n in range(ly + 1):
                        val[(m, n)] = lcs(x[:m], y[:n])
                        pts.append((m, n))
                for i, (m, n) in enumerate(pts):
                    for mp, np_ in pts[i:]:
                        lhs = abs(val[(m, n)] - val[(mp, np_)])
                        rhs = max(abs(m - mp), abs(n - np_))
                        assert lhs <= rhs
                        cases += 1

# Exact check of the negative-binomial mean absolute deviation identity
# mu_r = E|T_r-2r| = r*C(2r,r)/2^(2r-1).
for r in range(1, 33):
    finite_lower_tail = Fraction(0, 1)
    for t in range(r, 2 * r):
        finite_lower_tail += (
            (2 * r - t) * Fraction(comb(t - 1, r - 1), 2 ** t)
        )
    mu_from_tail = 2 * finite_lower_tail
    mu_closed = Fraction(r * comb(2 * r, r), 2 ** (2 * r - 1))
    assert mu_from_tail == mu_closed

# High-precision deterministic diagnostics for the bridge comparison.
PI = Decimal(
    "3.141592653589793238462643383279502884197169399375105820974944592307816406286"
)
LN2 = Decimal(2).ln()
KAPPA = Decimal(1) / PI.sqrt() + (
    Decimal(1) - Decimal(2) / PI
).sqrt() / Decimal(2)


def alexander_term(r):
    r = Decimal(r)
    L = (Decimal(2) * r).ln()
    q = Decimal(2) / (Decimal(2) * r * L).sqrt() + Decimal(1) / L
    p = (
        Decimal(1)
        + Decimal(1) / (Decimal(2) * r * L)
        + (Decimal("5.1").ln() - Decimal(1)) / L
        + L.ln() / (Decimal(2) * L)
    )
    lam = (q + (q * q + Decimal(4) * p).sqrt()) / Decimal(2)
    theta = (Decimal(2) + Decimal(4).ln() / L).sqrt()
    return (
        (Decimal(2) * lam + theta) * (L / (Decimal(2) * r)).sqrt()
        + (Decimal(2) * LN2 / r).sqrt()
    )


def exact_old_boundary(r):
    num = comb(2 * r, r)
    den = 2 ** (2 * r - 1)
    return Decimal(num) / Decimal(den)


def exact_beta(r):
    mu = Decimal(r * comb(2 * r, r)) / Decimal(2 ** (2 * r - 1))
    rr = Decimal(r)
    return (mu + (rr - mu * mu / Decimal(2)).sqrt()) / (Decimal(2) * rr)


M = 20
CAP = Decimal(2) ** Decimal(-(M - 1))
WIDTH = (
    Decimal("0.826275942762282625015106581537296632823461996193190023880806183312562944430299564491109755")
    - Decimal("0.792665992")
)

for r in (110760, 110762, 111000, 116350, 1000000):
    A = alexander_term(r)
    old = A + exact_old_boundary(r) + CAP
    beta = exact_beta(r)
    new_exact = A + beta + CAP
    new_uniform = A + KAPPA / Decimal(r).sqrt() + CAP
    print("r =", r)
    print("  old_bridge =", old)
    print("  beta_r =", beta)
    print("  new_exact_beta_bridge =", new_exact)
    print("  new_uniform_kappa_bridge =", new_uniform)
    print("  internal_width =", WIDTH)
    print("  uniform_bridge_below_width =", new_uniform < WIDTH)

print("kappa =", KAPPA)
print("exhaustive_prefix_endpoint_cases =", cases)
print("negative_binomial_mu_checks = 32")
print("PREFIX_ENDPOINT_LINF_SELF_CHECK_PASS")
