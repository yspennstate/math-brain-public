# Three-slab bound 1/E_pi[c] from the stationary law of the count chain, with and
# without backward vertical edges (b->a: max(b-a,0); c->b: max(c-b,0)).
import sys, numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
d, C, back = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
m = d - 1
f = [0]*(C+2)
for n in range(1, C+2): f[n] = f[n-1] + bin(n-1).count("1")
sig = [2*m*n - 2*f[n] for n in range(C+2)]
idx = lambda a,b,c: ((a-1)*C + (b-1))*C + (c-1)
N = C**3; R=[]; Cc=[]; V=[]; cvec=np.zeros(N)
for a in range(1,C+1):
  for b in range(1,C+1):
    for c in range(1,C+1):
      s = idx(a,b,c); cvec[s] = c
      ra = (sig[a] + (max(b-a,0) if back else 0)) if a < C else 0
      rb = (sig[b] + max(a-b,0) + (max(c-b,0) if back else 0)) if b < C else 0
      rc = (sig[c] + max(b-c,0)) if c < C else 0
      for r,t in ((ra,idx(a+1,b,c) if a<C else s),(rb,idx(a,b+1,c) if b<C else s),(rc,idx(a,b,c+1) if c<C else s),(c,idx(b,c,1))):
        if r and t != s: R.append(s); Cc.append(t); V.append(r); R.append(s); Cc.append(s); V.append(-r)
Q = sp.csr_matrix((V,(R,Cc)),shape=(N,N)).T.tolil()
Q[0,:] = 1.0
rhs = np.zeros(N); rhs[0] = 1.0
pi = sla.spsolve(Q.tocsc(), rhs)
print(d, C, back, "bound", 1.0/float(pi @ cvec))
