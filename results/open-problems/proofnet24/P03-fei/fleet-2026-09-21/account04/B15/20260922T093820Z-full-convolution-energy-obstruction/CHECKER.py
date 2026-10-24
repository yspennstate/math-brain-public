"""Independent standard-library check for account04/B15 full-convolution-energy theorem.

This is a falsification/self-consistency checker, not the proof.  It reconstructs the
sign-aligned product I-projection amplitudes, directly sums every nonzero XOR-shift
autocorrelation for small m, and compares with the exact closed formula.  It also
prints the normalized KL and entropy quantities from the genuine one-point-defect
Boolean suspension family.
"""
from fractions import Fraction
from math import log2, sqrt


def exact_energy(m: int) -> Fraction:
    p = Fraction(1, 2 ** (m - 1))
    return (
        -16 * (1 - p) ** (2 * m)
        + 24 * (1 - p) ** m
        - 8 * (1 + p - 2 * p * p) ** m
        + (1 + 4 * p - 4 * p * p) ** m
        - 1
    )


def direct_energy(m: int) -> float:
    p = 2.0 ** (1 - m)
    A, B = sqrt(1.0 - p), sqrt(p)
    coeff = {}
    for mask in range(1 << m):
        k = mask.bit_count()
        amp = (A ** (m - k)) * (B ** k)
        coeff[mask] = amp if mask == 0 else -amp
    total = 0.0
    for u in range(1, 1 << m):
        corr = sum(coeff[t] * coeff[t ^ u] for t in range(1 << m))
        total += corr * corr
    return total


def normalized(m: int):
    p = 2.0 ** (1 - m)
    I = m * p
    H = -(1 - p) ** 2 * log2((1 - p) ** 2) + (2 * p - p * p) * 2 * (m - 1)
    h = -p * log2(p) - (1 - p) * log2(1 - p)
    K = m * h - H
    return float(exact_energy(m)) / I, K / I, H / I


max_err = 0.0
for m in range(2, 7):
    direct = direct_energy(m)
    closed = float(exact_energy(m))
    err = abs(direct - closed)
    max_err = max(max_err, err)
    print(f"m={m} direct={direct:.17g} closed={closed:.17g} abs_err={err:.3e}")
    assert err < 1e-12

print(f"max_small_m_error={max_err:.3e}")
for m in (4, 8, 12, 16, 20, 24):
    b, k, h = normalized(m)
    print(f"m={m:2d} B_over_I={b:.15f} K_over_I={k:.15f} H_over_I={h:.15f}")

# The finite table visibly approaches the analytic limits B/I -> 4 and H/I -> 4,
# while K/I grows without bound.  Check only conservative finite diagnostics here.
b24, k24, h24 = normalized(24)
assert abs(b24 - 4.0) < 1e-3
assert 3.9 < h24 < 4.0
assert k24 > 20.0
print("PASS")
