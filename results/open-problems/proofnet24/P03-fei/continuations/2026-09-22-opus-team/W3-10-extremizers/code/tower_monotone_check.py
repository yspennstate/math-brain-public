"""Corollary A (towers): rho_0 and min_i B_i/Inf_i are nondecreasing along G_k = g(G_{k-1},...,G_{k-1}) for every
balanced seed g.  Brute-force check at depth 2 on every balanced 3- and 4-variable NPN class (depth 2 = 9 or 16 variables),
and a control: the same comparison for a BIASED seed, where the statement is not claimed."""
import sys
import numpy as np
sys.path.insert(0, '.')
from core import polite, stats, relevant
polite()
out = open('../logs/tower_monotone_check.log', 'w')
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n'); out.flush()

def tower2(g):
    m = int(round(np.log2(g.shape[0])))
    n = m * m
    x = np.arange(1 << n)
    idx = np.zeros(1 << n, dtype=np.int64)
    for j in range(m):
        sub = (x >> (m * j)) & ((1 << m) - 1)
        idx |= ((g[sub] == -1).astype(np.int64)) << j
    return g[idx].astype(np.int8)

for m in (3, 4):
    reps = np.load('../logs/npn_reps_n%d.npy' % m)
    cnt = 0; worst_rho = np.inf; worst_B = np.inf; biased_viol = 0; nb = 0
    for c in reps:
        g = np.array([-1 if (int(c) >> x) & 1 else 1 for x in range(1 << m)], dtype=np.int8)
        if len(relevant(g)) < 2:
            continue
        s1 = stats(g)
        s2 = stats(tower2(g))
        if abs(s1['mean']) < 1e-12:
            cnt += 1
            worst_rho = min(worst_rho, s2['rho0'] - s1['rho0'])
            worst_B = min(worst_B, s2['minB'] - s1['minB'])
        else:
            nb += 1
            if s2['rho0'] < s1['rho0'] - 1e-12:
                biased_viol += 1
    log('m=%d: %d balanced seeds, min over seeds of rho0(G_2)-rho0(g) = %.3e, of minB(G_2)-minB(g) = %.3e ; biased seeds %d, of which rho0 decreased in %d' % (
        m, cnt, worst_rho, worst_B, nb, biased_viol))
