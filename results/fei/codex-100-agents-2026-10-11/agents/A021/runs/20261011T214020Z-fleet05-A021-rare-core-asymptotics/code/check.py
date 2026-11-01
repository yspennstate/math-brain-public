"""v1: exact truth-table/Walsh/prime-log checks; no floating logarithms."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from itertools import combinations
import json, time
from pathlib import Path

@lru_cache(None)
def factors(n):
    out = {}; p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0)+1; n //= p
        p += 1
    if n > 1: out[n] = out.get(n, 0)+1
    return out

def logadd(out, x, weight):
    assert x > 0
    for n, s in ((x.numerator, 1), (x.denominator, -1)):
        for p, e in factors(n).items(): out[p] += weight*s*e

def clean(d): return {p:v for p,v in d.items() if v}
def add(*terms):
    out=defaultdict(F)
    for weight, d in terms:
        for p,v in d.items(): out[p] += weight*v
    return clean(out)
def entropy(probs):
    out=defaultdict(F)
    for p in probs:
        if p: logadd(out,p,-p)
    return clean(out)
def walsh(a):
    b=a.copy(); h=1
    while h<len(b):
        for j in range(0,len(b),2*h):
            for i in range(j,j+h): b[i],b[i+h]=b[i]+b[i+h],b[i]-b[i+h]
        h*=2
    return [F(v,len(b)) for v in b]
def influence(a):
    n=(len(a)-1).bit_length()
    return sum((F(sum(a[x]!=a[x^(1<<j)] for x in range(len(a))),len(a)) for j in range(n)),F(0))
def tensor(a,t):
    n=(len(a)-1).bit_length(); mask=len(a)-1
    ans=[]
    for x in range(1<<(n*t)):
        value=1
        for j in range(t): value*=a[(x>>(n*j))&mask]
        ans.append(value)
    return ans
def activated(a,k):
    return a+[1]*(len(a)*((1<<k)-1))
def B(q,k):
    out=defaultdict(F); out[2]=(4*q-2*q*q)*k
    logadd(out,1-q,-2*(1-q)**2)
    return clean(out)

def run():
    start=time.perf_counter(); cases=0; assertions=0; max_dimension=0
    seeds=[]
    for neg in combinations(range(8),4):
        seeds.append([-1 if x in neg else 1 for x in range(8)])
    for a in seeds:
        ah=entropy([c*c for c in walsh(a)]); ai=influence(a)
        for t in (1,2):
            core=tensor(a,t); cs=walsh(core); ch=entropy([c*c for c in cs])
            assert ch==add((F(t),ah)); assertions+=1
            assert influence(core)==t*ai; assertions+=1
            for k in (1,2,3):
                q=F(1,1<<k); f=activated(core,k); fs=walsh(f)
                max_dimension=max(max_dimension,(len(f)-1).bit_length())
                assert sum(c*c for c in fs)==1; assertions+=1
                assert entropy([c*c for c in fs])==add((q,ch),(F(1),B(q,k))); assertions+=1
                assert influence(f)==q*(t*ai+k); assertions+=1
                assert fs[0]==1-q; assertions+=1
                # Restrict the last control: inactive child is constant; active has k-1 controls.
                active=activated(core,k-1); b=walsh(active)
                e=[]; packets=[]
                for j,c in enumerate(b):
                    av=F(j==0); e.append((abs(av)-abs(c))**2/4)
                    packets.append((av*av+c*c)/2)
                mu=sum(e); assert mu==q; assertions+=1
                # J=mu[log(1/mu)-D(nu||packets)]=sum e log(packets/e).
                J=defaultdict(F)
                for m,p in zip(e,packets):
                    if m: logadd(J,p/m,m)
                Q0=1-2*q+2*q*q
                predicted=defaultdict(F); predicted[2]=q-q*q
                logadd(predicted,Q0/(q*q),q*q)
                assert clean(J)==clean(predicted); assertions+=1
                # Core spectrum cancels from entropy decrement at every active control node.
                child_h=entropy([c*c for c in b])
                delta=add((F(1),entropy([c*c for c in fs])),(-F(1,2),child_h))
                prev={} if k==1 else B(2*q,k-1)
                # At k=1 the active child is exactly the balanced core.
                assert delta==add((F(1),B(q,k)),(-F(1,2),prev)); assertions+=1
                cases+=1
    result={"helper_version":"1","cases":cases,"balanced_three_bit_seeds":len(seeds),"assertions_passed":assertions,"arithmetic":"integer Walsh, Fraction, exact formal prime-log vectors","max_dimension":max_dimension,"elapsed_seconds":time.perf_counter()-start,"full_fei":"OPEN"}
    print(json.dumps(result,indent=2))
    (Path(__file__).resolve().parents[1]/'out'/'validation.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__': run()
