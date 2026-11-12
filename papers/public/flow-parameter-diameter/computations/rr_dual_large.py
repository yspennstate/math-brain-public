"""Table 3, random rows: larger cones over random d-regular graphs. The certificate of Lemma 3.3 is exact
(a rigorous lower bound on F given the exact distance counts); mu_2 by a sparse eigensolver."""
import time, csv
from fractions import Fraction
import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import shortest_path
from scipy.sparse.linalg import eigsh
import networkx as nx
from flowlib import two_length_dual_cone, best_two_length_dual_cone, hub_routing_upper_bound, ball_bound_lower

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

cases = [(3,1000),(3,4000),(3,16000),(4,1000),(4,4000)]
out = open("rr_dual_large_results.csv", "w", newline=""); w = csv.writer(out)
w.writerow("d,n,mu2,tau2,diam_H,mean_dist_H,best_certificate,r,ball_bound,hub_bound,ratio_lower_bound,d_plus_1_minus_mu2,seconds".split(","))
print("d n mu2 tau2 diam_H mean_dist_H best_certificate r ball_bound hub_bound ratio_lower_bound d_plus_1_minus_mu2 seconds", flush=True)
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
    row=[d,n,f"{mu2:.7f}",f"{t2:.7f}",diam,f"{meand:.3f}",f"{float(best):.5f}",r,f"{float(bb[0]):.5f}(r={bb[1]})",f"{float(ub):.5f}",f"{float(best)/(2*t2):.7f}",f"{d+1-mu2:.7f}",f"{time.time()-t0:.0f}"]
    print(*row, flush=True); w.writerow(row); out.flush()
