"""Check the leveled-tower recursion against direct Walsh transforms of the composed truth tables."""
import numpy as np, itertools, math
import tlib, towers
tlib.setup_process()

def compose(G, f, kf):
    """truth table of G(f(x^1),...,f(x^k)) on k*kf variables (block j = bits j*kf..)"""
    k = G.k
    N = 1 << (k * kf)
    x = np.arange(N)
    idx = np.zeros(N, dtype=np.int64)
    for j in range(k):
        blk = (x >> (j * kf)) & ((1 << kf) - 1)
        val = f[blk]            # +-1 ; true = -1
        idx |= ((val < 0).astype(np.int64) << j)
    return G.table[idx]

gl = {g.name: g for g in towers.gate_library()}
seqs = [('AND2', 'OR2'), ('MAJ3', 'AND2'), ('OR3', 'AND2'), ('THR4_2', 'AND3')]
for seq in seqs:
    f = np.array([1.0, -1.0])  # dictator, true = -1
    kf = 1
    st = (0.5, 0.0, 1.0, ())
    for nm in seq:
        g = gl[nm]
        f = compose(g, f, kf); kf *= g.k
        st = towers.step(st, g)
    H, I, c = tlib.spectral_stats(f)
    p = float((f < 0).mean())
    print(seq, 'direct p=%.12f H=%.12f I=%.12f | recursion p=%.12f H=%.12f I=%.12f' % (p, H, I, st[0], st[1], st[2]))
