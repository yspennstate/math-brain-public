from fractions import Fraction as F
from functools import lru_cache

def check(ok,label):
    assert ok,label

class L:
    def __init__(self,d=None): self.d={p:F(v) for p,v in (d or {}).items() if v}
    def __add__(self,b):
        d=self.d.copy()
        for p,v in b.d.items(): d[p]=d.get(p,F(0))+v
        return L(d)
    def __sub__(self,b): return self+b*(-1)
    def __mul__(self,b): return L({p:v*b for p,v in self.d.items()})
    __rmul__=__mul__
    def __truediv__(self,b): return self*(F(1)/b)
    def __eq__(self,b): return self.d==b.d
    def pack(self): return {str(p):str(v) for p,v in sorted(self.d.items())}
def factor(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p=3 if p==2 else p+2
    if n>1: out[n]=out.get(n,0)+1
    return out
@lru_cache(None)
def log(q):
    q=F(q); assert q>0
    d=factor(q.numerator)
    for p,v in factor(q.denominator).items(): d[p]=d.get(p,0)-v
    return L(d)
def sumL(xs):
    z=L()
    for x in xs: z=z+x
    return z
@lru_cache(None)
def ln_bounds(p):
    a=F(p); power=0
    while a>=2: a/=2; power+=1
    z=(a-1)/(a+1); steps=24
    lower=2*sum((z**(2*j+1)/F(2*j+1) for j in range(steps)),F(0))
    remainder=2*z**(2*steps+1)/(F(2*steps+1)*(1-z*z))
    z2=F(1,3)
    l2=2*sum((z2**(2*j+1)/F(2*j+1) for j in range(steps)),F(0))
    r2=2*z2**(2*steps+1)/(F(2*steps+1)*(1-z2*z2))
    return lower+power*l2, lower+remainder+power*(l2+r2)
def nat_bounds(x):
    lo=hi=F(0)
    for p,v in x.d.items():
        a,b=ln_bounds(p); lo+=v*(a if v>=0 else b); hi+=v*(b if v>=0 else a)
    return lo,hi
def transform(table):
    w=list(table); step=1
    while step<len(w):
        for j in range(0,len(w),2*step):
            for z in range(step):
                a,b=w[j+z],w[j+z+step]; w[j+z]=a+b;w[j+z+step]=a-b
        step*=2
    return [F(a,len(table)) for a in w]
def cube(table):
    n=(len(table)-1).bit_length(); a=transform(table); p=[v*v for v in a]
    e=[F(sum(table[x]!=table[x^(1<<i)] for x in range(len(table))),len(table)) for i in range(n)]
    check(sum(p)==1,'Parseval')
    for i in range(n): check(e[i]==sum((v for s,v in enumerate(p) if s&(1<<i)),F(0)),'physical derivative versus spectrum')
    return a,p,e
