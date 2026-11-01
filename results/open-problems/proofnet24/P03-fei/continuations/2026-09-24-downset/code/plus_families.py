# Family checks for the strengthened inequality (Theorem 1.6) and the composition corollary (Corollary 1.7):
#   * H+ / (I - Var) against Cplus(w) for monotone DNFs/CNFs of width w on up to 20 variables;
#   * the step Delta+_v / Var(D_v f) at the coordinate chosen by the proof (largest influence), against Cplus(w);
#   * H / I for read-once compositions: AND / OR / majority of 2-DNFs on disjoint vertex sets.
import sys, random, itertools, numpy as np
from gdnf import fwht, phi, popcounts
from gdnf_battery import complete, kab, random_regular, gnp, crown, paley, cycle, path, matching

JSC = 2 / np.log(2)
def Psi(r): r = max(r, 0.0); return float(np.log2(np.e * (r + 2 * np.sqrt(r) + 2)))
def Cplus(w): return max(8.80, 2 * (1.0615 + JSC + Psi(2.0 ** (w + 1) - 4)))

def tt_dnf(n, terms):
    x = np.arange(1 << n, dtype=np.int64); f = np.zeros(1 << n, dtype=bool)
    for t in terms:
        m = 0
        for v in t: m |= 1 << v
        f |= (x & m) == m
    return f

def spectral(n, f):
    G = fwht(np.where(f, -1.0, 1.0)) / (1 << n)
    return G

def plus_stats(n, f):
    G = spectral(n, f); P = G * G; N = 1 << n
    pc = popcounts(N)
    Hp = float(phi(P[1:]).sum()); H = float(phi(P).sum())
    I = float((P * pc).sum()); Var = 1 - float(P[0])
    idx = np.arange(N)
    best = None
    for v in range(n):
        m0 = ((idx >> v) & 1) == 0
        a = G[m0]; d = G[idx[m0] | (1 << v)]
        inf = float((d * d).sum())
        if inf < 1e-14: continue
        dp = Hp - 0.5 * (float(phi(((a + d) ** 2)[1:]).sum()) + float(phi(((a - d) ** 2)[1:]).sum()))
        vd = inf - inf * inf
        if best is None or inf > best[0]: best = (inf, dp, vd)
    return H, I, Var, Hp, best

def compose(n_each, leaves, gate):
    """truth table of gate(leaf_1, ..., leaf_k) with leaves on disjoint blocks of n_each variables"""
    k = len(leaves); n = n_each * k
    x = np.arange(1 << n, dtype=np.int64)
    vals = [leaves[j][(x >> (n_each * j)) & ((1 << n_each) - 1)] for j in range(k)]
    s = np.sum(vals, axis=0)
    if gate == 'and': return n, s == k
    if gate == 'or': return n, s >= 1
    if gate == 'maj': return n, s >= (k + 1) // 2
    raise ValueError(gate)

if __name__ == '__main__':
    rng = random.Random(5)
    print('Cplus: w=1 %.3f  w=2 %.3f  w=3 %.3f  w=4 %.3f' % tuple(Cplus(w) for w in (1, 2, 3, 4)))
    rows = []
    fams = []
    for n in (8, 12, 16, 20): fams += [('path%d' % n, n, path(n)), ('cycle%d' % n, n, cycle(n))]
    for n in (8, 12, 16): fams.append(('K%d' % n, n, complete(n)))
    for a, b in ((2, 10), (5, 5), (8, 8)): fams.append(('K%d,%d' % (a, b), a + b, kab(a, b)))
    for m in (4, 8, 10): fams.append(('matching%d' % m, 2 * m, matching(m)))
    for n, d in ((16, 3), (20, 3), (16, 6)):
        e = random_regular(n, d, rng)
        if e: fams.append(('rr%d_d%d' % (n, d), n, e))
    for n, p in ((16, 0.15), (20, 0.1), (20, 0.3)): fams.append(('gnp%d_%.2f' % (n, p), n, gnp(n, p, rng)))
    for (n, mt, w) in ((14, 20, 3), (16, 40, 3), (16, 12, 4), (18, 30, 4)):
        for s in range(2):
            fams.append(('w%d_n%d_m%d_s%d' % (w, n, mt, s), n, [tuple(rng.sample(range(n), w)) for _ in range(mt)]))
    worst_class = 0.0; worst_step = 0.0
    print('%-18s %3s %2s %8s %8s %9s %9s' % ('function', 'n', 'w', 'H/I', 'H+/(I-V)', 'ratio_cls', 'step/Var'))
    for name, n, terms in fams:
        terms = [tuple(t) for t in terms]
        w = max(len(t) for t in terms)
        f = tt_dnf(n, terms)
        for tag, ff in (('dnf', f), ('cnf', ~f[::-1])):       # dual: f*(x) = 1 - f(1-x)
            H, I, Var, Hp, best = plus_stats(n, ff)
            if I - Var < 1e-14: continue
            rc = Hp / (Cplus(w) * (I - Var)); worst_class = max(worst_class, rc)
            st = best[1] / best[2] if best[2] > 1e-14 else 0.0
            worst_step = max(worst_step, st / Cplus(w))
            print('%-18s %3d %2d %8.4f %8.4f %9.4f %9.4f' % (name + '_' + tag, n, w, H / I, Hp / (I - Var), rc, st), flush=True)
    print('largest H+/(Cplus(w)(I-Var)) = %.4f ; largest step/(Cplus(w) Var) at the most influential coordinate = %.4f'
          % (worst_class, worst_step))
    # compositions of 2-DNF leaves
    print('\ncompositions (leaves: 2-DNFs on disjoint vertex sets)')
    leafgraphs = {'P4': (4, path(4)), 'C5': (5, cycle(5)), 'K4': (4, complete(4)), 'star4': (5, [(0, i) for i in range(1, 5)])}
    worst_comp = 0.0
    for gname, (nl, edges) in leafgraphs.items():
        leaf = tt_dnf(nl, edges)
        for gate, k in (('and', 2), ('and', 3), ('and', 4), ('or', 3), ('maj', 3)):
            if nl * k > 20: continue
            n, f = compose(nl, [leaf] * k, gate)
            H, I, Var, Hp, best = plus_stats(n, f)
            c = Cplus(2) if gate in ('and', 'or') else max(Cplus(2), 760.0)
            worst_comp = max(worst_comp, H / I / c)
            print('%-6s %3s(%d) n=%2d  H/I %.4f  H+/(I-Var) %.4f  (bound %.2f)' % (gname, gate, k, n, H / I, Hp / (I - Var), c), flush=True)
    print('largest (H/I)/bound over compositions = %.4f' % worst_comp)
