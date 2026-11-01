#!/usr/bin/env python3
"""
Exact finite certificate for R7-06 / F0011 (Vu Conjecture 9.4).

Enumerates one representative of every diagonal-sign switching orbit of real
symmetric {+1,-1} matrices, for n <= 7, and classifies integral spectra with
integer arithmetic only.

No floating eigenvalue computation is used.

Correctness:
1. Every switching orbit has a unique representative with M[0,j]=+1 for j>0.
2. If all eigenvalues are integers then |lambda| <= n, sum lambda^2=n^2, and:
   n even -> every lambda is even;
   n odd  -> exactly one lambda is odd.
3. We enumerate all integer multisets satisfying these necessary constraints.
4. For n>=4, (p1,p3,p4) is an exact no-false-negative prefilter over that
   finite candidate list. Survivors are checked against p_k=tr(M^k), k=1..n.
   Newton identities imply equality of p_1,...,p_n is equality of the monic
   characteristic polynomial, so the matched candidate spectrum is exact.
5. All matrix powers use signed int64. For n<=7 and k<=n,
   |(M^k)_{ij}| <= n^(k-1) <= 7^6 = 117649, so overflow is impossible.
"""

from itertools import combinations_with_replacement
from collections import Counter
from fractions import Fraction
import numpy as np

EXPECTED = {
    1: (2, 2, 2),
    2: (4, 2, 2),
    3: (16, 10, 6),
    4: (128, 10, 5),
    5: (2048, 154, 14),
    6: (65536, 274, 14),
    7: (4194304, 15446, 44),
}


def candidate_spectra(n):
    out = []
    for lam in combinations_with_replacement(range(-n, n + 1), n):
        if sum(x * x for x in lam) != n * n:
            continue
        # char_M(x) mod 2 = char_J(x), because M == J mod 2.
        if n % 2 == 0:
            if any(x & 1 for x in lam):
                continue
        else:
            if sum(abs(x) & 1 for x in lam) != 1:
                continue
        # trace(M) is a sum of n signs.
        tr = sum(lam)
        if abs(tr) > n or ((tr - n) & 1):
            continue
        out.append(lam)
    return out


def power_sums(lam, n):
    return tuple(sum(x ** k for x in lam) for k in range(1, n + 1))


def key134(p1, p3, p4):
    # Collision-free on all values occurring for n<=7.
    return ((p1 + 20) * 10000 + (p3 + 5000)) * 50000 + p4


def normalized_batch(n, start, count):
    """Canonical orbit representatives with M[0,j]=+1 for j>0."""
    idx = np.arange(start, start + count, dtype=np.uint64)
    A = np.ones((count, n, n), dtype=np.int64)
    bit = 0
    for i in range(n):
        v = 2 * ((idx >> np.uint64(bit)) & 1).astype(np.int64) - 1
        A[:, i, i] = v
        bit += 1
    for i in range(1, n):
        for j in range(i + 1, n):
            v = 2 * ((idx >> np.uint64(bit)) & 1).astype(np.int64) - 1
            A[:, i, j] = v
            A[:, j, i] = v
            bit += 1
    assert bit == n + (n - 1) * (n - 2) // 2
    return A


def enumerate_n(n, batch=65536):
    assert n <= 7
    assert n ** (n - 1) < 2 ** 62

    candidates = candidate_spectra(n)
    by_powers = {power_sums(lam, n): lam for lam in candidates}

    free_bits = n + (n - 1) * (n - 2) // 2
    total = 1 << free_bits
    integral_count = 0
    spectrum_counts = Counter()
    prefilter_count = 0

    if n < 4:
        for start in range(0, total, batch):
            b = min(batch, total - start)
            A = normalized_batch(n, start, b)
            P = A.copy()
            traces = [np.trace(P, axis1=1, axis2=2)]
            for _k in range(2, n + 1):
                P = P @ A
                traces.append(np.trace(P, axis1=1, axis2=2))
            for j in range(b):
                ps = tuple(int(traces[k][j]) for k in range(n))
                lam = by_powers.get(ps)
                if lam is not None:
                    integral_count += 1
                    spectrum_counts[lam] += 1
    else:
        key_to_lam = {}
        key_to_powers = {}
        for lam in candidates:
            ps = power_sums(lam, n)
            key = key134(ps[0], ps[2], ps[3])
            # Direct finite check: p1,p3,p4 uniquely identify candidate list.
            assert key not in key_to_lam
            key_to_lam[key] = lam
            key_to_powers[key] = ps
        candidate_keys = np.array(list(key_to_lam), dtype=np.int64)

        for start in range(0, total, batch):
            b = min(batch, total - start)
            A = normalized_batch(n, start, b)
            A2 = A @ A
            A3 = A2 @ A
            A4 = A2 @ A2
            p1 = np.trace(A, axis1=1, axis2=2)
            p3 = np.trace(A3, axis1=1, axis2=2)
            p4 = np.trace(A4, axis1=1, axis2=2)
            keys = key134(p1, p3, p4)
            mask = np.isin(keys, candidate_keys)
            inds = np.flatnonzero(mask)
            prefilter_count += len(inds)
            if not len(inds):
                continue

            As = A[inds]
            P = A4[inds]
            traces = {
                1: p1[inds],
                2: np.full(len(inds), n * n, dtype=np.int64),
                3: p3[inds],
                4: p4[inds],
            }
            for k in range(5, n + 1):
                P = P @ As
                traces[k] = np.trace(P, axis1=1, axis2=2)

            for j, key0 in enumerate(keys[inds]):
                key = int(key0)
                expected = key_to_powers[key]
                if all(
                    int(traces[k][j]) == expected[k - 1]
                    for k in range(1, n + 1)
                ):
                    integral_count += 1
                    spectrum_counts[key_to_lam[key]] += 1

    assert (total, integral_count, len(spectrum_counts)) == EXPECTED[n]
    return {
        "n": n,
        "total": total,
        "arithmetic_candidates": len(candidates),
        "prefilter": prefilter_count,
        "integral": integral_count,
        "realized_spectra": len(spectrum_counts),
        "probability": Fraction(integral_count, total),
        "spectrum_counts": spectrum_counts,
    }


def main():
    print("n total candidates prefilter integral spectra probability")
    results = {}
    for n in range(1, 8):
        r = enumerate_n(n)
        results[n] = r
        print(
            n,
            r["total"],
            r["arithmetic_candidates"],
            r["prefilter"] if n >= 4 else "-",
            r["integral"],
            r["realized_spectra"],
            r["probability"],
        )

    print("\nn=7 spectrum counts:")
    for lam, count in sorted(results[7]["spectrum_counts"].items()):
        print(f"{count:5d}  {lam}")


if __name__ == "__main__":
    main()
