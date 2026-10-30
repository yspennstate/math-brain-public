# Optimistic ceiling for small-shape tracking: replace sigma(n) by the Eden mean boundary for n <= K.
import sys, random, numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
d, C = int(sys.argv[1]), int(sys.argv[2]); m = d-1; random.seed(7)
f=[0]*(C+2)
for n in range(1,C+2): f[n]=f[n-1]+bin(n-1).count("1")
sig0=[2*m*n-2*f[n] for n in range(C+2)]
def nb(x):
    for i in range(m):
        for s in (1,-1):
            y=list(x); y[i]+=s; yield tuple(y)
tot=[0.0]*(C+2); runs=200
for r in range(runs):
    o=(0,)*m; S={o}; E=[(o,y) for y in nb(o)]; tot[1]+=len(E)
    while len(S)<C:
        x,y=E[random.randrange(len(E))]
        if y in S: continue
        S.add(y); E=[(u,v) for (u,v) in E if v!=y]+[(y,z) for z in nb(y) if z not in S]; tot[len(S)]+=len(E)
eden=[t/runs for t in tot]
def bound(sig):
    idx=lambda a,b,c: ((a-1)*C+(b-1))*C+(c-1); N=C**3; R=[];K=[];V=[]; cv=np.zeros(N)
    for a in range(1,C+1):
     for b in range(1,C+1):
      for c in range(1,C+1):
        s=idx(a,b,c); cv[s]=c
        ra=sig[a] if a<C else 0; rb=(sig[b]+max(a-b,0)) if b<C else 0; rc=(sig[c]+max(b-c,0)) if c<C else 0
        for r,t in ((ra,idx(a+1,b,c) if a<C else s),(rb,idx(a,b+1,c) if b<C else s),(rc,idx(a,b,c+1) if c<C else s),(c,idx(b,c,1))):
          if r and t!=s: R+= [s,s]; K+=[t,s]; V+=[r,-r]
    Q=sp.csr_matrix((V,(R,K)),shape=(N,N)).T.tolil(); Q[0,:]=1.0; rhs=np.zeros(N); rhs[0]=1
    return 1.0/float(sla.spsolve(Q.tocsc(),rhs)@cv)
print("eden/sigma n=1..8:", [round(eden[n]/sig0[n],4) for n in range(1,9)])
b0=bound(sig0); print(d,C,"base",b0)
for Kc in (2,4,8,16,C):
    sig=[eden[n] if 1<=n<=Kc else sig0[n] for n in range(C+2)]
    b=bound(sig); print(d,C,"eden up to n=%d"%Kc, b, "rel gain %.4f"%(1-b/b0))
