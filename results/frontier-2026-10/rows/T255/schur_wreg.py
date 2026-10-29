# numeric regularity in the tilt w: drift(log trSchur/V11)/|W|^2 at transverse size s -> 0 and tilt |w| = eps -> 0, vs mu_S
import numpy as np
from gen import bdrift, noise_basis
def rate(V,g2):
    m=V.shape[0]; P=np.eye(m)-1.0/m; a=V[0,0]; x=V[1:,0]; g=np.trace(V[1:,1:])-x@x/a
    def dg(E): return np.trace(E[1:,1:])-2*x@E[1:,0]/a+(x@x)*E[0,0]/a**2
    def d2g(E): return -2*E[1:,0]@E[1:,0]/a+4*(x@E[1:,0])*E[0,0]/a**2-2*(x@x)*E[0,0]**2/a**3
    b=bdrift(V,g2); dr=dg(b)/g-b[0,0]/a; ito=0
    for E in noise_basis(V,g2,att=True,lin=False):
        ito+=d2g(E)/g-dg(E)**2/g**2+E[0,0]**2/a**2
    W=P@V@P; return (dr+ito/2)/np.sum(W*W)
rng=np.random.default_rng(2)
for m in (4,5):
    for g2 in (0.5,1.0):
        mu=g2/m**2*(g2-m*(m-2)/(m-1)); out=[]
        for eps in (1e-1,1e-2,1e-3):
            errs=[]
            for _ in range(20):
                w=rng.standard_normal(m-1); w*=eps/np.linalg.norm(w)
                T=np.tril(rng.standard_normal((m-1,m-1))); s=1e-6
                L=np.zeros((m,m)); L[0,0]=1; L[1:,0]=w; L[1:,1:]=s*T
                errs.append(abs(rate(L@L.T,g2)-mu))
            out.append("|w| %.0e: max err %.2e"%(eps,max(errs)))
        print("m %d g2 %.1f mu_S %+.5f | "%(m,g2,mu)+" | ".join(out),flush=True)
