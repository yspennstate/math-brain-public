# m=2: sup alpha with a QSO P>=alpha whose fixed point has |f'(p)|>=1. Dense grid over (a,b,c).
import numpy as np
def fp(a,b,c):
    A=a-2*b+c; B=2*b-2*c-1; C=c
    if abs(A)<1e-14: return -C/B
    r=np.roots([A,B,C]); r=[x.real for x in r if abs(x.imag)<1e-12 and -1e-12<=x.real<=1+1e-12]
    return min(r, key=lambda x: abs(x-0.5))
def fprime(a,b,c,x): return 2*a*x+2*b*(1-2*x)-2*c*(1-x)
best=0; arg=None
g=np.linspace(0,1,201)
for a in g:
    for b in g:
        for c in g:
            lam=min(a,b,c,1-a,1-b,1-c)
            if lam<=best: continue
            p=fp(a,b,c)
            if abs(fprime(a,b,c,p))>=1:
                best=lam; arg=(a,b,c,p,fprime(a,b,c,p))
print("grid sup alpha:",best,arg,"  target (3-sqrt7)/2 =",(3-7**0.5)/2)
# refine around a=alpha, c=1-alpha, scan b, bisect alpha
def ok(alpha):
    for b in np.linspace(alpha,1-alpha,2001):
        for (a,c) in [(alpha,1-alpha),(1-alpha,alpha)]:
            p=fp(a,b,c)
            if abs(fprime(a,b,c,p))>=1: return True
    return False
lo,hi=0.1,0.25
for _ in range(45):
    mid=(lo+hi)/2
    if ok(mid): lo=mid
    else: hi=mid
print("refined:",lo)
