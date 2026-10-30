#!/usr/bin/env python3
"""Exact Walsh/cap certificate for the four-bit KL-versus-JS falsifier."""

from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 100
D = Decimal


def fwht(values):
    values = list(values)
    h = 1
    while h < len(values):
        for a in range(0, len(values), 2 * h):
            for j in range(a, a + h):
                x, y = values[j], values[j + h]
                values[j], values[j + h] = x + y, x - y
        h *= 2
    return tuple(Fraction(x, len(values)) for x in values)


def upper_caps(q):
    q = list(q)
    n = len(q).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not s & bit:
                q[s] += q[s | bit]
    return tuple(q)


def dec(x):
    return D(x.numerator) / D(x.denominator)


def h2(p):
    if p == 0 or p == 1:
        return D(0)
    p = dec(p)
    return -(p * p.ln() + (1 - p) * (1 - p).ln()) / D(2).ln()


def dber(eta, x):
    ans = D(0)
    for p, q in ((Fraction(1) + eta, Fraction(1) + x),
                 (Fraction(1) - eta, Fraction(1) - x)):
        p /= 2
        q /= 2
        if p:
            assert q > 0
            ans += dec(p) * (dec(p) / dec(q)).ln() / D(2).ln()
    return ans


def coordinate_terms(hat, cap, i):
    bit = 1 << i
    kl = D(0)
    js = D(0)
    rows = []
    for t in range(len(hat)):
        if t & bit:
            continue
        u, v = hat[t], hat[t | bit]
        m = u * u + v * v
        if not m:
            continue
        eta = 2 * u * v / m
        c = sum(hat[q] * hat[q | bit]
                for q in range(len(hat))
                if not q & bit and (q & t) == t)
        x = 2 * c / cap[t]
        kt = dec(m) * dber(eta, x)
        jt = dec(m) * (D(1) - h2((Fraction(1) + eta) / 2))
        kl += kt
        js += jt
        rows.append((t, u, v, m, eta, cap[t], c, x, kt, jt))
    return kl, js, rows


def main():
    truth = (1, -1, -1, 1, -1, 1, 1, -1,
             -1, -1, -1, 1, -1, 1, 1, 1)
    hat = fwht(truth)
    expected = {
        1: Fraction(-1, 4), 2: Fraction(-1, 4), 4: Fraction(-1, 4),
        7: Fraction(3, 4), 9: Fraction(1, 4), 10: Fraction(1, 4),
        12: Fraction(1, 4), 15: Fraction(1, 4),
    }
    assert {s: a for s, a in enumerate(hat) if a} == expected
    assert sum(a * a for a in hat) == 1
    influence = sum(Fraction(s.bit_count()) * a * a
                    for s, a in enumerate(hat))
    assert influence == Fraction(5, 2)
    cap = upper_caps(tuple(a * a for a in hat))

    totals = []
    all_rows = []
    for i in range(4):
        kl, js, rows = coordinate_terms(hat, cap, i)
        totals.append((kl, js))
        all_rows.append(rows)
    tiny = D("1e-90")
    for i in range(3):
        assert abs(totals[i][0]) < tiny
        assert abs(totals[i][1]) < tiny

    selector = all_rows[3]
    assert [(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])
            for r in selector] == [
        (1, Fraction(-1, 4), Fraction(1, 4), Fraction(1, 8),
         Fraction(-1), Fraction(3, 4), Fraction(1, 8), Fraction(1, 3)),
        (2, Fraction(-1, 4), Fraction(1, 4), Fraction(1, 8),
         Fraction(-1), Fraction(3, 4), Fraction(1, 8), Fraction(1, 3)),
        (4, Fraction(-1, 4), Fraction(1, 4), Fraction(1, 8),
         Fraction(-1), Fraction(3, 4), Fraction(1, 8), Fraction(1, 3)),
        (7, Fraction(3, 4), Fraction(1, 4), Fraction(5, 8),
         Fraction(3, 5), Fraction(5, 8), Fraction(3, 16), Fraction(3, 5)),
    ]

    ln2 = D(2).ln()
    kl_exact = D(3) / 8 * D(3).ln() / ln2
    js_exact = D(2) - D(5) / 8 * D(5).ln() / ln2
    kl, js = totals[3]
    assert abs(kl - kl_exact) < tiny
    assert abs(js - js_exact) < tiny
    assert 3 ** 3 * 5 ** 5 == 84375
    assert 2 ** 16 == 65536
    assert 3 ** 3 * 5 ** 5 > 2 ** 16
    defect = kl - js
    assert defect > 0

    # Independent direct check of the first tensor step.  The proof of all-r
    # additivity is algebraic in KL_JS_FALSIFIER.tex.
    tensor_truth = tuple(a * b for b in truth for a in truth)
    tensor_hat = fwht(tensor_truth)
    tensor_cap = upper_caps(tuple(a * a for a in tensor_hat))
    tensor_kl = tensor_js = D(0)
    for i in range(8):
        k, j, _ = coordinate_terms(tensor_hat, tensor_cap, i)
        tensor_kl += k
        tensor_js += j
    assert abs(tensor_kl - 2 * kl) < tiny
    assert abs(tensor_js - 2 * js) < tiny

    print("truth_mask=6038")
    print("walsh_nonzero=" + repr(expected))
    print(f"influence={influence}")
    print(f"aggregate_KL={kl:.50f}")
    print(f"aggregate_JS={js:.50f}")
    print(f"defect_bits={defect:.50f}")
    print(f"defect_over_I={defect / dec(influence):.50f}")
    print("tensor_square_additivity=EXACT_RATIONAL_STRUCTURE_AND_100_DIGIT_CHECK_PASS")
    print("exact_sign_test=3^3*5^5=84375 > 2^16=65536")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
