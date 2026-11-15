"""MST on (binary tree of depth n) x K2 with iid uniform labels; tree path between (root,0) and (root,1).
If the free MSF is connected, the path length and its max depth stay tight as n grows."""
import sys, numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, breadth_first_order
rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
def trial(n):
    N = 2 ** (n + 1) - 1               # heap-indexed binary tree, root 0
    ch = np.arange(1, N); par = (ch - 1) // 2
    rows = np.concatenate([par, par + N, np.arange(N)]); cols = np.concatenate([ch, ch + N, np.arange(N) + N])
    w = rng.random(rows.size) + 1e-12
    T = minimum_spanning_tree(coo_matrix((w, (rows, cols)), shape=(2 * N, 2 * N)).tocsr())
    T = T + T.T
    _, pred = breadth_first_order(T, 0, directed=False, return_predecessors=True)
    v, L, dmax = N, 0, 0               # walk back from (root,1)
    while v != 0:
        dmax = max(dmax, int(np.floor(np.log2((v % N) + 1)))); v = pred[v]; L += 1
    return L, dmax
reps = int(sys.argv[1])
for n in (4, 6, 8, 10, 12, 14):
    res = np.array([trial(n) for _ in range(reps)])
    L, d = res[:, 0], res[:, 1]
    print(f"n={n:2d} pathlen mean {L.mean():6.2f} q90 {np.quantile(L,.9):5.0f}  maxdepth mean {d.mean():5.2f} q90 {np.quantile(d,.9):3.0f}  P(depth>=n-1) {np.mean(d>=n-1):.3f}", flush=True)
