"""Checks of FLOW.md section 2 on every Boolean function of n variables (default 4) or a random sample.

m(R) = sum_{S contains R} mu(S) / C(|S|, |R|)           (flow of a uniformly ordered spectral sample through R)
  (g) sum_R m(R) = I + 1
  (h) A1 = sum_{R nonempty} m(R) (1/|R|) sum_{s in R} log2(alpha(R-s)/alpha(R))     (alpha = E|g_R|)
  (i) generalized Talagrand: m(R) <= up(R) min(1, r!/L^r),  L = ln(||g_R||_2/||g_R||_1)
  (j) size statement: sum_{S contains R, |S-R| <= k} mu(S) <= 3^k ||g_R||_{4/3}^2
  (k) level-1: E_S log2(1/min_{i in S} Inf_i) / I  (report the largest ratio; the proof gives a constant)
usage: python check_flow.py [n] [sample]
"""
import sys
from math import comb, factorial
import numpy as np

n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
N = 1 << n
sample = int(sys.argv[2]) if len(sys.argv) > 2 else 0
rng = np.random.default_rng(3)
if sample:
    F = rng.integers(0, 2, size=(sample, N), dtype=np.int8) * 2 - 1
    # mix in biased functions so that peaked derivatives occur
    q = rng.uniform(0.02, 0.5, size=(sample, 1))
    Fb = (rng.uniform(size=(sample, N)) < q).astype(np.int8) * 2 - 1
    F = np.concatenate([F, Fb], axis=0)
else:
    idx = np.arange(1 << (N - 1), dtype=np.int64)
    F = (1 - 2 * ((idx[:, None] >> np.arange(N)[None, :]) & 1)).astype(np.int8)
    F = F[:, ::-1].copy()
F = F.astype(np.float64)
M = F.shape[0]
pc = np.array([bin(s).count("1") for s in range(N)])


def partial(Fa, S):
    a = Fa.copy()
    for i in range(n):
        if S >> i & 1:
            h = 1 << i
            lo = np.array([x for x in range(N) if not x & h])
            u, v = a[:, lo], a[:, lo | h]
            a[:, lo] = (u + v) / 2
            a[:, lo | h] = (u - v) / 2
    cols = np.array([x for x in range(N) if (x & S) == S])
    return a[:, cols]


mu = np.zeros((M, N)); up = np.zeros((M, N)); ab = np.zeros((M, N)); n43 = np.zeros((M, N))
for S in range(N):
    c = partial(F, S)
    mu[:, S] = c.mean(axis=1) ** 2
    up[:, S] = (c ** 2).mean(axis=1)
    ab[:, S] = np.abs(c).mean(axis=1)
    n43[:, S] = (np.abs(c) ** (4 / 3)).mean(axis=1) ** 1.5      # ||g||_{4/3}^2

I = (mu * pc[None, :]).sum(axis=1)
m = np.zeros((M, N))
for R in range(N):
    r = pc[R]
    for S in range(N):
        if S & R == R:
            m[:, R] += mu[:, S] / comb(int(pc[S]), int(r))
print("n", n, "functions", M)
print("(g) max |sum m - (I+1)|", np.abs(m.sum(axis=1) - I - 1).max())

A1 = np.zeros(M)
for S in range(N):
    nz = mu[:, S] > 1e-15
    A1[nz] += mu[nz, S] * np.log2(1 / ab[nz, S])
chain = np.zeros(M)
for R in range(1, N):
    r = pc[R]
    nz = m[:, R] > 1e-15            # m(R) > 0 forces alpha(R) > 0 and alpha(R-s) > 0
    step = np.zeros(M)
    for s in range(n):
        if R >> s & 1:
            step[nz] += np.log2(ab[nz, R ^ (1 << s)] / ab[nz, R])
    chain[nz] += m[nz, R] * step[nz] / r
print("(h) max |A1 - chain form|", np.abs(A1 - chain).max())

worst_i = -1e9; tight = 0.0
for R in range(1, N):
    r = int(pc[R])
    nz = up[:, R] > 1e-15
    L = np.zeros(M)
    L[nz] = np.log(np.sqrt(up[nz, R]) / ab[nz, R])
    bound = np.where(L > 0, np.minimum(1.0, factorial(r) / np.where(L > 0, L, 1) ** r), 1.0) * up[:, R]
    worst_i = max(worst_i, (m[:, R] - bound).max())
    ok = bound > 1e-15
    tight = max(tight, (m[ok, R] / bound[ok]).max())
print("(i) max m(R) - up(R) min(1, r!/L^r)", worst_i, " largest m/bound", tight)

worst_j = -1e9
for R in range(1, N):
    for k in range(0, n - int(pc[R]) + 1):
        lhs = np.zeros(M)
        for S in range(N):
            if S & R == R and pc[S] - pc[R] <= k:
                lhs += mu[:, S]
        worst_j = max(worst_j, (lhs - 3.0 ** k * n43[:, R]).max())
print("(j) max sum_{|S-R|<=k} mu - 3^k ||g_R||_{4/3}^2", worst_j)

inf = np.stack([up[:, 1 << i] for i in range(n)], axis=1)
lv = np.zeros(M)
for S in range(1, N):
    mem = [i for i in range(n) if S >> i & 1]
    mn = inf[:, mem].min(axis=1)
    nz = mu[:, S] > 1e-15
    lv[nz] += mu[nz, S] * np.log2(1 / mn[nz])
ok = I > 1e-12
print("(k) max E_S log2(1/min Inf) / I", (lv[ok] / I[ok]).max())
r = np.where(ok, A1 / np.where(ok, I, 1), -1)
print("    max A1/I", r.max())
