# Battery of graph DNFs f_G = OR_{uv in E} x_u x_v: H/I, averaged step, erasure, and the restriction-step ratio
# Delta_v/Inf_v at the best vertex (rho0), at a max-degree vertex and at a min-degree vertex.
import sys, itertools, random, numpy as np
from gdnf import summary, truth_table, analyse

def path(n): return [(i, i + 1) for i in range(n - 1)]
def cycle(n): return [(i, (i + 1) % n) for i in range(n)]
def star(k): return [(0, i) for i in range(1, k + 1)]
def complete(n): return list(itertools.combinations(range(n), 2))
def kab(a, b): return [(i, a + j) for i in range(a) for j in range(b)]
def grid(r, c):
    e = []
    for i in range(r):
        for j in range(c):
            v = i * c + j
            if j + 1 < c: e.append((v, v + 1))
            if i + 1 < r: e.append((v, v + c))
    return e
def hypercube(d): return [(v, v ^ (1 << k)) for v in range(1 << d) for k in range(d) if v < v ^ (1 << k)]
def petersen():
    outer = [(i, (i + 1) % 5) for i in range(5)]
    inner = [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    spokes = [(i, 5 + i) for i in range(5)]
    return outer + inner + spokes
def paley(q):
    sq = {(x * x) % q for x in range(1, q)}
    return [(i, j) for i in range(q) for j in range(i + 1, q) if (j - i) % q in sq]
def crown(k): return [(i, k + j) for i in range(k) for j in range(k) if i != j]
def matching(m): return [(2 * i, 2 * i + 1) for i in range(m)]
def random_regular(n, d, rng):
    for _ in range(1000):
        stubs = [v for v in range(n) for _ in range(d)]
        rng.shuffle(stubs)
        e = set(); ok = True
        for i in range(0, len(stubs), 2):
            u, v = stubs[i], stubs[i + 1]
            if u == v or (min(u, v), max(u, v)) in e: ok = False; break
            e.add((min(u, v), max(u, v)))
        if ok: return sorted(e)
    return None
def gnp(n, p, rng): return [(i, j) for i in range(n) for j in range(i + 1, n) if rng.random() < p]

if __name__ == '__main__':
    rng = random.Random(1)
    # sanity: AND_2 = single edge on 2 vertices: H = 2, I = 1
    o, r = summary(2, [(0, 1)], name='AND2')
    assert abs(o['H'] - 2) < 1e-12 and abs(o['I'] - 1) < 1e-12, o
    assert abs(r['P'].sum() - 1) < 1e-12 and abs(r['Inf'].sum() - r['I']) < 1e-12
    fams = []
    for n in (4, 8, 12, 16, 20): fams.append(('path%d' % n, n, path(n)))
    for n in (4, 8, 12, 16, 20): fams.append(('cycle%d' % n, n, cycle(n)))
    for k in (3, 7, 12, 19): fams.append(('star%d' % k, k + 1, star(k)))
    for n in (5, 8, 12, 16, 20): fams.append(('K%d' % n, n, complete(n)))
    for a, b in ((2, 2), (3, 3), (4, 4), (2, 10), (5, 5), (3, 12), (8, 8), (10, 10)): fams.append(('K%d,%d' % (a, b), a + b, kab(a, b)))
    for rr, cc in ((3, 3), (3, 4), (4, 4), (4, 5)): fams.append(('grid%dx%d' % (rr, cc), rr * cc, grid(rr, cc)))
    for d in (2, 3, 4): fams.append(('Q%d' % d, 1 << d, hypercube(d)))
    fams.append(('petersen', 10, petersen()))
    for q in (5, 13, 17): fams.append(('paley%d' % q, q, paley(q)))
    for k in (3, 4, 6, 8, 10): fams.append(('crown%d' % k, 2 * k, crown(k)))
    for m in (4, 8, 10): fams.append(('matching%d' % m, 2 * m, matching(m)))
    for n, d in ((12, 3), (16, 3), (20, 3), (16, 5), (20, 5), (20, 8), (18, 10)):
        for s in range(2):
            e = random_regular(n, d, rng)
            if e: fams.append(('rr%d_d%d_s%d' % (n, d, s), n, e))
    for n, p in ((16, 0.1), (16, 0.2), (20, 0.1), (20, 0.15), (20, 0.3), (20, 0.5)):
        fams.append(('gnp%d_%.2f' % (n, p), n, gnp(n, p, rng)))
    print('%-16s %3s %4s %10s %8s %9s %7s %8s %8s %7s %4s %8s %8s %8s' % ('graph', 'n', 'm', 'Var', 'I', 'H', 'H/I',
          'avgstep', 'erasure', 'rho0', 'deg', 'r@maxdeg', 'r@mindeg', 'r_max'))
    for name, n, e in fams:
        o, _ = summary(n, e, name=name)
        print('%-16s %3d %4d %10.3e %8.4f %9.4f %7.4f %8.4f %8.4f %7.4f %4d %8.4f %8.4f %8.4f' % (name, n, o['m'], o['Var'],
              o['I'], o['H'], o['HI'], o['avgstep'], o['erasure'], o['rho0'], o['rho0_deg'], o['ratio_maxdeg'],
              o['ratio_mindeg'], o['ratio_max']), flush=True)
