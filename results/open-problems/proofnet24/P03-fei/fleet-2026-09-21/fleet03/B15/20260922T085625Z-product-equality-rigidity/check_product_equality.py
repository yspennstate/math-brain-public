#!/usr/bin/env python3
import itertools
import math

TOL = 2e-10


def fwht_int(a):
    a = list(map(int, a))
    h = 1
    n = len(a)
    while h < n:
        for j in range(0, n, 2 * h):
            for i in range(j, j + h):
                x, y = a[i], a[i + h]
                a[i], a[i + h] = x + y, x - y
        h *= 2
    return a


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def entropy(p):
    return -sum(x * math.log2(x) for x in p if x > 0.0)


def solve_c(r):
    mu = sum(r)
    assert mu > 1.0 + 1e-12

    def F(c):
        prod = 1.0
        for x in r:
            prod *= 1.0 - c * x
        return 1.0 - c - prod

    if abs(F(1.0)) < 2e-13:
        return 1.0
    lo, hi = 1e-12, 1.0
    assert F(lo) > -1e-12 and F(hi) < 0.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if F(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def kocc_and_structure(f, n):
    N = 1 << n
    W = fwht_int(f)
    assert W[0] == 0
    P = [(w * w) / (N * N) for w in W]
    r = [
        sum(P[S] for S in range(N) if ((S >> i) & 1))
        for i in range(n)
    ]
    mu = sum(r)
    if abs(mu - 1.0) < 1e-12:
        hmax = entropy(r)
    else:
        c = solve_c(r)
        hmax = (sum(h2(c * x) for x in r) - h2(c)) / c
    kocc = hmax - entropy(P)

    types = []
    matches = True
    for x in r:
        if abs(x) < TOL:
            types.append(0)
        elif abs(x - 0.5) < TOL:
            types.append(1)
        elif abs(x - 1.0) < TOL:
            types.append(2)
        else:
            matches = False
            types.append(-1)

    if matches:
        Fmask = sum(1 << i for i, t in enumerate(types) if t == 2)
        Amask = sum(1 << i for i, t in enumerate(types) if t == 1)
        if Fmask == 0 or (Amask.bit_count() % 2):
            matches = False
        else:
            expected = []
            R = Amask
            while True:
                expected.append(Fmask | R)
                if R == 0:
                    break
                R = (R - 1) & Amask
            expected = set(expected)
            support = {S for S, p in enumerate(P) if p > 1e-15}
            if support != expected:
                matches = False
            elif any(abs(P[S] - 1.0 / len(expected)) > TOL for S in expected):
                matches = False

    return kocc, matches


def main():
    print("balanced equality stress test for PRODUCT-EQUALITY-RIGIDITY-v1")
    final_bad = 0
    for n in range(2, 5):
        N = 1 << n
        total = eq = bad = 0
        min_positive = None
        for neg in itertools.combinations(range(N), N // 2):
            f = [1] * N
            for x in neg:
                f[x] = -1
            total += 1
            kocc, matches = kocc_and_structure(f, n)
            if abs(kocc) < 2e-9:
                eq += 1
                if not matches:
                    bad += 1
            elif kocc > 0:
                if min_positive is None or kocc < min_positive:
                    min_positive = kocc
        final_bad += bad
        print(
            f"n={n} balanced={total} Kocc_zero={eq} "
            f"structure_mismatches={bad} min_positive_Kocc="
            + ("NONE" if min_positive is None else f"{min_positive:.16f}")
        )
    print("PASS" if final_bad == 0 else "FAIL")


if __name__ == "__main__":
    main()
