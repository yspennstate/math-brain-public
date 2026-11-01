#!/usr/bin/env python3
"""Exact finite self-check for B13 affine-critical exchange constraints.

Standard library only.  Boolean functions are enumerated modulo global output sign
through dimension four.  All inequalities are checked with fractions / integers.
"""

from fractions import Fraction
from functools import lru_cache
import json
import math
import time


def vals_from_mask(n, mask):
    N = 1 << n
    vals = [1] * N
    for x in range(1, N):
        if (mask >> (x - 1)) & 1:
            vals[x] = -1
    return vals


def correlations(vals, n):
    N = 1 << n
    return [sum(vals[x] * vals[x ^ u] for x in range(N)) for u in range(N)]


def greedy_min_basis(C, n):
    """Minimum qtilde-weight vector-matroid basis; qtilde proportional to N-|C[u]|."""
    N = 1 << n
    candidates = sorted(range(1, N), key=lambda u: (N - abs(C[u]), u))
    basis = []
    pivots = {}
    for u in candidates:
        w = u
        for b in sorted(pivots, reverse=True):
            if (w >> b) & 1:
                w ^= pivots[b]
        if not w:
            continue
        pivots[w.bit_length() - 1] = w
        basis.append(u)
        if len(basis) == n:
            break
    assert len(basis) == n
    return basis


def folded_J(vals_tuple):
    vals = list(vals_tuple)
    if len(vals) == 1:
        return Fraction(0)
    n = (len(vals)).bit_length() - 1
    N = 1 << n
    C = correlations(vals, n)
    return sum(Fraction(N - abs(C[1 << i]), 2 * N) for i in range(n))


@lru_cache(None)
def iaff(vals_tuple):
    vals = list(vals_tuple)
    if len(vals) == 1:
        return Fraction(0)
    if vals[0] < 0:
        vals = [-v for v in vals]
    n = (len(vals)).bit_length() - 1
    N = 1 << n
    C = correlations(vals, n)
    B = greedy_min_basis(C, n)
    return sum((Fraction(N - abs(C[u]), 2 * N) for u in B), Fraction(0))


def minimizing_gauge(vals, n, basis, C):
    """Pull back along basis columns and orient each basis correlation positive."""
    N = 1 << n
    signs = [1 if C[u] < 0 else 0 for u in basis]
    out = [0] * N
    for y in range(N):
        x = 0
        phase = 0
        for i, u in enumerate(basis):
            if (y >> i) & 1:
                x ^= u
                phase ^= signs[i]
        out[y] = vals[x] * (-1 if phase else 1)
    return out


def restricted_tuple(g, n, A_mask, A_value):
    A = [i for i in range(n) if (A_mask >> i) & 1]
    B = [i for i in range(n) if not ((A_mask >> i) & 1)]
    out = []
    for yB in range(1 << len(B)):
        y = 0
        for t, i in enumerate(A):
            if (A_value >> t) & 1:
                y |= 1 << i
        for t, i in enumerate(B):
            if (yB >> t) & 1:
                y |= 1 << i
        out.append(g[y])
    if out[0] < 0:
        out = [-v for v in out]
    return tuple(out)


def witness(kind, n):
    N = 1 << n
    vals = []
    for x in range(N):
        if kind == "one_point":
            vals.append(-1 if x == 0 else 1)
        elif kind == "bent":
            assert n % 2 == 0
            q = 0
            for i in range(0, n, 2):
                q ^= ((x >> i) & 1) & ((x >> (i + 1)) & 1)
            vals.append(-1 if q else 1)
        else:
            raise ValueError(kind)
    C = correlations(vals, n)
    B = greedy_min_basis(C, n)
    p = [Fraction(N - abs(C[u]), 2 * N) for u in B]
    orient = [1 if C[u] >= 0 else -1 for u in B]
    d = [Fraction(0) for _ in B]
    for i in range(n):
        for j in range(i + 1, n):
            cij = orient[i] * orient[j] * C[B[i] ^ B[j]]
            pij = Fraction(N - abs(C[B[i]]) - abs(C[B[j]]) + cij, 4 * N)
            d[i] += pij
            d[j] += pij
    I = sum(p, Fraction(0))
    m = max(p)
    i = p.index(m)
    delta = float(d[i] / m) - 0.5 * math.log2(1 / float(m))
    cap = 0.5 * (float(I / m) - 1 - math.log2(1 / float(m)))
    return {
        "kind": kind,
        "n": n,
        "p": [f"{x.numerator}/{x.denominator}" for x in p],
        "I_aff": f"{I.numerator}/{I.denominator}",
        "m": f"{m.numerator}/{m.denominator}",
        "d_max": f"{d[i].numerator}/{d[i].denominator}",
        "delta_max": delta,
        "scalar_cap": cap,
    }


def main():
    start = time.time()
    counts = {
        "functions": 0,
        "all_parity_exchange": 0,
        "pair_interval": 0,
        "depth_cap": 0,
        "folded_restriction_drift": 0,
        "affine_restriction_drift": 0,
        "witness_equalities": 0,
    }

    for n in range(1, 5):
        N = 1 << n
        for mask in range(1 << (N - 1)):
            vals = vals_from_mask(n, mask)
            C = correlations(vals, n)
            B = greedy_min_basis(C, n)
            weights = [N - abs(C[u]) for u in B]
            p = [Fraction(w, 2 * N) for w in weights]

            for subset in range(1, 1 << n):
                v = 0
                max_w = 0
                for i, u in enumerate(B):
                    if (subset >> i) & 1:
                        v ^= u
                        max_w = max(max_w, weights[i])
                assert N - abs(C[v]) >= max_w
                counts["all_parity_exchange"] += 1

            orient = [1 if C[u] >= 0 else -1 for u in B]
            d = [Fraction(0) for _ in B]
            for i in range(n):
                for j in range(i + 1, n):
                    cij = orient[i] * orient[j] * C[B[i] ^ B[j]]
                    pij = Fraction(
                        N - abs(C[B[i]]) - abs(C[B[j]]) + cij, 4 * N
                    )
                    upper = min(p[i], p[j]) / 2
                    lower = max(
                        Fraction(0),
                        max(p[i], p[j]) + min(p[i], p[j]) / 2 - Fraction(1, 2),
                    )
                    assert lower <= pij
                    assert pij <= upper
                    counts["pair_interval"] += 2
                    d[i] += pij
                    d[j] += pij
            for i in range(n):
                cap = sum(
                    (min(p[i], p[k]) for k in range(n) if k != i), Fraction(0)
                ) / 2
                assert d[i] <= cap
                counts["depth_cap"] += 1

            g = minimizing_gauge(vals, n, B, C)
            parent = sum(p, Fraction(0))
            for A_mask in range(1, (1 << n) - 1):
                k = A_mask.bit_count()
                avg_J_child = Fraction(0)
                avg_Iaff_child = Fraction(0)
                for a in range(1 << k):
                    child = restricted_tuple(g, n, A_mask, a)
                    avg_J_child += folded_J(child)
                    avg_Iaff_child += iaff(child)
                avg_J_child /= 1 << k
                avg_Iaff_child /= 1 << k
                I_A = sum(
                    (p[i] for i in range(n) if (A_mask >> i) & 1), Fraction(0)
                )
                assert parent - avg_J_child >= I_A
                assert parent - avg_Iaff_child >= I_A
                counts["folded_restriction_drift"] += 1
                counts["affine_restriction_drift"] += 1

            counts["functions"] += 1

    witnesses = [
        witness("one_point", 4),
        witness("one_point", 8),
        witness("bent", 4),
        witness("bent", 8),
    ]
    for w in witnesses:
        assert abs(w["delta_max"] - w["scalar_cap"]) < 1e-12
        counts["witness_equalities"] += 1

    out = {
        "status": "PASS",
        "scope": "all Boolean functions modulo global output sign through n=4",
        "counts": counts,
        "total_checks": (
            counts["all_parity_exchange"]
            + counts["pair_interval"]
            + counts["depth_cap"]
            + counts["folded_restriction_drift"]
            + counts["affine_restriction_drift"]
            + counts["witness_equalities"]
        ),
        "witnesses": witnesses,
        "elapsed_seconds": time.time() - start,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
