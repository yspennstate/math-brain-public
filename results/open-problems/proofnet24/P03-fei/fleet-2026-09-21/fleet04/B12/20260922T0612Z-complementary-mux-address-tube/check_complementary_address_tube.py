#!/usr/bin/env python3
"""Exact-algebra / numerical-entropy checker for the B12 complementary-MUX address tube.

The imported h96 source bounds and peer interval certificate are hypotheses of the
report; this checker independently verifies the new algebra, entropy decomposition,
and rational reserve arithmetic derived from them.
"""
from fractions import Fraction
from math import log2


def h2(x: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x)


def entropy(xs):
    return sum(-x * log2(x) for x in xs if x > 0.0)


# Exact symbolic coefficient identities on a dense rational mesh.
checked = 0
max_ent_err = 0.0
min_refund = 10.0
for qn in range(1, 65):
    q = Fraction(qn, 128)  # 0<q<=1/2
    V = 4 * q * (1 - q)
    A = (1 - 2 * q) ** 2
    d = 1 - V / 2
    assert A + V == 1
    assert d - A == V / 2
    assert d + 1 - 2 * q == 2 * (1 - q) ** 2

    # Include tau=0 and a symmetric rational mesh well inside the 2^-14 proof window.
    for tn in range(-110, 111):
        tau = Fraction(tn, 2_000_000)
        if abs(tau) > Fraction(1, 2**14):
            continue
        z = 4 * tau * tau
        masses = [
            z * A,
            (1 - z) * A,
            V * (Fraction(1, 2) - tau) ** 2,
            V * (Fraction(1, 2) + tau) ** 2,
            V * (Fraction(1, 4) - tau * tau),
            V * (Fraction(1, 4) - tau * tau),
        ]
        assert all(x >= 0 for x in masses)
        assert sum(masses) == 1

        rho = [
            (Fraction(1, 2) - tau) ** 2,
            (Fraction(1, 2) + tau) ** 2,
            Fraction(1, 4) - tau * tau,
            Fraction(1, 4) - tau * tau,
        ]
        assert sum(rho) == 1
        assert all(x >= 0 for x in rho)

        mf = [float(x) for x in masses]
        Htau = entropy(mf)
        base = [0.0, float(A), float(V / 4), float(V / 4), float(V / 4), float(V / 4)]
        H0 = entropy(base)
        rhs = float(A) * h2(float(z)) + float(V) * (entropy([float(x) for x in rho]) - 2.0)
        err = abs((Htau - H0) - rhs)
        max_ent_err = max(max_ent_err, err)
        # The report only needs H(rho)<=2, i.e. this correction is nonpositive.
        refund = 2.0 - entropy([float(x) for x in rho])
        min_refund = min(min_refund, refund)
        assert refund > -2e-14
        checked += 1

# Exact theorem arithmetic from the imported peer lower bounds.
small_gap = Fraction(29, 10) - Fraction(120, 64)
assert small_gap == Fraction(41, 40)
compact_gap = Fraction(1, 64) - Fraction(120, 2**14)
assert compact_gap == Fraction(17, 2048)

# Owner-comparable margin translations.
a = Fraction(268204856, 1_000_000_000)
compact_margin = a - Fraction(17, 256)
small_margin = a - Fraction(41, 20)
assert compact_margin == Fraction(100899303, 500_000_000)
assert small_margin < 0

print("PASS")
print("rational_states_checked", checked)
print("max_entropy_identity_error", f"{max_ent_err:.3e}")
print("min_entropy_refund_numeric", f"{min_refund:.3e}")
print("small_branch_exact_gap", f"{small_gap.numerator}/{small_gap.denominator}")
print("compact_branch_exact_gap", f"{compact_gap.numerator}/{compact_gap.denominator}")
print("compact_owner_margin_upper", f"{float(compact_margin):.9f}")
print("small_owner_margin_upper", f"{float(small_margin):.9f}")
print("scope", "new exact MUX algebra + entropy decomposition + rational theorem arithmetic; imported h96 bounds not recertified")
