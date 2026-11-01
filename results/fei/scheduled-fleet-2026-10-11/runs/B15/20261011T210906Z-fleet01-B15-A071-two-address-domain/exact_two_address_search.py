#!/usr/bin/env python3
"""Exact bounded countersearch for the two-spectral-address FEI endpoint.

Frozen domain (chosen before the run): four physical bits; the address Fourier
slices indexed by 01, 10, 11 are constant signed indicators of three disjoint
cube edges; the 00 slice is supported on the ten-point complement and has an
arbitrary sign pattern, modulo overall negation.  Only candidates for which
the squared spectrum of the 00 slice is a product law are retained.  The three
edge slices automatically have product squared spectra.

All Walsh transforms, product tests, influences and truth-table checks use
integers.  Logarithms used in the final comparison are enclosed by rational
atanh-series intervals.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import log2
from pathlib import Path

M = 4
N = 1 << M
FULL_DEN = N * N  # squared normalized Walsh denominator, 256
KNOWN_C = Fraction(40, 17)


def parity(v: int) -> int:
    return v.bit_count() & 1


CHI = [[-1 if parity(s & x) else 1 for x in range(N)] for s in range(N)]


def walsh(values: list[int]) -> list[int]:
    return [sum(values[x] * CHI[s][x] for x in range(N)) for s in range(N)]


def is_product_squared(w: list[int]) -> bool:
    """Exact test that q_s=w_s^2, after normalization, is a product law."""
    q = [z * z for z in w]
    total = sum(q)
    if total == 0:
        return False
    marg = []
    for i in range(M):
        one = sum(q[s] for s in range(N) if (s >> i) & 1)
        marg.append((total - one, one))
    scale = total ** (M - 1)
    for s, qs in enumerate(q):
        rhs = 1
        for i in range(M):
            rhs *= marg[i][(s >> i) & 1]
        if qs * scale != rhs:
            return False
    return True


def ln_interval(q: Fraction, terms: int = 80) -> tuple[Fraction, Fraction]:
    """Rational enclosure of ln(q), for 1 <= q <= 2."""
    assert 1 <= q <= 2
    z = (q - 1) / (q + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= z2
    lower = 2 * partial
    # Tail <= 2 z^(2T+1) / ((2T+1)(1-z^2)).
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return lower, lower + tail


LN2 = ln_interval(Fraction(2), 80)


def log2_int_interval(v: int) -> tuple[Fraction, Fraction]:
    assert v >= 1
    k = v.bit_length() - 1
    q = Fraction(v, 1 << k)
    lo, hi = ln_interval(q, 80)
    # Positive denominators: lo/upper <= quotient <= hi/lower.
    return Fraction(k) + lo / LN2[1], Fraction(k) + hi / LN2[0]


LOG_CACHE: dict[int, tuple[Fraction, Fraction]] = {}


def entropy_interval(w: list[int]) -> tuple[Fraction, Fraction]:
    """Enclose entropy of the full six-bit law from residual Walsh values.

    The 24 edge-slice atoms each have mass 1/64, contributing exactly 9/4.
    """
    lo = hi = Fraction(9, 4)
    for z in w:
        q = z * z
        if q == 0:
            continue
        if q not in LOG_CACHE:
            LOG_CACHE[q] = log2_int_interval(q)
        lq, uq = LOG_CACHE[q]
        lo += Fraction(q, FULL_DEN) * (8 - uq)
        hi += Fraction(q, FULL_DEN) * (8 - lq)
    return lo, hi


def influence(w: list[int]) -> Fraction:
    """Full influence: residual physical energy plus fixed edge/address cost."""
    residual_num = sum((s.bit_count()) * z * z for s, z in enumerate(w))
    # Three edges: physical energy 9/16. Address weights 1+1+2 at mass 1/8: 1/2.
    return Fraction(residual_num, FULL_DEN) + Fraction(17, 16)


def entropy_float(w: list[int]) -> float:
    ans = 9.0 / 4.0
    for z in w:
        q = z * z
        if q:
            p = q / FULL_DEN
            ans += p * log2(1.0 / p)
    return ans


def all_edge_matchings() -> tuple[list[tuple[tuple[int, int], ...]], dict[tuple[int, ...], tuple[tuple[int, int], ...]]]:
    edges = [(u, u ^ (1 << b)) for u in range(N) for b in range(M) if u < (u ^ (1 << b))]
    matchings = []
    zero_to_matching = {}
    for es in combinations(edges, 3):
        vertices = [v for e in es for v in e]
        if len(set(vertices)) != 6:
            continue
        matchings.append(es)
        zero_to_matching.setdefault(tuple(sorted(vertices)), es)
    return matchings, zero_to_matching


def full_truth_table(g: list[int], edges: tuple[tuple[int, int], ...]) -> list[int]:
    """Order bits as (y0,y1,x0,x1,x2,x3), y0 least significant."""
    edge_char = {}
    for a, edge in zip((1, 2, 3), edges):
        for x in edge:
            edge_char[x] = a
    out = []
    for x in range(N):
        for y in range(4):
            if g[x]:
                value = g[x]
            else:
                value = -1 if parity(edge_char[x] & y) else 1
            assert value in (-1, 1)
            out.append(value)
    return out


def direct_full_metrics(table: list[int]) -> tuple[list[int], Fraction]:
    assert len(table) == 64 and set(table) <= {-1, 1}
    wf = []
    for s in range(64):
        wf.append(sum(table[x] * (-1 if parity(s & x) else 1) for x in range(64)))
    assert sum(z * z for z in wf) == 64 * 64
    influence_num = sum(s.bit_count() * z * z for s, z in enumerate(wf))
    return wf, Fraction(influence_num, 64 * 64)


def main() -> None:
    source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    matchings, zero_to_matching = all_edge_matchings()
    tested = 0
    retained = 0
    distinct_laws = set()
    certified_gt = 0
    certified_le = 0
    ambiguous = 0
    metric_signatures = Counter()
    best = None
    best_ratio = -1.0

    for zeros, edges in sorted(zero_to_matching.items()):
        zero_set = set(zeros)
        comp = [x for x in range(N) if x not in zero_set]
        # Fix g[comp[0]]=+1; global negation leaves the squared law unchanged.
        g = [0] * N
        for x in comp:
            g[x] = 1
        w = walsh(g)
        prev_gray = 0
        for step in range(1 << 9):
            if step:
                gray = step ^ (step >> 1)
                bit = (gray ^ prev_gray).bit_length() - 1
                x = comp[1 + bit]
                old = g[x]
                g[x] = -old
                for s in range(N):
                    w[s] -= 2 * old * CHI[s][x]
                prev_gray = gray
            tested += 1
            if not is_product_squared(w):
                continue
            retained += 1
            law = tuple(z * z for z in w)
            distinct_laws.add(law)
            I = influence(w)
            Hf = entropy_float(w)
            ratio = Hf / float(I)
            Hlo, Hhi = entropy_interval(w)
            if Hlo / I > KNOWN_C:
                certified_gt += 1
            elif Hhi / I <= KNOWN_C:
                certified_le += 1
            else:
                ambiguous += 1
            hist = tuple(sorted(Counter(z * z for z in w if z).items()))
            metric_signatures[(hist, I)] += 1
            if ratio > best_ratio:
                best_ratio = ratio
                best = (zeros, edges, g.copy(), w.copy(), I, Hlo, Hhi)

    assert best is not None
    zeros, edges, g, w, I, Hlo, Hhi = best
    table = full_truth_table(g, edges)
    wf, direct_I = direct_full_metrics(table)
    assert direct_I == I
    nonzero_full_sq = Counter(z * z for z in wf if z)

    # Independent reconstruction of the archived 40/17 witness.
    known_g = [1, -1, -1, 0, -1, 0, 0, 1, -1, -1, -1, 0, -1, 0, 0, 1]
    known_edges = ((3, 11), (5, 13), (6, 14))
    known_w = walsh(known_g)
    assert is_product_squared(known_w)
    known_table = full_truth_table(known_g, known_edges)
    _, known_I_direct = direct_full_metrics(known_table)
    known_Hlo, known_Hhi = entropy_interval(known_w)
    assert known_I_direct == Fraction(17, 8)
    assert known_Hlo <= 5 <= known_Hhi

    print("B15 exact two-address edge-partition search")
    print("source_sha256=", source_hash, sep="")
    print("frozen_domain=4 physical bits; 3 disjoint constant-sign edges; arbitrary complement signs modulo global negation")
    print("resource_cap=all unique six-vertex unions of 3 disjoint 4-cube edges, times 2^9 complement sign patterns")
    print("cube_edges=32")
    print("edge_matchings=", len(matchings), sep="")
    print("unique_zero_supports=", len(zero_to_matching), sep="")
    print("candidate_sign_patterns=", tested, sep="")
    print("product_residual_candidates=", retained, sep="")
    print("distinct_ordered_residual_squared_laws=", len(distinct_laws), sep="")
    print("certified_ratio_gt_40_over_17_count=", certified_gt, sep="")
    print("certified_ratio_le_40_over_17_count=", certified_le, sep="")
    print("interval_ambiguous_count=", ambiguous, sep="")
    print("metric_signatures_histogram_and_I=")
    for (hist, sig_I), count in sorted(metric_signatures.items(), key=lambda item: (float(item[0][1]), item[0][0])):
        sig_w = []
        for q, multiplicity in hist:
            sig_w.extend([int(q ** 0.5)] * multiplicity)
        sig_Hlo, sig_Hhi = entropy_interval(sig_w)
        print("  ", count, " x residual_q_hist=", hist, " I=", sig_I,
              " H/I_interval=[", float(sig_Hlo / sig_I), ",", float(sig_Hhi / sig_I), "]", sep="")
    print("best_zero_support=", list(zeros), sep="")
    print("best_edge_partition=", [list(e) for e in edges], sep="")
    print("best_residual_truth_table=", g, sep="")
    print("best_residual_walsh=", w, sep="")
    print("best_full_unnormalized_walsh_square_histogram=", dict(sorted(nonzero_full_sq.items())), sep="")
    print("best_I=", I, sep="")
    print("best_H_interval=[", float(Hlo), ",", float(Hhi), "]", sep="")
    print("best_H_over_I_interval=[", float(Hlo / I), ",", float(Hhi / I), "]", sep="")
    print("best_full_truth_table_yfast=", table, sep="")
    print("known_witness_H_interval=[", float(known_Hlo), ",", float(known_Hhi), "]", sep="")
    print("known_witness_I=", known_I_direct, sep="")
    print("KNOWN_WITNESS_RECONSTRUCTION_PASS")
    print("ALL_INTEGER_AND_INTERVAL_CHECKS_PASS")


if __name__ == "__main__":
    main()
