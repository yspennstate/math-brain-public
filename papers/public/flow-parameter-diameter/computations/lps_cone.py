"""Table 3, LPS rows: cones over the Lubotzky-Phillips-Sarnak graphs X^{5,q} (6-regular Ramanujan),
built as Cayley graphs of PGL(2,q) from the six quaternions of norm 5; exact certificate of Lemma 3.3."""
import time, csv
import numpy as np, scipy.sparse as sp
from scipy.sparse.csgraph import shortest_path, connected_components
from scipy.sparse.linalg import eigsh
from collections import deque
from flowlib import best_two_length_dual_cone, hub_routing_upper_bound, ball_bound_lower

def lps(p, q):
    # quaternion solutions a^2+b^2+c^2+d^2 = p, a>0 odd, b,c,d even  (p=5: (1,+-2,0,0) and permutations)
    sols=[]
    for a in range(1,int(p**0.5)+2,2):
        for b in range(-p,p+1):
            for c in range(-p,p+1):
                for d in range(-p,p+1):
                    if a*a+b*b+c*c+d*d==p and b%2==0 and c%2==0 and d%2==0: sols.append((a,b,c,d))
    assert len(sols)==p+1, sols
    i = next(x for x in range(q) if (x*x)%q==q-1)   # sqrt(-1) mod q
    gens=[]
    for (a,b,c,d) in sols:
        M=((a+b*i)%q,(c+d*i)%q,(-c+d*i)%q,(a-b*i)%q)
        gens.append(M)
    def canon(M):
        for x in M:
            if x%q:
                inv=pow(x,q-2,q); return tuple((y*inv)%q for y in M)
    def mul(A,B):
        a,b,c,d=A; e,f,g,h=B
        return canon(((a*e+b*g)%q,(a*f+b*h)%q,(c*e+d*g)%q,(c*f+d*h)%q))
    I=canon((1,0,0,1)); idx={I:0}; verts=[I]; dq=deque([I]); edges=[]
    while dq:
        M=dq.popleft(); u=idx[M]
        for gM in gens:
            N=mul(M,gM)
            if N not in idx: idx[N]=len(verts); verts.append(N); dq.append(N)
            v=idx[N]
            if u<v: edges.append((u,v))
    n=len(verts)
    rows=[u for u,v in edges]+[v for u,v in edges]; cols=[v for u,v in edges]+[u for u,v in edges]
    A=sp.csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(n,n))
    A.data[:]=1.0
    return A, n

def dist_counts(A, n, chunk=2000):
    counts={}
    for s0 in range(0,n,chunk):
        idx=np.arange(s0,min(n,s0+chunk))
        D=shortest_path(A,method='D',directed=False,unweighted=True,indices=idx).astype(np.int64)
        vals,cnts=np.unique(D,return_counts=True)
        for v,c in zip(vals,cnts):
            if v>0: counts[int(v)]=counts.get(int(v),0)+int(c)
    return counts

out=open("lps_results.csv", "w", newline=""); w=csv.writer(out)
w.writerow("p,q,n,d,simple,mu2,two_sqrt_p,tau2,diam_H,mean_dist_H,best_certificate,r,ball_bound,hub_bound,ratio_lower_bound,d_plus_1_minus_mu2,seconds".split(","))
print("p q n d simple mu2 two_sqrt_p tau2 diam_H mean_dist_H best_certificate r ball_bound hub_bound ratio_lower_bound d_plus_1_minus_mu2 seconds", flush=True)
for q in [13,17,29]:
    t0=time.time()
    A,n=lps(5,q); d=int(A.sum(1).max()); dmin=int(A.sum(1).min())
    simple = (A.data.max()==1.0) and d==dmin and d==6
    mu=eigsh(A,k=2,which='LA',return_eigenvectors=False); mu2=float(sorted(mu)[0])
    t2=(d+1)/(d+1-mu2)
    cnt=dist_counts(A,n); best,r=best_two_length_dual_cone(cnt,n,d)
    bb=max((ball_bound_lower(n,d,rr),rr) for rr in range(1,30)); ub=hub_routing_upper_bound(n,d)
    diam=max(cnt); meand=sum(t*c for t,c in cnt.items())/sum(cnt.values())
    row=[5,q,n,d,simple,f"{mu2:.7f}",f"{2*5**0.5:.5f}",f"{t2:.7f}",diam,f"{meand:.3f}",f"{float(best):.5f}",r,f"{float(bb[0]):.5f}(r={bb[1]})",f"{float(ub):.5f}",f"{float(best)/(2*t2):.7f}",f"{d+1-mu2:.7f}",f"{time.time()-t0:.0f}"]
    print(*row, flush=True); w.writerow(row); out.flush()
