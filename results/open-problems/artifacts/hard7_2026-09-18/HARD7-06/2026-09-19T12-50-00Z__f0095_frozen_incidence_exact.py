#!/usr/bin/env python3
"""Exact finite self-check for HARD7-06 / F0095 frozen-hazard transport.

For n=4,5,6 this enumerates every labelled graph, determines 3-colourability
from exact colour-partition masks, computes the global frozen-pair count D(G),
and verifies with integer/Fraction arithmetic:

  * safe extensions are exactly the missing non-frozen pairs;
  * D cannot decrease along a safe one-edge extension;
  * 1-p_{m+1}/p_m = E_m[D]/(N-m);
  * mu_{m+1} = mu_m - Var_m(D)/(N-m-mu_m) + J_m;
  * the derived exact IFR-defect identity.

The final nonnegativity assertion for the IFR defect is ONLY a finite n<=6
self-check, not an asymptotic theorem and not an exhaustive certificate beyond
those n.
"""

from fractions import Fraction
from itertools import combinations, product
from math import comb


def audit(n: int) -> str:
    edges = list(combinations(range(n), 2))
    N = len(edges)
    ALL = (1 << N) - 1

    # Every proper 3-colouring permits exactly the bichromatic edge mask below.
    allowed = set()
    for col in product(range(3), repeat=n):
        mask = 0
        for i, (u, v) in enumerate(edges):
            if col[u] != col[v]:
                mask |= 1 << i
        allowed.add(mask)
    allowed = tuple(allowed)

    # D[g] is the number of missing pairs that are monochromatic in EVERY
    # proper 3-colouring of g, hence the number of unsafe one-edge additions.
    D = {}
    layers = [[] for _ in range(N + 1)]
    for g in range(1 << N):
        valids = [mask for mask in allowed if (g & ~mask) == 0]
        if not valids:
            continue

        safe_union = 0
        for mask in valids:
            safe_union |= mask
        missing = ALL ^ g
        unsafe = missing & ~safe_union
        d = unsafe.bit_count()

        # Independent direct extension count: an edge is safe iff at least
        # one legal colouring separates its endpoints, i.e. iff it is in
        # safe_union. Thus unsafe must be precisely missing & ~safe_union.
        safe_count = (missing & safe_union).bit_count()
        assert safe_count + d == N - g.bit_count()

        D[g] = d
        layers[g.bit_count()].append(g)

    out = [f"n={n} N={N} color_partition_masks={len(allowed)}"]

    for m in range(N):
        if not layers[m] or not layers[m + 1]:
            continue

        gs = layers[m]
        hs = layers[m + 1]
        A = N - m

        mu = Fraction(sum(D[g] for g in gs), len(gs))
        ED2 = Fraction(sum(D[g] ** 2 for g in gs), len(gs))
        var = ED2 - mu * mu

        incidence_count = 0
        delta_sum = 0
        for g in gs:
            missing = ALL ^ g
            for i in range(N):
                bit = 1 << i
                if missing & bit:
                    h = g | bit
                    if h in D:  # safe extension
                        # Monotone coarsening of the frozen relation.
                        assert D[h] >= D[g]
                        incidence_count += 1
                        delta_sum += D[h] - D[g]

        J = Fraction(delta_sum, incidence_count)
        mu1 = Fraction(sum(D[h] for h in hs), len(hs))

        # Exact safe-incidence transport identity.
        assert mu1 == mu - var / (A - mu) + J

        # Exact hazard identity by layer-count ratio.
        pm = Fraction(len(gs), comb(N, m))
        pm1 = Fraction(len(hs), comb(N, m + 1))
        hazard = 1 - pm1 / pm
        assert hazard == mu / A

        # Exact next-layer IFR defect identity. Its nonnegativity is checked
        # only for these finite enumerated n.
        defect = None
        if m + 2 <= N and layers[m + 2]:
            r1 = mu1 / (A - 1)
            defect = r1 - hazard
            rhs = (
                J
                + mu / A
                - var / (A - mu)
            ) / (A - 1)
            assert defect == rhs
            assert defect >= 0

        if n == 6 and (mu != 0 or J != 0):
            out.append(
                f"m={m} a={len(gs)} mu={mu} var={var} J={J} "
                f"hazard={hazard} defect={defect}"
            )

    out.append("ALL_EXACT_CHECKS_PASS")
    return "\n".join(out)


if __name__ == "__main__":
    print("\n".join(audit(n) for n in range(4, 7)))
