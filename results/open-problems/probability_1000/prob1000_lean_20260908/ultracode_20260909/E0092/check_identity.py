# Check, on a small random instance, the three facts the memo rests on:
# (1) the walk on Z_2^d driven by V_1..V_N is the image under M (columns V_i) of the
#     nearest-neighbour walk on Z_2^N, so its law at time k is sum_w P(W_k=w) * M nu_w;
# (2) Q_w(M) := 2^d P(Mz = Mz') - 1 (z,z' iid uniform on the weight-w shell) equals
#     2^d sum_u B_u P_w(u)/C(N,u) - 1 with B_u the weight distribution of ker M;
# (3) TV(M nu_w, U) <= sqrt(Q_w)/2 and the whole-walk TV bound
#     TV <= P(W_k outside window) + max_w sqrt(Q_w)/2 holds against the exact TV.
import numpy as np, itertools, math, random
rng=np.random.default_rng(1)
d,N=6,12
M=rng.integers(0,2,size=(d,N))
allz=np.array(list(itertools.product([0,1],repeat=N)),dtype=np.int64)  # 2^N x N
wt=allz.sum(1)
img=(allz@M.T)%2
code=img@(1<<np.arange(d))   # index of Mz in Z_2^d
# (2): Q_w two ways
from math import comb
def Pw(u,w):  # P(wt(z+z')=u) for z,z' iid uniform on shell w
    if u%2: return 0.0
    return comb(u,u//2)*comb(N-u,w-u//2)*comb(N,u)/comb(N,w)**2 if w-u//2>=0 and w-u//2<=N-u else 0.0
kernel=allz[(code==0)]
B=np.bincount(kernel.sum(1),minlength=N+1)
for w in range(N+1):
    idx=np.where(wt==w)[0]
    cnt=np.bincount(code[idx],minlength=2**d)
    Q1=2**d*(cnt.astype(float)**2).sum()/len(idx)**2-1
    Q2=2**d*sum(B[u]*Pw(u,w)/comb(N,u) for u in range(N+1))-1
    tv=0.5*np.abs(cnt/len(idx)-2.0**-d).sum()
    print(f"w={w:2d} Q(direct)={Q1:.6f} Q(weights)={Q2:.6f} TV(M nu_w,U)={tv:.4f} sqrt(Q)/2={math.sqrt(max(Q1,0))/2:.4f}")
# (1),(3): exact walk law by dynamic programming on Z_2^N projected, vs. direct walk on Z_2^d
# exact law on Z_2^d: mu_{k+1}(x) = (1/N) sum_i mu_k(x + V_i)
mu=np.zeros(2**d); mu[0]=1.0
cols=[int(sum(M[r,i]<<r for r in range(d))) for i in range(N)]
xs=np.arange(2**d)
# hypercube weight law by Ehrenfest recursion
pw=np.zeros(N+1); pw[0]=1.0
for k in range(1,25):
    mu=sum(mu[xs^c] for c in cols)/N
    pw2=np.zeros(N+1)
    for w in range(N+1):
        if w>0: pw2[w]+=pw[w-1]*(N-(w-1))/N
        if w<N: pw2[w]+=pw[w+1]*(w+1)/N
    pw=pw2
    # law via projection identity (1)
    mu_proj=np.zeros(2**d)
    for w in range(N+1):
        idx=np.where(wt==w)[0]
        mu_proj+=pw[w]*np.bincount(code[idx],minlength=2**d)/len(idx)
    assert np.allclose(mu,mu_proj), k
    tv=0.5*np.abs(mu-2.0**-d).sum()
    # bound (3) with window = weights having Q_w <= 0.5 ; crude
    Qs=[]
    for w in range(N+1):
        idx=np.where(wt==w)[0]; cnt=np.bincount(code[idx],minlength=2**d)
        Qs.append(2**d*(cnt.astype(float)**2).sum()/len(idx)**2-1)
    best=min(pw[[w for w in range(N+1) if Qs[w]>t]].sum()+0.5*math.sqrt(max(max([q for q in Qs if q<=t],default=0),0)) for t in sorted(set(Qs)))
    print(f"k={k:2d} exact TV={tv:.4f}  projection identity OK  shell bound={best:.4f}")
