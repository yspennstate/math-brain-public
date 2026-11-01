"""Exact check of the vertex-coding inequality for functions of the edges of K_n.

For f on the edges of K_n with spectral sample S, V(S) = vertices touched by S. The bound:
  H(f) <= h(eps) + log2(3) * sum_{N internal node of a binary tree on [n]} Pr[S touches N]
          + H(|S|) + E[ |S| log2( e C(v(S),2) / |S| ) ]
and its consequence with Jensen,
  E[|S| log2(e C(v,2)/|S|)] <= I log2(e E[v(S)^2] / (2 I)).
Also checked, for the k-clique property: Pr[S touches N] <= 4 Pr[some k-clique touches N] Pr[G - N has no k-clique]
(the Parseval / Harris step), and the mixed-component bound for two vertices u, w:
  Pr[S meets E_u - uw and E_w - uw] <= 8 (E[g_A g_B] + E[g_AB]) Pr[G - {u,w} has no k-clique].
"""
import itertools, math, functools
import numpy as np
print = functools.partial(print, flush=True)


def wht(v):
    a = v.astype(np.float64).copy(); n = a.size; h = 1
    while h < n:
        a = a.reshape(-1, 2 * h); x = a[:, :h].copy(); y = a[:, h:].copy()
        a[:, :h] = x + y; a[:, h:] = x - y; a = a.reshape(n); h *= 2
    return a / n


def phi(p):
    return -p * math.log2(p) if p > 0 else 0.0


def graph_setup(n):
    E = list(itertools.combinations(range(n), 2))
    idx = {e: i for i, e in enumerate(E)}
    return E, idx


def clique_tt(n, k):
    E, idx = graph_setup(n); N = len(E)
    masks = [sum(1 << idx[e] for e in itertools.combinations(c, 2)) for c in itertools.combinations(range(n), k)]
    x = np.arange(1 << N)
    f = np.zeros(1 << N, dtype=bool)
    for mk in masks:
        f |= (x & mk) == mk
    return f, masks


def tree_nodes(n):
    """internal nodes of a balanced binary tree with leaves 0..n-1 (as vertex lists)."""
    out = []
    def rec(lo, hi):
        if hi - lo <= 1:
            return
        out.append(list(range(lo, hi)))
        mid = (lo + hi) // 2
        rec(lo, mid); rec(mid, hi)
    rec(0, n)
    return out


def analyse(n, f, name, masks=None, k=None):
    E, idx = graph_setup(n); N = len(E)
    F = np.where(f, -1.0, 1.0)
    P = wht(F) ** 2
    Tset = np.arange(1 << N)
    size = np.array([bin(t).count('1') for t in Tset])
    H = sum(phi(p) for p in P)
    I = float((P * size).sum())
    eps = 1 - P[0]
    if I < 1e-12:
        return
    vmask = [sum(1 << idx[e] for e in E if u in e) for u in range(n)]     # edges at u
    touch = np.array([[bool(t & vmask[u]) for u in range(n)] for t in Tset])
    v = touch.sum(axis=1)
    VI = float((P * v).sum()); Ev2 = float((P * v * v).sum())
    # tree code
    tsum = 0.0
    for node in tree_nodes(n):
        hit = touch[:, node].any(axis=1)
        tsum += float(P[hit].sum())
    # H(|S|)
    Hs = sum(phi(float(P[size == s].sum())) for s in range(N + 1))
    heps = phi(eps) + phi(1 - eps)
    # conditional edge term
    cond = 0.0
    for t in range(1, 1 << N):
        if P[t] > 0:
            M = v[t] * (v[t] - 1) // 2
            cond += P[t] * size[t] * math.log2(math.e * M / size[t])
    bound1 = heps + math.log2(3) * tsum + Hs + cond
    bound2 = heps + math.log2(3) * tsum + Hs + I * math.log2(math.e * Ev2 / (2 * I))
    ok = H <= bound1 + 1e-9 and bound1 <= bound2 + 1e-9
    line = (f"{name:30s} n={n} N={N}: H/I={H/I:.3f}  VI/I={VI/I:.3f}  Ev2/I={Ev2/I:.3f}  tree/I={tsum/I:.3f}  "
            f"bound1/I={bound1/I:.3f}  bound2/I={bound2/I:.3f}  {'ok' if ok else 'FAIL'}")
    if masks is not None:
        # Parseval / Harris check for every tree node
        x = Tset
        worst = 0.0
        for node in tree_nodes(n) + [[u] for u in range(n)]:
            A = 0
            for u in node:
                A |= vmask[u]
            hit = touch[:, node].any(axis=1)
            lhs = float(P[hit].sum())
            touchN = np.zeros(1 << N, dtype=bool)
            avoidN = np.zeros(1 << N, dtype=bool)
            for mk in masks:
                present = (x & mk) == mk
                if mk & A:
                    touchN |= present
                else:
                    avoidN |= present
            rhs = 4 * touchN.mean() * (1 - avoidN.mean())
            worst = max(worst, lhs / rhs if rhs > 0 else (0 if lhs < 1e-15 else float('inf')))
        # mixed component check for pairs u, w
        worst2 = 0.0
        for u, w in itertools.combinations(range(n), 2):
            uw = 1 << idx[(u, w)]
            Am = vmask[u] & ~uw; Bm = vmask[w] & ~uw
            both = np.array([bool(t & Am) and bool(t & Bm) for t in Tset])
            lhs = float(P[both].sum())
            gA = np.zeros(1 << N, dtype=bool); gB = np.zeros(1 << N, dtype=bool)
            gAB = np.zeros(1 << N, dtype=bool); g0 = np.zeros(1 << N, dtype=bool)
            for mk in masks:
                present = (x & mk) == mk
                inu = bool(mk & vmask[u]); inw = bool(mk & vmask[w])
                if inu and inw:
                    gAB |= present
                elif inu:
                    gA |= present
                elif inw:
                    gB |= present
                else:
                    g0 |= present
            rhs = 8 * ((gA & gB).mean() + gAB.mean()) * (1 - g0.mean())
            worst2 = max(worst2, lhs / rhs if rhs > 0 else (0 if lhs < 1e-15 else float('inf')))
        line += f"  | Parseval-Harris max ratio {worst:.3f}  mixed max ratio {worst2:.3f}"
    print(line)


def main():
    for n, k in [(4, 3), (5, 3), (5, 4), (6, 3), (6, 4), (6, 5)]:
        f, masks = clique_tt(n, k)
        analyse(n, f, f"contains K_{k}", masks=masks, k=k)
    # other graph properties on 5 and 6 vertices
    for n in (5, 6):
        E, idx = graph_setup(n); N = len(E); x = np.arange(1 << N)
        deg = np.zeros((1 << N, n), dtype=int)
        for i, (a, b) in enumerate(E):
            bit = (x >> i) & 1
            deg[:, a] += bit; deg[:, b] += bit
        for d in (2, 3):
            analyse(n, deg.max(axis=1) >= d, f"max degree >= {d}")
        ne = np.array([bin(t).count('1') for t in x])
        analyse(n, ne >= N // 2 + 1, "edges >= N/2+1 (majority)")
        # connectivity
        conn = np.zeros(1 << N, dtype=bool)
        for t in range(1 << N):
            adj = {u: set() for u in range(n)}
            for i, (a, b) in enumerate(E):
                if (t >> i) & 1:
                    adj[a].add(b); adj[b].add(a)
            seen = {0}; st = [0]
            while st:
                u = st.pop()
                for w in adj[u]:
                    if w not in seen:
                        seen.add(w); st.append(w)
            conn[t] = len(seen) == n
        analyse(n, conn, "connected")
    rng = np.random.default_rng(1)
    for trial in range(3):
        n = 5; N = 10
        analyse(n, rng.random(1 << N) < 0.5, f"random function #{trial}")


if __name__ == "__main__":
    main()
