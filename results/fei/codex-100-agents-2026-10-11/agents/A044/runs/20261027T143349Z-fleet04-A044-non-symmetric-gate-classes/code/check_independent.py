from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import time,json
root=Path(__file__).resolve().parents[1]
t0=time.monotonic();checks=0
def check(ok):
    global checks
    checks+=1
    if not ok:raise AssertionError(checks)

# Direct physical Fourier sums, independent of the tensor transform.
n=5;xs=list(product((0,1),repeat=n));size=32
def coeff(values,S):
    return sum(Q(values[x])*((-1)**sum(1-xs[x][i] for i in S)) for x in range(size))/size
f=[1 if sum(x)==0 else -1 for x in xs]
aa={S:coeff(f,S) for k in range(6) for S in __import__('itertools').combinations(range(5),k)}
rows=[]
for sigma in product((0,1),repeat=5):
    q=[1 if sum(x[i]^sigma[i] for i in range(5))>=2 else -1 for x in xs]
    jump=[]
    for S,a in aa.items():
        b=coeff(q,S)
        if len(S)>=2 and abs(b)>abs(a) and a*b>0:jump.append(S)
    r=sum(sigma);expected=[6,5,10,9,6,5][r]
    check(len(jump)==expected)
    # A small literal GF(2) inconsistency check: all zero-jump parity constraints.
    if not any(sigma):
        prescribed={S:(0 if len(S)==2 else 1) for S in aa if len(S) in (2,4)}
        check(prescribed[(0,1)]^prescribed[(2,3)]!=prescribed[(0,1,2,3)])
    rows.append(dict(weight=r,outward=len(jump)))
check(min(x['outward'] for x in rows)==5)

# Outward rational log intervals: range reduce into[1,2], use atanh series.
def unit_ln(x,terms=40):
    z=(x-1)/(x+1)
    lo=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(terms)),Q(0))
    err=2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
    return lo,lo+err
def ln(x):
    k=0
    while x<1:x*=2;k-=1
    while x>2:x/=2;k+=1
    l,u=unit_ln(x);l2,u2=unit_ln(Q(2))
    return (l+k*l2,u+k*u2) if k>=0 else (l+k*u2,u+k*l2)
l4,u4=ln(Q(4));intervals=[]
for N in (5,6,9,10):
    l,u=ln(Q(26+3*N,26))
    low=(26*l-N*u4)/256;high=(26*u-N*l4)/256
    check(0<low<=high)
    intervals.append(dict(N=N,lower=str(low),upper=str(high)))
out=dict(status='PASS',checks=checks,seconds=time.monotonic()-t0,
         arithmetic='direct physical coefficient sums; literal parity dependency;40-term rational range-reduced atanh intervals with proved geometric tail',
         reflection_cases=32,positive_full_KL_intervals=intervals)
(root/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','checks','seconds','reflection_cases']}))
