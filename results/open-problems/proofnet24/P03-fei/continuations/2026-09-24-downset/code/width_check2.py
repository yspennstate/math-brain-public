# Refined check (Psi form) on structured families and random monotone DNFs of width <= w, including cases
# built to push the relative influence down (many short terms sharing vertices, high degree, dense bipartite).
#   T1: Delta_v <= Inf_v (2/ln2 + c0 + Psi(4m/Inf_v - 2)) at every coordinate;
#   T5: at v* = argmax Inf_v, Inf_{v*} >= 4m/(2^(k+1) - 2) with k = shortest certificate (minterm or maxterm) size,
#       hence Delta_{v*}/Inf_{v*} <= 2/ln2 + c0 + Psi(2^(k+1) - 4).
import sys, random, itertools, numpy as np
from gdnf import truth_table, analyse
from gdnf_battery import complete, kab, random_regular, gnp, crown, paley

C0 = 2 * np.exp(-0.5) / np.log(2); JSC = 2 / np.log(2)
def Psi(r): r = max(r, 0.0); return float(np.log2(np.e * (r + 2 * np.sqrt(r) + 2)))

def minterms_min_size(n, f):
    """smallest minterm and smallest maxterm sizes of a monotone truth table (brute force over subsets by size)."""
    N = 1 << n
    best1 = best0 = None
    for k in range(0, n + 1):
        for S in itertools.combinations(range(n), k):
            m = 0
            for v in S: m |= 1 << v
            if best1 is None and f[m]: best1 = k
            if best0 is None and not f[(N - 1) ^ m]: best0 = k
        if best1 is not None and best0 is not None: break
    return best1, best0

def check(n, terms, name, rows):
    f = truth_table(n, terms)
    r = analyse(n, f)
    q = 1.0 - f.mean(); m = min(q, 1 - q)
    Inf, D = r['Inf'], r['Delta']
    rel = Inf > 1e-14
    if not rel.any() or m <= 0: return
    b1 = max(float(D[v] / (Inf[v] * (JSC + C0 + Psi(4 * m / Inf[v] - 2)))) for v in range(n) if rel[v])
    vs = int(np.argmax(Inf)); eps = Inf[vs] / (4 * m)
    k1, k0 = minterms_min_size(n, f) if n <= 16 else (None, None)
    k = min(x for x in (k1, k0) if x is not None) if k1 is not None else None
    epsbound = 1.0 / (2 ** (k + 1) - 2) if k else None
    step = D[vs] / Inf[vs]; bound5 = JSC + C0 + Psi(2 ** (k + 1) - 4) if k else None
    rows.append((name, n, q, r['H'] / r['I'], b1, eps, epsbound, step, bound5, k))

if __name__ == '__main__':
    rng = random.Random(11)
    rows = []
    # dense and high-degree graphs (width 2)
    for n in (6, 10, 14, 16): check(n, complete(n), 'K%d' % n, rows)
    for a, b in ((1, 15), (2, 14), (3, 13), (4, 12), (6, 10), (8, 8)): check(a + b, kab(a, b), 'K%d,%d' % (a, b), rows)
    for k in (4, 6, 8): check(2 * k, crown(k), 'crown%d' % k, rows)
    check(13, paley(13), 'paley13', rows)
    for n, d in ((14, 4), (16, 6), (16, 9), (16, 12)):
        e = random_regular(n, d, rng)
        if e: check(n, e, 'rr%d_d%d' % (n, d), rows)
    # complete multipartite K_{3,3,3,3,3} (15 vertices)
    parts = [list(range(3 * i, 3 * i + 3)) for i in range(5)]
    e = [(u, v) for i in range(5) for j in range(i + 1, 5) for u in parts[i] for v in parts[j]]
    check(15, e, 'K3x5', rows)
    # random width-3/4 DNFs of many terms (unbounded read)
    for (n, mterms, w) in ((12, 40, 3), (14, 80, 3), (14, 20, 3), (16, 120, 3), (12, 30, 4), (14, 60, 4), (16, 16, 3)):
        for s in range(3):
            terms = [tuple(rng.sample(range(n), rng.randint(2, w))) for _ in range(mterms)]
            check(n, terms, 'w%d_n%d_m%d_s%d' % (w, n, mterms, s), rows)
    # width-w CNFs (dual side): AND over clauses = NOT OR over complements; build as monotone via clause list
    for (n, mcl, w) in ((12, 10, 3), (14, 25, 3), (16, 40, 2)):
        clauses = [tuple(rng.sample(range(n), rng.randint(1, w))) for _ in range(mcl)]
        # CNF: f(x) = AND_c OR_{v in c} x_v; compute truth table directly
        N = 1 << n; x = np.arange(N)
        f = np.ones(N, dtype=bool)
        for c in clauses:
            mm = 0
            for v in c: mm |= 1 << v
            f &= (x & mm) != 0
        r = analyse(n, f)
        q = 1.0 - f.mean(); m = min(q, 1 - q)
        if m > 0:
            Inf, D = r['Inf'], r['Delta']
            b1 = max(float(D[v] / (Inf[v] * (JSC + C0 + Psi(4 * m / Inf[v] - 2)))) for v in range(n) if Inf[v] > 1e-14)
            vs = int(np.argmax(Inf)); k1, k0 = minterms_min_size(n, f); k = min(k1, k0)
            rows.append(('cnf_w%d_n%d_m%d' % (w, n, mcl), n, q, r['H'] / r['I'], b1, Inf[vs] / (4 * m),
                         1.0 / (2 ** (k + 1) - 2), D[vs] / Inf[vs], JSC + C0 + Psi(2 ** (k + 1) - 4), k))
    print('%-18s %3s %9s %7s %9s %8s %9s %7s %8s %2s' % ('function', 'n', 'q', 'H/I', 'T1ratio', 'eps*', 'epsbound',
          'step*', 'bound5', 'k'))
    worst1 = 0; worst5 = 0; epsok = True
    for row in rows:
        name, n, q, HI, b1, eps, eb, step, bd, k = row
        worst1 = max(worst1, b1)
        if bd: worst5 = max(worst5, step / bd)
        if eb and eps < eb - 1e-12: epsok = False
        print('%-18s %3d %9.3e %7.4f %9.4f %8.4f %9.4f %7.4f %8.4f %2s' % (name, n, q, HI, b1, eps, eb or 0, step, bd or 0, k))
    print('largest T1 ratio: %.4f ; largest step/bound5: %.4f ; eps* >= 1/(2^(k+1)-2) on every row: %s' % (worst1, worst5, epsok))
