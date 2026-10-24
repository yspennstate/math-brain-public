"""Reproducible checks for PROB20-19 partition-law reduction.

This is a self-review artifact, not an independent proof.

Checks:
  1. Exact symbolic formulas for the universal top-two stochastic facet.
  2. Exact symbolic quintic top-three gap reduction used for r>=18.
  3. Brute polynomial checks that even coefficients of powers of random PSD
     quadratic forms are nonnegative for ranks > 2 as predicted by the
     Gaussian coefficient theorem.
  4. Exact normalization of the partition law for random projections.
  5. Empirical dominance checks for partition laws at k<=6 (evidence only).
  6. Reproduction of the diagonal-only obstruction at rank 10, p=15,
     seed 10000.

Requires numpy and sympy.
"""
from __future__ import annotations

import collections
import itertools
import math
from typing import Dict, Iterable, Tuple

import numpy as np
import sympy as sp


Exponent = Tuple[int, ...]
Partition = Tuple[int, ...]


def random_projection(p: int, r: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    a = rng.normal(size=(p, r))
    q, _ = np.linalg.qr(a)
    return q @ q.T


def q_polynomial(P: np.ndarray) -> Dict[Exponent, float]:
    p = P.shape[0]
    out: Dict[Exponent, float] = {}
    for i in range(p):
        e = [0] * p
        e[i] = 2
        out[tuple(e)] = float(P[i, i])
        for j in range(i + 1, p):
            e = [0] * p
            e[i] = e[j] = 1
            out[tuple(e)] = float(2.0 * P[i, j])
    return out


def multiply(a: Dict[Exponent, float], b: Dict[Exponent, float]) -> Dict[Exponent, float]:
    out = collections.defaultdict(float)
    for ea, ca in a.items():
        for eb, cb in b.items():
            out[tuple(x + y for x, y in zip(ea, eb))] += ca * cb
    return dict(out)


def polynomial_power(P: np.ndarray, k: int) -> Dict[Exponent, float]:
    p = P.shape[0]
    poly: Dict[Exponent, float] = {(0,) * p: 1.0}
    q = q_polynomial(P)
    for _ in range(k):
        poly = multiply(poly, q)
    return poly


def partition_weights(P: np.ndarray, k: int) -> Dict[Partition, float]:
    out = collections.defaultdict(float)
    for exp, coeff in polynomial_power(P, k).items():
        if all(e % 2 == 0 for e in exp):
            lam = tuple(sorted((e // 2 for e in exp if e), reverse=True))
            out[lam] += coeff
    return dict(out)


def partitions(n: int, max_part: int | None = None) -> Iterable[Partition]:
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def odd_double_factorial_for_part(m: int) -> int:
    ans = 1
    for j in range(1, m + 1):
        ans *= 2 * j - 1
    return ans


def c_lambda(lam: Partition) -> int:
    ans = 1
    for m in lam:
        ans *= odd_double_factorial_for_part(m)
    return ans


def falling(r: int, ell: int) -> int:
    ans = 1
    for j in range(ell):
        ans *= r - j
    return ans


def coordinate_weight(lam: Partition, r: int) -> float:
    ell = len(lam)
    if ell > r:
        return 0.0
    mult = collections.Counter(lam)
    assignments = falling(r, ell)
    for count in mult.values():
        assignments /= math.factorial(count)
    coeff = math.factorial(sum(lam))
    for m in lam:
        coeff /= math.factorial(m)
    return assignments * coeff


def T_rk(r: int, k: int) -> int:
    ans = 1
    for j in range(k):
        ans *= r + 2 * j
    return ans


def majorizes(a: Partition, b: Partition) -> bool:
    L = max(len(a), len(b))
    aa = list(a) + [0] * (L - len(a))
    bb = list(b) + [0] * (L - len(b))
    return all(sum(aa[:j]) >= sum(bb[:j]) for j in range(1, L + 1))


def all_upper_sets(ps: list[Partition]) -> list[list[Partition]]:
    out = []
    for mask in range(1 << len(ps)):
        S = [ps[i] for i in range(len(ps)) if (mask >> i) & 1]
        Sset = set(S)
        ok = True
        for x in S:
            for y in ps:
                if majorizes(y, x) and y not in Sset:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(S)
    return out


def elementary(xs: np.ndarray, m: int) -> float:
    if m == 0:
        return 1.0
    ans = 0.0
    for inds in itertools.combinations(range(len(xs)), m):
        prod = 1.0
        for i in inds:
            prod *= float(xs[i])
        ans += prod
    return ans


def symbolic_checks() -> None:
    k, r, x = sp.symbols("k r x", positive=True)
    A = k * (r + 2 * k - 2)
    B = (k - 1) * (2 * k - 1)
    endpoint = sp.expand((k - 2) * A - (k - 1) * B)
    assert sp.factor(endpoint) == k**2 * r - k**2 - 2 * k * r + 1

    # Quintic top-three bound reduction.
    r = sp.symbols("r", positive=True)
    S2, S3, S4, S5 = sp.symbols("S2 S3 S4 S5")
    d2, d3, d4, d5 = sp.symbols("d2 d3 d4 d5")
    WA = S5
    WB = 5 * (r + 8) * S4 - 45 * S5
    WC_ub = 10 * S2 * S3 + 200 * S3 - 280 * S4 + 70 * S5
    coord = 945 * r + 105 * 5 * r * (r - 1) + 45 * 10 * r * (r - 1)
    gap = sp.expand(coord - (945 * WA + 105 * WB + 45 * WC_ub))
    reduced = sp.expand(gap.subs({S2: r-d2, S3: r-d3, S4: r-d4, S5: r-d5}) / 15)
    target = (
        30 * r * (d2 + d3)
        - 30 * d2 * d3
        + 600 * d3
        + (35 * r - 560) * d4
        - 42 * d5
    )
    assert sp.simplify(reduced - target) == 0
    print("symbolic formulas: PASS")


def coefficient_positivity_checks() -> None:
    # Includes rank > 2, beyond the previous rank-two theorem.
    for p, r, k, seed in [(5, 3, 3, 101), (5, 4, 4, 102), (6, 3, 4, 103)]:
        P = random_projection(p, r, seed)
        poly = polynomial_power(P, k)
        evens = [c for e, c in poly.items() if all(v % 2 == 0 for v in e)]
        minimum = min(evens)
        assert minimum > -1e-9, (p, r, k, minimum)
    print("arbitrary-rank even coefficient checks: PASS")


def partition_law_checks() -> None:
    for k in [4, 5, 6]:
        ps = list(partitions(k))
        uppers = all_upper_sets(ps)
        for r in [2, 3, 4]:
            p = max(7, r + 2)
            for seed in range(5):
                P = random_projection(p, r, 10000 + 1000*k + 100*r + seed)
                W = partition_weights(P, k)
                total = T_rk(r, k)
                pi = {lam: c_lambda(lam) * W.get(lam, 0.0) / total for lam in ps}
                pic = {lam: c_lambda(lam) * coordinate_weight(lam, r) / total for lam in ps}
                assert abs(sum(pi.values()) - 1.0) < 1e-8
                assert abs(sum(pic.values()) - 1.0) < 1e-12

                # Empirical only: no violation found in this small bank.
                for U in uppers:
                    lhs = sum(pic[lam] for lam in U)
                    rhs = sum(pi[lam] for lam in U)
                    assert lhs + 2e-8 >= rhs, (k, r, seed, U, lhs, rhs)
    print("empirical partition stochastic-dominance bank: PASS (evidence only)")


def diagonal_shortcut_obstruction() -> None:
    p, r, seed = 15, 10, 10000
    P = random_projection(p, r, seed)
    d = np.diag(P)
    H = 3 * r * elementary(d, 4) - 13 * elementary(d, 5)
    coord = 3 * r * math.comb(r, 4) - 13 * math.comb(r, 5)
    print(f"diagonal shortcut example: H={H:.12f}, coordinate={coord:.12f}")
    assert H < coord


if __name__ == "__main__":
    symbolic_checks()
    coefficient_positivity_checks()
    partition_law_checks()
    diagonal_shortcut_obstruction()
