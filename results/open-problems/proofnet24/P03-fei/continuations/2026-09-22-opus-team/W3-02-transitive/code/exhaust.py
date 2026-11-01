"""Exhaustive enumeration of all G-invariant Boolean functions for small transitive groups.

For each function (global sign fixed: F[orbit of x=0] = +1) computes H, I and orbit quantities and
records: max H/I over non-constant functions, max H/(I-1) over exactly balanced functions, and
the maxima of the orbit ratios Horb/I and Elog/I (Horb = entropy of the orbit of S, Elog = E log2|orbit|).
Usage: python exhaust.py NAME   (NAME in the table below)
"""
import sys, time, json
import numpy as np
import os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tlib
tlib.setup_process()


def space(name):
    if name.startswith('Z'):
        n = int(name[1:]); return tlib.InvariantSpace(tlib.cyclic_gens(n), n, name)
    if name.startswith('D'):
        n = int(name[1:]); return tlib.InvariantSpace(tlib.dihedral_gens(n), n, name)
    if name.startswith('K') and len(name) == 2:
        g, n, _ = tlib.graph_gens(int(name[1])); return tlib.InvariantSpace(g, n, name)
    if name.startswith('B'):  # Bab bipartite
        a, b = int(name[1]), int(name[2]); g, n = tlib.bipartite_gens(a, b, transpose=(a == b))
        return tlib.InvariantSpace(g, n, name)
    if name.startswith('W'):  # Wws wreath S_w wr S_s
        w, s = int(name[1]), int(name[2]); g, n = tlib.wreath_gens(w, s)
        return tlib.InvariantSpace(g, n, name)
    if name.startswith('A'):  # AGL(1,p)
        p = int(name[1:]); return tlib.InvariantSpace(tlib.affine_line_gens(p), p, name)
    if name.startswith('T'):  # Z_2^k regular
        k = int(name[1:]); return tlib.InvariantSpace(tlib.translations_F2(k), 1 << k, name)
    raise ValueError(name)


def run(name, batch_bits=16):
    V = space(name)
    k = V.k
    assert V.reps[0] == 0
    t0 = time.time()
    osz = V.osize.astype(np.float64)
    lev = V.level.astype(np.float64)
    logo = np.log2(osz)
    free = k - 1
    total = 1 << free
    B = 1 << min(batch_bits, free)
    best = dict(ratio=-1, bal=-1, horb=-1, elog=-1, naive=-1)
    arg = {}
    cnt_bal = 0
    idx = np.arange(B, dtype=np.int64)
    bitsB = ((idx[:, None] >> np.arange(min(batch_bits, free))) & 1)
    for hi in range(total // B):
        Fb = np.ones((B, k))
        nb = min(batch_bits, free)
        Fb[:, 1:1 + nb] = 1 - 2 * bitsB
        if free > nb:
            hb = ((hi >> np.arange(free - nb)) & 1)
            Fb[:, 1 + nb:] = 1 - 2 * hb[None, :]
        C = Fb @ V.K
        P = C * C
        with np.errstate(divide='ignore', invalid='ignore'):
            L = np.where(P > 0, -np.log2(np.where(P > 0, P, 1.0)), 0.0)
        H = (osz * P * L).sum(1)
        I = (osz * lev * P).sum(1)
        W = osz * P
        with np.errstate(divide='ignore', invalid='ignore'):
            Horb = np.where(W > 0, -W * np.log2(np.where(W > 0, W, 1.0)), 0.0).sum(1)
        Elog = (W * logo).sum(1)
        nz = I > 1e-12
        r = np.where(nz, H / np.where(nz, I, 1), -1)
        j = int(np.argmax(r))
        if r[j] > best['ratio']:
            best['ratio'] = float(r[j]); arg['ratio'] = Fb[j].astype(int).tolist(); arg['ratio_HI'] = [float(H[j]), float(I[j])]
        hr = np.where(nz, Horb / np.where(nz, I, 1), -1)
        j = int(np.argmax(hr))
        if hr[j] > best['horb']:
            best['horb'] = float(hr[j]); arg['horb'] = Fb[j].astype(int).tolist()
        er = np.where(nz, Elog / np.where(nz, I, 1), -1)
        j = int(np.argmax(er))
        if er[j] > best['elog']:
            best['elog'] = float(er[j]); arg['elog'] = Fb[j].astype(int).tolist()
        bal = np.abs(C[:, 0]) < 1e-12
        cnt_bal += int(bal.sum())
        if bal.any():
            rb = np.where(bal & (I > 1 + 1e-9), H / np.where(bal, I - 1, 1), -1)
            j = int(np.argmax(rb))
            if rb[j] > best['bal']:
                best['bal'] = float(rb[j]); arg['bal'] = Fb[j].astype(int).tolist(); arg['bal_HI'] = [float(H[j]), float(I[j])]
    out = dict(name=name, n=V.n, orbits=k, functions=total, balanced=cnt_bal, best=best, arg=arg,
               seconds=time.time() - t0, reps=V.reps.tolist(), osize=V.osize.tolist())
    print(json.dumps({kk: out[kk] for kk in ('name', 'n', 'orbits', 'functions', 'balanced', 'best', 'seconds')}))
    return out


if __name__ == '__main__':
    res = []
    for nm in sys.argv[1:]:
        res.append(run(nm))
    tag = '_'.join(sys.argv[1:])
    with open(os.path.join(HERE, '..', 'logs', 'exhaust_%s.json' % tag), 'w') as fh:
        json.dump(res, fh)
