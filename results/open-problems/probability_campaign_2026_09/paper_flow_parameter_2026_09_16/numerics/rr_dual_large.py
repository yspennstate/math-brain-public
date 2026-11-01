# Larger cones over random d-regular graphs: exact two-length dual certificate (rigorous lower bound
# given the graph's exact distance distribution), hub upper bound, mu_2 by sparse eigensolver.
import sys, time, csv
from fractions import Fraction
import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import shortest_path
from scipy.sparse.linalg import eigsh
import networkx as nx
from af449lib import two_length_dual_cone, best_two_length_dual_cone, hub_routing_upper_bound, ball_bound_lower
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass

def dist_counts(A, n, chunk=2000):
    counts = {}
    for s0 in range(0, n, chunk):
        idx = np.arange(s0, min(n, s0+chunk))
        D = shortest_path(A, method='D', directed=False, unweighted=True, indices=idx)
        D = D.astype(np.int64)
        vals, cnts = np.unique(D, return_counts=True)
        for v,c in zip(vals,cnts):
            if v>0: counts[int(v)] = counts.get(int(v),0)+int(c)
    return counts

cases = [(3,1000),(3,4000),(3,16000),(4,1000),(4,4000),(4,16000),(5,1000),(5,4000),(5,16000),(6,4000),(6,16000),(8,4000),(8,16000),(10,16000),(3,50000),(4,50000),(6,50000)]
out = open("rr_dual_large_results.csv","a"); w = csv.writer(out)
print("d n mu2 tau2 diamH meandist twolen_dual r ballbound(r) hubUB ratioLB=(dual/(2tau2)) d+1-mu2 secs", flush=True)
for d,n in cases:
    t0=time.time()
    seed=1
    while True:
        H = nx.random_regular_graph(d, n, seed=seed)
        if nx.is_connected(H): break
        seed+=1
    A = nx.to_scipy_sparse_array(H, format='csr', dtype=np.float64)
    mu = eigsh(A, k=2, which='LA', return_eigenvectors=False)
    mu2 = float(sorted(mu)[0])
    t2 = (d+1)/(d+1-mu2)
    cnt = dist_counts(A, n)
    best, r = best_two_length_dual_cone(cnt, n, d)
    bb = max((ball_bound_lower(n,d,rr), rr) for rr in range(1,40))
    ub = hub_routing_upper_bound(n,d)
    diam = max(cnt); meand = sum(t*c for t,c in cnt.items())/sum(cnt.values())
    row=[d,n,f"{mu2:.5f}",f"{t2:.5f}",diam,f"{meand:.3f}",f"{float(best):.5f}",r,f"{float(bb[0]):.5f}(r={bb[1]})",f"{float(ub):.5f}",f"{float(best)/(2*t2):.5f}",f"{d+1-mu2:.5f}",f"{time.time()-t0:.0f}"]
    print(*row, flush=True); w.writerow(row); out.flush()
