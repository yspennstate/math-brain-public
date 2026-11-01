#!/usr/bin/env python3
"""Finite-state sanity check for the deterministic pivotal classification in NEW-L58.

This is not a proof of the Z^3 theorem.  It exhaustively checks all permutations on
cycle graphs C4,C5,C6 and all M up to min(3,n-1), using left multiplication by an
edge transposition (the interchange convention in the report).
"""

import itertools
import json


def left_transpose(sigma, u, v):
    out = []
    for x in range(len(sigma)):
        y = sigma[x]
        if y == u:
            y = v
        elif y == v:
            y = u
        out.append(y)
    return tuple(out)


def inverse(sigma):
    inv = [0] * len(sigma)
    for x, y in enumerate(sigma):
        inv[y] = x
    return tuple(inv)


def power_at_zero(sigma, j):
    if j < 0:
        return power_at_zero(inverse(sigma), -j)
    x = 0
    for _ in range(j):
        x = sigma[x]
    return x


def root_cycle_length(sigma):
    x = 0
    for ell in range(1, len(sigma) + 1):
        x = sigma[x]
        if x == 0:
            return ell
    raise RuntimeError("not a permutation")


def check_cycle_graph(n):
    edges = [(i, (i + 1) % n) for i in range(n)]
    failures = []
    tested = 0
    max_pivotal = {}

    for sigma in itertools.permutations(range(n)):
        L = root_cycle_length(sigma)
        for M in range(1, min(3, n - 1) + 1):
            tested += 1
            pivotal = []
            for e in edges:
                sigma2 = left_transpose(sigma, *e)
                if (L <= M) != (root_cycle_length(sigma2) <= M):
                    pivotal.append(e)

            max_pivotal[str(M)] = max(max_pivotal.get(str(M), 0), len(pivotal))

            if L <= M:
                # Degree is 2 on C_n, so the analogue of 6M is 2M.
                if len(pivotal) > 2 * M:
                    failures.append({
                        "kind": "short_cycle_degree_bound",
                        "sigma": sigma,
                        "M": M,
                        "L": L,
                        "pivotal": pivotal,
                    })
                    return tested, max_pivotal, failures
            else:
                W = {power_at_zero(sigma, j) for j in range(-M - 1, M + 2)}
                bad = [e for e in pivotal if not (e[0] in W and e[1] in W)]
                if bad:
                    failures.append({
                        "kind": "long_cycle_window_bound",
                        "sigma": sigma,
                        "M": M,
                        "L": L,
                        "W": sorted(W),
                        "pivotal": pivotal,
                        "bad": bad,
                    })
                    return tested, max_pivotal, failures

    return tested, max_pivotal, failures


def main():
    result = {"graphs": {}, "pass": True}
    for n in (4, 5, 6):
        tested, max_pivotal, failures = check_cycle_graph(n)
        result["graphs"][f"C{n}"] = {
            "permutation_M_cases_tested": tested,
            "max_pivotal_by_M": max_pivotal,
            "failures": failures,
        }
        if failures:
            result["pass"] = False
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
