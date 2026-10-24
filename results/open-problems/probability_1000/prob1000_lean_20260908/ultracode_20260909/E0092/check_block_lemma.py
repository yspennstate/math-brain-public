# Check the assembled block lemma at b = 10 (N = 20) on a random Toeplitz block:
#   TV(law(M Z_K), U) <= P(W_K outside [w0, N-w0]) + max_{w in window} sqrt(Q_w(M))/2
# against the exact TV of the block walk, for every K up to 30, and every window w0.
import numpy as np, math, itertools
from math import comb
rng=np.random.default_rng(7)
b=10; N=2*b
bits=rng.integers(0,2,size=N+b-1)
M=np.array([[bits[c-r+b-1] for c in range(N)] for r in range(b)],dtype=np.int8)
allz=((np.arange(2**N)[:,None]>>np.arange(N))&1).astype(np.int8)
wt=allz.sum(1).astype(np.int64)
code=((allz.astype(np.int64)@M.T.astype(np.int64))%2)@(1<<np.arange(b))
Q=np.zeros(N+1)
for w in range(N+1):
    idx=np.where(wt==w)[0]; cnt=np.bincount(code[idx],minlength=2**b)
    Q[w]=2**b*(cnt.astype(float)**2).sum()/len(idx)**2-1
eta=np.array([2*(N+1)*2**b/comb(N,w) for w in range(N+1)])
print("Q_w <= eta_w for all w:",bool(np.all(Q<=eta)), " max Q_w/eta_w =",float((Q/eta).max()))
# exact block walk law and Ehrenfest weight law
cols=[int(sum(int(M[r,i])<<r for r in range(b))) for i in range(N)]
mu=np.zeros(2**b); mu[0]=1; xs=np.arange(2**b)
pw=np.zeros(N+1); pw[0]=1
worst=0.0
for K in range(1,31):
    mu=sum(mu[xs^c] for c in cols)/N
    pw2=np.zeros(N+1)
    for w in range(N+1):
        if w>0: pw2[w]+=pw[w-1]*(N-(w-1))/N
        if w<N: pw2[w]+=pw[w+1]*(w+1)/N
    pw=pw2
    tv=0.5*np.abs(mu-2.0**-b).sum()
    best=1.0
    for w0 in range(0,b+1):
        win=range(w0,N-w0+1)
        bd=pw[[w for w in range(N+1) if w not in win]].sum()+0.5*math.sqrt(max(Q[list(win)].max(),0))
        best=min(best,bd)
    worst=max(worst,tv-best)
    if K%3==0 or K<4: print(f"K={K:2d} exact TV={tv:.5f} best window bound={best:.5f} ok={tv<=best+1e-12}")
print("max (exact - bound) over K =",worst,"(must be <= 0)")
# Lemma 6 (mean of the weight) check
EW=[N/2*(1-(1-2/N)**K) for K in range(31)]
pwk=np.zeros(N+1); pwk[0]=1; ok=True
for K in range(1,31):
    p2=np.zeros(N+1)
    for w in range(N+1):
        if w>0: p2[w]+=pwk[w-1]*(N-(w-1))/N
        if w<N: p2[w]+=pwk[w+1]*(w+1)/N
    pwk=p2
    ok&=abs((pwk*np.arange(N+1)).sum()-EW[K])<1e-9
print("E W_K = (N/2)(1-(1-2/N)^K) exact for K<=30:",ok)
