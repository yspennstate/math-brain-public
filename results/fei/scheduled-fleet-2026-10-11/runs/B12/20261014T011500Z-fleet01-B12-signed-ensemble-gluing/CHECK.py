#!/usr/bin/env python3
"""Exact/deterministic controls for signed-ensemble gluing."""

from __future__ import annotations

import itertools
import math
import random


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


def raw_entropy(vals):
    nums = fwht(vals)
    den = len(vals)
    ans = 0.0
    for z in nums:
        if z:
            u = (z / den) ** 2
            ans += u * math.log2(1.0 / u)
    return ans


def influence(vals):
    n = int(math.log2(len(vals)))
    return sum(
        sum((vals[x] - vals[x ^ (1 << i)]) ** 2 for x in range(len(vals)))
        / (4 * len(vals))
        for i in range(n)
    )


def entropy_exact_signature(vals):
    """Return histogram of nonzero squared Walsh numerators for certificates."""
    hist = {}
    for z in fwht(vals):
        if z:
            hist[z * z] = hist.get(z * z, 0) + 1
    return dict(sorted(hist.items()))


def all_sign_sums(pieces):
    for eps in itertools.product((-1, 1), repeat=len(pieces)):
        yield eps, [sum(eps[j] * pieces[j][x] for j in range(len(pieces))) for x in range(len(pieces[0]))]


def verify_ensemble(pieces, tol=3e-11):
    # Supports must be pairwise disjoint.
    N = len(pieces[0])
    assert all(sum(piece[x] != 0 for piece in pieces) <= 1 for x in range(N))
    sums = list(all_sign_sums(pieces))
    avg_E = sum(raw_entropy(v) for _, v in sums) / len(sums)
    avg_I = sum(influence(v) for _, v in sums) / len(sums)
    piece_E = sum(raw_entropy(v) for v in pieces)
    piece_I = sum(influence(v) for v in pieces)
    assert avg_E <= piece_E + tol
    assert abs(avg_I - piece_I) <= tol
    return avg_E, piece_E, avg_I, piece_I


def exhaustive_two_piece_n3():
    # Point states: 0, +piece0, -piece0, +piece1, -piece1.
    N = 8
    cache_E = {}
    cache_I = {}

    def EI(v):
        t = tuple(v)
        if t not in cache_E:
            cache_E[t] = raw_entropy(t)
            cache_I[t] = influence(t)
        return cache_E[t], cache_I[t]

    count = 0
    nontrivial = 0
    max_single_excess = -1e100
    witness = None
    min_pair_slack = 1e100
    for states in itertools.product(range(5), repeat=N):
        b0 = [0] * N
        b1 = [0] * N
        for x, s in enumerate(states):
            if s == 1:
                b0[x] = 1
            elif s == 2:
                b0[x] = -1
            elif s == 3:
                b1[x] = 1
            elif s == 4:
                b1[x] = -1
        if not any(b0) or not any(b1):
            continue
        plus = [x + y for x, y in zip(b0, b1)]
        minus = [x - y for x, y in zip(b0, b1)]
        E0, I0 = EI(b0)
        E1, I1 = EI(b1)
        Ep, Ip = EI(plus)
        Em, Im = EI(minus)
        pair_slack = 2 * (E0 + E1) - Ep - Em
        assert pair_slack >= -3e-11
        assert abs((Ip + Im) - 2 * (I0 + I1)) < 3e-11
        single_excess = Ep - E0 - E1
        if single_excess > max_single_excess + 1e-14:
            max_single_excess = single_excess
            witness = (tuple(b0), tuple(b1), tuple(plus), tuple(minus), E0, E1, Ep, Em, I0, I1, Ip, Im)
        min_pair_slack = min(min_pair_slack, pair_slack)
        count += 1
        nontrivial += int(single_excess > 1e-12)
    return count, nontrivial, max_single_excess, min_pair_slack, witness


def deterministic_multi_piece():
    rng = random.Random(20261014011500)
    cases = 0
    max_ratio = 0.0
    for n in range(2, 7):
        N = 1 << n
        for k in range(3, min(6, N) + 1):
            for _ in range(80):
                pieces = [[0] * N for _ in range(k)]
                for x in range(N):
                    label = rng.randrange(k + 1)
                    if label < k:
                        pieces[label][x] = -1 if rng.randrange(2) else 1
                if any(not any(v) for v in pieces):
                    continue
                avg_E, piece_E, avg_I, piece_I = verify_ensemble(pieces)
                if piece_E:
                    max_ratio = max(max_ratio, avg_E / piece_E)
                cases += 1
    return cases, max_ratio


def main():
    count, nontrivial, max_excess, min_slack, w = exhaustive_two_piece_n3()
    multi_cases, max_avg_ratio = deterministic_multi_piece()
    b0, b1, plus, minus, E0, E1, Ep, Em, I0, I1, Ip, Im = w
    assert max_excess > 0.01  # averaging is genuinely necessary
    exact_left = 7 ** 98
    exact_right = (2 ** 128) * (3 ** 72)
    assert exact_left > exact_right
    print(f"exhaustive_two_piece_cases={count}")
    print(f"single_sign_subadditivity_failures={nontrivial}")
    print(f"maximum_single_sign_excess={max_excess:.15g}")
    print(f"minimum_pair_entropy_slack={min_slack:.15g}")
    print(f"deterministic_multi_piece_cases={multi_cases}")
    print(f"largest_average_to_piece_entropy_ratio={max_avg_ratio:.15g}")
    print(f"witness_b0={list(b0)}")
    print(f"witness_b1={list(b1)}")
    print(f"witness_plus_hist={entropy_exact_signature(plus)}")
    print(f"witness_b0_hist={entropy_exact_signature(b0)}")
    print(f"witness_b1_hist={entropy_exact_signature(b1)}")
    print(f"witness_minus_hist={entropy_exact_signature(minus)}")
    print(f"witness_entropies={(E0,E1,Ep,Em)}")
    print(f"witness_influences={(I0,I1,Ip,Im)}")
    print("witness_exact_inequality=7^98>2^128*3^72")
    print(f"witness_integer_bitlengths={(exact_left.bit_length(),exact_right.bit_length())}")
    print("full_FEI=OPEN")
    print("PASS")


if __name__ == "__main__":
    main()
