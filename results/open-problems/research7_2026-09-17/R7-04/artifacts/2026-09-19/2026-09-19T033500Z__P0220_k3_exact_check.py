from fractions import Fraction
from functools import lru_cache
from math import comb, factorial

MAX_TOTAL = 9


def shape_qr(q, r):
    return tuple([2] * q + [1] * r)


def hook_dim(shape):
    n = sum(shape)
    if n == 0:
        return 1
    hp = 1
    for i, row in enumerate(shape):
        for j in range(row):
            right = row - j - 1
            below = sum(1 for ii in range(i + 1, len(shape)) if shape[ii] > j)
            hp *= 1 + right + below
    return factorial(n) // hp


def skew_bruteforce(q, r, m):
    shape = shape_qr(q, r)
    cells = []
    for i, row in enumerate(shape, start=1):
        for j in range(1, row + 1):
            if j == 1 and i <= m:
                continue
            cells.append((i, j))
    idx = {c: h for h, c in enumerate(cells)}
    preds = [0] * len(cells)
    for c, h in idx.items():
        i, j = c
        for p in ((i - 1, j), (i, j - 1)):
            if p in idx:
                preds[h] |= 1 << idx[p]
    full = (1 << len(cells)) - 1

    @lru_cache(None)
    def count(mask):
        if mask == full:
            return 1
        total = 0
        for h in range(len(cells)):
            if ((mask >> h) & 1) == 0 and (preds[h] & ~mask) == 0:
                total += count(mask | (1 << h))
        return total

    return count(0)


def skew_ballot(q, r, m):
    d = 2 * q + r - m
    bad = q - m - 1
    reflected = comb(d, bad) if 0 <= bad <= d else 0
    return comb(d, q) - reflected


def closed_coefficients(max_total):
    # Coefficients C[m,d] in e^u P(X1>s,X2>t,X3>u)
    # with a=t-s, b=u-t: sum C[m,d] a^m b^d.
    out = {}
    for q in range(max_total // 2 + 1):
        for r in range(max_total - 2 * q + 1):
            n = 2 * q + r
            f = hook_dim(shape_qr(q, r))
            for m in range(q + r + 1):
                d = n - m
                g = skew_ballot(q, r, m)
                key = (m, d)
                out[key] = out.get(key, Fraction(0)) + Fraction(
                    f * g,
                    factorial(n) * factorial(m) * factorial(d),
                )
    return out


def brute_coefficients(max_total):
    out = {}
    for q in range(max_total // 2 + 1):
        for r in range(max_total - 2 * q + 1):
            n = 2 * q + r
            f = hook_dim(shape_qr(q, r))
            for m in range(q + r + 1):
                d = n - m
                g = skew_bruteforce(q, r, m)
                key = (m, d)
                out[key] = out.get(key, Fraction(0)) + Fraction(
                    f * g,
                    factorial(n) * factorial(m) * factorial(d),
                )
    return out


def coeff_i0_sq_minus_i1_sq(n):
    i0sq = sum(
        (Fraction(1, factorial(i) ** 2 * factorial(n - i) ** 2) for i in range(n + 1)),
        Fraction(0),
    )
    i1sq = Fraction(0)
    if n >= 1:
        for i in range(n):
            j = n - 1 - i
            i1sq += Fraction(
                1,
                factorial(i) * factorial(i + 1) * factorial(j) * factorial(j + 1),
            )
    return i0sq - i1sq


def main():
    checked_shapes = 0
    checked_skews = 0
    for q in range(MAX_TOTAL // 2 + 1):
        for r in range(MAX_TOTAL - 2 * q + 1):
            n = 2 * q + r
            exact = hook_dim(shape_qr(q, r))
            closed = factorial(n) * (r + 1) // (factorial(q) * factorial(q + r + 1))
            assert exact == closed, (q, r, exact, closed)
            checked_shapes += 1
            for m in range(q + r + 1):
                brute = skew_bruteforce(q, r, m)
                ballot = skew_ballot(q, r, m)
                assert brute == ballot, (q, r, m, brute, ballot)
                checked_skews += 1

    closed = closed_coefficients(MAX_TOTAL)
    brute = brute_coefficients(MAX_TOTAL)
    assert closed == brute

    for m in range(MAX_TOTAL + 1):
        # u=t => b=0, recovering e^{-t} I_0(2 sqrt(t-s)).
        assert closed.get((m, 0), Fraction(0)) == Fraction(1, factorial(m) ** 2)

    for n in range(MAX_TOTAL + 1):
        # s=t => a=0, recovering the k=3 one-time Bessel determinant.
        assert closed.get((0, n), Fraction(0)) == coeff_i0_sq_minus_i1_sq(n)

    print(f"MAX_TOTAL={MAX_TOTAL}")
    print(f"TWO_COLUMN_SHAPES_CHECKED={checked_shapes}")
    print(f"SKEW_SHAPES_CHECKED={checked_skews}")
    print(f"TRIPLE_COEFFICIENTS_CHECKED={len(closed)}")
    print("HOOK_DIMENSION_FORMULA=PASS")
    print("SKEW_BALLOT_FORMULA=PASS")
    print("NESTED_PARTITION_COEFFICIENT_MATCH=PASS")
    print("B0_REDUCTION_TO_K2_I0=PASS")
    print("A0_REDUCTION_TO_K3_BESSEL_DETERMINANT=PASS")
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
