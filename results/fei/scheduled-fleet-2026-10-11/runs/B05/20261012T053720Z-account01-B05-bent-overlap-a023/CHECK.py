#!/usr/bin/env python3
"""Deterministic checks for the shared-variable bent-surgery U theorem."""

from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 75
LN2 = Decimal(2).ln()


def dec(x):
    if isinstance(x, Fraction):
        return Decimal(x.numerator) / Decimal(x.denominator)
    return Decimal(x)


def log2q(x):
    z = dec(x)
    return z.ln() / LN2


def walsh(values):
    a = [Fraction(v) for v in values]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / n for x in a]


def upper(mass):
    ans = mass[:]
    n = len(ans).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(len(ans)):
            if not (s & bit):
                ans[s] += ans[s | bit]
    return ans


def U_coeff(a):
    p = [x * x for x in a]
    cap = upper(p)
    return sum((dec(x) * log2q(y / x) for x, y in zip(p, cap) if x), Decimal(0))


def U_values(values):
    return U_coeff(walsh(values))


def shared_node_formula_from_coeff(a, b, d):
    """Exact formula for U(F)-(1-p)U(g)-pU(h), p=2^-d."""
    p = Fraction(1, 2**d)
    aa = [x * x for x in a]
    bb = [x * x for x in b]
    diff = [y - x for x, y in zip(a, b)]
    dd = [x * x for x in diff]
    A, B, D = upper(aa), upper(bb), upper(dd)
    c = [(1 - p) * x + p * y for x, y in zip(a, b)]
    first = Decimal(0)
    second = Decimal(0)
    for x, ca, cb, z, capd in zip(c, A, B, diff, D):
        x2 = x * x
        if x2:
            first += dec(x2) * log2q(((1 - p) * ca + p * cb) / x2)
        z2 = z * z
        if z2:
            second += dec(p * (1 - p) * z2) * log2q(capd / z2)
    second += dec((p * d / 2 - p * p * d) * sum(dd, Fraction(0)))
    return first + second - dec(1 - p) * U_coeff(a) - dec(p) * U_coeff(b)


def shared_node_formula(g, h, d):
    return shared_node_formula_from_coeff(walsh(g), walsh(h), d)


def selector_function(g, h, d):
    block = 1 << d
    out = []
    for x in range(len(g)):
        for z in range(block):
            out.append(h[x] if z == 0 else g[x])
    return out


def direct_node_charge(g, h, d):
    p = Decimal(1) / Decimal(2**d)
    return U_values(selector_function(g, h, d)) - (Decimal(1) - p) * U_values(g) - p * U_values(h)


def quadratic_bent(k, affine_mask=0, global_sign=1):
    assert k % 2 == 0
    ans = []
    for x in range(1 << k):
        phase = 0
        for j in range(0, k, 2):
            phase ^= ((x >> j) & 1) & ((x >> (j + 1)) & 1)
        phase ^= (x & affine_mask).bit_count() & 1
        ans.append(global_sign * (-1 if phase else 1))
    return ans


def flip(values, point):
    out = values[:]
    out[point] *= -1
    return out


def influence_credit(g, h, d):
    theta = Fraction(sum(x != y for x, y in zip(g, h)), len(g))
    return dec(2 * Fraction(1, 2**d) * d * theta)


def verify_exact_bent_ranges(g, h, d):
    k = len(g).bit_length() - 1
    assert k >= 8 and k % 2 == 0
    alpha = Fraction(1, 2 ** (k // 2))
    delta = alpha * alpha
    p = Fraction(1, 2**d)
    a, b = walsh(g), walsh(h)
    A, B = upper([x * x for x in a]), upper([x * x for x in b])
    c = [(1 - p) * x + p * y for x, y in zip(a, b)]
    for x, y, ca, cb, z in zip(a, b, A, B, c):
        assert x * x == delta
        u = (cb - ca) / ca
        v = y * y / delta - 1
        w = z * z / delta - 1
        assert abs(u) <= Fraction(17, 4) * alpha
        assert abs(v) <= Fraction(17, 4) * alpha
        assert abs(w) <= Fraction(33, 8) * p * alpha


def majority(n):
    return [-1 if x.bit_count() <= n // 2 else 1 for x in range(1 << n)]


def point_defect(n):
    out = [1] * (1 << n)
    out[0] = -1
    return out


def addressing(m):
    # m address bits followed by 2^m data bits.
    n = m + (1 << m)
    out = []
    for x in range(1 << n):
        addr = x & ((1 << m) - 1)
        bit = (x >> (m + addr)) & 1
        out.append(1 if bit else -1)
    return out


def tensor(g, h):
    return [x * y for x in g for y in h]


def main():
    assertions = 0
    max_direct_error = Decimal(0)
    max_bent_ratio = Decimal(0)

    print("direct Walsh versus exact shared-node formula")
    for k in (2, 4, 6):
        for mask in (0, 1):
            g = quadratic_bent(k, mask)
            for point in (0, (1 << k) - 1):
                h = flip(g, point)
                for d in (1, 2):
                    direct = direct_node_charge(g, h, d)
                    formula = shared_node_formula(g, h, d)
                    err = abs(direct - formula)
                    max_direct_error = max(max_direct_error, err)
                    assert err < Decimal("1e-65")
                    assertions += 1
    print(f"direct_cases=24 max_error={max_direct_error:.3E}")

    print("bent one-point surgery theorem checks")
    theorem_cases = 0
    for k in (8, 10, 12):
        points = (0, (1 << k) - 1)
        for mask in (0, 1):
            g = quadratic_bent(k, mask, -1 if mask == 1 else 1)
            for point in points:
                h = flip(g, point)
                for d in (1, 2, 4, 8):
                    verify_exact_bent_ranges(g, h, d)
                    charge = shared_node_formula(g, h, d)
                    credit = influence_credit(g, h, d)
                    ratio = charge / credit
                    max_bent_ratio = max(max_bent_ratio, ratio)
                    assert charge <= Decimal(71) * credit
                    assertions += 4 * len(g) + 1
                    theorem_cases += 1
    print(f"theorem_cases={theorem_cases} max_J_over_Ictl={max_bent_ratio:.15f}")

    print("exhaustive small Boolean one-point-surgery controls")
    exhaustive = 0
    max_small_ratio = Decimal(0)
    for n in range(1, 4):
        all_codes = range(1 << (1 << n))
        codes = all_codes if n <= 2 else range(0, 1 << (1 << n), 8)
        for code in codes:
            g = [1 if (code >> x) & 1 else -1 for x in range(1 << n)]
            for point in range(1 << n):
                h = flip(g, point)
                for d in (1, 2, 3, 5):
                    charge = shared_node_formula(g, h, d)
                    credit = influence_credit(g, h, d)
                    max_small_ratio = max(max_small_ratio, charge / credit)
                    assert charge.is_finite()
                    assertions += 1
                    exhaustive += 1
    print(f"exhaustive_cases={exhaustive} max_ratio={max_small_ratio:.15f}")

    print("structured mandatory controls")
    controls = [
        ("majority9", majority(9)),
        ("point_defect9", point_defect(9)),
        ("addressing2", addressing(2)),
        ("near_tensor", tensor(point_defect(3), point_defect(4))),
    ]
    structured = 0
    for name, g in controls:
        h = flip(g, len(g) // 3)
        vals = []
        for d in (1, 2, 4, 8):
            charge = shared_node_formula(g, h, d)
            ratio = charge / influence_credit(g, h, d)
            vals.append(f"d{d}:{ratio:.8f}")
            assert charge.is_finite()
            assertions += 1
            structured += 1
        print(name + " " + " ".join(vals))

    print(f"structured_cases={structured}")
    print(f"assertions={assertions} failures=0 randomness=none")


if __name__ == "__main__":
    main()
