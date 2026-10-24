#!/usr/bin/env python3
"""Large-order and exhaustive checks for the maximal Kemeny constant.

The exact checker beside this file works in rational arithmetic on graphs of order at most 7.
This script covers what that one cannot reach: the balanced barbell at orders in the hundreds
and above, the location of the optimal split, the exact maximum over every connected graph of
small order, and the bipartite constant 1/108. It uses only numpy (spectral formula) and one
exact rational cross-check that pins the floating-point route to the exact one.

None of this proves the theorem. It shows the family the paper names behaves as the theorem
says at orders far beyond the exact checker, and it records the exact small-order maxima so the
gap between the asymptotic statement and finite maximizers is visible rather than assumed.

Run:  python large_order_checks.py > large_order_output.json
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from fractions import Fraction

import numpy as np


# ----------------------------------------------------------------------------- Kemeny's constant

def kemeny_spectral(adj: np.ndarray) -> float:
    """K(G) = sum_{j>=2} 1/(1 - lambda_j) over eigenvalues of D^{-1/2} A D^{-1/2}.

    The matrix is symmetric, so eigvalsh is exact up to rounding; the top eigenvalue 1 is
    simple for a connected graph and is dropped. An eigenvalue -1 (bipartite graph) contributes
    1/2, as in the paper's convention: periodicity is allowed and no absolute gap is used.
    """
    deg = adj.sum(axis=1)
    inv_sqrt = 1.0 / np.sqrt(deg)
    normalized = inv_sqrt[:, None] * adj * inv_sqrt[None, :]
    lam = np.linalg.eigvalsh(normalized)          # ascending
    lam = lam[:-1]                                # drop the eigenvalue 1
    return float(np.sum(1.0 / (1.0 - lam)))


def kemeny_exact(edges: list[tuple[int, int]], n: int) -> Fraction:
    """K(G) = (1/2m) sum_{u<v} d_u d_v R(u,v) in exact rationals, via a grounded Laplacian solve."""
    deg = [0] * n
    lap = [[Fraction(0)] * n for _ in range(n)]
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
        lap[u][v] -= 1
        lap[v][u] -= 1
    for i in range(n):
        lap[i][i] = Fraction(deg[i])
    # invert the (n-1)x(n-1) grounded Laplacian by Gauss-Jordan
    k = n - 1
    aug = [lap[i][:k] + [Fraction(int(i == j)) for j in range(k)] for i in range(k)]
    for col in range(k):
        piv = next(r for r in range(col, k) if aug[r][col] != 0)
        aug[col], aug[piv] = aug[piv], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(k):
            if r != col and aug[r][col] != 0:
                f = aug[r][col]
                aug[r] = [a - f * b for a, b in zip(aug[r], aug[col])]
    inv = [row[k:] for row in aug]

    def g(i, j):
        return inv[i][j] if i < k and j < k else Fraction(0)

    m = len(edges)
    total = Fraction(0)
    for u in range(n):
        for v in range(u + 1, n):
            r = g(u, u) + g(v, v) - 2 * g(u, v)
            total += deg[u] * deg[v] * r
    return total / (2 * m)


# ----------------------------------------------------------------------------- graph families

def barbell(q: int, ell: int, block: str = "complete", parts: int = 2) -> np.ndarray:
    """Two copies of a q-vertex block joined at one vertex each by a path of length ell.

    block = "complete"  : K_q                        (the paper's main lower bound)
    block = "turan"     : balanced complete `parts`-partite graph on q vertices (clique-free)
    n = 2q + ell - 1.
    """
    n = 2 * q + ell - 1
    adj = np.zeros((n, n), dtype=np.float64)

    def block_edges(offset: int):
        if block == "complete":
            for i in range(q):
                for j in range(i + 1, q):
                    yield offset + i, offset + j
        else:
            part = [i % parts for i in range(q)]
            for i in range(q):
                for j in range(i + 1, q):
                    if part[i] != part[j]:
                        yield offset + i, offset + j

    for u, v in itertools.chain(block_edges(0), block_edges(q)):
        adj[u, v] = adj[v, u] = 1.0
    route = [0] + list(range(2 * q, 2 * q + ell - 1)) + [q]
    for u, v in zip(route, route[1:]):
        adj[u, v] = adj[v, u] = 1.0
    return adj


def barbell_edge_list(q: int, ell: int) -> tuple[list[tuple[int, int]], int]:
    adj = barbell(q, ell)
    n = adj.shape[0]
    return [(i, j) for i in range(n) for j in range(i + 1, n) if adj[i, j]], n


# ----------------------------------------------------------------------------- the checks

def check_exact_pin() -> dict:
    """The float route agrees with exact rationals on a real barbell, to 1e-9 relative."""
    q, ell = 4, 6
    edges, n = barbell_edge_list(q, ell)
    exact = kemeny_exact(edges, n)
    approx = kemeny_spectral(barbell(q, ell))
    rel = abs(approx - float(exact)) / float(exact)
    assert rel < 1e-9, rel
    return {"n": n, "q": q, "ell": ell, "K_exact": str(exact), "K_float": approx, "rel_err": rel}


def check_balanced_barbell(orders) -> list[dict]:
    """K(barbell) * 54 / n^3 -> 1, and the paper's explicit lower bound (2e+1)ell/2 <= K."""
    rows = []
    for n in orders:
        q = n // 3
        ell = n - 2 * q + 1
        t0 = time.time()
        K = kemeny_spectral(barbell(q, ell))
        e = q * (q - 1) // 2
        lower = (2 * e + 1) * ell / 2            # Lemma 5.1 with B = K_q
        assert K >= lower * (1 - 1e-9), (n, K, lower)
        rows.append({"n": n, "q": q, "ell": ell, "K": K, "K54_over_n3": 54 * K / n ** 3,
                     "paper_lower_bound": lower, "n3_over_54_minus_K_over_n2": (n ** 3 / 54 - K) / n ** 2,
                     "seconds": round(time.time() - t0, 2)})
    return rows


def check_optimal_split(orders) -> list[dict]:
    """Among complete barbells of order n, the best block size q* satisfies q*/n -> 1/3."""
    rows = []
    for n in orders:
        best = None
        for q in range(max(2, n // 6), n // 2):
            ell = n - 2 * q + 1
            if ell < 1:
                continue
            K = kemeny_spectral(barbell(q, ell))
            if best is None or K > best[1]:
                best = (q, K)
        q, K = best
        rows.append({"n": n, "q_star": q, "q_star_over_n": q / n, "K": K, "K54_over_n3": 54 * K / n ** 3})
    return rows


def check_exhaustive_small_orders(max_n: int = 7) -> list[dict]:
    """Exact maximum of K over EVERY connected graph of order n <= max_n (Graph Atlas), compared
    with the best barbell of that order. This records what the finite maximizers actually are;
    the paper does not classify them, and at these orders they need not be barbells."""
    import networkx as nx
    best = {}
    for g in nx.graph_atlas_g():
        n = g.number_of_nodes()
        if n < 2 or n > max_n or not nx.is_connected(g):
            continue
        adj = nx.to_numpy_array(g, dtype=np.float64)
        K = kemeny_spectral(adj)
        if n not in best or K > best[n][0] + 1e-12:
            best[n] = (K, sorted(tuple(sorted(e)) for e in g.edges()))
    rows = []
    for n in sorted(best):
        K, edges = best[n]
        # best complete barbell of the same order (including degenerate q=1 = a path)
        bb = max(kemeny_spectral(barbell(q, n - 2 * q + 1)) for q in range(1, n // 2 + 1) if n - 2 * q + 1 >= 1)
        rows.append({"n": n, "K_max_all_graphs": K, "maximizer_edges": edges,
                     "K_best_barbell": bb, "K_max_54_over_n3": 54 * K / n ** 3})
    return rows


def check_bipartite_constant(orders) -> list[dict]:
    """Two balanced complete bipartite blocks joined by a path: K * 108 / n^3 -> 1 (Theorem 1.3, r=2)."""
    rows = []
    for n in orders:
        q = n // 3
        ell = n - 2 * q + 1
        K = kemeny_spectral(barbell(q, ell, block="turan", parts=2))
        rows.append({"n": n, "q": q, "ell": ell, "K": K, "K108_over_n3": 108 * K / n ** 3})
    return rows


def main() -> None:
    t0 = time.time()
    out = {
        "exact_pin": check_exact_pin(),
        "balanced_barbell": check_balanced_barbell([30, 60, 120, 240, 480, 960, 1440]),
        "optimal_split": check_optimal_split([60, 120, 240]),
        "exhaustive_small_orders": check_exhaustive_small_orders(7),
        "bipartite_barbell": check_bipartite_constant([60, 120, 240, 480, 960]),
    }
    last = out["balanced_barbell"][-1]["K54_over_n3"]
    first = out["balanced_barbell"][0]["K54_over_n3"]
    out["summary"] = {
        "K54_over_n3_at_n30": first,
        "K54_over_n3_at_n1440": last,
        "approaches_one": bool(abs(last - 1.0) < abs(first - 1.0) and abs(last - 1.0) < 0.05),
        "q_star_over_n_at_n240": out["optimal_split"][-1]["q_star_over_n"],
        "bipartite_K108_over_n3_at_n960": out["bipartite_barbell"][-1]["K108_over_n3"],
        "seconds_total": round(time.time() - t0, 1),
        "scope": "Floating-point spectral evaluation pinned to one exact rational case; families and finite maxima only. Not a proof of the asymptotic theorem.",
    }
    assert out["summary"]["approaches_one"]
    json.dump(out, sys.stdout, indent=1)
    print()


if __name__ == "__main__":
    main()
