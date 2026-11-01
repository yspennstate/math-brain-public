#!/usr/bin/env python3
"""High-precision audit for A042 weighted-threshold endpoint formulas.

No randomness is used.  Decimal arithmetic is only a numerical check; the
all-parameter limits are proved in REPORT.md and BIASED_ENDPOINT_SERIES.tex.
"""

from decimal import Decimal, getcontext

getcontext().prec = 180
D = Decimal
ONE = D(1)
TWO = D(2)
FOUR = D(4)
LN2 = TWO.ln()


def hnat(x):
    if x == 0 or x == 1:
        return D(0)
    return -x * x.ln() - (ONE - x) * (ONE - x).ln()


def log2(x):
    return x.ln() / LN2


def weighted(m):
    M = D(m)
    q = ONE / (M * M)
    eta = ONE / M
    a = q ** m
    d = ONE + (M - ONE) * a
    q0 = (M - ONE) * a / d
    alpha = M * a / d
    r = eta + (ONE - eta) * q
    tc = M * hnat(r) - (M - ONE) * hnat(q)
    iscale = TWO - ONE / M - q - q0  # I/(4 alpha)
    event_ratio = tc / (FOUR * iscale)

    L = -alpha.ln()
    residual_scaled = (
        (ONE - alpha) * (L - FOUR.ln() - (ONE - alpha).ln())
        - (ONE - ONE / M - q0)
        * (L + (ONE - a).ln() - (ONE - alpha).ln())
        - (ONE - q) * (M.ln() - (ONE - alpha).ln())
    )
    credit_ratio = residual_scaled / iscale

    delta_g = FOUR * a * (M * (ONE - q) - ONE + a)
    hplus_g = TWO * delta_g + D(8) * M * a * (q - a) * log2(ONE / q)
    delta_o = FOUR * q0 * a * (ONE - q0) * (ONE - a)
    hplus_o = (
        D(8) * q0 * (ONE - q0) * (ONE - a) ** 2 * log2(ONE / (ONE - a))
        + D(8) * a * (ONE - a) * (ONE - q0) ** 2 * log2(ONE / (ONE - q0))
        + D(8) * q0 * a * (ONE - q0) * (ONE - a)
    )
    delta_f = delta_o + (ONE - q0) * delta_g
    hplus_f = hplus_o + (ONE - q0) * hplus_g
    genuine_ratio = hplus_f / delta_f
    return event_ratio, credit_ratio, genuine_ratio


def pair_mi_light(q):
    r = (ONE + q) / TWO
    cells = (
        (ONE + q * q) / TWO,
        q * (ONE - q) / TWO,
        q * (ONE - q) / TWO,
        (ONE - q) ** 2 / TWO,
    )
    marg = (r, ONE - r)
    products = (marg[0] ** 2, marg[0] * marg[1], marg[0] * marg[1], marg[1] ** 2)
    return sum((p * (p / z).ln() for p, z in zip(cells, products) if p), D(0))


def local_ratios(m, q):
    M = D(m)
    a = q ** m
    q0 = a / (ONE + a)
    r = (ONE + q) / TWO
    mi_hl = hnat(r) - hnat(q) / TWO
    mi_ll = pair_mi_light(q)
    i0_over_alpha = FOUR * (ONE / TWO - q0)
    il_over_alpha = TWO * (ONE - q)
    heavy = M * mi_hl / i0_over_alpha
    light = (mi_hl + (M - ONE) * mi_ll) / il_over_alpha
    return heavy, light


print("weighted family q=m^-2, eta=1/m")
print("m event_ratio_nats credit_ratio_nats genuine_Hplus_over_Delta_bits")
for m in (2, 3, 4, 8, 16, 32, 64):
    vals = weighted(m)
    print(m, *(format(x, ".24g") for x in vals))

print("\nscaled asymptotic checks")
print("m event_minus_(lnm+1)/8 credit_minus_(lnm/2-ln2) genuine_minus_2")
for m in (4, 8, 16, 32, 64):
    er, cr, gr = weighted(m)
    M = D(m)
    print(
        m,
        format(er - (M.ln() + ONE) / D(8), ".18g"),
        format(cr - (M.ln() / TWO - LN2), ".18g"),
        format(gr - TWO, ".18g"),
    )

print("\nlocal-TC iterated limit eta=1/2")
print("m q heavy_coordinate_ratio light_coordinate_ratio target_m_ln2_over_2")
for m in (2, 4, 8):
    for exp in (2, 4, 8, 16):
        q = D(10) ** (-exp)
        heavy, light = local_ratios(m, q)
        target = D(m) * LN2 / TWO
        print(
            m,
            f"1e-{exp}",
            format(heavy, ".24g"),
            format(light, ".24g"),
            format(target, ".24g"),
        )
