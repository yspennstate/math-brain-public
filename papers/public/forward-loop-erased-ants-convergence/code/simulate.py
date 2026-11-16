"""Numerical checks for the forward-loop-erased ants walk at nest-food distance two.

1) The edge identities P(edge {N,u} reinforced) = w h(u) / C and P(edge {u,F} reinforced) = w (1 - h(u)) / C,
   h(u) = P_u(tau_F < tau_N), C = sum_u w_{Nu} h(u), against Monte Carlo loop-erased paths for random weights.
2) Long runs from unit weights on two graphs and several seeds: log(Q_i / Q_j), Q_i = W_{Ni} W_{iF}, and the
   normalized weights W / n.
Usage: python3 simulate.py
"""
import math
import random
import sys

import numpy as np

N, F = 0, 1
GRAPHS = {
    # middles 2, 3; extra vertices 4, 5; chords 2-3 and 4-5
    "A": [(0, 2), (2, 1), (0, 3), (3, 1), (0, 4), (4, 2), (3, 5), (5, 1), (2, 3), (4, 5)],
    # middles 2, 3, 4; extra vertices 5, 6; chords 2-3, 3-4, 5-6
    "B": [(0, 2), (2, 1), (0, 3), (3, 1), (0, 4), (4, 1), (0, 5), (5, 2), (5, 6), (6, 4), (6, 1), (2, 3), (3, 4)],
}


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.V = 1 + max(max(e) for e in edges)
        self.adj = {v: [] for v in range(self.V)}
        for idx, (a, b) in enumerate(edges):
            self.adj[a].append((b, idx))
            self.adj[b].append((a, idx))
        self.eid = {frozenset(e): i for i, e in enumerate(edges)}
        self.middles = sorted(u for u, _ in self.adj[N] if any(x == F for x, _ in self.adj[u]))

    def edge(self, a, b):
        return self.eid[frozenset((a, b))]

    def walk_le(self, W, rng):
        """Edges of the forward loop erasure of a W-walk from N stopped at F."""
        path = [N]
        pos = {N: 0}
        v = N
        while v != F:
            nb = self.adj[v]
            r = rng.random() * sum(W[e] for _, e in nb)
            acc = 0.0
            for u, e in nb:
                acc += W[e]
                if r < acc:
                    break
            v = u
            if v in pos:
                k = pos[v]
                for x in path[k + 1:]:
                    del pos[x]
                path = path[:k + 1]
            else:
                pos[v] = len(path)
                path.append(v)
        return [self.edge(path[t], path[t + 1]) for t in range(len(path) - 1)]

    def hit(self, W):
        """h(v) = P_v(tau_F < tau_N)."""
        A = np.eye(self.V)
        b = np.zeros(self.V)
        b[F] = 1.0
        for v in range(self.V):
            if v in (N, F):
                continue
            tot = sum(W[e] for _, e in self.adj[v])
            for u, e in self.adj[v]:
                A[v, u] -= W[e] / tot
        return np.linalg.solve(A, b)


def check_identities(g, rng, M=200000):
    W = [rng.uniform(0.5, 5.0) for _ in g.edges]
    h = g.hit(W)
    C = sum(W[e] * h[u] for u, e in g.adj[N])
    cnt = [0] * len(g.edges)
    for _ in range(M):
        for e in g.walk_le(W, rng):
            cnt[e] += 1
    worst = 0.0
    lines = []
    for u, e in g.adj[N]:
        ex, mc = W[e] * h[u] / C, cnt[e] / M
        worst = max(worst, abs(ex - mc) / math.sqrt(ex * (1 - ex) / M))
        lines.append("  N-%d exact %.4f mc %.4f" % (u, ex, mc))
    for u, e in g.adj[F]:
        ex, mc = W[e] * (1 - h[u]) / C, cnt[e] / M
        worst = max(worst, abs(ex - mc) / math.sqrt(ex * (1 - ex) / M))
        lines.append("  %d-F exact %.4f mc %.4f" % (u, ex, mc))
    return lines, worst


def long_run(g, seed, n_tot, marks):
    rng = random.Random(seed)
    W = [1.0] * len(g.edges)
    m = g.middles
    out = []
    for n in range(1, n_tot + 1):
        for e in g.walk_le(W, rng):
            W[e] += 1
        if n in marks:
            Q = [W[g.edge(N, i)] * W[g.edge(i, F)] for i in m]
            lr = [math.log(Q[k] / Q[0]) for k in range(1, len(m))]
            shares = [W[g.edge(N, i)] / n for i in m]
            off = max(W[e] / n for e in range(len(g.edges))
                      if e not in {g.edge(N, i) for i in m} | {g.edge(i, F) for i in m})
            out.append((n, lr, shares, off))
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    rng = random.Random(20261116)
    for name, edges in GRAPHS.items():
        g = Graph(edges)
        lines, worst = check_identities(g, rng)
        print("graph %s, middles %s: edge identities, exact vs Monte Carlo (200000 walks)" % (name, g.middles))
        print("\n".join(lines))
        print("  largest deviation in standard errors: %.2f" % worst)
    marks = (2000, 10000, 30000, 60000, 100000)
    for name, edges in GRAPHS.items():
        g = Graph(edges)
        for seed in (1, 2, 3):
            print("graph %s seed %d: n, log(Q_i/Q_%d) for i in %s, W_Ni/n, largest off-geodesic W/n"
                  % (name, seed, g.middles[0], g.middles[1:]))
            for n, lr, sh, off in long_run(g, seed, marks[-1], marks):
                print("  %6d  %s  %s  %.4f" % (n, " ".join("%+.3f" % x for x in lr),
                                               " ".join("%.3f" % s for s in sh), off))


if __name__ == "__main__":
    main()
