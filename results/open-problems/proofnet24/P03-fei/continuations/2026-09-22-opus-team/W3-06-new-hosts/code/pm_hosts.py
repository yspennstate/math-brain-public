"""Monotone matching/containment properties as hosts: basic statistics (probability, influence, entropy, maximal
false sets by weight) and the value of 'site' coin completions.

A host is a monotone f on m variables given by its minimal true sets (as bitmasks)."""
import sys, os, itertools, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hc import fwht, phi_table, evaluate


def upset_table(m, mins):
    N = 1 << m
    t = np.zeros(N, dtype=bool)
    for a in mins:
        # mark all supersets of a
        t |= (np.arange(N) & a) == a
    return t


def pm_general(nv, allowed_edges=None):
    """perfect matchings of K_nv (or of a graph given by allowed edge list) as edge-index bitmasks."""
    E = allowed_edges if allowed_edges is not None else list(itertools.combinations(range(nv), 2))
    idx = {e: i for i, e in enumerate(E)}
    out = []

    def rec(rem, acc):
        if not rem:
            out.append(acc); return
        a = rem[0]
        for b in rem[1:]:
            e = (a, b) if a < b else (b, a)
            if e in idx:
                rec([v for v in rem if v != a and v != b], acc | (1 << idx[e]))
    rec(list(range(nv)), 0)
    return E, out


def stats(name, m, truth):
    N = 1 << m
    t = int(truth.sum())
    f = np.where(truth, -1, 1).astype(np.int64)
    W = fwht(f)
    I = 0.0
    pc = np.array([bin(s).count('1') for s in range(N)])
    I = float((pc * (W.astype(np.float64) / N) ** 2).sum())
    w2 = (W.astype(np.float64) / N) ** 2
    nz = w2 > 0
    H = float(-(w2[nz] * np.log2(w2[nz])).sum())
    # maximal false sets by weight
    x = np.arange(N)
    maxfalse = []
    for i in range(m):
        pass
    isfalse = ~truth
    upall = np.ones(N, dtype=bool)
    for i in range(m):
        y = x | (1 << i)
        upall &= (y == x) | truth[y]
    mf = x[isfalse & upall]
    wts = np.bincount(pc[mf], minlength=m + 1)
    print(f"{name}: m={m} Pr[true]={t}/{N}={t/N:.4f} deficit cells N-2t={N-2*t} I={I:.4f} H(incl. mean)={H:.4f} "
          f"maximal false sets by weight={wts.tolist()}", flush=True)
    return dict(t=t, I=I, H=H, mf=mf, wts=wts)


if __name__ == '__main__':
    # K_{3,3}
    E33 = [(r, 3 + c) for r in range(3) for c in range(3)]
    _, pm33 = pm_general(6, E33)
    stats('PM(K33)', 9, upset_table(9, pm33))
    # K_6
    E6, pm6 = pm_general(6)
    s6 = stats('PM(K6)', 15, upset_table(15, pm6))
    # K_{2,2,2} octahedron (12 edges), prism, cube, Petersen(15), K_4 (6)
    E4, pm4 = pm_general(4)
    stats('PM(K4)', 6, upset_table(6, pm4))
    Eoct = [e for e in itertools.combinations(range(6), 2) if e not in [(0, 1), (2, 3), (4, 5)]]
    _, pmo = pm_general(6, Eoct)
    stats('PM(K222)', 12, upset_table(12, pmo))
    Eprism = [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5), (0, 3), (1, 4), (2, 5)]
    _, pmp = pm_general(6, sorted(tuple(sorted(e)) for e in Eprism))
    stats('PM(prism)', 9, upset_table(9, pmp))
    Ecube = sorted(tuple(sorted((a, a ^ (1 << i)))) for a in range(8) for i in range(3) if a < a ^ (1 << i))
    _, pmc = pm_general(8, Ecube)
    stats('PM(Q3)', 12, upset_table(12, pmc))
    # K_{3,3} plus one edge inside a side (10 edges) and K_{3,3} plus a PM of each side? skip
    # Petersen graph
    outer = [(i, (i + 1) % 5) for i in range(5)]
    inner = [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    spokes = [(i, 5 + i) for i in range(5)]
    Epet = sorted(tuple(sorted(e)) for e in outer + inner + spokes)
    _, pmpet = pm_general(10, Epet)
    stats('PM(Petersen)', 15, upset_table(15, pmpet))
    # K_{2,4}+... bipartite 3x4 saturating left side
    E34 = [(r, 3 + c) for r in range(3) for c in range(4)]
    idx = {e: i for i, e in enumerate(E34)}
    mins = []
    for cols in itertools.permutations(range(4), 3):
        mins.append(sum(1 << idx[(r, 3 + cols[r])] for r in range(3)))
    stats('Match3(K34)', 12, upset_table(12, mins))
