# Calibrate the definition: for m=2, compute sup alpha such that some QSO with all P_{ij,k} >= alpha
# has a fixed point with |f'(p)| >= 1 (local loss of stability). Compare with (3-sqrt7)/2.
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(0)
def fp(a,b,c):
    # f(x)=a x^2 + 2b x(1-x) + c(1-x)^2 ; solve f(x)=x on [0,1]
    # (a-2b+c) x^2 + (2b-2c-1) x + c = 0
    A=a-2*b+c; B=2*b-2*c-1; C=c
    if abs(A)<1e-14: return -C/B
    r=np.roots([A,B,C]); r=[x.real for x in r if abs(x.imag)<1e-12 and -1e-12<=x.real<=1+1e-12]
    return min(r, key=lambda x: abs(x-0.5))
def fprime(a,b,c,x): return 2*a*x+2*b*(1-2*x)-2*c*(1-x)
def worst(alpha):
    # maximise |f'(p)| over a,b,c in [alpha,1-alpha]
    best=0
    for _ in range(200):
        x0=rng.uniform(alpha,1-alpha,3)
        res=minimize(lambda v: -abs(fprime(*v,fp(*v))), x0, bounds=[(alpha,1-alpha)]*3, method='L-BFGS-B')
        best=max(best,-res.fun)
    return best
lo,hi=0.0,0.25
for _ in range(40):
    mid=(lo+hi)/2
    if worst(mid)>=1: lo=mid
    else: hi=mid
print("local threshold m=2:",lo,"  (3-sqrt7)/2 =",(3-7**0.5)/2)
