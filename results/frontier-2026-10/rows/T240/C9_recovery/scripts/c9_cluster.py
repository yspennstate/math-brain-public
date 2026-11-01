"""Clustered block frame for the C9 tube (agent H, 18 Oct 2026). Eigenvalues closer than DELTA (single linkage on
|w_i - w_j|) form one block; the block's columns are an orthonormal basis of the invariant subspace ker prod (J - w)
(real for a conjugate-closed cluster), oriented deterministically by projecting fixed vectors. An eigenvector frame is
singular where two eigenvalues collide and turn complex (the unstable and a stable eigenvalue do so near t = 331); the
invariant subspace of the pair is continuous there."""
import math
import numpy as np

import os as _os
DELTA = float(_os.environ.get('C9_DELTA', '0.02'))   # 0.03 keeps the slow 3-cluster whole past t~421 (gap reaches 0.0200 at node 889)
G = np.array([[1, 2, 3, 4, 5, 6, 7], [7, -6, 5, -4, 3, -2, 1], [1, -1, 2, -2, 3, -3, 4],
              [2, 7, 1, 8, 2, 8, 1], [3, 1, 4, 1, 5, 9, 2], [1, 0, -1, 0, 1, 0, -1], [0, 1, 0, -1, 0, 1, 0]], float).T

def clusters(w, delta=None):
    delta = DELTA if delta is None else delta   # read at call time, so a caller can change DELTA
    n = len(w); parent = list(range(n))
    def find(a):
        while parent[a] != a: a = parent[a]
        return a
    for i in range(n):
        for j in range(i + 1, n):
            if abs(w[i] - w[j]) < delta: parent[find(i)] = find(j)
    groups = {}
    for i in range(n): groups.setdefault(find(i), []).append(i)
    return sorted(groups.values(), key=lambda g: -max(w[i].real for i in g))

def subspace(J, w, g):
    n = J.shape[0]
    if len(g) == 1 and abs(w[g[0]].imag) < 1e-12:
        M = J - w[g[0]].real * np.eye(n)
    else:
        M = np.eye(n)
        for i in g: M = (J - w[i] * np.eye(n)) @ M
        M = M.real
    _, s, Vt = np.linalg.svd(M)
    Q = Vt[-len(g):].T                       # orthonormal basis of ker M
    cols = []
    for gv in G.T:                           # deterministic orientation: Gram-Schmidt on projections of fixed vectors
        v = Q @ (Q.T @ gv)
        for c in cols: v = v - c * (c @ v)
        if np.linalg.norm(v) > 1e-6: cols.append(v / np.linalg.norm(v))
        if len(cols) == len(g): break
    return np.column_stack(cols), s

def frame_c(Jf, delta=None):
    delta = DELTA if delta is None else delta
    w = np.linalg.eigvals(Jf)
    blocks, cols = [], []
    for g in clusters(w, delta):
        Qg, _ = subspace(Jf, w, g)
        blocks.append(list(range(len(cols), len(cols) + Qg.shape[1]))); cols += list(Qg.T)
    return np.column_stack(cols), blocks
