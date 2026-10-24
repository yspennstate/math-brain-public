#!/usr/bin/env python3
"""Independent A094 checker for B05_ODD_SURGERY_PAYMENT_v1.

The script does not import the author's checker.  It reconstructs Walsh
coefficients and physical influences exactly on an exhaustive small cube,
checks the entropy identities at high precision, and certifies every
rational inequality used in the two Taylor boxes.
"""

from fractions import Fraction as F
from itertools import combinations
from decimal import Decimal as D, getcontext

getcontext().prec = 90
LN2 = D(2).ln()


def dec(x):
    if isinstance(x, F):
        return D(x.numerator) / D(x.denominator)
    return D(x)


def log2(x):
    return dec(x).ln() / LN2


def fwht_exact(a):
    a = [F(x) for x in a]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    n = len(a)
    return [x / n for x in a]


def upper_caps(q, n):
    z = list(q)
    for bit in range(n):
        for s in range(1 << n):
            if not ((s >> bit) & 1):
                z[s] += z[s | (1 << bit)]
    return z


def U(spec, n):
    q = [x * x for x in spec]
    cap = upper_caps(q, n)
    ans = D(0)
    for x, y in zip(q, cap):
        if x:
            xx, yy = dec(x), dec(y)
            ans += xx * log2(yy / xx)
    return ans


def bent(k):
    r = k // 2
    out = []
    for x in range(1 << k):
        dot = 0
        for j in range(r):
            dot ^= ((x >> j) & 1) & ((x >> (r + j)) & 1)
        out.append(-1 if dot else 1)
    return out


def flip(g, pts):
    h = list(g)
    for x in pts:
        h[x] = -h[x]
    return h


def selector_truth(g, h, k, d):
    active = (1 << d) - 1
    return [
        (h if z == active else g)[x]
        for z in range(1 << d)
        for x in range(1 << k)
    ]


def predicted_spectrum(a, b, k, d):
    p = F(1, 1 << d)
    e = [bb - aa for aa, bb in zip(a, b)]
    out = []
    for A in range(1 << d):
        phase = -1 if A.bit_count() & 1 else 1  # active address is all ones
        for T in range(1 << k):
            out.append(a[T] + p * e[T] if A == 0 else phase * p * e[T])
    return out


def direct_control_influence(truth, k, d):
    N = len(truth)
    total = F(0)
    for j in range(d):
        bit = 1 << (k + j)
        piv = sum(truth[x] != truth[x ^ bit] for x in range(N))
        total += F(piv, N)
    return total


def identity_terms(g, h, k, d):
    a, b = fwht_exact(g), fwht_exact(h)
    p = F(1, 1 << d)
    e = [bb - aa for aa, bb in zip(a, b)]
    c = [aa + p * ee for aa, ee in zip(a, e)]
    A = upper_caps([x * x for x in a], k)
    B = upper_caps([x * x for x in b], k)
    Dcaps = upper_caps([x * x for x in e], k)

    base = D(0)
    udiff = D(0)
    for ct, At, Bt, et, Dt in zip(c, A, B, e, Dcaps):
        if ct:
            cc = dec(ct * ct)
            mix = (1 - p) * At + p * Bt
            mm = dec(mix)
            base += cc * log2(mm / cc)
        if et:
            ee = et * et
            ex = dec(ee)
            dx = dec(Dt)
            udiff += ex * log2(dx / ex)
    norm = sum(x * x for x in e)
    normx = dec(norm)
    coeff = p * d / 2 - p * p * d
    coeffx = dec(coeff)
    rhs3 = base + dec(p * (1 - p)) * udiff + coeffx * normx

    delta = F(1, 1 << k)
    scalar = D(0)
    for at, bt, ct, At, Bt in zip(a, b, c, A, B):
        u = Bt / At - 1
        v = bt * bt / delta - 1
        w = ct * ct / delta - 1
        ux, vx, wx = (dec(x) for x in (u, v, w))
        px = dec(p)
        phi = (1 + wx) * ((1 + px * ux) / (1 + wx)).ln()
        phi -= px * (1 + vx) * ((1 + ux) / (1 + vx)).ln()
        scalar += dec(delta) * phi / LN2
    K = udiff
    for T, et in enumerate(e):
        ee = et * et
        K -= dec(ee) * (k - T.bit_count())
    m = sum(x != y for x, y in zip(g, h))
    ictl = F(2 * d * m, (1 << d) * (1 << k))
    ictlx = dec(ictl)
    px = dec(p)
    J7 = scalar + px * (1 - px) * K + (1 - 2 * px) * ictlx
    return rhs3, J7, U(a, k), U(b, k), ictl, e, Dcaps


def ln_interval(q, terms=180):
    """Exact rational enclosure via ln q = 2 sum z^(2j+1)/(2j+1)."""
    q = F(q)
    z = (q - 1) / (q + 1)
    assert 0 <= z < 1
    s = F(0)
    for j in range(terms):
        s += 2 * z ** (2 * j + 1) / (2 * j + 1)
    # Replace all remaining odd denominators by the first remaining one.
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return s, s + tail


def certify_rational_boxes():
    # Sparse odd-m box: |u|,|v|<=5/32, |w|<=5/64.
    huu = F(1, 2) * F(69, 64) / F(59, 64) ** 2 + F(37, 32) / F(27, 32) ** 2
    assert huu < F(23, 10)
    assert F(32, 27) < F(12, 10)      # uv, vv after factoring p
    assert F(64, 59) < F(11, 10)      # uw after factoring p, and ww

    # The half-Hessian remainder after p^2<=p/2.
    general_rem = F(1, 2) * (
        F(23, 10) * 25 + 2 * F(12, 10) * 25
        + 2 * F(11, 10) * 25 * F(1, 2)
        + F(12, 10) * 25 + F(11, 10) * 25 * F(1, 2)
    )
    assert general_rem == F(755, 8)  # 94.375
    assert 4 + general_rem < 99

    # Triple box: |u|,|v|<=7/16, |w|<=13/64.
    huu3 = F(1, 2) * F(77, 64) / F(25, 32) ** 2 + F(23, 16) / F(9, 16) ** 2
    assert huu3 < 6
    assert F(16, 9) < F(18, 10)
    assert F(32, 25) < F(13, 10)
    assert F(64, 51) < F(13, 10)
    triple_rem = F(1, 2) * (
        6 * 14**2
        + 2 * F(18, 10) * 14**2
        + 2 * F(13, 10) * 14 * 13 * F(1, 2)
        + F(18, 10) * 14**2
        + F(13, 10) * 13**2 * F(1, 2)
    )
    assert triple_rem == F(51617, 40)  # 1290.425
    assert 36 + triple_rem < 1327

    ln2_lo, ln2_hi = ln_interval(2)
    ln3_lo, ln3_hi = ln_interval(3)
    C_lo = 1 + F(1327, 6) / ln2_hi + 4 * ln3_lo / ln2_hi
    C_hi = 1 + F(1327, 6) / ln2_lo + 4 * ln3_hi / ln2_lo
    assert C_hi < 327
    return huu, general_rem, huu3, triple_rem, C_lo, C_hi


def main():
    boxes = certify_rational_boxes()
    g = bent(4)
    exact_spectrum = 0
    exact_influence = 0
    entropy_checks = 0
    max_err3 = D(0)
    max_err7 = D(0)
    min_abs_ratio = None
    max_K_gap = D("-Infinity")

    for case_index, pts in enumerate(combinations(range(16), 3)):
        h = flip(g, pts)
        a, b = fwht_exact(g), fwht_exact(h)
        for d in (1, 2):
            truth = selector_truth(g, h, 4, d)
            direct = fwht_exact(truth)
            predicted = predicted_spectrum(a, b, 4, d)
            assert direct == predicted
            exact_spectrum += len(direct)

            ictl = direct_control_influence(truth, 4, d)
            expected = F(2 * d * 3, (1 << d) * 16)
            assert ictl == expected
            exact_influence += 1

            # A deterministic 1/28 subsample for independent entropy reconstruction.
            if case_index % 28 == 0:
                rhs3, J7, Ug, Uh, _, e, Dcaps = identity_terms(g, h, 4, d)
                directU = U(direct, 4 + d)
                p = D(1) / (1 << d)
                directJ = directU - (1 - p) * Ug - p * Uh
                max_err3 = max(max_err3, abs(directU - rhs3))
                max_err7 = max(max_err7, abs(directJ - J7))
                assert abs(directU - rhs3) < D("1e-75")
                assert abs(directJ - J7) < D("1e-75")

                delta = F(1, 16)
                for et in e:
                    r = abs(et) / (2 * delta)
                    assert r.denominator == 1 and r.numerator % 2 == 1
                    min_abs_ratio = r if min_abs_ratio is None else min(min_abs_ratio, r)
                # Verify K <= 8m delta log2 m numerically with 80+ digits.
                udiff = D(0)
                level = D(0)
                for T, (et, Dt) in enumerate(zip(e, Dcaps)):
                    ee = et * et
                    ex = dec(ee)
                    dx = dec(Dt)
                    udiff += ex * log2(dx / ex)
                    level += ex * (4 - T.bit_count())
                K = udiff - level
                gap = K - D(8 * 3) / 16 * log2(3)
                max_K_gap = max(max_K_gap, gap)
                assert gap <= 0
                entropy_checks += 1

    print("STATUS PASS")
    print("EXHAUSTIVE_TRIPLE_SETS", 560)
    print("EXACT_WALSH_COEFFICIENT_ASSERTIONS", exact_spectrum)
    print("EXACT_CONTROL_INFLUENCE_ASSERTIONS", exact_influence)
    print("HIGH_PRECISION_ENTROPY_CASES", entropy_checks)
    print("MAX_EQ3_ERROR", f"{max_err3:.8E}")
    print("MAX_EQ7_ERROR", f"{max_err7:.8E}")
    print("MIN_ODD_ATOM_MULTIPLIER", min_abs_ratio)
    print("MAX_K_BOUND_GAP", f"{max_K_gap:.12E}")
    print("GENERAL_HUU_COEFF_UPPER", float(boxes[0]))
    print("GENERAL_REMAINDER", float(boxes[1]))
    print("TRIPLE_HUU_COEFF_UPPER", float(boxes[2]))
    print("TRIPLE_REMAINDER", float(boxes[3]))
    print("TRIPLE_CONSTANT_INTERVAL", f"{dec(boxes[4]):.16f}", f"{dec(boxes[5]):.16f}")


if __name__ == "__main__":
    main()
