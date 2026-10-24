"""Independent exact replication of the depth-1..4 values behind W-E3/W-E5 (evidence, not a proved claim):
AND-OR tree, fan-in 2, alternating, AND on top; left-to-right short-circuit decision tree; cells of the level set f = 1;
path order inside each cell (root first). Prints H/I and R_path/I with R as in Prop 12.1. Author's exact values:
H/I = 2.00, 2.23, 3.62, 3.66 and R_path/I = 0.250, 0.490, 0.644, 0.967 for d = 1..4.
"""
import math
import numpy as np
from rc_common import coords, fwht_int, popcount


def formula(d, op='AND', start=0):
    if d == 0:
        return ('var', start), start + 1
    nxt = 'OR' if op == 'AND' else 'AND'
    l, s = formula(d - 1, nxt, start)
    r, s = formula(d - 1, nxt, s)
    return (op, [l, r]), s


def ev(node, asg):
    """Short-circuit evaluation: returns True/False or ('need', var)."""
    if node[0] == 'var':
        v = node[1]
        return asg[v] if v in asg else ('need', v)
    for ch in node[1]:
        r = ev(ch, asg)
        if isinstance(r, tuple):
            return r
        if node[0] == 'AND' and r is False:
            return False
        if node[0] == 'OR' and r is True:
            return True
    return node[0] == 'AND'


def cells(node, asg=None, path=()):
    asg = asg or {}
    r = ev(node, asg)
    if not isinstance(r, tuple):
        return [(path, r)]
    v = r[1]
    out = []
    for val in (True, False):
        a2 = dict(asg); a2[v] = val
        out += cells(node, a2, path + ((v, val),))
    return out


def eval_full(node, X):
    if node[0] == 'var':
        return X[node[1]] == 1
    vals = [eval_full(c, X) for c in node[1]]
    out = vals[0]
    for v_ in vals[1:]:
        out = (out & v_) if node[0] == 'AND' else (out | v_)
    return out


for d in range(1, 5):
    fm, n = formula(d)
    X = coords(n)
    f = np.where(eval_full(fm, X), 1, -1).astype(np.int8)
    F = fwht_int(f).astype(np.float64)
    N = 1 << n
    S = np.nonzero(F)[0]
    p = (F[S] / N) ** 2
    size = np.array([popcount(int(s)) for s in S])
    H = float(-(p * np.log2(p)).sum())
    nz = S != 0
    I = float((p * size).sum())
    cl = [path for path, val in cells(fm) if val is True]
    # owner weights and rank sums, vectorized over sets
    wsum = np.zeros(len(S)); rsum = np.zeros(len(S))
    for path in cl:
        V = 0
        for v, val in path:
            V |= 1 << v
        own = ((S & ~V) == 0) & nz
        pl = 2.0 ** (-len(path))
        rk = np.zeros(len(S))
        for pos, (v, val) in enumerate(path):
            has = ((S >> v) & 1).astype(bool) & own
            rk[has] += np.maximum(0.0, np.log2((pos + 1) / size[has]))
        wsum[own] += pl
        rsum[own] += pl * rk[own]
    assert np.all(wsum[nz] > 0)
    R = float((p[nz] * rsum[nz] / wsum[nz]).sum())
    print(f'd={d} n={n}: H/I = {H / I:.4f}   R_path/I = {R / I:.4f}   cells(f=1) = {len(cl)}')
