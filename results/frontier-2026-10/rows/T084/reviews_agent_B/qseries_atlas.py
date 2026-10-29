# T084, agent B (independent of the referee's d3_exh.py): for every graph in the networkx atlas with n vertices and
# every edge pair (e,f), N = Z10*Z01 - Z00*Z11 (the Rayleigh difference of Z = sum_A q^k(A) prod z, at z = lam), split by
# lam-power s; test q-series positivity of N_s/(1-q)^2 (all second partial sums of N_s's q-coefficients >= 0, tail included).
import numpy as np, networkx as nx, sys, itertools, json
from scipy.signal import convolve2d
nmin, nmax = int(sys.argv[1]), int(sys.argv[2])
def comps_all(n, edges):
    m = len(edges); L = np.arange(n, dtype=np.int8)[None, :].copy()
    for b, (u, v) in enumerate(edges):
        Lb = L.copy(); lu = Lb[:, u:u+1]; lv = Lb[:, v:v+1]
        Lb = np.where(Lb == lv, lu, Lb); L = np.concatenate([L, Lb])
    return (L == np.arange(n, dtype=np.int8)[None, :]).sum(1)  # index = subset bitmask
def check(n, edges):
    m = len(edges); k = comps_all(n, edges); masks = np.arange(1 << m)
    pc = np.array([bin(x).count('1') for x in range(1 << m)]) if m <= 16 else np.unpackbits(masks.view(np.uint8).reshape(-1, 8), axis=1).sum(1)
    out = []
    for e, f in itertools.combinations(range(m), 2):
        Z = {}
        for a in (0, 1):
            for b in (0, 1):
                sel = (((masks >> e) & 1) == a) & (((masks >> f) & 1) == b)
                s = pc[sel] - a - b; H = np.zeros((m - 1, n + 1), dtype=np.int64)
                np.add.at(H, (s, k[sel]), 1); Z[(a, b)] = H
        conv = lambda X, Y: convolve2d(X, Y).astype(np.int64)  # integer direct convolution, exact below 9e18
        N = conv(Z[(1, 0)], Z[(0, 1)]) - conv(Z[(0, 0)], Z[(1, 1)])
        bad = []; nonzero = False; first_fail = [0]
        for s in range(N.shape[0]):
            c = [int(x) for x in N[s]]
            if any(c): nonzero = True
            p1 = np.cumsum(np.array(c, dtype=object)); p2 = np.cumsum(p1)
            tail_slope = sum(c)  # beyond the degree the second partial sums grow by N_s(1) per step
            if min(p2) < 0 or tail_slope < 0: bad.append((s, c))
            if min(p1) < 0: first_fail[0] += 1
        p1fail = first_fail[0] > 0
        negN_caught = (not nonzero) or any(min(np.cumsum(np.cumsum(-np.array([int(x) for x in N[s_]], dtype=object)))) < 0 for s_ in range(N.shape[0]))
        raw_neg = any(int(x) < 0 for x in N.flat)
        q2 = sum(int(N[s_, j]) * 2 ** j for s_ in range(N.shape[0]) for j in range(N.shape[1]))
        qh = sum(int(N[s_, j]) * 0.5 ** j for s_ in range(N.shape[0]) for j in range(N.shape[1]))
        adj = len({*edges[e]} & {*edges[f]}) > 0
        out.append((e, f, adj, nonzero, bad, raw_neg, q2, qh, p1fail, negN_caught))
    return out
tot = {'graphs': 0, 'pairs': 0, 'nonzero': 0, 'bad': 0, 'raw_neg': 0, 'q2_pos': 0, 'qhalf_neg': 0, 'first_partial_fail': 0, 'negated_N_missed': 0}
for G in nx.graph_atlas_g():
    n = G.number_of_nodes()
    if n < nmin or n > nmax or G.number_of_edges() < 2: continue
    edges = list(G.edges()); tot['graphs'] += 1
    for e, f, adj, nz, bad, rn, q2, qh, p1f, nc in check(n, edges):
        tot['negated_N_missed'] += not nc
        tot['first_partial_fail'] += p1f
        tot['pairs'] += 1; tot['nonzero'] += nz; tot['raw_neg'] += rn; tot['q2_pos'] += q2 > 0; tot['qhalf_neg'] += qh < -1e-9
        if bad: tot['bad'] += 1; print("NEGATIVE", n, edges, e, f, adj, bad[:2], flush=True)
    if n >= 7 and tot['graphs'] % 50 == 0: print('progress', json.dumps(tot), flush=True)
print(json.dumps(tot))
