try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
# Theorem 2, high-frequency part, Gaussian model for (L,V): window integrals int_T^{2T} |phi| versus the proven
# bound 16.8 |lam|^{-1/2} (sigma T)^{-1/6}, for rough hub laws (the laws that defeat pointwise bounds).
import numpy as np, time
s2=1/12.
def Psi(t,y,sigma,lam):
    z1=1-2j*t*sigma*s2; z2=1-2j*t*lam*s2
    return z1**-0.5*np.exp(-y**2*s2/(2*z1))*z2**-0.5
rng=np.random.default_rng(3)
def rough_law(width, lo=-1, hi=1, N=400001):
    x=np.linspace(lo,hi,N); dx=x[1]-x[0]
    nb=int((hi-lo)/width); keep=rng.random(nb)<0.5
    idx=np.minimum(((x-lo)/width).astype(int),nb-1)
    f=keep[idx].astype(float); f/= f.sum()*dx   # density ~1 on half the cells
    return x,f,dx
sigma=0.1; lam=1.0
laws={'uniform[-1/2,1/2]':None,'rough w=0.01':0.01,'rough w=0.002':0.002}
for name,wd in laws.items():
    if wd is None:
        x=np.linspace(-0.5,0.5,200001); dx=x[1]-x[0]; f=np.ones_like(x)
    else:
        x,f,dx=rough_law(wd)
    print(name, " max f=%.3f"%f.max(), flush=True)
    t0=time.time()
    for T in [5,20,80,320,1280]:
        ts=np.linspace(T,2*T,max(400,int(8*T)))
        vals=[]
        for t in ts:
            # restrict x to where |Psi| is non-negligible: |x| <~ 8 sqrt((1+4 t^2 sigma^2 s2^2)/(4 t^2 s2))
            r=8*np.sqrt((1+4*t*t*sigma*sigma*s2*s2)/(4*t*t*s2))
            m=np.abs(x)<=r
            vals.append(abs((f[m]*Psi(t,2*t*x[m],sigma,lam)).sum()*dx))
        vals=np.array(vals); I=np.trapezoid(vals,ts)
        bound=16.8*lam**-0.5*(sigma*T)**(-1/6)
        print(f"   T={T:5d}  int_T^2T|phi|={I:.4e}   max_t t^1.5|phi|={np.max(ts**1.5*vals):7.3f}   proven window bound (valid for sigma T>=1/2) {bound:.2f}  ({time.time()-t0:.0f}s)",flush=True)
