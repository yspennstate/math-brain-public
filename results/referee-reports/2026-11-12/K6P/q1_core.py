"""Exact and numerical tools for the single-pair lumping question.

All loops count once in row mass; an edge inside a lump counts twice in
its loop.  No network or worker processes are used.
"""
import os
for _k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[_k] = '1'
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

from fractions import Fraction as Q
from itertools import combinations
import numpy as np


def solve(A, b):
    n = len(b)
    a = [[Q(x) for x in row] + [Q(y)] for row, y in zip(A, b)]
    for j in range(n):
        k = next(k for k in range(j, n) if a[k][j])
        a[j], a[k] = a[k], a[j]
        z = a[j][j]
        a[j] = [x / z for x in a[j]]
        for k in range(n):
            if k != j and a[k][j]:
                z = a[k][j]
                a[k] = [x - z*y for x, y in zip(a[k], a[j])]
    return [row[-1] for row in a]


def exact(w):
    w = [[Q(x) for x in row] for row in w]
    n = len(w)
    d = list(map(sum, w)); W = sum(d); pi = [x/W for x in d]
    H = [[Q(0) for j in range(n)] for i in range(n)]
    L = [[(d[i] if i == j else Q(0))-w[i][j]
          for j in range(n)] for i in range(n)]
    for j in range(n):
        ix = [i for i in range(n) if i != j]
        h = solve([[L[i][k] for k in ix] for i in ix], [d[i] for i in ix])
        for i, v in zip(ix, h): H[i][j] = v
    F = [[H[i][j]-sum(pi[k]*H[k][j] for k in range(n))
          for j in range(n)] for i in range(n)]
    assert all(F[i][j] == F[j][i] for i in range(n) for j in range(n))
    t = max(map(max, F))
    return {'t': t, 'F': F, 'H': H, 'pi': pi, 'W': W,
            'pairs': [(i,j) for i in range(n) for j in range(n) if F[i][j] == t]}


def blocks(n, pair):
    return [[i] for i in range(n) if i not in pair] + [list(pair)]


def lump(w, bs):
    return [[sum(w[i][j] for i in a for j in b) for b in bs] for a in bs]


def numeric(w, details=False):
    n = len(w)
    d = np.sum(w, axis=1); W = np.sum(d); pi = d/W
    root = int(np.argmax(d)); ix = [i for i in range(n) if i != root]
    # Form the diagonal without subtracting the loop (large loops cancel).
    off = w.copy(); np.fill_diagonal(off, 0)
    L = np.diag(np.sum(off, axis=1))-off
    K = np.zeros((n,n)); K[np.ix_(ix,ix)] = np.linalg.inv(L[np.ix_(ix,ix)])
    a = K@d; mu = pi@a
    F = a[:,None]+a[None,:]-mu-W*K
    t = np.max(F)
    return (t, F) if details else t


def scan(w):
    t = numeric(w)
    n = len(w); ans = []
    for pair in combinations(range(n), 2):
        bs = blocks(n, pair)
        wh = np.array(lump(w, bs))
        ans.append((numeric(wh)/t, pair))
    return max(ans)


def exact_scan(w):
    x = exact(w); ans = []
    for pair in combinations(range(len(w)), 2):
        z = exact(lump(w, blocks(len(w), pair)))
        ans.append((z['t']/x['t'], pair, z['t']))
    return x, sorted(ans, reverse=True)


def serialize(x):
    if isinstance(x, Q): return str(x)
    if isinstance(x, np.ndarray): return x.tolist()
    if isinstance(x, dict): return {str(k):serialize(v) for k,v in x.items()}
    if isinstance(x, (list,tuple)): return [serialize(v) for v in x]
    if isinstance(x, np.generic): return x.item()
    return x
