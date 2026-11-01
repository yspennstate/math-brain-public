"""Structure of the J = H/(I-1) maximisers found exhaustively (n<=5) and by annealing (n=6)."""
import sys, json
import numpy as np
sys.path.insert(0, '.')
from core import polite, stats, is_prime, decompose, walsh_int, compress
from structure import max_coin_set, core_with_holes, hole_shape, interaction_matrix
polite()
out = open('../logs/analyze_J.log', 'w')
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n')
def tab(s):
    return np.array([-1 if ch == '1' else 1 for ch in s], dtype=np.int8)
cands = {
 'J4_max (n=4, J=6)': '1100000011101110',
 'J5_best5var (J=5.947)': '11101010110000001110111011100000',
 'J5_second (J=5.7735)': '11110000000000001111010101110111',
 'J5_composite_best (5.6)': None,
}
rows = json.load(open('../logs/search_J_n6_s1.json'))
cands['J6_max (n=6, J=6.347)'] = rows[0]['table']
cands['J6_second (6.2789)'] = [r for r in rows if abs(r['value'] - 6.278945253) < 1e-6][0]['table']
for name, s in cands.items():
    if s is None: continue
    t = tab(s)
    st = stats(t)
    Y = max_coin_set(t)
    X, core, holes = core_with_holes(t, Y)
    W = walsh_int(t) / t.shape[0]
    nz = np.abs(W[np.abs(W) > 1e-12])
    log('== %s   table %s' % (name, s))
    log('   H=%.9f I=%.6f J=%.9f  prime=%s  rho0=%.5f  nonzero coefficients=%d  distinct |fhat|=%s' % (
        st['H'], st['I'], st['H'] / (st['I'] - 1), is_prime(t), st['rho0'], len(nz), sorted(set(np.round(nz, 6)))))
    log('   influences:', np.round(st['Inf'], 5), ' Delta/Inf:', np.round(st['Delta'] / np.maximum(st['Inf'], 1e-300), 4))
    log('   coin set Y =', Y, ' core variables X =', X)
    m = len(X)
    for y in Y:
        cells = holes[y]
        sh = hole_shape(cells, m)
        log('   coin x%d: hole cells (core index, bits over X) %s  -> subcube dim %s exact=%s  Inf=%.5f' % (
            y, cells, sh[0], sh[1], st['Inf'][y]))
    grid = ' '.join('%s:%s' % (format(a, '0%db' % m)[::-1], core[a]) for a in range(1 << m))
    log('   core (x-bits in order X, value):', grid)
    ntrue = sum(1 for a in core if core[a] == 'T'); nfalse = sum(1 for a in core if core[a] == 'F')
    log('   core cells: T=%d F=%d holes=%d of %d' % (ntrue, nfalse, (1 << m) - ntrue - nfalse, 1 << m))
