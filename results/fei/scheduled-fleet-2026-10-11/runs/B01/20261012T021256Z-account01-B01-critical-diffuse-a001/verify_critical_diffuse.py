#!/usr/bin/env python3
"""Checks for the A001 critical-diffuse restriction normal form."""
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache

getcontext().prec = 90
LN2 = Decimal(2).ln()
TOL = Decimal("1e-70")


def dec(q):
    if isinstance(q, Fraction):
        return Decimal(q.numerator) / Decimal(q.denominator)
    return Decimal(q)


def h2(q):
    x = dec(q)
    ans = Decimal(0)
    if x:
        ans -= x * x.ln() / LN2
    if x != 1:
        ans -= (1 - x) * (1 - x).ln() / LN2
    return ans


def envelope(q):
    x = dec(q)
    return h2(q) / x + Decimal(2) / LN2 * min(x, 1 - x) / x


def fwht(values):
    values = list(values)
    step = 1
    while step < len(values):
        for start in range(0, len(values), 2 * step):
            for j in range(step):
                a, b = values[start + j], values[start + j + step]
                values[start + j], values[start + j + step] = a + b, a - b
        step *= 2
    return values


@lru_cache(None)
def metrics(values):
    values = tuple(values)
    N = len(values)
    n = N.bit_length() - 1
    raw = fwht(values)
    probs = [Fraction(a * a, N * N) for a in raw]
    H = Decimal(0)
    for p in probs:
        if p:
            x = dec(p)
            H -= x * x.ln() / LN2
    influence = sum((p * s.bit_count() for s, p in enumerate(probs)), Fraction())
    coordinates = tuple(
        sum((p for s, p in enumerate(probs) if (s >> i) & 1), Fraction())
        for i in range(n)
    )
    return H, influence, coordinates


def restrict(values, i, bit):
    n = len(values).bit_length() - 1
    return tuple(values[x] for x in range(1 << n) if ((x >> i) & 1) == bit)


def is_critical(values):
    H, I, alphas = metrics(tuple(values))
    if I == 0:
        return False, []
    R = H / dec(I)
    rows = []
    for i, alpha in enumerate(alphas):
        if not alpha:
            continue
        child = (metrics(restrict(values, i, 0))[0] + metrics(restrict(values, i, 1))[0]) / 2
        delta = H - child
        rows.append((alpha, delta))
        if delta + TOL < R * dec(alpha):
            return False, rows
    return True, rows


def q_entropy(n):
    delta = Fraction(1, 1 << n)
    p0 = (1 - 2 * delta) ** 2
    p1 = 4 * delta * delta
    H = Decimal(0)
    for count, p in ((1, p0), ((1 << n) - 1, p1)):
        if p:
            x = dec(p)
            H -= count * x * x.ln() / LN2
    return H


def main():
    assertions = 0
    critical_counts = {}
    high_ratio_actual = 0
    threshold = Decimal(2) + Decimal(2) / LN2

    # Exhaust through three variables and use a deterministic bounded n=4 pilot.
    for n in range(1, 5):
        count = 0
        if n <= 3:
            masks = range(1 << (1 << n))
        else:
            masks = sorted({(k * 40503) % 65536 for k in range(4096)} |
                           {1, 2, 4, 8, 32768, 65534, 65533, 65531, 65527, 32767})
        for mask in masks:
            values = tuple(1 if (mask >> x) & 1 else -1 for x in range(1 << n))
            H, I, alphas = metrics(values)
            if not I:
                continue
            critical, rows = is_critical(values)
            if not critical:
                continue
            count += 1
            R = H / dec(I)
            for alpha, delta in rows:
                assert R <= envelope(alpha) + TOL
                assertions += 1
                if R > threshold:
                    high_ratio_actual += 1
                    assert alpha < Fraction(1, 2)
                    assert dec(alpha) <= Decimal(3).exp() * (Decimal(2) ** (-R)) + TOL
                    assertions += 2
        critical_counts[n] = count

    # Scalar envelope monotonicity and its explicit exponential inversion.
    previous = None
    for k in range(1, 10000):
        alpha = Fraction(k, 20000)
        value = envelope(alpha)
        if previous is not None:
            assert value < previous
            assertions += 1
        previous = value
        assert value <= -dec(alpha).ln() / LN2 + Decimal(3) / LN2 + TOL
        assertions += 1
        assert dec(alpha) <= Decimal(3).exp() * Decimal(2) ** (-value) + TOL
        assertions += 1

    # Genuine sparse prime-gate control: one-point defects are critical but
    # remain below the high-ratio threshold in the checked dimensions.
    q_rows = []
    for n in range(2, 61):
        Hn = q_entropy(n)
        Hchild = q_entropy(n - 1)
        alpha = Fraction(1, 1 << (n - 1))
        influence = n * alpha
        ratio = Hn / dec(influence)
        delta_H = Hn - Hchild / 2
        assert delta_H + TOL >= ratio * dec(alpha)
        assert ratio < threshold
        q_rows.append((n, ratio, delta_H / dec(alpha)))
        assertions += 2

    print("PASS")
    print(f"assertions={assertions}")
    print("randomness=NONE")
    print("entropy_arithmetic=decimal.Decimal 90-digit context")
    print("influence_arithmetic=fractions.Fraction")
    print("critical_counts=" + ",".join(f"n{n}:{c}" for n, c in critical_counts.items()))
    print(f"high_ratio_actual_coordinate_checks={high_ratio_actual}")
    print(f"threshold={threshold}")
    print(f"q_60_ratio={q_rows[-1][1]}")
    print(f"q_60_step_ratio={q_rows[-1][2]}")


if __name__ == "__main__":
    main()
