"""E1: per lam power, the q-coefficients of N/(1-q) (partial sums of N's q-coefficients) are nonnegative.
Stronger than D3; suggested by kappa(i, t, r) being nondecreasing in t on K_n.
python e1_check.py kn adj|dis nlo nhi   |   python e1_check.py atlas V"""
import sys, itertools
from math import comb


def e1_neg(N):
    """N as {(lam, u power): c}; returns [(lam, q power, partial sum)] that are negative."""
    q = {}
    for (i, k), c in N.items():
        for s in range(k + 1):
            q[(i, s)] = q.get((i, s), 0) + c * comb(k, s) * (-1) ** s
    out = []
    for i in sorted({i for i, _ in q}):
        acc = 0
        for s in range(max(s for ii, s in q if ii == i) + 1):
            acc += q.get((i, s), 0)
            if acc < 0:
                out.append((i, s, acc))
    return out


if __name__ != "__main__":
    pass
elif sys.argv[1] == "kn":
    import rec
    kind, lo, hi = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    for n in range(lo, hi + 1):
        N = {}
        for k, x in enumerate(rec.Npoly(n, kind)):
            for i, c in enumerate(int(c) for c in x.coeffs()):
                if c:
                    N[(i, k)] = c
        bad = e1_neg(N)
        print('K_%d %s E1 failures %d' % (n, kind, len(bad)), bad[:3], flush=True)
else:
    import networkx as nx, brute
    V = int(sys.argv[2])
    cnt = bad = 0
    for g in nx.graph_atlas_g():
        if g.number_of_nodes() != V:
            continue
        E = sorted(tuple(sorted(e)) for e in g.edges())
        for e, f in itertools.combinations(E, 2):
            N = brute.N_of(V, E, e, f)
            if not N:
                continue
            cnt += 1
            b = e1_neg(N)
            if b:
                bad += 1
                if bad <= 5:
                    print('FAIL', E, e, f, b[:3], flush=True)
    print('graphs on %d vertices: pairs with N != 0: %d, E1 failures %d' % (V, cnt, bad))
