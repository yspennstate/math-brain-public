#!/usr/bin/env python3
"""Deterministic checks for B05/A023 order-swap credit boundary.

The interval part uses exact rational arithmetic and a rigorously bounded
atanh series for logarithms.  Floating-point enumeration is explicitly
reported only as corroboration.
"""

from fractions import Fraction as Q
import math
import itertools


def mul_pow2(x, k):
    return x * (1 << k) if k >= 0 else x / (1 << (-k))


def ln_interval(x, terms=90):
    assert x > 0
    k = 0
    y = x
    while y < 1:
        y *= 2
        k -= 1
    while y >= 2:
        y /= 2
        k += 1

    def atanh_ln_interval(v):
        z = (v - 1) / (v + 1)
        s = Q(0)
        power = z
        for j in range(terms):
            s += 2 * power / (2 * j + 1)
            power *= z * z
        rem = 2 * power / ((2 * terms + 1) * (1 - z * z))
        return s, s + rem

    ylo, yhi = atanh_ln_interval(y)
    l2lo, l2hi = atanh_ln_interval(Q(2))
    if k >= 0:
        return ylo + k * l2lo, yhi + k * l2hi
    return ylo + k * l2hi, yhi + k * l2lo


LN2 = ln_interval(Q(2))


def log2_recip_interval(t):
    assert 0 < t <= 1
    lo, hi = ln_interval(t)
    nlo, nhi = -hi, -lo
    return nlo / LN2[1], nhi / LN2[0]


def phi_interval(t):
    if t == 0:
        return Q(0), Q(0)
    lo, hi = log2_recip_interval(t)
    return t * lo, t * hi


def iadd(x, y):
    return x[0] + y[0], x[1] + y[1]


def isub(x, y):
    return x[0] - y[1], x[1] - y[0]


def iscale(c, x):
    return (c * x[0], c * x[1]) if c >= 0 else (c * x[1], c * x[0])


def psi_interval(a, e):
    return isub(iadd(phi_interval(a * a), phi_interval(e)),
                phi_interval(a * a + e))


def L_and_interval(n):
    d = Q(1, 1 << n)
    return iadd(psi_interval(1 - d, d * d),
                (2 * d - 2 * d * d, 2 * d - 2 * d * d))


def gamma_and_interval(n):
    return isub(L_and_interval(n), iscale(Q(1, 2), L_and_interval(n - 1)))


def L_two_gate_interval(a, b):
    A, B = Q(1, 1 << a), Q(1, 1 << b)
    d = A * B
    ca0, ca1 = -1 + 2 * A, 2 * A
    cb0, cb1 = -1 + 2 * B, 2 * B
    cats = [
        (1, ca0 * cb0),
        ((1 << a) - 1, ca1 * cb0),
        ((1 << b) - 1, ca0 * cb1),
        (((1 << a) - 1) * ((1 << b) - 1), ca1 * cb1),
    ]
    out = (Q(0), Q(0))
    for mult, c in cats:
        out = iadd(out, iscale(mult, psi_interval(c - d, d * d)))
    return out


def gamma_two_gate_interval(a, b, which):
    parent = L_two_gate_interval(a, b)
    child = L_two_gate_interval(a - 1, b) if which == "A" else L_two_gate_interval(a, b - 1)
    return isub(parent, iscale(Q(1, 2), child))


def fwht(vals):
    a = [float(v) for v in vals]
    N = len(a)
    for j in range(N.bit_length() - 1):
        s = 1 << j
        for base in range(0, N, 2 * s):
            for t in range(s):
                x, y = a[base + t], a[base + t + s]
                a[base + t], a[base + t + s] = x + y, x - y
    return [x / N for x in a]


def phi_float(t):
    return 0.0 if t == 0 else t * math.log2(1 / t)


def psi_float(a, e):
    return phi_float(a * a) + phi_float(e) - phi_float(a * a + e)


def L_float(vals):
    d = 1 / len(vals)
    return sum(psi_float(c - d, d * d) for c in fwht(vals))


def restrict(vals, i, bit):
    return [v for j, v in enumerate(vals) if ((j >> i) & 1) == bit]


def direct_credit(vals, i):
    return L_float(vals) - 0.5 * L_float(restrict(vals, i, 0))


def bent_values(k):
    h = k // 2
    return [1 if sum(((x >> (2*j)) & 1) * ((x >> (2*j+1)) & 1)
                     for j in range(h)) % 2 == 0 else -1
            for x in range(1 << k)]


def addressing_values(r):
    m, n = 1 << r, r + (1 << r)
    out = []
    for x in range(1 << n):
        address = x & (m - 1)
        data_bit = (x >> (r + address)) & 1
        out.append(1 if data_bit == 0 else -1)
    return out


def dec(iv):
    return float(iv[0]), float(iv[1])


def main():
    rigorous = 0
    certified_caps = {
        3: Q(-48, 10_000),
        4: Q(-112, 10_000),
        8: Q(-17, 100_000),
        12: Q(-115, 100_000_000),
        20: Q(-322, 10_000_000_000_000),
    }
    for n in range(3, 21):
        iv = gamma_and_interval(n)
        assert iv[1] < 0
        rigorous += 1
        if n in (3, 4, 8, 12, 20):
            assert iv[1] < certified_caps[n]
            print(f"AND n={n:2d} gamma interval={dec(iv)}; "
                  f"certified_upper<{float(certified_caps[n]):.14g}")

    ga = gamma_two_gate_interval(4, 5, "A")
    gb = gamma_two_gate_interval(4, 5, "B")
    assert ga[1] < Q(-22, 100_000)
    assert gb[1] < Q(-26, 100_000)
    rigorous += 2
    print("q4 tensor q5, query q4 coordinate:", dec(ga),
          "; certified_upper<-0.00022")
    print("q4 tensor q5, query q5 coordinate:", dec(gb),
          "; certified_upper<-0.00026")

    # Exact Walsh restriction relations underlying the pairwise formula.
    exact_relations = 0
    negative_credits = 0
    for n in range(2, 5):
        N = 1 << n
        for tail in itertools.product((-1, 1), repeat=N - 1):
            vals = (1,) + tail
            coeff = [Q(round(x * N), N) for x in fwht(vals)]
            for i in range(n):
                child = restrict(vals, i, 0)
                cchild = [Q(round(x * (N // 2)), N // 2) for x in fwht(child)]
                for mask in range(N):
                    if (mask >> i) & 1:
                        continue
                    low = mask & ((1 << i) - 1)
                    high = mask >> (i + 1)
                    child_mask = low | (high << i)
                    assert cchild[child_mask] == coeff[mask] + coeff[mask | (1 << i)]
                    exact_relations += 1
                if direct_credit(vals, i) < -1e-12:
                    negative_credits += 1

    for k in (2, 4, 6, 8, 10):
        vals = bent_values(k)
        h = k // 2
        credits = [direct_credit(vals, 2*j) for j in range(h)]
        assert min(credits) >= -1e-12

    for r in (1, 2, 3):
        vals = addressing_values(r)
        credits = [direct_credit(vals, i) for i in range(r + (1 << r))]
        print(f"addressing r={r}: address_min={min(credits[:r]):.12g}, "
              f"data_min={min(credits[r:]):.12g}")

    print(f"rigorous_negative_interval_assertions={rigorous}")
    print(f"exact_walsh_restriction_relations={exact_relations}")
    print(f"enumerated_negative_coordinate_credits={negative_credits}")
    print("bent_controls_checked=k=2,4,6,8,10")
    print("addressing_controls_checked=r=1,2,3")
    print("random_seed=None")
    print("status=PASS")


if __name__ == "__main__":
    main()
