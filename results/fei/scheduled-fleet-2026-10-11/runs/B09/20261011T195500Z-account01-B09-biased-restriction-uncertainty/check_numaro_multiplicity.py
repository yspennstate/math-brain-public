#!/usr/bin/env python3
"""Exact-table deterministic check on the 18-bit Numaro prime gate."""

import json
import numpy as np

from check_restriction_multiplicity import block_metrics


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
PIVOTS = [0, 3, 8, 4, 1, 7, 5, 2, 6]


def reconstruct():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    hosts = [[x for x in range(512) if (mask >> x) & 1] for mask in masks]
    core = np.array([-1 if (base >> x) & 1 else 1 for x in range(512)], dtype=np.int8)
    table = np.tile(core, (1 << 9, 1))
    for j, cells in enumerate(hosts):
        active = (np.arange(1 << 9) & (1 << j)) != 0
        table[np.ix_(active, np.array(cells, dtype=int))] = -1
    return table.ravel()


def main():
    table = reconstruct()
    rows = []
    for j, pivot in enumerate(PIVOTS):
        for kind, A, Q in [
            ("aux", [9 + j], 255 / 262144),
            ("aux_host", [9 + j, pivot], 5799 / 131072),
        ]:
            r = block_metrics(table, 18, A)
            assert -1e-10 <= r["J"] <= r["M"] + 1e-10
            r.update(j=j, kind=kind, A=A, M_over_4Q=r["M"]/(4*Q), J_over_4Q=r["J"]/(4*Q), L_over_4Q=r["L"]/(4*Q))
            rows.append(r)
    print(json.dumps({"status": "PASS", "n": 18, "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
