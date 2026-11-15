"""Exact certificates and extra semigroup checks, independent of code/.
Resource limits: one Python process, 280 second alarm, tiny matrices only.
"""
import signal
import time
from fractions import Fraction as F
from math import factorial
import resource
import mpmath as mp
signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError("280 second limit")))
signal.alarm(280)
START=time.monotonic()
mp.mp.dps=65

# e's Taylor remainder is bounded using a geometric majorant after the first omitted term.
elow=sum((F(1,factorial(j)) for j in range(21)),F(0))
eup=elow+F(22,21*factorial(21))
eps=F(1,100)
flow=3-eup-(4+2*eup**2)*eps-4*eps**2
excess=flow/eup**2
assert eup<F(27183,10000) and eup**2<F(73891,10000)
assert flow>F(9,100) and excess>F(1,100)
print("Taylor rational certificate: e <",float(eup),"e^2 <",float(eup**2))
print("Exact certified lower bounds f(1/100) >",float(flow),"exp(-2)*f >",float(excess))
print("Rational lower bound f:",flow)
print("Rational lower bound distance excess:",excess)

# Exact birth/death hitting-time calculation: sum across edges, no spectral input.
for k in (1,2,3,4,5):
    e=F(1,100)
    pi=[e**i/sum(e**j for j in range(k+1)) for i in range(k+1)]
    t0=F(0)
    for i in range(1,k+1):
        left=sum(pi[:i]);right=sum(pi[i:])
        t0+=left*right/pi[i]
    if k==2:assert t0==2*(1+e)/(1+e+e**2)
    print("Exact edge-sum Kemeny k",k,"eps 1/100:",t0)

# Check all pairs, not only the presumed extremal endpoints. Use direct expm here.
largest_error=mp.mpf(0);cases=0
for k in range(1,7):
    for e in (mp.mpf(0),mp.mpf("0.001"),mp.mpf("0.01"),mp.mpf("0.5"),mp.mpf(1),mp.mpf(2)):
        q=mp.zeros(k+1)
        for i in range(k+1):
            if i:q[i,i-1]=1
            if i<k:q[i,i+1]=e
            q[i,i]=-sum(q[i,j] for j in range(k+1) if j!=i)
        for t in (mp.mpf("0.01"),mp.mpf("0.5"),mp.mpf(2),mp.mpf(5)):
            p=mp.expm(t*q)
            values=[sum(abs(p[i,l]-p[j,l]) for l in range(k+1))/2 for i in range(k+1) for j in range(i+1,k+1)]
            ends=sum(abs(p[0,l]-p[k,l]) for l in range(k+1))/2
            assert max(values)-ends<mp.mpf("1e-60")
            if not e:
                tail=mp.exp(-t)*sum(t**j/mp.factorial(j) for j in range(k))
                largest_error=max(largest_error,abs(tail-ends))
            cases+=1
print("Direct expm endpoint maximization:",cases,"cases passed (k=1..6, eps=0,.001,.01,.5,1,2, four times).")
print("Pure-death Gamma identity largest discrepancy",mp.nstr(largest_error,6))
print("All assertions passed; wall seconds",round(time.monotonic()-START,3))
print("Peak resident bytes (macOS ru_maxrss)",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
