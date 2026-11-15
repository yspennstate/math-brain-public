"""Referee checks of worker claims (FEIB03, FEIB04), written independently of their code.

(1) majority, n odd: alpha(S) = E|D_S f| is the same for every nonempty S; Gamma = H/2 + log2(alpha).
(2) composition with balanced inner gates on disjoint blocks: X(f o g) = X(f) + sum_j Inf_j(f) X(g_j)
    for X = A, Gamma, A1, B (so also H = 2A1 + 2Gamma composes).
truth tables as arrays of +-1 indexed by x (bit i of x = coordinate i, bit set means x_i = -1).
"""
import itertools
import numpy as np


def stats(f):
    N = len(f); n = N.bit_length() - 1
    pc = np.array([bin(s).count("1") for s in range(N)])
    mu = np.zeros(N); up = np.zeros(N); ab = np.zeros(N)
    for S in range(N):
        a = f.astype(float).copy()
        for i in range(n):
            if S >> i & 1:
                h = 1 << i
                a = a.reshape(-1, 2, h)
                a = np.stack([(a[:, 0] + a[:, 1]) / 2, (a[:, 0] - a[:, 1]) / 2], axis=1).reshape(-1)
        c = a[(np.arange(N) & S) == S]
        mu[S] = c.mean() ** 2; up[S] = (c ** 2).mean(); ab[S] = np.abs(c).mean()
    nz = mu > 1e-15
    H = (mu[nz] * np.log2(1 / mu[nz])).sum()
    A = (mu[nz] * np.log2(1 / up[nz])).sum()
    A1 = (mu[nz] * np.log2(1 / ab[nz])).sum()
    G = (mu[nz] * np.log2(ab[nz] / np.sqrt(mu[nz]))).sum()
    B = H - A
    I = (mu * pc).sum()
    inf = np.array([up[1 << i] for i in range(n)])
    return dict(H=H, A=A, A1=A1, G=G, B=B, I=I, inf=inf, ab=ab, mu=mu, n=n)


def table(fn, n):
    xs = np.array(list(itertools.product([1, -1], repeat=n)))[:, ::-1]   # bit i of index -> coordinate i
    return np.array([fn(x) for x in xs])


maj = lambda x: 1 if x.sum() > 0 else -1
print("(1) majority")
for n in (3, 5, 7, 9):
    s = stats(table(maj, n))
    ab = s["ab"][1:]
    print("  n", n, "alpha min/max over nonempty S", ab.min(), ab.max(),
          " Gamma", s["G"], " H/2+log2(alpha)", s["H"] / 2 + np.log2(ab[0]), " Gamma/I", s["G"] / s["I"])

print("(2) composition")
xor2 = lambda x: x[0] * x[1]
maj3 = lambda x: 1 if x.sum() > 0 else -1
and2 = lambda x: -1 if (x[0] == -1 and x[1] == -1) else 1
sel = lambda x: x[1] if x[0] == 1 else x[2]            # balanced mux
cases = [("maj3 o (maj3,maj3,maj3)", maj3, 3, [(maj3, 3)] * 3),
         ("and2 o (xor2, maj3)", and2, 2, [(xor2, 2), (maj3, 3)]),
         ("maj3 o (sel, xor2, maj3)", maj3, 3, [(sel, 3), (xor2, 2), (maj3, 3)]),
         ("and2 o (sel, sel)", and2, 2, [(sel, 3), (sel, 3)])]
for name, f, k, inner in cases:
    sizes = [m for _, m in inner]
    n = sum(sizes)
    offs = np.cumsum([0] + sizes)

    def comp(x, f=f, inner=inner, offs=offs):
        return f(np.array([g(x[offs[j]:offs[j + 1]]) for j, (g, _) in enumerate(inner)]))
    sc = stats(table(comp, n))
    sf = stats(table(f, k))
    sg = [stats(table(g, m)) for g, m in inner]
    out = []
    for X in ("A", "G", "A1", "B", "H"):
        pred = sf[X] + sum(sf["inf"][j] * sg[j][X] for j in range(k))
        out.append("%s %.12f vs %.12f" % (X, sc[X], pred))
    print("  ", name, "|", "; ".join(out))
