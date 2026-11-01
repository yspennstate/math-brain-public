# Is K_n a strict local minimum of E_pi C over reversible chains?
# Parametrize by symmetric weights W (off-diagonal and self-loops); P = W / rowsum.
import numpy as np, itertools
from cover_exact import *

def f_from_vec(theta, n, pairs):
    W = np.ones((n, n)) - np.eye(n)
    for t, (i, j) in zip(theta, pairs):
        W[i, j] += t
        if i != j: W[j, i] += t
    return E_pi_cover(rw_on_graph(W))

for n in range(3, 8):
    pairs = [(i, j) for i in range(n) for j in range(i, n)]  # includes self loops (i,i)
    m = len(pairs)
    eps = 1e-3
    f0 = f_from_vec(np.zeros(m), n, pairs)
    grad = np.zeros(m); Hs = np.zeros((m, m))
    fp = {}
    def F(v):
        key = tuple(np.round(v, 9))
        if key not in fp: fp[key] = f_from_vec(v, n, pairs)
        return fp[key]
    for a in range(m):
        e = np.zeros(m); e[a] = eps
        grad[a] = (F(e) - F(-e)) / (2 * eps)
    for a in range(m):
        for b in range(a, m):
            ea = np.zeros(m); ea[a] = eps; eb = np.zeros(m); eb[b] = eps
            Hs[a, b] = Hs[b, a] = (F(ea + eb) - F(ea - eb) - F(-ea + eb) + F(-ea - eb)) / (4 * eps * eps)
    off = [k for k, (i, j) in enumerate(pairs) if i != j]
    diag = [k for k, (i, j) in enumerate(pairs) if i == j]
    print("n=%d f0=%.6f target=%.6f" % (n, f0, target(n)))
    print("   grad off-diag (should be 0): max|.| = %.2e ; grad self-loop dirs: %s" % (np.max(abs(grad[off])), np.round(grad[diag], 4)))
    # Hessian restricted to off-diagonal weights, projected off the scaling direction (all ones)
    Hoff = Hs[np.ix_(off, off)]
    ones = np.ones(len(off)) / np.sqrt(len(off))
    Pj = np.eye(len(off)) - np.outer(ones, ones)
    ev = np.linalg.eigvalsh(Pj @ Hoff @ Pj)
    print("   Hessian eigenvalues on off-diag tangent space (excluding scaling): min %.5f  (all: %s)" % (np.sort(ev)[1], np.round(np.sort(ev), 4)))
