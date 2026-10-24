#!/usr/bin/env python3
"""Finite diagnostic for the annealed upper-set envelope.

The proof in ANNEALED_UPPER_SET_ENVELOPE.tex is analytic and all-dimensional.
This script independently enumerates every Boolean truth table through n=4,
checks the Jensen envelope against literal physical restrictions, and checks
the coordinate chain decomposition.  It also reports fixed-n H/I maximizers.
"""

from __future__ import annotations

import math
from collections import defaultdict


TOL = 2.0e-11


def parity(x: int) -> int:
    return x.bit_count() & 1


def walsh_prob(vals: list[int], n: int) -> list[float]:
    size = 1 << n
    out = []
    for s in range(size):
        w = sum(vals[x] * (-1 if parity(s & x) else 1) for x in range(size))
        out.append((w / size) ** 2)
    return out


def metrics_from_prob(p: list[float]) -> tuple[float, float, float, float, float]:
    n = (len(p) - 1).bit_length()
    H = sum(-q * math.log2(q) for q in p if q > 0.0)
    I = sum(s.bit_count() * p[s] for s in range(1 << n))
    U = 0.0
    for a, q in enumerate(p):
        if q == 0.0:
            continue
        pi = sum(p[s] for s in range(1 << n) if (s & a) == a)
        U += q * math.log2(pi / q)
    var = 1.0 - p[0]
    b = -p[0] * math.log2(p[0]) if p[0] > 0.0 else 0.0
    return H, I, U, var, b


def static_envelope(p: list[float]) -> tuple[float, list[float]]:
    """Return F_{1/2}(p) and its ordered absence-surprise charges."""
    n = (len(p) - 1).bit_length()
    size = 1 << n
    total = 0.0
    charges = [0.0] * n
    for j in range(size):
        m = [0.0] * size
        for s, q in enumerate(p):
            m[s & j] += q
        for a in range(size):
            if a & ~j or m[a] == 0.0:
                continue
            pi = sum(p[s] for s in range(size) if (s & a) == a)
            term = m[a] * math.log2(pi / m[a])
            total += term / size
            prev = pi
            excluded = 0
            for i in range(n):
                bit = 1 << i
                if not (j & bit) or (a & bit):
                    continue
                excluded |= bit
                nxt = sum(
                    p[s]
                    for s in range(size)
                    if (s & a) == a and (s & excluded) == 0
                )
                charges[i] += m[a] * math.log2(prev / nxt) / size
                prev = nxt
            assert abs(prev - m[a]) <= TOL
    return total, charges


def restricted_values(vals: list[int], n: int, j: int, assignment: int) -> list[int]:
    live = [i for i in range(n) if (j >> i) & 1]
    fixed = [i for i in range(n) if not ((j >> i) & 1)]
    out = []
    for y in range(1 << len(live)):
        x = 0
        for k, i in enumerate(live):
            x |= ((y >> k) & 1) << i
        for k, i in enumerate(fixed):
            x |= ((assignment >> k) & 1) << i
        out.append(vals[x])
    return out


def literal_restriction_average(vals: list[int], n: int) -> dict[str, float]:
    sums = defaultdict(float)
    for j in range(1 << n):
        k = n - j.bit_count()
        branch_weight = 1.0 / ((1 << n) * (1 << k))
        for z in range(1 << k):
            child = restricted_values(vals, n, j, z)
            cp = walsh_prob(child, j.bit_count())
            H, I, U, var, b = metrics_from_prob(cp)
            sums["H"] += branch_weight * H
            sums["I"] += branch_weight * I
            sums["U"] += branch_weight * U
            sums["var"] += branch_weight * var
            sums["b"] += branch_weight * b
    return dict(sums)


def truth_values(code: int, n: int) -> list[int]:
    return [1 if ((code >> x) & 1) else -1 for x in range(1 << n)]


def summarize_control(name: str, vals: list[int], n: int) -> None:
    p = walsh_prob(vals, n)
    H, I, _, _, _ = metrics_from_prob(p)
    F, charges = static_envelope(p)
    literal = literal_restriction_average(vals, n)
    ratios = []
    for i in range(n):
        pi = sum(p[s] for s in range(1 << n) if s & (1 << i))
        if pi > TOL:
            ratios.append(charges[i] / pi)
    print(
        f"control={name}: H/I={(H/I if I else 0.0):.12f}, "
        f"F/I={(F/I if I else 0.0):.12f}, "
        f"EU/I={(literal['U']/I if I else 0.0):.12f}, "
        f"max(C_i/p_i)={(max(ratios) if ratios else 0.0):.12f}"
    )


def main() -> None:
    total_functions = 0
    total_nonconstant = 0
    max_envelope_gap = -math.inf
    min_envelope_gap = math.inf
    max_chain_error = 0.0
    min_witness_gap = math.inf
    maximizers_by_n: dict[int, list[tuple[int, float, float, float, list[float]]]] = {}

    for n in range(1, 5):
        records = []
        c_n = -math.inf
        for code in range(1 << (1 << n)):
            total_functions += 1
            vals = truth_values(code, n)
            p = walsh_prob(vals, n)
            H, I, U, var, b = metrics_from_prob(p)
            F, charges = static_envelope(p)
            literal = literal_restriction_average(vals, n)
            gap = F - literal["U"]
            min_envelope_gap = min(min_envelope_gap, gap)
            max_envelope_gap = max(max_envelope_gap, gap)
            if gap < -TOL:
                raise AssertionError(("envelope", n, code, F, literal["U"]))
            chain_error = abs(sum(charges) - F)
            max_chain_error = max(max_chain_error, chain_error)
            if chain_error > TOL:
                raise AssertionError(("chain", n, code, sum(charges), F))
            if I > TOL:
                total_nonconstant += 1
                witness = max(
                    (charges[i] / sum(p[s] for s in range(1 << n) if s & (1 << i)))
                    for i in range(n)
                    if sum(p[s] for s in range(1 << n) if s & (1 << i)) > TOL
                )
                min_witness_gap = min(min_witness_gap, witness - F / I)
                if witness + TOL < F / I:
                    raise AssertionError(("witness", n, code, witness, F / I))
                ratio = H / I
                if ratio > c_n + TOL:
                    c_n = ratio
                    records = [(code, H, I, F, charges)]
                elif abs(ratio - c_n) <= TOL:
                    records.append((code, H, I, F, charges))
        maximizers_by_n[n] = records
        print(f"n={n}: c_n={c_n:.15f}, maximizers={len(records)}")
        for code, H, I, F, charges in records[:2]:
            vals = truth_values(code, n)
            literal = literal_restriction_average(vals, n)
            coarse = ((c_n - 2.0) / 4.0 - 1.0 / (2.0 * math.log(2.0))) * I
            terminal = literal["var"] + 0.5 * literal["b"]
            delta = c_n * literal["I"] - literal["H"]
            exact_lower = ((c_n - 2.0) / 2.0) * literal["I"] - 0.5 * delta + terminal
            if literal["U"] + TOL < exact_lower or F + TOL < coarse + terminal:
                raise AssertionError(("persistence", n, code, literal, exact_lower, F, coarse, terminal))
            print(
                "  sample maximizer "
                f"code={code}, F/I={F/I:.12f}, EU/I={literal['U']/I:.12f}, "
                f"coarse+terminal={coarse+terminal:.12f}, max(C_i/p_i)="
                f"{max(charges[i] / sum(walsh_prob(vals,n)[s] for s in range(1<<n) if s & (1<<i)) for i in range(n) if sum(walsh_prob(vals,n)[s] for s in range(1<<n) if s & (1<<i)) > TOL):.12f}"
            )

    print(f"functions_checked={total_functions}")
    print(f"nonconstant_functions={total_nonconstant}")
    print(f"minimum_F_minus_EU={min_envelope_gap:.17g}")
    print(f"maximum_F_minus_EU={max_envelope_gap:.17g}")
    print(f"maximum_chain_error={max_chain_error:.17g}")
    print(f"minimum_witness_margin={min_witness_gap:.17g}")
    summarize_control("four-bit point defect", truth_values(1, 4), 4)
    summarize_control(
        "two disjoint two-bit point defects",
        [
            (1 if (x & 0b0011) == 0 else -1)
            * (1 if (x & 0b1100) == 0 else -1)
            for x in range(16)
        ],
        4,
    )
    summarize_control(
        "three-bit fresh selector",
        [1 if (((x >> 1) & 1) if (x & 1) else ((x >> 2) & 1)) else -1 for x in range(8)],
        3,
    )
    summarize_control("four-bit parity atom", [1 if parity(x) == 0 else -1 for x in range(16)], 4)
    print("STATUS: PASS")


if __name__ == "__main__":
    main()
