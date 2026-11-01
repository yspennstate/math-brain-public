try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np
from scipy.special import exp1
from scipy.integrate import quad
sig=np.sqrt(1/12)
def p(s,lam=1.0,sig=sig,beta=0.0):
    # Gaussian limit: L,V ~ N(0,sig^2) indep, X_h~U[-1/2,1/2], Q=2 X_h (L+beta) + lam V^2
    # p(s) = E[1{|s-lam V^2|<=|L+beta|}/(2|L+beta|)]
    # inner: int_{|l+beta|>=a} phi(l)/(2|l+beta|) dl
    def inner(a):
        if beta==0.0:
            return exp1(a*a/(2*sig*sig))/(2*sig*np.sqrt(2*np.pi))
        f=lambda t: np.exp(-(t-beta)**2/(2*sig*sig))/(sig*np.sqrt(2*np.pi))/(2*abs(t))
        return quad(f,a,np.inf,limit=200)[0]+quad(f,-np.inf,-a,limit=200)[0]
    g=lambda v: np.exp(-v*v/(2*sig*sig))/(sig*np.sqrt(2*np.pi))*inner(abs(s-lam*v*v)+1e-300)
    pts=[np.sqrt(s/lam)] if s*lam>0 else []
    r=quad(g,-np.inf,np.inf,points=None,limit=400)[0] if not pts else (quad(g,-np.inf,-pts[0],limit=400)[0]+quad(g,-pts[0],0,limit=400)[0]+quad(g,0,pts[0],limit=400)[0]+quad(g,pts[0],np.inf,limit=400)[0])
    return r
for lam in [1.0,-1.0,2.0]:
    ss=np.linspace(-0.3,0.3,61)
    vals=[p(s,lam) for s in ss]
    k=int(np.argmax(vals))
    fine=np.linspace(ss[max(k-1,0)],ss[min(k+1,60)],41); fv=[p(s,lam) for s in fine]
    kk=int(np.argmax(fv))
    print(f"lam={lam}: max p = {fv[kk]:.4f} at s={fine[kk]:.4f};  p(0)={p(0.0,lam):.4f}", flush=True)
for beta in [0.05,0.1,0.2]:
    ss=np.linspace(-0.3,0.3,31); vals=[p(s,1.0,beta=beta) for s in ss]; k=int(np.argmax(vals))
    print(f"beta={beta}: max p ~ {vals[k]:.4f} at s={ss[k]:.3f}", flush=True)
