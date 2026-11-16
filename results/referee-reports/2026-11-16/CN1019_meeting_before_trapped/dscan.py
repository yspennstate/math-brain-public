"""CN1019 refined bound, optimiser-free scan: D = F - 1/3 - (2/3) sum pi^3 on random and structured chains.
Families: Erdos-Renyi conductances with lognormal weights, star, path, barbell, lollipop, cycle with a chord;
pi uniform, Dirichlet, or concentrated (one state carrying 0.5..0.95). Prints the smallest D per n and family.

    python dscan.py N1 N2 TRIALS
"""
import sys

import numpy as np

from meet import F


def graph(kind, n, rng):
    A = np.zeros((n, n))
    if kind == "random":
        A = (rng.random((n, n)) < rng.uniform(0.3, 1.0)).astype(float)
    elif kind == "star":
        A[0, 1:] = 1
    elif kind == "path":
        for i in range(n - 1):
            A[i, i + 1] = 1
    elif kind == "barbell":
        h = n // 2
        A[:h, :h] = 1
        A[h:, h:] = 1
        A[h - 1, h] = 1
    elif kind == "lollipop":
        h = max(2, n // 2)
        A[:h, :h] = 1
        for i in range(h - 1, n - 1):
            A[i, i + 1] = 1
    elif kind == "cyclechord":
        for i in range(n):
            A[i, (i + 1) % n] = 1
        A[0, n // 2] = 1
    A = np.triu(A, 1)
    A = A + A.T
    # keep it connected: add a path if needed
    for i in range(n - 1):
        if not A[i].any() or not A[:, i + 1].any():
            A[i, i + 1] = A[i + 1, i] = 1
    return A


def connected(A):
    n = len(A)
    seen, stack = {0}, [0]
    while stack:
        u = stack.pop()
        for v in np.nonzero(A[u])[0]:
            if v not in seen:
                seen.add(int(v))
                stack.append(int(v))
    return len(seen) == n


if __name__ == "__main__":
    n1, n2, T = (int(a) for a in sys.argv[1:4])
    rng = np.random.default_rng(31)
    kinds = ["random", "star", "path", "barbell", "lollipop", "cyclechord"]
    overall = np.inf
    for n in range(n1, n2 + 1):
        for kind in kinds:
            worst = (np.inf, None)
            for t in range(T):
                A = graph(kind, n, rng)
                if not connected(A):
                    continue
                W = np.exp(rng.normal(0, rng.choice([0.5, 2.0, 5.0]), (n, n)))
                W = np.triu(W, 1)
                C = A * (W + W.T)
                mode = rng.integers(3)
                if mode == 0:
                    pi = np.ones(n) / n
                elif mode == 1:
                    pi = rng.dirichlet(np.full(n, rng.choice([0.3, 1.0, 3.0])))
                else:
                    big = rng.uniform(0.5, 0.95)
                    pi = rng.dirichlet(np.ones(n - 1)) * (1 - big)
                    pi = np.insert(pi, rng.integers(n), big)
                pi = np.maximum(pi, 1e-4)
                pi /= pi.sum()
                f = F(pi, C)
                if f == 1.0:
                    continue
                d = f - 1 / 3 - 2 / 3 * (pi ** 3).sum()
                if d < worst[0]:
                    worst = (d, pi)
            overall = min(overall, worst[0])
            print("n=%d %-10s min D=%.3e  pi_max=%.3f" % (n, kind, worst[0], worst[1].max() if worst[1] is not None else -1),
                  flush=True)
            if worst[0] < -1e-9:
                print("NEGATIVE n=%d kind=%s D=%.3e pi=%s" % (n, kind, worst[0], np.round(worst[1], 4)), flush=True)
    print("overall min D=%.3e" % overall, flush=True)
