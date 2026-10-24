#!/usr/bin/env python3
"""
HARD10-03 finite-state sanity check for NEW-L39.

On C5, enumerate the full interchange chain on S_5.  For r=1,2,3 and
several physical phases s, compute exactly (up to matrix-exponential floating
point error) the Campbell intensity of a distinguished rate-one edge bar that
changes the same-phase pair (0, P^r 0) from nonadjacent immediately before the
bar to adjacent immediately after it.

The theorem predicts that this intensity is independent of s after cyclic
Palm rotation.  This script is only a finite-state numerical certificate; it
is not the proof.
"""

import itertools
import json
import numpy as np
from scipy.linalg import expm

N = 5
BETA = 1.2
PHASES = [0.0, 0.2, 0.6, 1.0, 1.2]
LAGS = [1, 2, 3]
EDGES = [(i, (i + 1) % N) for i in range(N)]
STATES = list(itertools.permutations(range(N)))
INDEX = {p: i for i, p in enumerate(STATES)}
IDENTITY = tuple(range(N))
IDENTITY_INDEX = INDEX[IDENTITY]


def left_edge_transposition(p, edge):
    """Apply the ringing edge to positions: new permutation = tau_e o p."""
    a, b = edge
    return tuple(b if x == a else a if x == b else x for x in p)


def permutation_power_at_zero(p, r):
    x = 0
    for _ in range(r):
        x = p[x]
    return x


def adjacent(a, b):
    return ((a - b) % N) in (1, N - 1)


# Full interchange generator on S_N.
GEN = np.zeros((len(STATES), len(STATES)), dtype=float)
for i, p in enumerate(STATES):
    for edge in EDGES:
        q = left_edge_transposition(p, edge)
        GEN[i, INDEX[q]] += 1.0
        GEN[i, i] -= 1.0


def entry_intensity(beta, r, s):
    """
    Campbell intensity per unit physical time at phase s.

    h is the permutation just before the distinguished bar, h2=tau_e o h just
    after it, and g is the final period permutation.  The selected second label
    is b=g^r(0), so the calculation keeps the anticipative dependence exactly.
    """
    before = expm(GEN * s)[IDENTITY_INDEX]
    future = expm(GEN * (beta - s))
    total = 0.0

    for ih, h in enumerate(STATES):
        ph = before[ih]
        if abs(ph) < 1e-16:
            continue
        for edge in EDGES:  # each edge has rate one
            h2 = left_edge_transposition(h, edge)
            row = future[INDEX[h2]]
            for ig, g in enumerate(STATES):
                pg = row[ig]
                if abs(pg) < 1e-16:
                    continue
                b = permutation_power_at_zero(g, r)
                pre = adjacent(h[0], h[b])
                post = adjacent(h2[0], h2[b])
                if (not pre) and post:
                    total += ph * pg
    return float(total)


def main():
    out = {
        "graph": "C5",
        "beta": BETA,
        "phases": PHASES,
        "lags": {},
        "interpretation": (
            "For each fixed lag r, NEW-L39 predicts phase-independent "
            "Campbell entry intensity. Spreads below are numerical matrix-"
            "exponential error only; this computation is not a proof."
        ),
    }
    for r in LAGS:
        vals = [entry_intensity(BETA, r, s) for s in PHASES]
        out["lags"][str(r)] = {
            "entry_intensities": vals,
            "max_minus_min": max(vals) - min(vals),
        }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
