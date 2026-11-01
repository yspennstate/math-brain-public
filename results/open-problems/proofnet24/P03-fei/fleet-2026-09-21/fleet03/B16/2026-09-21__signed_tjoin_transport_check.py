#!/usr/bin/env python3
"""Exact finite checks for the B16 signed T-join transport lemma.

This is verification only.  It does not infer universal FEI from finite cases.
It exhausts all Boolean phases on Q_3 and all affine-relation-code supports.
"""

from fractions import Fraction
import json


def cube_edges(n):
    edges = []
    for x in range(1 << n):
        for i in range(n):
            y = x ^ (1 << i)
            if x < y:
                edges.append((x, y, i))
    return edges


def xor_vertices(mask, n):
    z = 0
    for v in range(1 << n):
        if (mask >> v) & 1:
            z ^= v
    return z


def c0_relations(n):
    N = 1 << n
    return [
        A for A in range(1 << N)
        if A.bit_count() % 2 == 0 and xor_vertices(A, n) == 0
    ]


def agreement_components(n, fbits, edges):
    N = 1 << n
    adj = [[] for _ in range(N)]
    disagreement = []
    for j, (u, v, _i) in enumerate(edges):
        if ((fbits >> u) & 1) ^ ((fbits >> v) & 1):
            disagreement.append(j)
        else:
            adj[u].append(v)
            adj[v].append(u)
    comp = [-1] * N
    cid = 0
    for v in range(N):
        if comp[v] != -1:
            continue
        comp[v] = cid
        stack = [v]
        while stack:
            a = stack.pop()
            for b in adj[a]:
                if comp[b] == -1:
                    comp[b] = cid
                    stack.append(b)
        cid += 1
    return comp, cid, disagreement


def component_terminal_mask(A, comp, ncomp):
    parity = [0] * ncomp
    for v, c in enumerate(comp):
        if (A >> v) & 1:
            parity[c] ^= 1
    ans = 0
    for c, bit in enumerate(parity):
        if bit:
            ans |= 1 << c
    return ans


def main():
    n = 3
    N = 1 << n
    edges = cube_edges(n)
    E = len(edges)
    assert E == 12

    # Precompute each F_2 edge-chain boundary and its direction-parity vector.
    boundary = [0] * (1 << E)
    size = [0] * (1 << E)
    direction_parity = [0] * (1 << E)
    for s in range(1, 1 << E):
        lsb = s & -s
        j = lsb.bit_length() - 1
        prev = s ^ lsb
        u, v, i = edges[j]
        boundary[s] = boundary[prev] ^ ((1 << u) | (1 << v))
        size[s] = size[prev] + 1
        direction_parity[s] = direction_parity[prev] ^ (1 << i)

    relations = c0_relations(n)
    frustrated_instances = 0
    max_min_disagreement_tjoin = 0

    for fbits in range(1 << N):
        comp, ncomp, D = agreement_components(n, fbits, edges)
        Dmask = sum(1 << j for j in D)

        # For each terminal boundary, select first by minimum number of actual
        # f-disagreement edges, then by minimum total chain size.
        best_key = {}
        best_chain = {}
        for s in range(1 << E):
            b = boundary[s]
            key = ((s & Dmask).bit_count(), size[s])
            if b not in best_key or key < best_key[b]:
                best_key[b] = key
                best_chain[b] = s

        # Independently solve the T-join problem after contracting every
        # monochromatic connected component.  Each retained edge is one actual
        # physical disagreement edge, so this is the quotient minimum.
        qbest = {0: 0}
        for j in D:
            u, v, _i = edges[j]
            toggle = (1 << comp[u]) ^ (1 << comp[v])
            old = dict(qbest)
            for mask, cost in old.items():
                nm = mask ^ toggle
                cand = cost + 1
                if cand < qbest.get(nm, 10**9):
                    qbest[nm] = cand

        # Toy signed radial coefficients are used only to verify the algebraic
        # disintegration.  Their magnitudes are arbitrary positive rationals;
        # the genuine R32 coefficient signs (-1)^(|A|/2) are retained.
        edge_load = {j: Fraction(0) for j in D}
        original_signed_sum = Fraction(0)

        for A in relations:
            if A == 0 or (A & fbits).bit_count() % 2 == 0:
                continue
            frustrated_instances += 1
            w = A.bit_count()
            chain = best_chain[A]
            d = (chain & Dmask).bit_count()
            assert d >= 1 and d % 2 == 1
            max_min_disagreement_tjoin = max(max_min_disagreement_tjoin, d)

            # Quotient minimum equals cube minimum in disagreement-edge cost.
            tmask = component_terminal_mask(A, comp, ncomp)
            assert qbest[tmask] == d

            # The affine-relation constraint xor(A)=0 is exactly even parity
            # of used physical edge directions for every chain with boundary A.
            assert direction_parity[chain] == 0

            sign = 1 if (w // 2) % 2 == 0 else -1
            coeff = Fraction(sign, w + 1)
            original_signed_sum += coeff
            for j in D:
                if (chain >> j) & 1:
                    edge_load[j] += coeff / d

        # Every frustrated relation contributes total routed mass exactly equal
        # to its signed coefficient.  Negative 2 mod 4 credits stay negative.
        assert sum(edge_load.values(), Fraction(0)) == original_signed_sum

    out = {
        "status": "PASS",
        "dimension": n,
        "boolean_phases_checked": 1 << N,
        "affine_relation_codewords": len(relations),
        "frustrated_relation_instances_checked": frustrated_instances,
        "max_minimum_disagreement_tjoin_size_seen": max_min_disagreement_tjoin,
        "checks": [
            "cube minimum disagreement T-join equals monochromatic-quotient minimum",
            "frustrated relation uses an odd positive number of disagreement edges",
            "xor-zero relation forces even parity in every physical direction",
            "signed relation mass is conserved exactly by normalized edge routing"
        ],
        "scope": "finite verification only; no universal FEI inference"
    }
    print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
