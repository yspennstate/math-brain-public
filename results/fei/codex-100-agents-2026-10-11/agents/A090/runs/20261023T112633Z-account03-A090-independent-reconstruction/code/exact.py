from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import json,time,hashlib

run=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0
def check(x):
    global assertions
    assertions+=1
    if not x:raise AssertionError(assertions)
def combine(*terms):
    ans={}
    for c,d in terms:
        for p,v in d.items():ans[p]=ans.get(p,F(0))+c*v
    return {p:v for p,v in ans.items() if v}
@lru_cache(None)
def logq(q):
    q=F(q); check(q>0); ans={}
    for a,sign in [(q.numerator,1),(q.denominator,-1)]:
        p=2
        # All probability denominators from smoothing are small except 2^m;
        # handle that factor first, leaving the large Mersenne numerator as
        # a whole logarithmic atom instead of factoring an arbitrary integer.
        while a%2==0 and a>1:
            ans[2]=ans.get(2,F(0))+sign; a//=2
        while p<=31 and p*p<=a:
            while a%p==0:ans[p]=ans.get(p,F(0))+sign; a//=p
            p+=1
        if a>1:ans[a]=ans.get(a,F(0))+sign
    return {p:v for p,v in ans.items() if v}
def entropy(p):return combine(*[(-x,logq(x)) for x in p if x])
def ce(p,q):
    check(len(p)==len(q) and sum(p)==sum(q)==1)
    check(all(not x or y>0 for x,y in zip(p,q)))
    return combine(*[(-x,logq(y)) for x,y in zip(p,q) if x])
def ln_bounds(x):
    t=(x-1)/(x+1); check(0<=t<=F(1,3))
    val=sum((2*t**(2*k+1)/F(2*k+1) for k in range(40)),F(0))
    return val,val+2*t**81/(81*(1-t*t))
ln2=ln_bounds(F(2))
@lru_cache(None)
def log_bounds(a):
    k=a.bit_length()-1; l,h=ln_bounds(F(a,2**k))
    return F(k)+l/ln2[1],F(k)+h/ln2[0]
def bounds(d):
    lo=hi=F(0)
    for p,c in d.items():
        a,b=log_bounds(p)
        lo+=c*(a if c>=0 else b); hi+=c*(b if c>=0 else a)
    return lo,hi
def positive(d):return bounds(d)[0]>0
def display(d):return [float(v) for v in bounds(d)]
def walsh(v):
    a=list(v); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
        h*=2
    return a
def spectrum(v):return [F(x*x,len(v)**2) for x in walsh(v)]
def restrict(v,j,s):return [x for k,x in enumerate(v) if (k>>j)&1==s]
def marginal(p,j):return [p[k]+p[k|(1<<j)] for k in range(len(p)) if not k&(1<<j)]
def erased(p,j):return combine((1,entropy(p)),(-1,entropy(marginal(p,j))))
def inf(v,j):return F(sum(x!=v[k^(1<<j)] for k,x in enumerate(v)),len(v))
def query(v,q,j):
    p=spectrum(v); pm=marginal(p,j); r=marginal(q,j)
    children=[restrict(v,j,s) for s in (0,1)]
    ps=[spectrum(c) for c in children]
    check(all((a+b)/2==x for a,b,x in zip(ps[0],ps[1],pm)))
    E=erased(p,j)
    # R is obtained independently as the exact difference of two KLs.
    R=combine((1,ce(p,q)),(-1,entropy(p)),(-1,ce(pm,r)),(1,entropy(pm)))
    check(not R or bounds(R)[0]>=0)
    check(not combine((1,ce(p,q)),(-1,E),(-F(1,2),ce(ps[0],r)),(-F(1,2),ce(ps[1],r)),(-1,R)))
    return children,ps,r,E,R
def smooth(r):return [F(7,8)*x+F(1,8*len(r)) for x in r]
