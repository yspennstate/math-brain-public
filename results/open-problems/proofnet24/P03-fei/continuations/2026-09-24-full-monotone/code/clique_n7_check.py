"""Exact check at n = 7 (21 edges, 2^21 spectral coefficients) of every inequality used for the clique property.

For each k = 2..7: exact H/I; the vertex-coding bound of Proposition 2.1 with the exact tree sum and exact E C(v,2);
Lemma 3.1 (touching) at every node of the balanced tree and every single vertex; Lemma 3.2 (pairs) at every pair;
and the rigorous bound B(7,k) of clique_vertex_bound.py. Vectorised with numpy bit operations.
"""
import itertools, math, functools, sys
import numpy as np
print = functools.partial(print, flush=True)
sys.path.insert(0, 'code')
from clique_vertex_bound import Clique


def wht(v):
    a = v.astype(np.float64).copy(); n = a.size; h = 1
    while h < n:
        a = a.reshape(-1, 2 * h); x = a[:, :h].copy(); y = a[:, h:].copy()
        a[:, :h] = x + y; a[:, h:] = x - y; a = a.reshape(n); h *= 2
    return a / n


def popcount(x):
    x = x.astype(np.int64)
    c = np.zeros_like(x)
    while x.any():
        c += x & 1
        x >>= 1
    return c


def tree_nodes(n):
    out = []
    def rec(lo, hi):
        if hi - lo <= 1:
            return
        out.append(list(range(lo, hi)))
        mid = (lo + hi) // 2
        rec(lo, mid); rec(mid, hi)
    rec(0, n)
    return out


def main(n=7):
    E = list(itertools.combinations(range(n), 2)); idx = {e: i for i, e in enumerate(E)}; N = len(E)
    X = np.arange(1 << N, dtype=np.int64)
    size = popcount(X)
    vmask = [sum(1 << idx[e] for e in E if u in e) for u in range(n)]
    touch = np.stack([(X & vmask[u]) != 0 for u in range(n)], axis=1)
    v = touch.sum(axis=1)
    for k in range(2, n + 1):
        masks = [sum(1 << idx[e] for e in itertools.combinations(c, 2)) for c in itertools.combinations(range(n), k)]
        f = np.zeros(1 << N, dtype=bool)
        for mk in masks:
            f |= (X & mk) == mk
        P = wht(np.where(f, -1.0, 1.0)) ** 2
        nz = P > 1e-300
        H = float(-(P[nz] * np.log2(P[nz])).sum()); I = float((P * size).sum()); eps = 1 - float(P[0])
        T = sum(float(P[touch[:, node].any(axis=1)].sum()) for node in tree_nodes(n))
        EC2 = float((P * v * (v - 1) / 2).sum())
        h = (lambda e: 0 if e <= 0 or e >= 1 else -e * math.log2(e) - (1 - e) * math.log2(1 - e))(eps)
        prop_tree = h + eps * math.log2(math.e * I / eps) + math.log2(3) * T + I * math.log2(math.e * EC2 / I)
        # direct coding of V(S) (paper's Proposition 2.1): A + E log2 C(n, v) + I log2(e E C(v,2)/I)
        Ev = float((P * v).sum())
        Vterm = float((P * np.array([math.log2(math.comb(n, int(t))) for t in v])).sum())
        prop = (h + eps * math.log2(math.e * Ev / eps) + eps * math.log2(math.e * I / eps) + Vterm
                + I * math.log2(math.e * EC2 / I))
        # Lemma 3.1 at every tree node and every vertex
        w1 = 0.0
        for node in tree_nodes(n) + [[u] for u in range(n)]:
            A = 0
            for u in node:
                A |= vmask[u]
            lhs = float(P[touch[:, node].any(axis=1)].sum())
            present_touch = np.zeros(1 << N, dtype=bool); present_avoid = np.zeros(1 << N, dtype=bool)
            for mk in masks:
                pr = (X & mk) == mk
                if mk & A:
                    present_touch |= pr
                else:
                    present_avoid |= pr
            rhs = 4 * present_touch.mean() * (1 - present_avoid.mean())
            w1 = max(w1, lhs / rhs if rhs > 0 else (0.0 if lhs < 1e-15 else float('inf')))
        # Lemma 3.2 at every pair
        w2 = 0.0
        for u, w in itertools.combinations(range(n), 2):
            lhs = float(P[touch[:, u] & touch[:, w]].sum())
            uwbit = 1 << idx[(u, w)]
            inS = (X & uwbit) != 0
            pa = np.zeros(1 << N, dtype=bool); pb = np.zeros(1 << N, dtype=bool)
            pc = np.zeros(1 << N, dtype=bool); p0 = np.zeros(1 << N, dtype=bool)
            for mk in masks:
                pr = (X & mk) == mk
                tu = bool(mk & vmask[u]); tw = bool(mk & vmask[w])
                if tu and tw:
                    pc |= pr
                elif tu:
                    pa |= pr
                elif tw:
                    pb |= pr
                else:
                    p0 |= pr
            rhs = float(P[inS].sum()) + 8 * ((pa & pb).mean() + pc.mean()) * (1 - p0.mean())
            w2 = max(w2, lhs / rhs if rhs > 0 else (0.0 if lhs < 1e-15 else float('inf')))
        b = Clique(n, k).bound()
        B = float(b['B_direct']) if b else float('nan')
        print(f"n={n} k={k}: H/I={H/I:.4f}  Prop2.1/I={prop/I:.4f} (tree version {prop_tree/I:.4f})  "
              f"V/I={Vterm/I:.3f}  T/I={T/I:.3f}  EC2/I={EC2/I:.3f}  "
              f"Lemma3.1 max ratio {w1:.3f}  Lemma3.2 max ratio {w2:.3f}  B={B:.3f}  "
              f"{'ok' if H <= prop + 1e-9 and prop <= B * I + 1e-9 and w1 <= 1 + 1e-12 and w2 <= 1 + 1e-12 else 'FAIL'}")


if __name__ == "__main__":
    main()
