#!/usr/bin/env python3
"""
P05 deterministic checker for the phase-randomized renewal/Alexander bridge.

No Monte Carlo. The exact portion checks the negative-binomial mean-absolute-
deviation telescoping identity for r=1,...,40 using fractions. Floating-point
work is diagnostic only: it evaluates the explicit analytic bridge, scans the
inherited interval-width crossing at M=20, and specializes the recovered
Lember-Sova entropy inequality to the iid fair binary case.
"""

from fractions import Fraction
from math import comb, exp, lgamma, log, log2, sqrt

INTERNAL_LOWER = 0.792665992
INTERNAL_UPPER = 0.826275942762282625
WIDTH = INTERNAL_UPPER - INTERNAL_LOWER


def nb_mad_direct(r: int) -> Fraction:
    """E|T_r-2r|, T_r~NegBin(r,1/2), via the lower tail exactly."""
    s = Fraction(0, 1)
    for t in range(r, 2*r):
        p = Fraction(comb(t-1, r-1), 2**t)
        s += (2*r-t) * p
    return 2*s


def nb_mad_formula(r: int) -> Fraction:
    return Fraction(r * comb(2*r, r), 2**(2*r-1))


def alexander_parameters(r: int):
    L = log(2*r)
    q = 2/sqrt(2*r*L) + 1/L
    p = 1 + 1/(2*r*L) + (log(5.1)-1)/L + log(L)/(2*L)
    lam = (q + sqrt(q*q + 4*p))/2
    theta = sqrt(2 + log(4)/L)
    actual_rhs = (
        1 + 1/(2*r*L) + 2*lam/sqrt(2*r*L)
        + log(5.1*lam)/L + log(L)/(2*L)
    )
    return lam, theta, actual_rhs


def central_ratio(r: int) -> float:
    # binom(2r,r)/2^(2r-1), stably via log-gamma
    return 2*exp(lgamma(2*r+1) - 2*lgamma(r+1) - 2*r*log(2))


def bridge_delta(r: int, M: int) -> float:
    L = log(2*r)
    lam, theta, actual_rhs = alexander_parameters(r)
    assert lam*lam > actual_rhs
    return (
        (2*lam+theta)*sqrt(L/(2*r))
        + sqrt(2*log(2)/r)
        + central_ratio(r)
        + 2**(-(M-1))
    )


def h2(x: float) -> float:
    return -x*log2(x) - (1-x)*log2(1-x)


def entropy_root() -> float:
    lo, hi = 0.5, 0.999999
    for _ in range(200):
        mid = (lo+hi)/2
        if 2*h2(mid)+mid-2 > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


for r in range(1, 41):
    assert nb_mad_direct(r) == nb_mad_formula(r)

print("EXACT_NB_MAD_IDENTITY_PASS r=1..40")
print("identity: E|T_r-2r| = r*C(2r,r)/2^(2r-1)")
print(f"inherited_internal_width={WIDTH:.17f}")

M = 20
for r in (50_000, 100_000, 110_000, 115_000, 116_000, 116_100,
          116_200, 116_348, 116_350, 120_000, 193_072, 1_000_000):
    lam, theta, rhs = alexander_parameters(r)
    d = bridge_delta(r, M)
    print(
        f"r={r} M={M} lambda={lam:.15f} theta={theta:.15f} "
        f"delta={d:.15f}"
    )

first = None
for r in range(8, 116_352, 2):
    if bridge_delta(r, M) < WIDTH:
        first = r
        break
assert first == 116_350
print(f"first_even_scan_delta_below_inherited_width_M20={first}")
print(f"delta_r_minus_2={bridge_delta(first-2,M):.15f}")
print(f"delta_r={bridge_delta(first,M):.15f}")

root = entropy_root()
print(f"fair_binary_entropy_upper_root={root:.15f}")
print(f"entropy_lhs_at_Lueker_0.826280={2*h2(0.826280)+0.826280:.15f}")
assert root > 0.826280

print("PHASE_RANDOMIZED_RENEWAL_BRIDGE_CHECK_PASS")
