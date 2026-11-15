"""Independent exact recheck of the K5 run's fork comb (K(n) >= floor(n/2)).

Uses the hitting-time solver from referee_1112/LUMP/check_k4_family.py (Lovasz-Winkler
tmix = max_j max_i (E_i T_j - E_pi T_j)), not the run's grounded-inverse formula.
"""
from fractions import Fraction as F
import sys
sys.path.insert(0, r"~\agent_run\referee_1112\LUMP")


def hitting(P, j):
    n = len(P)
    idx = [i for i in range(n) if i != j]
    m = len(idx)
    A = [[(F(1) if a == b else F(0)) - P[idx[a]][idx[b]] for b in range(m)] + [F(1)] for a in range(m)]
    for c in range(m):
        p = next(r for r in range(c, m) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        piv = A[c][c]
        A[c] = [x / piv for x in A[c]]
        for r in range(m):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    h = [F(0)] * n
    for a in range(m):
        h[idx[a]] = A[a][m]
    return h


def tmix(w):
    n = len(w)
    deg = [sum(r) for r in w]
    tot = sum(deg)
    pi = [d / tot for d in deg]
    P = [[w[i][j] / deg[i] for j in range(n)] for i in range(n)]
    best = F(0)
    for j in range(n):
        h = hitting(P, j)
        hp = sum(pi[i] * h[i] for i in range(n))
        best = max(best, max(h[i] - hp for i in range(n)))
    return best


def lump(w, blocks):
    k = len(blocks)
    return [[sum(w[i][j] for i in blocks[a] for j in blocks[b]) for b in range(k)] for a in range(k)]


def fork_comb(N, t):
    t = F(t); r = t ** 3; al = t
    names = ["a", "b", "c"] + [f"z{k}" for k in range(N + 1)] + [f"y{k}" for k in range(N)]
    ix = {s: i for i, s in enumerate(names)}
    n = len(names)
    w = [[F(0)] * n for _ in range(n)]
    def s(x, y, v):
        w[ix[x]][ix[y]] += v
        if x != y:
            w[ix[y]][ix[x]] += v
    s("a", "z0", F(1))
    for k in range(N):
        s(f"z{k}", f"z{k+1}", r ** (k + 1))
        s(f"y{k}", f"z{k+1}", al * r ** (k + 1))
        s(f"y{k}", f"y{k}", (t - 1) * al * r ** (k + 1))
    s("b", f"z{N}", al * r ** (N + 1))
    s("c", f"z{N}", r ** (N + 2))
    s("a", "a", t - 1)
    s("b", "b", (t - 1) * al * r ** (N + 1))
    s("c", "c", (N + 2) * r ** (N + 4))
    blocks = [[ix["a"]], [ix["b"]], [ix[f"z{N}"], ix["c"]]] + [[ix[f"z{k}"], ix[f"y{k}"]] for k in range(N)]
    return w, blocks


print("N states q  t  ratio")
for N in (0, 1, 2):
    for t in (10, 100, 1000):
        w, blocks = fork_comb(N, t)
        a = tmix(w); b = tmix(lump(w, blocks))
        print(N, len(w), len(blocks), t, f"{float(b / a):.12f}", flush=True)
