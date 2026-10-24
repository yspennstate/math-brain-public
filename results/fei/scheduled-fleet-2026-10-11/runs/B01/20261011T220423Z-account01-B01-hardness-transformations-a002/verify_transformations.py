#!/usr/bin/env python3
"""Deterministic finite audit of the A002 Boolean transformation ledger.

Universal statements are proved analytically in REPORT.md.  This script checks
the exact truth-table/FWHT identities on every nonconstant sign table through
dimension three, plus the odd-negative-count full-support lemma through n=4.
"""

from itertools import product
from math import log2


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def metrics(vals):
    N = len(vals)
    n = N.bit_length() - 1
    w = fwht(vals)
    probs = [(z / N) ** 2 for z in w]
    H = -sum(q * log2(q) for q in probs if q)
    I = sum(q * s.bit_count() for s, q in enumerate(probs))
    mean = sum(vals) / N
    infs = []
    for i in range(n):
        bit = 1 << i
        infs.append(sum(vals[x] != vals[x ^ bit] for x in range(N)) / N)
    return H, I, mean, infs, w


def tensor(f, g):
    return [a * b for a in f for b in g]


def dictator_balance(f):
    return f + [-x for x in f]


def two_cell_selector(g):
    out = []
    for y1, y2 in product((1, -1), repeat=2):
        out.extend([y1 if x == 1 else y2 for x in g])
    return out


def activate(g, r):
    out = []
    for z in product((1, -1), repeat=r):
        out.extend(g if all(x == 1 for x in z) else [1] * len(g))
    return out


def parity_lift(g):
    n = len(g).bit_length() - 1
    out = []
    for z in (1, -1):
        for x in range(1 << n):
            # Multiplying every physical sign by z complements every bit if z=-1.
            y = x if z == 1 else x ^ ((1 << n) - 1)
            out.append(g[y])
    return out


def phi(x):
    return 0.0 if x == 0 else x * log2(1 / x)


def close(a, b, tol=2e-11):
    assert abs(a - b) <= tol, (a, b, abs(a - b))


def main():
    function_count = 0
    identity_checks = 0
    max_error = 0.0
    for n in range(1, 4):
        N = 1 << n
        for bits in range(1, (1 << N) - 1):
            g = [1 if (bits >> x) & 1 else -1 for x in range(N)]
            Hg, Ig, mu, infs, _ = metrics(g)
            function_count += 1

            # Tensor square.
            t = tensor(g, g)
            Ht, It, mut, _, _ = metrics(t)
            for a, b in ((Ht, 2 * Hg), (It, 2 * Ig), (mut, mu * mu)):
                max_error = max(max_error, abs(a - b)); close(a, b); identity_checks += 1

            # Dictator balance and then the balanced two-cell selector.
            b = dictator_balance(g)
            Hb, Ib, mub, _, _ = metrics(b)
            for a, c in ((Hb, Hg), (Ib, Ig + 1), (mub, 0)):
                max_error = max(max_error, abs(a - c)); close(a, c); identity_checks += 1
            M = two_cell_selector(b)
            HM, IM, muM, _, _ = metrics(M)
            for a, c in ((HM, 2 + Hb / 2), (IM, 1 + Ib / 2), (muM, 0)):
                max_error = max(max_error, abs(a - c)); close(a, c); identity_checks += 1

            # Sparse activation at r=1,2, including the arbitrary-mean formula.
            for r in (1, 2):
                p = 2 ** (-r)
                F = activate(g, r)
                HF, IF, muF, infF, _ = metrics(F)
                expected_H = (
                    p * (Hg - phi(mu * mu))
                    + 2 * r * p * (1 - mu * mu)
                    + (2**r - 1) * phi(p * p * (1 - mu) ** 2)
                    + phi((1 - p + p * mu) ** 2)
                )
                expected_I = p * (Ig + r * (1 - mu))
                for a, c in ((HF, expected_H), (IF, expected_I), (muF, 1 - p + p * mu)):
                    max_error = max(max_error, abs(a - c)); close(a, c); identity_checks += 1
                # Physical coordinate costs: data p*Inf_i(g), controls p(1-mu).
                for a, c in zip(infF[:n], [p * x for x in infs]):
                    max_error = max(max_error, abs(a - c)); close(a, c); identity_checks += 1
                for a in infF[n:]:
                    max_error = max(max_error, abs(a - p * (1 - mu)))
                    close(a, p * (1 - mu)); identity_checks += 1

            # Parity lift: spectral masses are relabelled; influence gains odd-level mass.
            P = parity_lift(g)
            HP, IP, muP, _, _ = metrics(P)
            _, _, _, _, wg = metrics(g)
            odd_mass = sum((z / N) ** 2 for s, z in enumerate(wg) if s.bit_count() % 2)
            for a, c in ((HP, Hg), (IP, Ig + odd_mass), (muP, mu)):
                max_error = max(max_error, abs(a - c)); close(a, c); identity_checks += 1

    # Odd number of negative truth values gives full unnormalized Walsh support.
    full_support_tables = 0
    for n in range(2, 5):
        N = 1 << n
        for bits in range(1 << N):
            neg = bits.bit_count()
            if neg % 2:
                vals = [-1 if (bits >> x) & 1 else 1 for x in range(N)]
                assert all(z != 0 for z in fwht(vals))
                full_support_tables += 1

    print("status=PASS")
    print(f"nonconstant_functions_checked={function_count}")
    print(f"identity_checks={identity_checks}")
    print(f"odd_negative_full_support_tables_checked={full_support_tables}")
    print(f"max_abs_error={max_error:.3e}")
    print("random_seed=None")
    print("scope=finite corroboration; all-dimensional proofs are in REPORT.md")


if __name__ == "__main__":
    main()
