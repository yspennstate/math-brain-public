# Independent check (scipy quad, no grids): threshold policy at T=2, b=1, d=1.
# step 1: a1=-1 (record i), v1=+1 (record j). step 2: g1 >= c -> (a2,v2)=(1,-1) [conjectured]; g1 < c -> (a2,v2)=(1,1).
import sys, json, numpy as np
from scipy import integrate, optimize
from scipy.stats import norm
def inner(x1, s, e, a2, v2, rev):
    wa=.5*norm.pdf(x1,-1,s); w0=.5*norm.pdf(x1,0,s); wc=.5*norm.pdf(x1,1,s)
    f=lambda y: (lambda p,q: max(q-e*p,0) if rev else max(p-e*q,0))(wa*norm.pdf(y,v2,s)+wc*norm.pdf(y,a2,s), w0*norm.pdf(y,v2,s)+wc*norm.pdf(y,0,s))
    L=10*s+3
    return integrate.quad(f,-L,L,limit=400,epsabs=1e-13,points=[-1,0,1])[0]
def delta(c, s, eps, rev=False):
    e=np.exp(eps); L=10*s+3
    lo=integrate.quad(lambda x: inner(x,s,e,1,1,rev),-L,c,limit=200,epsabs=1e-11)[0] if c>-L else 0
    hi=integrate.quad(lambda x: inner(x,s,e,1,-1,rev),c,L,limit=200,epsabs=1e-11)[0]
    return lo+hi
def conj(s, eps):
    # conjectured pair == the threshold policy with c = -inf (always anti-aligned), both orders
    return max(delta(-1e9,s,eps,False), delta(-1e9,s,eps,True))
res={}
for s in [float(x) for x in sys.argv[1].split(",")]:
    for eps in [float(x) for x in sys.argv[2].split(",")]:
        dc=conj(s,eps)
        r=optimize.minimize_scalar(lambda c:-delta(c,s,eps), bounds=(-4*s-2,2*s+2), method="bounded", options={"xatol":1e-3})
        print("sigma %.2f eps %.2f conj %.8f threshold-policy %.8f at c=%.3f gain %+.3f%%" % (s,eps,dc,-r.fun,r.x,100*(-r.fun/dc-1)), flush=True)
        res["%g_%g"%(s,eps)]={"conj":dc,"policy":-r.fun,"c":r.x}
json.dump(res,open(sys.argv[3],"w"),indent=1)
