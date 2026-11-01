#!/usr/bin/env python3
"""Exact self-check for NM13-07 P0282 typical-shape linear window.

This is a SELF-CHECK, not an independent audit.  It verifies the finite tail
base cases and all cleared-denominator polynomial identities used in the
written proof of the 221 n >= 576 j sufficient region.
"""
from fractions import Fraction
from math import comb, factorial


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def padd(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pscale(a, c):
    return [c * x for x in a]


def pshift(a, k):
    return [0] * k + list(a)


def peval(a, x):
    y = 0
    for c in reversed(a):
        y = y * x + c
    return y


print("P0282 typical-shape Kerov linear-window exact self-check")
print("claim_condition=221*n>=576*j ; equivalent k/n>=355/576")

# -------------------------------------------------------------------------
# 1. RSK/Plancherel tail: r_s = ceil(9s/25), p_s = C(s,r_s)/r_s!.
#    Check the 25 exact base cases for p_s <= 1/[14000(s+1)].
# -------------------------------------------------------------------------
base = []
for s in range(66, 91):
    r = (9 * s + 24) // 25
    p = Fraction(comb(s, r), factorial(r))
    rhs = Fraction(1, 14000 * (s + 1))
    assert p < rhs, (s, r, p, rhs)
    base.append((s, r, p))
print("tail_base_cases=25 s=66..90 PASS")
mx = max(base, key=lambda z: z[2] * (z[0] + 1))
print("tail_base_max_at_s=%d r=%d scaled_p_times_splus1=%s" %
      (mx[0], mx[1], str(mx[2] * (mx[0] + 1))))

# If r=ceil(9s/25), then r_{s+25}=r+9.  The exact factorial ratio is bounded by
#   25^34 (s+25)^25 / (9^18 16^16 s^34).
# Its log derivative is 25/(s+25)-34/s < 0, so it suffices to check s=66.
s = 66
ratio_bound = Fraction((25 ** 34) * ((s + 25) ** 25),
                       (9 ** 18) * (16 ** 16) * (s ** 34))
assert 25 * ratio_bound < 1
print("tail_25step_ratio_upper_at_s66=%s < 1/25 PASS" % str(ratio_bound))
# The induction target also propagates because (s+26) < 25(s+1) for s>=0.
assert 66 + 26 < 25 * (66 + 1)
print("tail_residue_class_induction_algebra=PASS")

# -------------------------------------------------------------------------
# 2. Tilt normalization at K0=(355/221)j+1, s=j-1.
#    rho0=(K-s+1)/(K+1)=(134j+663)/(355j+442)>134/355,
#    hence rho0^{-2} < (355/134)^2 < 8.
# -------------------------------------------------------------------------
assert 355 * 663 - 134 * 442 == 176137 > 0
assert Fraction(355, 134) ** 2 < 8
print("tilt_normalization_rho0_gt_134_over_355_and_inverse_square_lt_8=PASS")

# -------------------------------------------------------------------------
# 3. Exact good-shape deterministic factor at the threshold.
#    With a=9/25, lambda=355/221, K=lambda*j+1, s=j-1,
#      y = 1 + s/[K(K-a s)]
#      B = (j+1)/j * ((K-y)/((K-1)y))^2.
#    Direct exact simplification gives
#      B=(j+1) P(j)^2 / [5041 j^3 Q(j)^2].
#    Verify symbolically with integer polynomial arithmetic that
#      B - (1+1/(1000j)) = H(j)/[5041000 j^3 Q(j)^2]
#    with every coefficient of H positive.
# -------------------------------------------------------------------------
# low-to-high coefficients
P = [53969305, 63932869, 297438596, 173561630]
Q = [439569, 5410301, 2444530]
P2 = pmul(P, P)
Q2 = pmul(Q, Q)
N = pmul([1, 1], P2)                  # (j+1) P^2
D = pscale(pshift(Q2, 3), 5041)       # 5041 j^3 Q^2
# numerator over common denominator 1000*j*D
cross = padd(pscale(pshift(N, 1), 1000),
             pscale(padd(pscale(pshift(D, 1), 1000), D), -1))
assert cross[0] == 0
H = cross[1:]                           # cancel one factor j
H_expected = [
    2912685882183025000,
    9813510895355115000,
    43092371337748869799,
    91960723425527755942,
    143293102107220385619,
    55386399948596945540,
    437092402143100,
]
assert H == H_expected, (H, H_expected)
assert all(c > 0 for c in H)
print("good_factor_exact_polynomial_identity=PASS")
print("good_factor_H_coefficients_low_to_high=" + ",".join(map(str, H)))
print("good_factor_conclusion=B(j,K0)>1+1/(1000j) for all j>=1")

# Independent exact spot checks of the rational formula obtained directly from
# a=9/25 and lambda=355/221 against the compact P/Q expression.
for jj in [1, 2, 3, 10, 67, 100, 1000]:
    K = Fraction(355 * jj, 221) + 1
    ss = jj - 1
    y = 1 + Fraction(ss, 1) / (K * (K - Fraction(9 * ss, 25)))
    B_direct = Fraction(jj + 1, jj) * ((K - y) / ((K - 1) * y)) ** 2
    B_pq = Fraction((jj + 1) * peval(P, jj) ** 2,
                    5041 * jj ** 3 * peval(Q, jj) ** 2)
    assert B_direct == B_pq
    assert B_direct > 1 + Fraction(1, 1000 * jj)
print("good_factor_direct_rational_spotchecks=7 PASS")

# -------------------------------------------------------------------------
# 4. Final multiplication.  From the tail and tilt bounds,
#    nu_bad < 8/[14000j] = 1/[1750j].
# -------------------------------------------------------------------------
for jj in [1, 2, 67, 100, 10000]:
    final_lb = (1 + Fraction(1, 1000 * jj)) * (1 - Fraction(1, 1750 * jj))
    assert final_lb > 1
# Symbolically the numerator of final_lb-1 is 750*j-1.
assert 750 * 1 - 1 > 0
print("final_product=(1+1/(1000j))*(1-1/(1750j))>1 for j>=1 PASS")

print("theorem_selfcheck_scope=j>=67_and_221n>=576j_plus_retained_j<=66")
print("ALL_EXACT_CHECKS_PASS")
