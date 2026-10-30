#!/usr/bin/env python3
"""Independent stress checker for B15 packet-minority KL identities.

Uses only exact integer Walsh transforms for grouping magnitude packets; logarithmic
comparisons are evaluated in float64 through Python's math module.  Finite checks are
not a proof of the universal theorem.
"""

from __future__ import annotations

import json
import math


def fwht_int(vals: list[int]) -> list[int]:
    a = vals[:]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def h2(q: float) -> float:
    if q <= 0.0 or q >= 1.0:
        return 0.0
    return -q * math.log2(q) - (1.0 - q) * math.log2(1.0 - q)


def coordinate_stats(w: list[int], n: int, i: int) -> dict[str, float | int]:
    N = 1 << n
    denom = float(N * N)
    p = [(z * z) / denom for z in w]
    bit = 1 << i

    groups: dict[tuple[int, int], list[float]] = {}
    M = W = delta = 0.0

    for s in range(N):
        if s & bit:
            continue
        x, y = p[s], p[s | bit]
        m = x + y
        b = min(x, y)
        if m == 0.0:
            continue

        q = b / m
        j = 1.0 - h2(0.5 + math.sqrt(q * (1.0 - q))) if q > 0.0 else 0.0
        delta += m * (h2(q) + j)

        if b > 0.0:
            M += b
            W += 0.5 * b * math.log2(m / (2.0 * b))

        key = tuple(sorted((abs(w[s]), abs(w[s | bit]))))
        pair_mass, minority_mass = groups.get(key, [0.0, 0.0])
        groups[key] = [pair_mass + m, minority_mass + b]

    if M > 0.0:
        D = 0.0
        for pair_mass, minority_mass in groups.values():
            if minority_mass == 0.0:
                continue
            mu = minority_mass / M
            pi = pair_mass
            D += mu * math.log2(mu / pi)
        rhs = M * (math.log2(1.0 / (2.0 * M)) - D)
    else:
        D = rhs = 0.0

    c0 = 1.0 + 3.0 / math.log(2.0)
    return {
        "M": M,
        "W": W,
        "packet_KL_bits": D,
        "two_W": 2.0 * W,
        "packet_identity_rhs": rhs,
        "packet_identity_abs_error": abs(2.0 * W - rhs),
        "restriction_delta": delta,
        "upper_bound_violation": max(0.0, delta - (2.0 * W + c0 * M)),
        "packet_pair_classes": len(groups),
    }


def exhaustive_through_n4() -> dict[str, object]:
    max_identity_error = 0.0
    max_upper_violation = 0.0
    max_W_over_J: dict[str, float] = {}
    counts: dict[str, int] = {}

    for n in range(1, 5):
        N = 1 << n
        max_ratio = 0.0
        count = 0
        for mask in range(1 << N):
            vals = [1 if (mask >> x) & 1 else -1 for x in range(N)]
            w = fwht_int(vals)
            coords = [coordinate_stats(w, n, i) for i in range(n)]
            max_identity_error = max(
                max_identity_error,
                max(float(c["packet_identity_abs_error"]) for c in coords),
            )
            max_upper_violation = max(
                max_upper_violation,
                max(float(c["upper_bound_violation"]) for c in coords),
            )

            p = [(z * z) / float(N * N) for z in w]
            folded = []
            for i in range(n):
                inf_i = sum(p[s] for s in range(N) if s & (1 << i))
                folded.append(min(inf_i, 1.0 - inf_i))
            J = sum(folded)
            Wsum = sum(float(c["W"]) for c in coords)
            if J > 1e-15:
                max_ratio = max(max_ratio, Wsum / J)
            count += 1

        counts[str(n)] = count
        max_W_over_J[str(n)] = max_ratio

    return {
        "truth_tables_by_n": counts,
        "truth_tables_total": sum(counts.values()),
        "max_packet_identity_abs_error": max_identity_error,
        "max_upper_bound_violation": max_upper_violation,
        "max_W_over_J_by_n": max_W_over_J,
    }


def one_point(n: int) -> dict[str, float | int]:
    N = 1 << n
    vals = [1] + [-1] * (N - 1)
    w = fwht_int(vals)
    c = coordinate_stats(w, n, 0)
    M = float(c["M"])
    twoW = float(c["two_W"])
    positive = M * math.log2(1.0 / (2.0 * M)) if M else 0.0
    return {
        "n": n,
        "N": N,
        "M_i": M,
        "packet_KL_bits": float(c["packet_KL_bits"]),
        "positive_normalizer": positive,
        "two_W_i": twoW,
        "positive_over_two_W": positive / twoW if twoW else float("inf"),
        "packet_pair_classes": int(c["packet_pair_classes"]),
        "identity_abs_error": float(c["packet_identity_abs_error"]),
    }


def width_two_tribes(m: int) -> dict[str, float | int]:
    n = 2 * m
    N = 1 << n
    vals = []
    for x in range(N):
        truth = any(
            ((x >> (2 * b)) & 1) and ((x >> (2 * b + 1)) & 1)
            for b in range(m)
        )
        vals.append(1 if truth else -1)
    w = fwht_int(vals)
    c = coordinate_stats(w, n, 0)
    p = [(z * z) / float(N * N) for z in w]
    inf = sum(p[s] for s in range(N) if s & 1)
    q = min(inf, 1.0 - inf)
    M = float(c["M"])
    return {
        "m": m,
        "n": n,
        "M_i": M,
        "folded_influence_q_i": q,
        "M_over_q": M / q if q else 0.0,
        "W_over_q": float(c["W"]) / q if q else 0.0,
        "packet_KL_bits": float(c["packet_KL_bits"]),
        "log_1_over_2M": math.log2(1.0 / (2.0 * M)) if M else 0.0,
        "two_W_over_M": float(c["two_W"]) / M if M else 0.0,
        "packet_pair_classes": int(c["packet_pair_classes"]),
    }


def main() -> None:
    result = {
        "status": "finite stress checks only; not a proof of FEI",
        "exhaustive": exhaustive_through_n4(),
        "one_point": [one_point(n) for n in (3, 4, 8, 12, 20)],
        "width_two_tribes": [width_two_tribes(m) for m in range(2, 9)],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
