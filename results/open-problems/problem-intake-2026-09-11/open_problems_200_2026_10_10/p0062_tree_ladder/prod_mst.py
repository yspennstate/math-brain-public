"""Free MST on (b-ary tree of depth n) x P_k, iid uniform labels; tree path between (root,0) and (root,k-1).
Tight path length as n grows = evidence the free MSF is connected on T x P_k.  usage: prod_mst.py b k reps nmax seed"""
import sys, numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, breadth_first_order
b, k, reps, nmax, seed = map(int, sys.argv[1:6]); rng = np.random.default_rng(seed)
def trial(n):
    N = (b ** (n + 1) - 1) // (b - 1); ch = np.arange(1, N); par = (ch - 1) // b
    R, C = [], []
    for s in range(k):
        R.append(par + s * N); C.append(ch + s * N)
    for s in range(k - 1):
        R.append(np.arange(N) + s * N); C.append(np.arange(N) + (s + 1) * N)
    R = np.concatenate(R); C = np.concatenate(C); w = rng.random(R.size) + 1e-12
    T = minimum_spanning_tree(coo_matrix((w, (R, C)), shape=(k * N, k * N)).tocsr()); T = T + T.T
    _, pred = breadth_first_order(T, 0, directed=False, return_predecessors=True)
    v, L, dmax = (k - 1) * N, 0, 0
    while v != 0:
        u = v % N; d = 0
        while u: u = (u - 1) // b; d += 1
        dmax = max(dmax, d); v = pred[v]; L += 1
    return L, dmax
for n in range(3, nmax + 1, 2):
    r = np.array([trial(n) for _ in range(reps)])
    print(f"b={b} k={k} n={n:2d} path mean {r[:,0].mean():6.2f} q90 {np.quantile(r[:,0],.9):4.0f} depth mean {r[:,1].mean():5.2f} q99 {np.quantile(r[:,1],.99):3.0f} P(depth>=n-1) {np.mean(r[:,1]>=n-1):.3f}", flush=True)
