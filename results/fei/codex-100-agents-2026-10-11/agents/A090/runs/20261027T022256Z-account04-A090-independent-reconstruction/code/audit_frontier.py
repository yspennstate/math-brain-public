"""Exact prime-log reconstruction of full two-outcome costs, independently optimized."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
from functools import lru_cache
import json,time,hashlib

ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
    global checks
    checks+=1
    if not x:raise AssertionError(checks)

def add(*items):
    d={}
    for item in items:
        for k,v in item.items():d[k]=d.get(k,F(0))+v
    return {k:v for k,v in d.items() if v}
def scale(d,t):return {k:v*t for k,v in d.items() if v*t}
@lru_cache(None)
def log(q):
    if q<=0:raise ValueError(q)
    d={}
    for num,sign in [(q.numerator,1),(q.denominator,-1)]:
        prime=2
        while prime*prime<=num:
            while num%prime==0:d[prime]=d.get(prime,0)+sign;num//=prime
            prime+=1
        if num>1:d[num]=d.get(num,0)+sign
    return {k:F(v) for k,v in d.items() if v}
def ce(p,q):return add(*(scale(log(y),-x) for x,y in zip(p,q) if x))
def spectrum(v):
    N=len(v)
    return tuple(F(sum(z*(-1 if (s&t).bit_count()%2 else 1) for t,z in enumerate(v))**2,N*N) for s in range(N))
def optimum(pi,T):
    sols=set();l=[t/2 for t in T]
    for bits in product((False,True),repeat=len(pi)):
        den=F(1)-sum(p for p,b in zip(pi,bits) if b)
        if not den:continue
        k=(F(1)-sum(f for f,b in zip(l,bits) if b))/den
        x=tuple(f if b else k*p for f,p,b in zip(l,pi,bits))
        if k>0 and all((k*p<=f if b else k*p>=f) for f,p,b in zip(l,pi,bits)):sols.add(x)
    ck(len(sols)==1);return sols.pop()
def main():
    start=time.monotonic();edges=frontiers=moves=0
    for n in range(1,4):
        N=1<<n
        for mask in range(1<<N):
            v=[1 if mask&(1<<j) else -1 for j in range(N)];p=spectrum(v)
            # Positive, paid/supplied current root; never source-priced here.
            q=tuple(F(1,4)*z+F(3,4*N) for z in p)
            for i in range(n):
                remain=[s for s in range(N) if not s&(1<<i)]
                inherited=tuple(q[s]+q[s|(1<<i)] for s in remain)
                children=[spectrum([v[s|bit*(1<<i)] for s in remain]) for bit in (0,1)]
                ck(sum(inherited)==1);ck(all(sum(pv)==1 for pv in children));edges+=1
                for choose in ((0,),(1,),(0,1)):
                    old=scale(add(*(ce(pv,inherited) for pv in children)),F(1,2))
                    refs=[inherited,inherited];delta={}
                    for bit in choose:
                        pv=children[bit];a=1-pv[0];w=1-inherited[0]
                        if not a:continue
                        pi=tuple(z/a for z in pv[1:]);M=tuple(z/w for z in inherited[1:])
                        T=tuple(F(j==0) for j in range(len(pi)));x=optimum(pi,T)
                        refs[bit]=(inherited[0],)+tuple(w*z for z in x)
                        local=add(*(scale(log(m/z),a*pij) for pij,m,z in zip(pi,M,x) if pij))
                        delta=add(delta,scale(local,F(1,2)));moves+=1
                        ck(refs[bit][0]==inherited[0]);ck(sum(refs[bit])==sum(inherited))
                    new=scale(add(*(ce(pv,r) for pv,r in zip(children,refs))),F(1,2))
                    ck(add(new,scale(old,-1))==delta)
                    B={2:F(1000)};U={2:F(7,8),3:F(1,4)}
                    oldmargin=add(B,scale(U,-1),scale(old,-1))
                    newmargin=add(B,scale(U,-1),scale(new,-1))
                    ck(newmargin==add(oldmargin,scale(delta,-1)))
                    # Untouched sibling remains literally the original full reference.
                    for bit in set((0,1))-set(choose):ck(refs[bit] is inherited)
                    frontiers+=1
    elapsed=time.monotonic()-start;ck(elapsed<55)
    out={'verdict':'PASS','arithmetic':'Fraction coefficients of exact prime-factor log2 expressions; independent direct character sums and exhaustive active sets','checks':checks,'physical_edges':edges,'full_two_child_frontiers':frontiers,'actual_nonconstant_replacements':moves,'runtime_seconds':elapsed,'scope':'all Boolean n1..3 functions, all physical coordinates, each one-child or two-child replacement; supplied positive root only; no source-price assertion','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'out/FRONTIER.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
