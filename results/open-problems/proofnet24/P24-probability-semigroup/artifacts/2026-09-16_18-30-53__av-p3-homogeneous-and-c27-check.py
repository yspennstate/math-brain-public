from fractions import Fraction
from math import isqrt

SCALE = 10**12


def invsqrt_upper(n: int, scale: int = SCALE) -> Fraction:
    """Minimal a/scale in this decimal lattice with (a/scale)^2 >= 1/n."""
    x = (scale * scale + n - 1) // n
    a = isqrt(x)
    if a * a < x:
        a += 1
    while a * a * n < scale * scale:
        a += 1
    while a > 0 and (a - 1) * (a - 1) * n >= scale * scale:
        a -= 1
    return Fraction(a, scale)


# Directed second-auditor check: C27-SUM-756.
max_ratio = Fraction(0)
max_k = None
for K in range(2, 64):
    qK = invsqrt_upper(K)
    S = Fraction(0)
    for r in range(1, K):
        qr = invsqrt_upper(r)
        a = qK + Fraction(4, 9) * qr
        S += (K - r) * a**3
    ratio = S / K
    assert ratio < Fraction(26, 25), (K, ratio)
    if ratio > max_ratio:
        max_ratio = ratio
        max_k = K

zeta16_upper = sum(invsqrt_upper(n) / n for n in range(1, 17))
assert zeta16_upper < Fraction(17, 8)
zeta_upper = zeta16_upper + Fraction(1, 2)
assert zeta_upper < Fraction(21, 8)

large_K_contrib = (
    Fraction(1, 16)
    + Fraction(1, 3)
    + Fraction(52, 135)
    + Fraction(56, 243)
)
assert large_K_contrib == Fraction(19663, 19440)
assert large_K_contrib < Fraction(26, 25)

final_constant = Fraction(2197, 27) + 648 * Fraction(26, 25)
assert final_constant == Fraction(509821, 675)
assert final_constant < 756

print("C27 finite-range max K:", max_k)
print("C27 finite-range max certified ratio:", max_ratio)
print("C27 finite-range max certified ratio decimal:", float(max_ratio))
print("C27 large-K contribution:", large_K_contrib)
print("C27 zeta first-16 upper:", zeta16_upper)
print("C27 zeta total upper after integral tail:", zeta_upper)
print("C27 final constant:", final_constant, float(final_constant))

# P24 fixed-candidate endpoint algebra.
# gamma_p is the post-pulse p-moment exponent p(p-3)/2.
# q=p/2 is the exponent in the Hilbert spectral Jensen calculation;
# -q*p + 2*q^2 must cancel exactly.
ps = [Fraction(2), Fraction(5, 2), Fraction(8, 3), Fraction(3), Fraction(4)]
for p in ps:
    gamma = p * (p - 3) / 2
    q = p / 2
    cancellation = -q * p + 2 * q * q
    gaussian_margin = 1 - p / 3
    assert cancellation == 0
    print(
        "P24 p=", p,
        " gamma=", gamma,
        " Jensen-cancellation=", cancellation,
        " operator-norm Gaussian margin=", gaussian_margin,
        sep=""
    )

assert Fraction(2) * (Fraction(2) - 3) / 2 < 0
assert Fraction(3) * (Fraction(3) - 3) / 2 == 0
assert Fraction(4) * (Fraction(4) - 3) / 2 > 0

print("ALL_EXACT_CHECKS_PASS")
