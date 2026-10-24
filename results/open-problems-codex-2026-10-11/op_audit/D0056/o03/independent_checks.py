from fractions import Fraction as F
from pathlib import Path
from itertools import product
import math,json
checks={}
# Derive PGF recurrence directly from convolution for many actual finite laws.
count=0
for weights in product(range(4),repeat=4):
    total=sum(weights)
    if total==0: continue
    p=[F(w,total) for w in weights]; g=sum(p[k]*2**k for k in range(4)); q=1-p[0]; e=g-1
    direct=sum(p[x]*p[y]*2**max(x+y-1,0) for x in range(4) for y in range(4))
    assert direct-1==e+e*e/2-q+q*q/2
    count+=1
checks['independent_convolution_identity_cases']=count
count=0
for n in range(2,151):
    b=F(3,2*n)
    # q=4/n^2 gives forcing >=3/n^2 for n>=3; test every valid grid point.
    for r in range(21):
        e=b*F(r,20)
        for s in range(31):
            q=F(s,30)
            if q-q*q/2<F(3,n*n): continue
            nxt=e+e*e/2-q+q*q/2
            assert nxt-F(3,2*(n+1)) <= e-b-F(3,8*n*n)
            count+=1
checks['independent_exact_barrier_cases']=count
A=sum(2.0**(-k)/k**3 for k in range(2,501))
# tail bounds make B rigorous to interval width <1e-5
M=100000
B=sum((k-1)/k**3 for k in range(2,M+1)); Btail_upper=1/M
checks['normalization_intervals']={'A':A,'B_lower':B,'B_upper':B+Btail_upper,'c_lower':1/(A+B+Btail_upper),'c_upper':1/(A+B)}
# A finite critical truncation, independently normalized, verifies critical cancellation.
for M in range(2,31):
    a=sum(F(1,2**k*k**3) for k in range(2,M+1)); b=sum(F(k-1,k**3) for k in range(2,M+1)); c=1/(a+b)
    p=[c*b,F(0)]+[c*F(1,2**k*k**3) for k in range(2,M+1)]
    assert sum(p)==1
    assert sum(F(k)*2**k*p[k] for k in range(M+1))==sum(2**k*p[k] for k in range(M+1))
checks['exact_finite_normalization_criticality_cases']=29
# Re-derive the log estimate analytically: derivative of log(1+x)-x+x^2/2=x^2/(1+x)>=0.
checks['log_estimate']='Derivative x^2/(1+x)>=0, value 0 at x=0; harmonic sum >= integral_N^n dx/x.'
Path('independent_checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
print(json.dumps(checks,indent=2))
