"""Attack on the KKL lemma: log(1/Inf_i) * sum_{S ni i} w(S)/|S| <= 2 Inf_i for every coordinate.
Reports the largest ratio (left side)/Inf_i over all functions on n <= 4 and over the families."""
import math, numpy as np
from fei_core import *
from exhaust_n4 import hadamard
lowprio()
out=[]
for n in [2,3,4]:
    N=1<<n; nf=1<<N; codes=np.arange(nf,dtype=np.int64)
    F=np.empty((nf,N))
    for x in range(N): F[:,x]=np.where((codes>>x)&1,-1.0,1.0)
    A=F@hadamard(n)/N; W=A*A; W[W<1e-15]=0
    k=popcounts(n).astype(float); idx=np.arange(N); best=0.0; arg=None
    for i in range(n):
        sel=((idx>>i)&1)==1
        inf=W[:,sel].sum(1); s=(W[:,sel]/k[sel]).sum(1)
        ok=(inf>0)&(inf<1-1e-12)
        r=np.where(ok, np.log(1/np.where(ok,inf,1))*s/np.where(ok,inf,1),0)
        if r.max()>best: best=r.max(); arg=(int(r.argmax()),i)
    out.append("n=%d max ratio %.6f at (f,i)=%s"%(n,best,arg))
fams=[("const 1-flip n=14",flip(np.ones(1<<14,dtype=np.int8),[0])),("maj21",majority(21)),("tribes 5x4",tribes(5,4)),
      ("bent n=14",inner_product(7)),("Numaro",load_numaro()),("addressing a=4",addressing(4))]
for name,f in fams:
    sp=Spec.from_table(f); inf=sp.influences(); best=0.0
    for i in range(sp.n):
        sel=(((sp.idx>>i)&1)==1)
        if 0<inf[i]<1:
            best=max(best, math.log(1/inf[i])*float((sp.ws[sel]/sp.ks[sel]).sum())/inf[i])
    out.append("%-20s max ratio %.6f"%(name,best))
# the one-point indicator: D_i f = point indicator on n-1 variables, ratio -> ?
for n in [6,10,14,18,22]:
    f=flip(np.ones(1<<n,dtype=np.int8),[0]); sp=Spec.from_table(f); inf=sp.influences(); i=0
    sel=(((sp.idx>>i)&1)==1)
    out.append("const1flip n=%d ratio %.6f"%(n, math.log(1/inf[i])*float((sp.ws[sel]/sp.ks[sel]).sum())/inf[i]))
txt='\n'.join(out); print(txt); open('../logs/kkl_check.log','w').write(txt+'\n')
