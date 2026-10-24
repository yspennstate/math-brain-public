"""Numaro's 18-input gate g: core (coordinates 0..8, 512 cells) plus nine auxiliaries (coordinates 9..17), auxiliary j
hosting two core cells that it sets TRUE.  Enumeration of all physical restrictions (each variable free / 0 / 1) up to
a nominal arity, with dummy auxiliaries (hosts outside the surviving core subcube) fixed to 0."""
import os, itertools
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
INP = os.path.join(HERE, "..", "..", "inputs")


def load():
    g = np.load(os.path.join(INP, "numaro18_pm1_table.npy")).astype(np.int8)
    core = g[:512].copy()                                  # all auxiliaries false
    hosts = []
    for j in range(9):
        t = g[(1 << (9 + j)):(1 << (9 + j)) + 512]          # auxiliary j true, the others false
        cells = np.flatnonzero(t != core)
        assert len(cells) == 2 and np.all(core[cells] == 1) and np.all(t[cells] == -1)
        hosts.append(tuple(int(c) for c in cells))
    # the full table is the core with hosts switched on by their auxiliaries
    chk = np.tile(core, 512).reshape(512, 512).copy()
    for j, cells in enumerate(hosts):
        on = (np.arange(512) >> j) & 1
        for c in cells:
            chk[on == 1, c] = -1
    assert np.array_equal(chk.ravel(), g), "host model does not reproduce g"
    return g, core, hosts


def restriction_table(g, assign):
    """assign: length-18 list, entries 'f' (free), 0 or 1.  Returns (+-1 table over the free variables in increasing
    coordinate order, list of free coordinates)."""
    free = [i for i in range(18) if assign[i] == 'f']
    base = sum((1 << i) for i in range(18) if assign[i] == 1)
    k = len(free)
    idx = np.full(1 << k, base, dtype=np.int64)
    ys = np.arange(1 << k)
    for l, j in enumerate(free):
        idx |= ((ys >> l) & 1) << j
    return g[idx].astype(float), free


def essential(vals, k):
    """indices of inputs the table depends on"""
    ess = []
    for i in range(k):
        x = np.arange(1 << k)
        if np.any(vals[x] != vals[x ^ (1 << i)]):
            ess.append(i)
    return ess


def drop_dummies(vals, k):
    ess = essential(vals, k)
    if len(ess) == k:
        return vals, ess
    kk = len(ess)
    ys = np.arange(1 << kk)
    idx = np.zeros(1 << kk, dtype=np.int64)
    for l, i in enumerate(ess):
        idx |= ((ys >> l) & 1) << i
    return vals[idx], ess


def enumerate_restrictions(g, core, hosts, max_nominal=10, min_nominal=1):
    """yield (assign, nominal arity) for every normalized representative: core in {f,0,1}^9, active auxiliaries in
    {f,0,1}, inactive auxiliaries fixed 0 (they are dummies)."""
    for ca in itertools.product(('f', 0, 1), repeat=9):
        nf = sum(1 for v in ca if v == 'f')
        if nf > max_nominal:
            continue
        # surviving core cells
        def alive(cell):
            for i, v in enumerate(ca):
                if v != 'f' and ((cell >> i) & 1) != v:
                    return False
            return True
        act = [j for j in range(9) if alive(hosts[j][0]) or alive(hosts[j][1])]
        for aa in itertools.product(('f', 0, 1), repeat=len(act)):
            na = sum(1 for v in aa if v == 'f')
            if nf + na > max_nominal or nf + na < min_nominal:
                continue
            assign = list(ca) + [0] * 9
            for j, v in zip(act, aa):
                assign[9 + j] = v
            yield assign, nf + na
