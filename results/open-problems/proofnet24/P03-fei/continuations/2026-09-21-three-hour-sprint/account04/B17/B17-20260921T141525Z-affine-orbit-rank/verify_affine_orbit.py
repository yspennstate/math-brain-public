#!/usr/bin/env python3
"""Exact affine/character orbit normalization test for the recovered Numaro n=18 FEI seed.

Reconstructs the already-recovered published seed, verifies its source hash,
computes every folded directional disagreement exactly, and uses the binary
vector-matroid greedy algorithm to certify the minimum total influence over
all invertible linear input changes plus output Walsh-character twists.

No claim of full FEI is made.
"""
from fractions import Fraction
from hashlib import sha256
import json
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

def fwht(v):
    a = np.asarray(v, dtype=np.int64).copy()
    h = 1
    while h < len(a):
        b = a.reshape(-1, 2*h)
        x = b[:, :h].copy()
        y = b[:, h:].copy()
        b[:, :h] = x + y
        b[:, h:] = x - y
        h *= 2
    return a

def reconstruct():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    seen = base
    hosts = []
    for m in masks:
        assert not (seen & m)
        assert m.bit_count() == 2
        seen |= m
        hosts.append([x for x in range(512) if (m >> x) & 1])
    core = np.array([-1 if (base >> x) & 1 else 1 for x in range(512)], dtype=np.int64)
    tab = np.tile(core, (1 << len(hosts), 1))
    for j, cells in enumerate(hosts):
        active = (np.arange(1 << len(hosts)) & (1 << j)) != 0
        tab[np.ix_(active, np.array(cells, dtype=int))] = -1
    tab = tab.ravel()
    got = sha256(",".join(map(str, tab)).encode()).hexdigest()
    assert got == EXPECTED_SHA
    return tab, hosts

def gf2_rank(vectors, n):
    piv = [0] * n
    rank = 0
    for vv in vectors:
        x = int(vv)
        for b in range(n-1, -1, -1):
            if not ((x >> b) & 1):
                continue
            if piv[b]:
                x ^= piv[b]
            else:
                piv[b] = x
                rank += 1
                break
    return rank

def greedy_basis(weights, n):
    N = len(weights)
    order = sorted(range(1, N), key=lambda v: (int(weights[v]), v))
    piv = [0] * n
    basis = []
    for v in order:
        x = v
        independent = False
        for b in range(n-1, -1, -1):
            if not ((x >> b) & 1):
                continue
            if piv[b]:
                x ^= piv[b]
            else:
                piv[b] = x
                independent = True
                break
        if independent:
            basis.append(v)
            if len(basis) == n:
                break
    assert len(basis) == n
    return basis

def main():
    table, hosts = reconstruct()
    n = 18
    N = 1 << n
    assert len(table) == N
    assert int(table.sum()) == 0

    W = fwht(table)
    W2 = W * W
    assert int(W2.sum()) == N*N

    weights = np.fromiter((s.bit_count() for s in range(N)), dtype=np.uint8, count=N)
    I_num = int(np.dot(W2, weights))
    I = Fraction(I_num, N*N)
    assert I == Fraction(261, 128)

    # Autocorrelation C(v)=sum_x f(x)f(x+v) = FWHT(W^2)(v)/N.
    corr_num_times_N = fwht(W2)
    assert np.all(corr_num_times_N % N == 0)
    corr_sum = corr_num_times_N // N
    disagree = (N - corr_sum) // 2
    assert np.all(2*disagree == N - corr_sum)

    # Output-character twist can complement each basis-coordinate directional
    # disagreement independently, so use folded cost min(q,1-q).
    folded_count = np.minimum(disagree, N - disagree).astype(np.int64)
    assert folded_count[0] == 0

    basis = greedy_basis(folded_count, n)
    J_count = sum(int(folded_count[v]) for v in basis)
    J = Fraction(J_count, N)

    # Rank-threshold certificate for the matroid optimum.
    tiers = []
    for c in sorted(set(map(int, folded_count[1:]))):
        vecs = np.nonzero(folded_count <= c)[0]
        vecs = vecs[vecs != 0]
        tiers.append({
            "folded_disagreement_count": c,
            "folded_cost": str(Fraction(c, N)),
            "vector_count": int(len(vecs)),
            "span_rank": gf2_rank(vecs, n),
        })

    # The decisive profile: all directions cheaper than 57/256 span only the
    # 9-dimensional host subspace; at 57/256 the span jumps to full rank 18.
    assert [t for t in tiers if t["folded_disagreement_count"] == 1024][0]["span_rank"] == 9
    assert [t for t in tiers if t["folded_disagreement_count"] == 9216][0]["span_rank"] == 9
    assert [t for t in tiers if t["folded_disagreement_count"] == 58368][0]["span_rank"] == 18
    assert J == I

    p = W2.astype(np.float64)/(N*N)
    nz = p > 0
    H = float(np.sum(-p[nz]*np.log2(p[nz])))
    recursive_score = H/(float(J)-1)
    assert abs(recursive_score - 6.521845710923046575) < 2e-13

    out = {
        "source_table_sha256": EXPECTED_SHA,
        "n": n,
        "balanced": True,
        "ordinary_influence_exact": str(I),
        "affine_character_orbit_min_influence_exact": str(J),
        "ordinary_equals_orbit_min": bool(I == J),
        "spectral_entropy_bits_binary64": H,
        "balanced_recursive_composition_score_H_over_J_minus_1_binary64": recursive_score,
        "greedy_basis": [
            {
                "vector_int": int(v),
                "hamming_weight": int(v).bit_count(),
                "raw_disagreement_count": int(disagree[v]),
                "folded_disagreement_count": int(folded_count[v]),
                "folded_cost": str(Fraction(int(folded_count[v]), N)),
            }
            for v in basis
        ],
        "rank_thresholds": tiers,
        "decisive_thresholds": {
            "cost_1_over_256_rank": 9,
            "all_costs_through_9_over_256_rank": 9,
            "cost_57_over_256_rank": 18,
            "minimum_basis_sum": "9*(1/256)+9*(57/256)=261/128",
        },
        "checks": [
            "published truth-table SHA-256 matched",
            "seed is exactly balanced",
            "Parseval matched exactly",
            "ordinary influence is exactly 261/128",
            "all 2^18 directional correlations computed by exact integer Walsh autocorrelation",
            "folded directional costs are exact disagreement counts divided by 2^18",
            "binary vector-matroid greedy basis computed from exact integer weights",
            "rank-threshold certificate forces the same minimum 261/128",
            "affine/character orbit cannot lower this seed's total influence",
        ],
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
