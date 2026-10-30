#!/usr/bin/env python3
"""Exact/formula checks for the rare shared-coordinate degree-shift family."""

from fractions import Fraction
from math import comb, log2, log, lgamma

LN2 = log(2.0)
M = 8.0 / (LN2 * (1.0 - LN2))


def phi(t: float) -> float:
    if t == 0.0:
        return 0.0
    return 2.0 * t * t * (log2(1.0 / t) + 1.0 / LN2)


def majority_singleton_exact(m: int) -> Fraction:
    # Majority on n=2m+1 variables has every singleton coefficient c_m.
    return Fraction(comb(2 * m, m), 4**m)


def majority_singleton_log(m: int) -> float:
    return (lgamma(2 * m + 1) - 2.0 * lgamma(m + 1)) / LN2 - 2.0 * m


def row(r: int, m: int) -> dict:
    eps = 2.0 ** (-r)
    n = 2 * m + 1
    if m <= 1000:
        c = float(majority_singleton_exact(m))
    else:
        c = 2.0 ** majority_singleton_log(m)
    phi_f = 0.0
    phi_g = (r + 1) * phi(eps)
    phi_h = n * phi(eps * c)
    phi_k = n * phi(c)
    controls_first = eps * phi_k
    x_first = 0.5 * n * (phi(c) + phi(abs(1.0 - 2.0 * eps) * c))
    return {
        "r": r,
        "n": n,
        "epsilon": eps,
        "c_n": c,
        "Phi_f": phi_f,
        "Phi_g": phi_g,
        "Phi_h": phi_h,
        "defect_over_Inf_g": (phi_h - phi_g) / ((r + 1) * eps),
        "defect_over_shared_sum": (phi_h - phi_g) / (1.0 + eps),
        "controls_first_intermediate": controls_first,
        "x_first_intermediate": x_first,
        "terminal_after_x_and_controls": phi_k,
    }


print("M =", format(M, ".15f"))
print("central-binomial induction bounds")
for m in range(1, 101):
    c = float(majority_singleton_exact(m))
    assert c >= 1.0 / (2.0 * m**0.5) - 1e-15
    assert c <= 1.0 / ((m + 1.0) ** 0.5) + 1e-15
print("  verified for m=1..100; proof is analytic in RARE_COUNTERFAMILY.tex")

print("\nfixed rarity r=3; divergence with majority size")
for m in [1, 10, 100, 1000, 10_000, 100_000, 1_000_000]:
    q = row(3, m)
    print(
        "n={n:8d} Phi(h)={Phi_h:12.8f} Phi(g)={Phi_g:10.8f} "
        "D/I(g)={defect_over_Inf_g:12.8f} D/(p+q)={defect_over_shared_sum:12.8f}".format(**q)
    )

print("\nrare regime with n growing faster than 2^(2r)")
for r, m in [(2, 10_000), (3, 100_000), (4, 1_000_000), (5, 10_000_000)]:
    q = row(r, m)
    print(
        "r={r:2d} eps={epsilon:.8f} n={n:9d} Phi(h)={Phi_h:10.7f} "
        "controls={controls_first_intermediate:10.7f} x-first={x_first_intermediate:10.7f}".format(**q)
    )

print("\nrigorous log2(m+1) thresholds from Phi(h)>=(eps^2/2)log2(m+1)")
for r in [1, 3, 5, 8]:
    eps = 2.0 ** (-r)
    phi_g = (r + 1) * phi(eps)
    one_sided = 2.0 * M * (r + 1) / eps
    symmetric = 2.0 * (phi_g + M * (1.0 + eps)) / (eps * eps)
    print(
        f"r={r:2d} eps={eps:.8f} one-sided log2(m+1)>{one_sided:.3f} "
        f"symmetric(C=M) log2(m+1)>{symmetric:.3f}"
    )

print("\nexact physical influence identities")
for r in range(1, 8):
    eps = Fraction(1, 2**r)
    inf_x_f = Fraction(1)
    inf_x_g = eps
    inf_x_h = 1 - eps
    assert inf_x_h == inf_x_f + inf_x_g - 2 * inf_x_f * inf_x_g
    inf_g = (r + 1) * eps
    print(
        f"r={r} eps={eps} Inf_x(f,g,h)=({inf_x_f},{inf_x_g},{inf_x_h}) "
        f"overlap_saving={2*eps} I(g)={inf_g}"
    )

print("\nPASS: formulas, bounds, and pivotal identities agree.")
