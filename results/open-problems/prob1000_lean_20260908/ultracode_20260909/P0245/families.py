import numpy as np, itertools, time
from cover_exact import *

def multipartite(parts):
    n = sum(parts); W = np.ones((n, n)); s = 0
    for m in parts:
        W[s:s+m, s:s+m] = 0; s += m
    return W

out = []
t0 = time.time()
for n in range(3, 13):
    T = target(n)
    rows = []
    # complete multipartite with equal parts
    for r in range(2, n + 1):
        if n % r == 0:
            m = n // r
            if m == 1: continue
            P = rw_on_graph(multipartite([m] * r))
            rows.append(("K_{%d x %d}" % (r, m), E_pi_cover(P)))
    # K_n minus a matching of size j
    for j in range(1, n // 2 + 1):
        W = np.ones((n, n)) - np.eye(n)
        for a in range(j): W[2*a, 2*a+1] = W[2*a+1, 2*a] = 0
        rows.append(("K_%d minus %d-matching" % (n, j), E_pi_cover(rw_on_graph(W))))
    # star, path, cycle
    W = np.zeros((n, n)); W[0, 1:] = 1; W[1:, 0] = 1
    rows.append(("star", E_pi_cover(rw_on_graph(W))))
    W = np.zeros((n, n))
    for i in range(n): W[i, (i+1) % n] = W[(i+1) % n, i] = 1
    rows.append(("cycle", E_pi_cover(rw_on_graph(W))))
    # K_n plus a pendant leaf (n total states: K_{n-1} + leaf)
    W = np.ones((n, n)) - np.eye(n); W[n-1, :] = 0; W[:, n-1] = 0; W[0, n-1] = W[n-1, 0] = 1
    rows.append(("K_{n-1}+leaf", E_pi_cover(rw_on_graph(W))))
    # two cliques of size n/2 joined by an edge
    if n % 2 == 0:
        m = n // 2; W = np.zeros((n, n)); W[:m, :m] = 1; W[m:, m:] = 1; W -= np.eye(n); W[0, m] = W[m, 0] = 1
        rows.append(("two K_{n/2} + bridge", E_pi_cover(rw_on_graph(W))))
    print("n=%d target=%.6f" % (n, T))
    for name, v in rows:
        print("   %-28s %.6f  ratio %.5f %s" % (name, v, v / T, "<<< BELOW" if v < T - 1e-9 else ""))
    print("   elapsed", round(time.time() - t0, 1))
