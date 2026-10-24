"""Reproduce account03/B13 zeta-Palm cancellation calculations.

Scope: numerical/exact support checks for a new FEI cancellation-elimination route.
This script does NOT prove full FEI.  It reconstructs Numaro's published n=18
seed from the already archived factual slices, verifies its published table hash,
and computes cancellation increments.  The exhaustive n<=4 search is over all
Boolean truth tables modulo global sign and all coordinate projections.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
import math
import numpy as np

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
    (TOP, BOT),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
    ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00", "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
    ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
    ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]


def fwht_int(v: np.ndarray) -> np.ndarray:
    a = np.asarray(v, dtype=np.int64).copy()
    h = 1
    while h < len(a):
        z = a.reshape(-1, 2 * h)
        x = z[:, :h].copy()
        y = z[:, h:].copy()
        z[:, :h] = x + y
        z[:, h:] = x - y
        h *= 2
    return a


def fwht_float(v: np.ndarray) -> np.ndarray:
    return fwht_int(np.asarray(v, dtype=np.int64)).astype(np.float64) / len(v)


def zeta(v: np.ndarray, n: int) -> np.ndarray:
    u = np.asarray(v, dtype=np.float64).copy()
    for i in range(n):
        h = 1 << i
        z = u.reshape(-1, 2 * h)
        z[:, :h] += z[:, h:]
    return u


def bcan(v: np.ndarray, n: int) -> float:
    u = zeta(v, n)
    keep = v > 0
    return float(np.sum(v[keep] * np.log2(u[keep] / v[keep])))


def remove_coordinate(v: np.ndarray, n: int, i: int) -> np.ndarray:
    h = 1 << i
    z = v.reshape(-1, 2 * h)
    return (z[:, :h] + z[:, h:]).reshape(-1)


def influence_from_law(v: np.ndarray, n: int, i: int) -> float:
    h = 1 << i
    return float(v.reshape(-1, 2 * h)[:, h:].sum())


def project(v: np.ndarray, n: int, mask: int) -> tuple[np.ndarray, list[int]]:
    labels = [i for i in range(n) if (mask >> i) & 1]
    out = np.zeros(1 << len(labels), dtype=np.float64)
    for s, mass in enumerate(v):
        t = 0
        for j, i in enumerate(labels):
            if (s >> i) & 1:
                t |= 1 << j
        out[t] += mass
    return out, labels


def local_increment(v: np.ndarray, n: int, i: int) -> tuple[float, float, float]:
    alpha = influence_from_law(v, n, i)
    if alpha == 0:
        return 0.0, 0.0, 0.0
    d = bcan(v, n) - bcan(remove_coordinate(v, n, i), n - 1)
    return d, alpha, d / alpha


def boolean_spectrum(table: list[int]) -> np.ndarray:
    a = fwht_float(np.asarray(table, dtype=np.int64))
    return a * a


def exhaustive_small_boolean() -> dict[int, dict[str, object]]:
    """All Boolean functions modulo global sign, all nonempty projections."""
    ans = {}
    for n in range(1, 5):
        N = 1 << n
        best = (-1.0, None)
        best_bottleneck = (-1.0, None)
        for code in range(1 << (N - 1)):
            table = [-1] + [1 if (code >> (j - 1)) & 1 else -1 for j in range(1, N)]
            p = boolean_spectrum(table)
            # Cache every projection and Bcan.
            pv = {0: np.array([1.0])}
            bc = {0: 0.0}
            bits = {0: []}
            for R in range(1, 1 << n):
                pv[R], bits[R] = project(p, n, R)
                bc[R] = bcan(pv[R], len(bits[R]))
            alpha = [sum(p[s] for s in range(N) if (s >> i) & 1) for i in range(n)]
            d = {}
            for R in range(1, 1 << n):
                for i in bits[R]:
                    if alpha[i] > 0:
                        ratio = (bc[R] - bc[R ^ (1 << i)]) / alpha[i]
                        d[R, i] = ratio
                        if ratio > best[0]:
                            best = (ratio, (table[:], R, i))
            # Exact finite DP for the minimum possible maximum increment ratio
            # along a coordinate-elimination order.
            memo = {0: (0.0, [])}
            for size in range(1, n + 1):
                for R in range(1, 1 << n):
                    if R.bit_count() != size:
                        continue
                    choices = []
                    for i in bits[R]:
                        prev, path = memo[R ^ (1 << i)]
                        rr = d.get((R, i), 0.0)
                        choices.append((max(rr, prev), [i] + path))
                    memo[R] = min(choices, key=lambda x: x[0])
            val, path = memo[(1 << n) - 1]
            if val > best_bottleneck[0]:
                best_bottleneck = (val, (table[:], path))
        ans[n] = {
            "max_any_projection_increment_ratio": best[0],
            "max_witness_truth_table": best[1][0],
            "max_witness_projection_mask": best[1][1],
            "max_witness_coordinate": best[1][2],
            "worst_optimal_bottleneck": best_bottleneck[0],
            "bottleneck_witness_truth_table": best_bottleneck[1][0],
            "one_optimal_order": best_bottleneck[1][1],
        }
    return ans


def arbitrary_law_example() -> dict[str, object]:
    """Exact-support arbitrary subset law with a large local increment.

    X has m=3 coordinates. q is Bernoulli(theta)^3 and conditional inclusion
    of the new coordinate has r_A=c*t^|A|.  This is a valid random-set law,
    but the returned shift-edge dominance proves it cannot be Boolean-spectral.
    """
    m = 3
    theta = Fraction(1, 16)
    t = 9
    c = Fraction(1, 72900)
    q = []
    r = []
    for A in range(1 << m):
        k = A.bit_count()
        q.append(theta**k * (1 - theta) ** (m - k))
        r.append(c * t**k)
    qf = np.array([float(x) for x in q])
    rf = np.array([float(x) for x in r])
    b = qf * rf
    U = zeta(qf, m)
    V = zeta(b, m)
    alpha = float(b.sum())
    d = 0.0
    for A in range(1 << m):
        rr = rf[A]
        bar = V[A] / U[A]
        if rr < 1:
            d += qf[A] * (1 - rr) * math.log2(1 / (1 - rr))
        if rr > 0:
            d += qf[A] * rr * math.log2(bar / rr)
    weights = [float(q[A]) * math.sqrt(float(r[A] * (1 - r[A]))) for A in range(1 << m)]
    # Exact sufficient proof of dominance: rest <= sqrt(c)[(9/8)^3-(15/16)^3].
    lhs_sq_factor = Fraction(3375, 4096) ** 2 * (1 - c)
    rhs_sq_factor = Fraction(2457, 4096) ** 2
    assert lhs_sq_factor > rhs_sq_factor
    return {
        "alpha_exact": "1/21600",
        "increment_ratio": d / alpha,
        "shift_edge_empty_weight": weights[0],
        "shift_edge_sum_other_weights": sum(weights[1:]),
        "exact_dominance_check": True,
    }


def negative_association_witness() -> dict[str, object]:
    table = [-1, 1, 1, -1, -1, -1, -1, -1]
    p = boolean_spectrum(table)
    support = [(s, p[s]) for s in range(8) if p[s] > 0]
    a0 = sum(p[s] for s in range(8) if s & 1)
    a1 = sum(p[s] for s in range(8) if s & 2)
    a01 = sum(p[s] for s in range(8) if (s & 1) and (s & 2))
    return {
        "truth_table": table,
        "spectral_support": [(s, float(x)) for s, x in support],
        "P0": float(a0),
        "P1": float(a1),
        "P01": float(a01),
        "covariance": float(a01 - a0 * a1),
    }


def reconstruct_numaro() -> np.ndarray:
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    assert all((m & base) == 0 and m.bit_count() == 2 for m in masks)
    hosts = [[x for x in range(512) if (m >> x) & 1] for m in masks]
    core = np.array([-1 if (base >> x) & 1 else 1 for x in range(512)], dtype=np.int64)
    table = np.tile(core, (1 << len(hosts), 1))
    for j, cells in enumerate(hosts):
        rows = (np.arange(1 << len(hosts)) & (1 << j)) != 0
        table[np.ix_(rows, np.asarray(cells, dtype=int))] = -1
    table = table.ravel()
    digest = hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()
    assert digest == EXPECTED_SHA
    return table


def numaro_projection_test() -> dict[str, object]:
    table = reconstruct_numaro()
    W = fwht_int(table)
    assert int(np.dot(W, W)) == len(table) ** 2
    p = (W.astype(np.float64) / len(table)) ** 2
    bc0 = bcan(p, 18)
    full = [local_increment(p, 18, i)[2] for i in range(18)]

    # Deliberately bad order: delete the nine auxiliary coordinates first.
    cur = p.copy()
    labels = list(range(18))
    aux_first = []
    for target in range(9, 18):
        pos = labels.index(target)
        d, alpha, ratio = local_increment(cur, len(labels), pos)
        aux_first.append((target, ratio, alpha, d))
        cur = remove_coordinate(cur, len(labels), pos)
        labels.pop(pos)

    # Greedy constructive diagnostic: at each stage remove the currently
    # smallest normalized increment.  This is evidence, not a theorem.
    cur = p.copy()
    labels = list(range(18))
    greedy = []
    while labels:
        candidates = []
        for pos, lab in enumerate(labels):
            d, alpha, ratio = local_increment(cur, len(labels), pos)
            candidates.append((ratio, pos, lab, alpha, d))
        ratio, pos, lab, alpha, d = min(candidates)
        greedy.append((lab, ratio, alpha, d))
        cur = remove_coordinate(cur, len(labels), pos)
        labels.pop(pos)

    return {
        "published_truth_table_sha256": EXPECTED_SHA,
        "Bcan": bc0,
        "I_exact": "261/128",
        "Bcan_over_I": bc0 / (261 / 128),
        "max_full_state_coordinate_ratio": max(full),
        "auxiliary_first_ratios": [x[1] for x in aux_first],
        "auxiliary_first_first_ratio_above_2_323994990262647": next((x for x in aux_first if x[1] > 2.323994990262647), None),
        "auxiliary_first_max_ratio": max(x[1] for x in aux_first),
        "greedy_min_max_ratio": max(x[1] for x in greedy),
        "greedy_min_order": [x[0] for x in greedy],
    }


def main() -> None:
    import json
    out = {
        "small_boolean_exhaustive": exhaustive_small_boolean(),
        "arbitrary_law_example": arbitrary_law_example(),
        "negative_association_witness": negative_association_witness(),
        "numaro_projection_test": numaro_projection_test(),
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
