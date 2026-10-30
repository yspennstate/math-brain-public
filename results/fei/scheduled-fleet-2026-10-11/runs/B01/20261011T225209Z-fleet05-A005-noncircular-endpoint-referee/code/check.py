"""A005 v1: exact activation erasure identities, no numerical logarithms."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import argparse, json, time

ROOT=Path(__file__).resolve().parents[1]
@lru_cache(None)
def factors(n):
    result={}; d=2
    while d*d<=n:
        while n%d==0: result[d]=result.get(d,0)+1; n//=d
        d+=1
    if n>1: result[n]=result.get(n,0)+1
    return result
def add(*terms):
    r={}
    for v in terms:
        for p,c in v.items(): r[p]=r.get(p,Q(0))+c
    return {p:c for p,c in r.items() if c}
def scale(v,c): return {p:c*x for p,x in v.items() if c*x}
def phi(x):
    if not x: return {}
    return add({p:-x*v for p,v in factors(x.numerator).items()},
               {p:x*v for p,v in factors(x.denominator).items()})
def L(u,v): return add(phi(u*u),phi(v*v),scale(phi(u*u+v*v),-1))
def fwht(v):
    a=list(v); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h): a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
        h*=2
    return [Q(x,len(a)) for x in a]
def entropy(a): return add(*(phi(x*x) for x in a))
def influence(a,i): return sum((x*x for s,x in enumerate(a) if s>>i&1),Q(0))
def erasure(a,i): return add(*(L(x,a[s|(1<<i)]) for s,x in enumerate(a) if not s>>i&1))
def total(a,n): return sum((influence(a,i) for i in range(n)),Q(0))
def seed(n,b): return [1 if b>>x&1 else -1 for x in range(1<<n)]
def activated(f,n,m,k):
    N=n*m+k; vals=[]
    for x in range(1<<N):
        g=1
        for j in range(m): g*=f[(x>>(j*n))&((1<<n)-1)]
        vals.append(g if (x>>(n*m))==0 else 1)
    return fwht(vals)

def run(nmax):
    count=0; cases=0; start=time.perf_counter()
    def eq(x,y):
        nonlocal count
        count+=1
        assert x==y,(x,y)
    for n in range(1,nmax+1):
        for b in range(1<<(1<<n)):
            f=seed(n,b); a=fwht(f); mu=a[0]
            for m in ([1,2] if n<=2 or b in [1,23,105,150] else [1]):
                for k in [1,2]:
                    cases+=1; t=Q(1,1<<k); c=mu**m
                    A=activated(f,n,m,k); N=n*m+k
                    eq(sum(x*x for x in A),Q(1))
                    eq(A[0],1-t+t*c)
                    eq(total(A,N),t*(m*total(a,n)+k*(1-c)))
                    q=1-c*c; w=(1-c)**2
                    expected=add(scale(add(scale(entropy(a),m),scale(phi(c*c),-1)),t),
                        phi((1-t+t*c)**2),scale(phi(w),t-t*t),
                        {2:2*k*(t*q+(t-t*t)*w)})
                    eq(entropy(A),expected)
                    for j in range(m):
                        for i in range(n):
                            d=a[1<<i]*mu**(m-1)
                            expected=add(scale(erasure(a,i),t),scale(L(c,d),-t),
                                scale(L(c-1,d),t-t*t),L(1-t+t*c,t*d))
                            eq(influence(A,j*n+i),t*influence(a,i))
                            eq(erasure(A,j*n+i),expected)
                    # Control formula is valid for unbalanced cores too.
                    control=add({2:t*(1-c*c)+(t-2*t*t)*(1-c)**2},
                                L(1-t+t*c,t*(c-1)))
                    for i in range(n*m,N):
                        eq(influence(A,i),t*(1-c))
                        eq(erasure(A,i),control)
    result={'helper_version':'A005-v1','nmax':nmax,'cases':cases,'assertions':count,
            'failures':0,'arithmetic':'integer FWHT; Fraction; exact log-prime vectors',
            'elapsed_seconds':time.perf_counter()-start}
    (ROOT/'out'/f'CHECK_n{nmax}.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--nmax',type=int,choices=[2,3],required=True)
    run(p.parse_args().nmax)
