#!/usr/bin/env python3
"""Exact composition-primality certificate for the published balanced n=18 FEI seed.

The truth table is reconstructed from the source-valid ten 512-bit slices used in
the preceding exact packet-profile continuation.  The program checks the published
truth-table SHA-256, monotonicity and exact influences, then certifies that no
proper nontrivial coordinate block can be compressed to one Boolean summary bit.

A block B is compressible only if the cofactors on the complementary variables
take at most two distinct values as the assignment on B varies.  For a monotone
Boolean function it is therefore enough to find an assignment z on B whose
cofactor true-count lies strictly between the all-zero and all-one endpoint
counts.  Exact subset/superset zeta transforms find such a singleton or pair
assignment for every block except the 511 blocks containing all nine core
variables.  Those 511 are eliminated analytically by the source reconstruction:
each omitted host variable controls its own disjoint pair of false core cells.
"""
from hashlib import sha256
import numpy as np

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
    (TOP, BOT),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
    ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00",
     "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
    ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
    ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]

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

    core = np.array([1 if (base >> x) & 1 else 0 for x in range(512)],
                    dtype=np.int64)
    g = np.tile(core, (1 << len(hosts), 1))
    for j, cells in enumerate(hosts):
        active = (np.arange(1 << len(hosts)) & (1 << j)) != 0
        g[np.ix_(active, np.array(cells, dtype=int))] = 1
    g = g.ravel()

    signed = np.where(g == 1, -1, 1)
    got = sha256(",".join(map(str, signed)).encode()).hexdigest()
    assert got == EXPECTED_SHA
    return g, hosts

def main():
    g, hosts = reconstruct()
    n = 18
    N = 1 << n
    ALL = N - 1
    CORE = (1 << 9) - 1

    assert len(g) == N
    assert int(g.sum()) == N // 2

    edge_counts = []
    violations = 0
    idx = np.arange(N, dtype=np.int64)
    for i in range(n):
        lo = idx[(idx & (1 << i)) == 0]
        hi = lo | (1 << i)
        violations += int(np.sum(g[lo] > g[hi]))
        edge_counts.append(int(np.sum(g[lo] != g[hi])))
    assert violations == 0
    assert edge_counts[:9] == [29184] * 9
    assert edge_counts[9:] == [512] * 9
    assert sum(edge_counts) * 128 == 261 * (1 << (n - 1))

    S = g.astype(np.int64).copy()
    for i in range(n):
        bit = 1 << i
        for m in range(N):
            if m & bit:
                S[m] += S[m ^ bit]

    U = g.astype(np.int64).copy()
    for i in range(n):
        bit = 1 << i
        for m in range(N):
            if not (m & bit):
                U[m] += U[m | bit]

    blocks_checked = 0
    singleton_survivors = []
    pair_survivors = []

    for B in range(1, N):
        k = B.bit_count()
        if k < 2 or k > n - 1:
            continue
        blocks_checked += 1
        C = ALL ^ B
        low = int(S[C])
        high = int(U[B])
        bits = [i for i in range(n) if (B >> i) & 1]

        witnessed = False
        for i in bits:
            z = int(S[C | (1 << i)] - S[C])
            if low < z < high:
                witnessed = True
                break
        if witnessed:
            continue
        singleton_survivors.append(B)

        for a in range(len(bits)):
            i = bits[a]
            for b in range(a + 1, len(bits)):
                j = bits[b]
                z = int(
                    S[C | (1 << i) | (1 << j)]
                    - S[C | (1 << i)]
                    - S[C | (1 << j)]
                    + S[C]
                )
                if low < z < high:
                    witnessed = True
                    break
            if witnessed:
                break
        if witnessed:
            continue
        pair_survivors.append(B)

    assert blocks_checked == (1 << n) - 2 - n
    assert len(singleton_survivors) == 20767
    assert len(pair_survivors) == 511

    expected = {
        CORE | (h << 9)
        for h in range(1 << 9)
        if h != (1 << 9) - 1
    }
    assert set(pair_survivors) == expected

    base = int("".join(SLICES[0]), 16)
    assert ((base >> 0) & 1) == 0
    assert ((base >> 511) & 1) == 1
    flat_special = [c for pair in hosts for c in pair]
    assert len(set(flat_special)) == 18
    assert all(((base >> c) & 1) == 0 for c in flat_special)

    analytic_witnesses = 0
    for B in pair_survivors:
        inside_hosts = (B >> 9) & ((1 << 9) - 1)
        outside = ((1 << 9) - 1) ^ inside_hosts
        assert outside
        j = (outside & -outside).bit_length() - 1
        r = outside.bit_count()
        c = hosts[j][0]

        outside_ids = [t for t in range(9) if (outside >> t) & 1]
        vals = []
        for pattern in range(1 << r):
            hostmask = 0
            for q, t in enumerate(outside_ids):
                if (pattern >> q) & 1:
                    hostmask |= 1 << t
            x = c | (hostmask << 9)
            vals.append(int(g[x]))
        jpos = outside_ids.index(j)
        assert all(vals[p] == ((p >> jpos) & 1) for p in range(1 << r))
        assert sum(vals) == (1 << (r - 1))
        assert 0 < sum(vals) < (1 << r)
        analytic_witnesses += 1

    assert analytic_witnesses == 511

    print("PASS")
    print("truth_sha256 =", EXPECTED_SHA)
    print("blocks_checked =", blocks_checked)
    print("singleton_survivors =", len(singleton_survivors))
    print("pair_survivors =", len(pair_survivors))
    print("pair_survivors_exactly_core_supersets =", set(pair_survivors) == expected)
    print("analytic_residual_witnesses =", analytic_witnesses)
    print("core_influence_edge_count_each =", edge_counts[0])
    print("host_influence_edge_count_each =", edge_counts[9])
    print("composition_prime = True")

if __name__ == "__main__":
    main()
