"""Numerical checks for HOOKS_AND_TWO_ROWS.md.

(1) Hooks: the spectrum of L(G, [n-k, 1^k]) is the set of sums of k distinct eigenvalues of the graph Laplacian
    on the complement of the constants.
(2) Conjugation: lambda_min(G, nu') = 2W - lambda_max(G, nu).
(3) Two rows: L(G, [n-2, 2]) is the pair-permutation Laplacian on the edge weightings of K_n with zero sum at
    every vertex.
(4) The family inequality  lambda_max(L_G) <= (2W + (n-2) lambda_max(G, [n-2,2])) / (n-1)  on random weights.
usage: hooks_check.py trials seed
"""
import sys, itertools
import numpy as np
from alon_search import edge_ops


def lap(n, edges, w):
    L = np.zeros((n, n))
    for (i, j), v in zip(edges, w):
        L[i - 1, i - 1] += v
        L[j - 1, j - 1] += v
        L[i - 1, j - 1] -= v
        L[j - 1, i - 1] -= v
    return L


def conj(shape):
    return tuple(sum(1 for r in shape if r > c) for c in range(shape[0]))


def two_row_model(n, edges):
    """Per-edge operators I - P_ij on {T in R^pairs : sum of T over the pairs at each vertex = 0}."""
    pairs = list(itertools.combinations(range(1, n + 1), 2))
    idx = {p: k for k, p in enumerate(pairs)}
    B = np.zeros((n, len(pairs)))
    for p, k in idx.items():
        B[p[0] - 1, k] = 1
        B[p[1] - 1, k] = 1
    _, s, vt = np.linalg.svd(B)
    Q = vt[n:].T                                    # orthonormal basis of the kernel of B
    assert Q.shape[1] == n * (n - 3) // 2 and abs(B @ Q).max() < 1e-12
    ops = []
    for (i, j) in edges:
        P = np.zeros((len(pairs), len(pairs)))
        for p, k in idx.items():
            q = tuple(sorted((j if a == i else i if a == j else a) for a in p))
            P[idx[q], k] = 1
        ops.append(Q.T @ (np.eye(len(pairs)) - P) @ Q)
    return np.array(ops)


def rand_w(rng, m, kind):
    if kind == 0:
        return rng.uniform(0, 1, m)
    if kind == 1:
        return np.exp(rng.normal(0, 2.5, m))
    return rng.uniform(0, 1, m) * (rng.uniform(0, 1, m) < 0.45)


def main():
    trials = int(sys.argv[1])
    rng = np.random.default_rng(int(sys.argv[2]))
    for n in (5, 6, 7):
        hooks = [tuple([n - k] + [1] * k) for k in range(1, n - 1)]
        ops = {}
        edges = None
        for sh in hooks + [(n - 2, 2), conj((n - 2, 2))]:
            A, e, _, _ = edge_ops(sh)
            ops[sh] = A
            edges = e
        M = two_row_model(n, edges)
        m = len(edges)
        dev_hook = dev_conj = dev_model = 0.0
        gap = float("inf")
        best_c = float("inf")
        for t in range(trials):
            w = rand_w(rng, m, t % 3)
            if w.sum() <= 0:
                w = rng.uniform(0, 1, m)
            w = w / w.sum()
            lam = np.linalg.eigvalsh(lap(n, edges, w))[1:]             # drop the constants
            for k, sh in enumerate(hooks, start=1):
                got = np.linalg.eigvalsh(np.tensordot(w, ops[sh], axes=1))
                want = np.sort([sum(c) for c in itertools.combinations(lam, k)])
                dev_hook = max(dev_hook, abs(got - want).max())
            e2 = np.linalg.eigvalsh(np.tensordot(w, ops[(n - 2, 2)], axes=1))
            ec = np.linalg.eigvalsh(np.tensordot(w, ops[conj((n - 2, 2))], axes=1))
            dev_conj = max(dev_conj, abs(ec[0] - (2.0 - e2[-1])))
            em = np.linalg.eigvalsh(np.tensordot(w, M, axes=1))
            dev_model = max(dev_model, abs(em - e2).max())
            gap = min(gap, (2.0 + (n - 2) * e2[-1]) / (n - 1) - lam[-1])
            if ec[0] > 1e-9:
                best_c = min(best_c, (2.0 - lam[-1]) / ec[0])
        print("n=%d trials=%d: hooks dev %.1e, conjugation dev %.1e, two-row model dev %.1e, "
              "family gap min %.3e (must be >= 0), smallest ratio seen %.6f (star value %.6f)"
              % (n, trials, dev_hook, dev_conj, dev_model, gap, best_c, (n - 2.0) / (n - 1.0)))


if __name__ == "__main__":
    main()
