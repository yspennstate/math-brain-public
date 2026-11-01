"""Growth along families built from hosts with coin completion (sites.py):
  maj:m         majority on m (odd) variables with a maximal packing of free middle-layer mixed sites
                (M of weight (m+1)/2 made FALSE, its partner M - p TRUE -> coin), constructed greedily
  pmknn:n       perfect matchings of K_{n,n} (m = n^2), coin completion
  pmkn:n        perfect matchings of K_n (m = n(n-1)/2), coin completion
  agq:q:a       AG(2,q): contains a line from the first a parallel classes (m = q^2), coin completion
"""
import sys, os, itertools, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sites import complete
from pm_hosts import upset_table, pm_general
from hc import evaluate, phi_table


def maj_sites(m):
    """Maj_m with free mixed sites: choose middle sets M (|M| = (m+1)/2, TRUE in Maj) and p in M such that
    M - p (FALSE) ... replace both cells by a coin.  A mixed site is free iff s(M) + s(M-p) = m + 1.
    In Maj_m, s(M) = (m+1)/2 (every down-edge flips) and s(M-p) = (m+1)/2, sum m+1: every such edge is free.
    Greedy maximal packing of disjoint edges between the two middle layers."""
    N = 1 << m
    x = np.arange(N)
    pc = np.array([bin(v).count('1') for v in range(N)])
    val = np.where(pc >= (m + 1) // 2, -1, 1).astype(np.int64)
    used = np.zeros(N, dtype=bool)
    c0 = val.copy()
    k = (m + 1) // 2
    for M in x[pc == k]:
        if used[M]:
            continue
        for p in range(m):
            if (M >> p) & 1:
                y = M ^ (1 << p)
                if not used[y]:
                    used[M] = used[y] = True
                    c0[M] = 0; c0[y] = 0
                    break
    return evaluate(c0, m), evaluate(val, m)


def agq_lines(q):
    """AG(2,q) for prime q: points (x,y) -> index q*x + y; parallel classes by slope (inf first)."""
    classes = []
    classes.append([[q * x + y for y in range(q)] for x in range(q)])          # x = const
    for s in range(q):
        classes.append([[q * x + (s * x + b) % q for x in range(q)] for b in range(q)])
    return classes


if __name__ == '__main__':
    out = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs', 'families.log'), 'a')
    which = sys.argv[1]
    if which == 'maj':
        for m in [3, 5, 7, 9, 11, 13, 15]:
            ev, ev0 = maj_sites(m)
            s = f"maj m={m}: Maj alone R={ev0['R']:.6f} I={ev0['I']:.5f} H={ev0['H']:.5f} | with free middle sites " \
                f"R={ev['R']:.6f} I={ev['I']:.5f} H={ev['H']:.5f} coins={ev['holes']//2} nvars={ev['nvars']}"
            print(s, flush=True); out.write(s + "\n"); out.flush()
    if which == 'pm':
        for n in [2, 3, 4]:
            E = [(r, n + c) for r in range(n) for c in range(n)]
            _, pms = pm_general(2 * n, E)
            tr = upset_table(n * n, pms)
            ev, c0 = complete(tr, n * n, local_iters=300 if n < 4 else 60)
            s = f"PM(K_{n},{n}) m={n*n}: Pr={tr.mean():.5f} R={ev['R']:.6f} I={ev['I']:.5f} H={ev['H']:.5f} " \
                f"holes={ev['holes']} pairs={ev['pairs']} nvars={ev['nvars']} dual={ev['dual_used']} Tmax={ev['Tmax']}"
            print(s, flush=True); out.write(s + "\n"); out.flush()
        for nv in [4, 6]:
            E, pms = pm_general(nv)
            m = len(E)
            tr = upset_table(m, pms)
            ev, c0 = complete(tr, m, local_iters=300 if m < 13 else 40)
            s = f"PM(K_{nv}) m={m}: Pr={tr.mean():.5f} R={ev['R']:.6f} I={ev['I']:.5f} H={ev['H']:.5f} " \
                f"holes={ev['holes']} pairs={ev['pairs']} nvars={ev['nvars']} dual={ev['dual_used']}"
            print(s, flush=True); out.write(s + "\n"); out.flush()
    if which == 'ag':
        for q in [2, 3]:
            cl = agq_lines(q)
            for a in range(1, q + 2):
                for ch in itertools.combinations(range(q + 1), a):
                    mins = [sum(1 << p for p in L) for c in ch for L in cl[c]]
                    m = q * q
                    tr = upset_table(m, mins)
                    ev, c0 = complete(tr, m, local_iters=300)
                    s = f"AG(2,{q}) classes {ch}: Pr={tr.mean():.5f} R={ev['R']:.6f} I={ev['I']:.5f} H={ev['H']:.5f} " \
                        f"holes={ev['holes']} pairs={ev['pairs']} nvars={ev['nvars']} dual={ev['dual_used']}"
                    print(s, flush=True); out.write(s + "\n"); out.flush()
                    break  # classes are equivalent under the collineation group for fixed a
    out.close()


def tie_coin_majority(m):
    """m even: c0 = +1 (FALSE) below the middle layer, -1 above, every middle cell a private coin.
    Exact symmetric formulas: W0(S) depends on |S| = k through Krawtchouk sums."""
    from math import comb, log2
    N = 2 ** m
    c = [1 if w < m // 2 else (-1 if w > m // 2 else 0) for w in range(m + 1)]
    Hc = 0.0
    for k in range(m + 1):
        # W0(S) for |S| = k: sum_x c0(x) chi_S(x) = sum_w c[w] K_w(k), K_w(k) = sum_j (-1)^j C(k,j) C(m-k,w-j)
        W = sum(c[w] * sum((-1) ** j * comb(k, j) * comb(m - k, w - j) for j in range(0, min(w, k) + 1)) for w in range(m + 1))
        t = abs(W) / N
        if t > 0:
            Hc += comb(m, k) * t * t * log2(1 / (t * t))
    C = comb(m, m // 2)
    H = Hc + 2 * m * C / N
    I = (m + 1) * C / N
    return H, I, (H / (I - 1) if I > 1 else float('nan')), m + C


if __name__ == '__main__' and sys.argv[1] == 'tie':
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs', 'families.log'), 'a') as out:
        for m in range(2, 31, 2):
            H, I, R, n = tie_coin_majority(m)
            s = f"tie-coin majority m={m}: n={n} H={H:.6f} I={I:.6f} R={R:.6f}"
            print(s); out.write(s + "\n")
