#!/usr/bin/env python3
"""Deterministic checks for the A005 endpoint-admission formulas.

The Walsh arithmetic is exact over Fraction.  Entropies and logarithmic
functionals are evaluated with 80-digit Decimal arithmetic.  The script does
not import author code and uses no random search.
"""

from decimal import Decimal, getcontext
from fractions import Fraction as F
from itertools import product

getcontext().prec = 80
LN2 = Decimal(2).ln()


def D(x):
    return Decimal(x.numerator) / Decimal(x.denominator)


def log2(x):
    return x.ln() / LN2


def phi(x):
    x = D(x) if isinstance(x, F) else x
    return Decimal(0) if x == 0 else x * (-log2(x))


def ell(x, y):
    x, y = D(x), D(y)
    return Decimal(0) if x == 0 else x * log2(Decimal(1) + y / x)


def fwht(values):
    out = list(values)
    step = 1
    while step < len(out):
        for base in range(0, len(out), 2 * step):
            for j in range(step):
                a, b = out[base + j], out[base + j + step]
                out[base + j], out[base + j + step] = a + b, a - b
        step *= 2
    return out


def coeffs(values):
    N = len(values)
    return [F(x, N) for x in fwht(values)]


def entropy(values):
    return sum(phi(a * a) for a in coeffs(values))


def influence(values):
    n = len(values).bit_length() - 1
    return sum(F(sum(values[x] != values[x ^ (1 << i)] for x in range(len(values))), len(values))
               for i in range(n))


def downward(values):
    a = coeffs(values)
    masses = [x * x for x in a]
    ans = Decimal(0)
    for A, x in enumerate(masses):
        for i in range(len(values).bit_length() - 1):
            if A & (1 << i):
                ans += ell(x, masses[A ^ (1 << i)])
    return ans


def mean(values):
    return F(sum(values), len(values))


def activate(values, r):
    n = len(values).bit_length() - 1
    out = []
    for idx in range(1 << (n + r)):
        data = idx & ((1 << n) - 1)
        controls = idx >> n
        out.append(values[data] if controls == (1 << r) - 1 else 1)
    return out


def restrict(values, coordinate, bit):
    n = len(values).bit_length() - 1
    out = []
    for small in range(1 << (n - 1)):
        low = small & ((1 << coordinate) - 1)
        high = small >> coordinate
        idx = low | (bit << coordinate) | (high << (coordinate + 1))
        out.append(values[idx])
    return out


def activation_L_formula(values, r):
    a = coeffs(values)
    mass = [x * x for x in a]
    mu = a[0]
    q = 1 - mu
    p = F(1, 1 << r)
    c = 1 - p * q
    n = len(values).bit_length() - 1

    data = Decimal(0)
    for S in range(1, len(values)):
        if S & (S - 1):
            for i in range(n):
                if S & (1 << i):
                    data += D(p) * ell(mass[S], mass[S ^ (1 << i)])
        else:
            x = mass[S]
            data += ell(p * p * x, c * c)
            data += ((1 << r) - 1) * ell(p * p * x, p * p * q * q)

    control = D(F(r, 2) * p * (1 - mu * mu))
    control += D(F(r, 2) * p * q * q - r * p * p * q * q)
    control += r * ell(p * p * q * q, c * c)
    return data + control


def activation_control_delta_formula(values, r):
    mu = mean(values)
    q = 1 - mu
    p = F(1, 1 << r)
    s = 1 - mu * mu
    c = 1 - p * q
    x = p * p * q * q
    ans = D(2 * p * s) + phi(x) + D(2 * p * q * q - 4 * p * p * q * q)
    ans += phi(c * c) - phi((1 - 2 * p * q) ** 2) / 2
    return ans


def all_nonconstant(n):
    N = 1 << n
    for bits in range(1, (1 << N) - 1):
        yield [1 if bits & (1 << x) else -1 for x in range(N)]


def close(a, b, tol=Decimal("1e-65")):
    return abs(a - b) <= tol


def main():
    activation_checks = 0
    tensor_checks = 0
    asymptotic_checks = 0
    max_error = Decimal(0)

    for n in (1, 2, 3):
        for values in all_nonconstant(n):
            for r in (1, 2, 3):
                av = activate(values, r)
                brute_L = downward(av)
                formula_L = activation_L_formula(values, r)
                err = abs(brute_L - formula_L)
                max_error = max(max_error, err)
                assert close(brute_L, formula_L)

                control = n
                brute_delta = entropy(av) - (
                    entropy(restrict(av, control, 0))
                    + entropy(restrict(av, control, 1))
                ) / 2
                formula_delta = activation_control_delta_formula(values, r)
                err = abs(brute_delta - formula_delta)
                max_error = max(max_error, err)
                assert close(brute_delta, formula_delta)
                activation_checks += 2

    # Exact tensor-additivity tests for L on every pair of nonconstant
    # one- and two-bit gates.
    small = list(all_nonconstant(1)) + list(all_nonconstant(2))
    for f, g in product(small, repeat=2):
        vals = [f[x % len(f)] * g[x // len(f)] for x in range(len(f) * len(g))]
        err = abs(downward(vals) - downward(f) - downward(g))
        max_error = max(max_error, err)
        assert close(downward(vals), downward(f) + downward(g))
        tensor_checks += 1

    # The control restriction-step ratio tends to 4.  Balanced one-bit
    # dictator is enough to isolate the scalar asymptotic.
    g = [-1, 1]
    q = 1 - mean(g)
    for r in (4, 8, 16, 32):
        p = F(1, 1 << r)
        ratio = activation_control_delta_formula(g, r) / D(p * q)
        assert ratio > Decimal(4)
        if r >= 16:
            assert abs(ratio - Decimal(4)) < Decimal("0.01")
        print(f"balanced_control_ratio_r={r}: {ratio}")
        asymptotic_checks += 1

    print(f"activation_formula_checks={activation_checks}")
    print(f"tensor_L_additivity_checks={tensor_checks}")
    print(f"control_asymptotic_checks={asymptotic_checks}")
    print(f"total_checks={activation_checks + tensor_checks + asymptotic_checks}")
    print(f"max_abs_error={max_error}")
    print("random_seed=None")
    print("status=PASS")


if __name__ == "__main__":
    main()
