"""BREAK-IT test of the semicircular-mixture conjecture, via the density.

If gamma_T = sqrt(V) S with S standard semicircular, then the density of
gamma_T is a superposition of semicircle densities,

    f(t) = E[ sqrt(4V - t^2)_+ / (2 pi V) ],     f(0) = E[V^{-1/2}]/pi,

and more usefully the whole profile f(t) is determined by the mixing law.
The mixing law's moments are s_k = m_2k/Cat_k, known exactly through k = 11.
This script:

  1. builds a discrete approximant of V by Gauss quadrature on (s_k),
  2. predicts f(t) on a grid,
  3. simulates real random symmetric Toeplitz matrices and estimates f(t)
     from eigenvalues - a completely independent data path (no moments, no
     polytopes),
  4. compares.  A gross mismatch refutes the conjecture.

Compute politeness: threads capped, small matrices, few replicates.

Run:  python -u density_falsification.py
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
os.environ.setdefault("MKL_NUM_THREADS", "2")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "2")

import sys
from fractions import Fraction as Fr
from math import comb, sqrt, pi
import numpy as np

def cat(k):
    return comb(2 * k, k) // (k + 1)

mT = {0: Fr(1), 1: Fr(1), 2: Fr(8,3), 3: Fr(11), 4: Fr(908,15), 5: Fr(415),
      6: Fr(23840,7), 7: Fr(325719,10), 8: Fr(112135066,315),
      9: Fr(3065263961,700), 10: Fr(69174280444,1155),
      11: Fr(5680684105259,6300)}
s = [mT[k] / cat(k) for k in range(12)]

def jacobi(mom, n):
    L = {i: mom[i] for i in range(len(mom))}
    polys = {0: {0: Fr(1)}}
    def lp(p, q):
        t = Fr(0)
        for i, a in p.items():
            for j, b in q.items():
                if i + j < len(mom):
                    t += a * b * L[i + j]
        return t
    h = {0: lp(polys[0], polys[0])}
    aa, bb = [], []
    for k in range(n):
        xp = {i + 1: c for i, c in polys[k].items()}
        ak = lp(xp, polys[k]) / h[k]
        aa.append(ak)
        nxt = dict(xp)
        for i, c in polys[k].items():
            nxt[i] = nxt.get(i, Fr(0)) - ak * c
        if k >= 1:
            b2 = h[k] / h[k - 1]
            bb.append(b2)
            for i, c in polys[k - 1].items():
                nxt[i] = nxt.get(i, Fr(0)) - b2 * c
        polys[k + 1] = nxt
        h[k + 1] = lp(polys[k + 1], polys[k + 1])
    return aa, bb

def gauss(mom, n):
    aa, bb = jacobi(mom, n)
    J = np.zeros((n, n))
    for i in range(n):
        J[i, i] = float(aa[i])
    for i in range(n - 1):
        J[i, i + 1] = J[i + 1, i] = sqrt(float(bb[i]))
    ev, evec = np.linalg.eigh(J)
    return ev, evec[0, :] ** 2

nodes, wts = gauss(s, 5)
print("mixing-law quadrature nodes/weights:")
for v, w in zip(nodes, wts):
    print(f"   V={v:8.4f}  w={w:.6f}")

def predicted_density(t):
    tot = 0.0
    for v, w in zip(nodes, wts):
        if 4 * v - t * t > 0:
            tot += w * sqrt(4 * v - t * t) / (2 * pi * v)
    return tot

print("\nsimulating real symmetric Toeplitz matrices...", flush=True)
rng = np.random.default_rng(20260824)
N = 700
REPS = 6
eigs = []
for rep in range(REPS):
    a = rng.standard_normal(N)
    idx = np.abs(np.subtract.outer(np.arange(N), np.arange(N)))
    T = a[idx] / sqrt(N)
    eigs.append(np.linalg.eigvalsh(T))
    print(f"   rep {rep+1}/{REPS} done", flush=True)
ev = np.concatenate(eigs)
print(f"eigenvalues: {ev.size}, empirical m2={np.mean(ev**2):.4f} (exact 1), "
      f"m4={np.mean(ev**4):.4f} (exact {float(mT[2]):.4f})")

grid = np.linspace(0.0, 2.5, 11)
h = 0.15
print("\n   t     predicted   simulated   ratio")
rows = []
for t in grid:
    sim = np.mean(np.abs(np.abs(ev) - t) < h) / (2 * h) / 2 * 2
    # density estimate symmetric: count both tails around +-t
    sim = (np.mean(np.abs(ev - t) < h) + np.mean(np.abs(ev + t) < h)) / (2 * 2 * h)
    pred = predicted_density(t)
    rows.append((t, pred, sim))
    r = sim / pred if pred > 1e-12 else float("nan")
    print(f"  {t:4.2f}   {pred:9.4f}   {sim:9.4f}   {r:6.3f}")

mask = [(p > 0.02) for _, p, _ in rows]
rel = [abs(sim - p) / p for (t, p, sim), m in zip(rows, mask) if m]
worst = max(rel)
print(f"\nworst relative deviation on the bulk: {worst:.3f}")
if worst < 0.25:
    print("CONJECTURE SURVIVES the density test (deviations within the "
          "combined quadrature-truncation and finite-n error)")
else:
    print("*** DENSITY TEST FLAGS A MISMATCH - investigate before trusting "
          "the mixture conjecture ***")
