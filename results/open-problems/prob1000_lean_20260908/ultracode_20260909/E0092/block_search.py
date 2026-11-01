# Deterministic search for a good block: d x N Toeplitz matrices over F_2 with N = 2d.
# For each M compute Q_w(M) = 2^d * P(Mz = Mz') - 1 (z, z' iid uniform on the weight-w shell)
# for every w, and accept the first M (lexicographic order of its N+d-1 defining bits)
# with Q_w(M) <= eta_w := 2 (N+1) 2^d / C(N,w) for all w.  The memo proves such an M exists
# (Markov + union bound over the Toeplitz family, which is 2-universal), and that
# eta_w is exponentially small in d for w/N >= H^{-1}(1/2) + delta.  For the tiny d run here
# eta_w >= 1 everywhere, so the threshold does not yet bite; the run demonstrates the
# algorithm and the identities, not the asymptotic regime.  Cost: 2^N vectors per matrix.
import numpy as np, itertools, math, sys, time
from math import comb
def toeplitz(bits,d,N):
    return np.array([[bits[c-r+d-1] for c in range(N)] for r in range(d)],dtype=np.int64)
def rank_f2(A):
    A=A.copy()%2; r=0
    for c in range(A.shape[1]):
        p=[i for i in range(r,A.shape[0]) if A[i,c]]
        if not p: continue
        A[[r,p[0]]]=A[[p[0],r]]
        for i in range(A.shape[0]):
            if i!=r and A[i,c]: A[i]^=A[r]
        r+=1
    return r
def Q_all(M,d,N,allz,wt):
    code=((allz@M.T)%2)@(1<<np.arange(d))
    Q=np.zeros(N+1)
    for w in range(N+1):
        idx=np.where(wt==w)[0]
        cnt=np.bincount(code[idx],minlength=2**d)
        Q[w]=2**d*(cnt.astype(float)**2).sum()/len(idx)**2-1
    return Q
def search(d,require_full_rank=False):
    N=2*d
    allz=np.array(list(itertools.product([0,1],repeat=N)),dtype=np.int64); wt=allz.sum(1)
    eta=np.array([2*(N+1)*2**d/comb(N,w) for w in range(N+1)])
    t0=time.time(); tried=0
    for bits in itertools.product([0,1],repeat=N+d-1):
        tried+=1
        M=toeplitz(bits,d,N)
        if require_full_rank and rank_f2(M)<d: continue
        Q=Q_all(M,d,N,allz,wt)
        if np.all(Q<=eta):
            return M,Q,eta,tried,time.time()-t0
    return None,None,eta,tried,time.time()-t0
if __name__=="__main__":
    for d in [5,6,7,8]:
        N=2*d
        M,Q,eta,tried,dt=search(d,require_full_rank=True)
        print(f"d={d} N={N}: first full-rank Toeplitz matrix passing Q_w<=eta_w for all w: candidate #{tried} ({dt:.1f}s)")
        print("  rows =",[''.join(map(str,r)) for r in M.tolist()])
        print("   w   Q_w      E_family[Q_w]=(2^d-1)/C(N,w)   eta_w")
        for w in range(N+1):
            print(f"  {w:2d}  {Q[w]:8.4f}  {(2**d-1)/comb(N,w):10.4f}  {eta[w]:10.4f}")
