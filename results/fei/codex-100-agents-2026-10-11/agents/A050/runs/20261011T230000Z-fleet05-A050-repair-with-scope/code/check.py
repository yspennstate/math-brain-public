import json,time
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
started=time.perf_counter()
checks=0
def ck(v):
    global checks
    assert v
    checks+=1
def walsh(t):
    a=list(t); k=1
    while k<len(a):
        for j in range(0,len(a),2*k):
            for l in range(j,j+k): a[l],a[l+k]=a[l]+a[l+k],a[l]-a[l+k]
        k*=2
    return tuple(a)
def entropy(p):
    # Exact formal sum of rational multiples of logarithms of primes.
    c=Counter()
    for v in p:
        if not v: continue
        for a,s in [(v.numerator,-1),(v.denominator,1)]:
            k=2
            while k*k<=a:
                while a%k==0: c[k]+=s*v; a//=k
                k+=1
            if a>1: c[a]+=s*v
    return {k:v for k,v in c.items() if v}
def plus(*es):
    c=Counter()
    for e in es:
        for k,v in e.items(): c[k]+=v
    return {k:v for k,v in c.items() if v}
def scale(e,a): return {k:a*v for k,v in e.items() if a*v}
def spectral(t): return tuple(Q(a,len(t)) for a in walsh(t))
def h2(p): return entropy([p,1-p])
def pair(g,h,n,biased=False):
    N=1<<n; G=spectral(g); H=spectral(h)
    same=all(not a or not b or a*a==b*b for a,b in zip(G,H))
    if not same: return False
    w=sum((a*a for a,b in zip(G,H) if a and b),Q(0))
    b=sum((a*a for a,c in zip(G,H) if a and c and a==-c),Q(0))
    d=Q(sum(x!=y for x,y in zip(g,h)),N)
    ck(d==(1-w)/2+b)
    f=list(g)+list(h); P=[a*a for a in spectral(f)]
    L=plus(entropy(P),scale(entropy([a*a for a in G]),Q(-1,2)),scale(entropy([a*a for a in H]),Q(-1,2)))
    ck(L==({2:2*(1-w)} if w!=1 else {}))
    ck(2*(1-w)<=4*d)
    if biased:
        for p in [Q(1,8),Q(1,4),Q(1,2),Q(3,4)]:
            a=[((1-p)*x+p*y)**2 for x,y in zip(G,H)]
            bmass=[p*(1-p)*(y-x)**2 for x,y in zip(G,H)]
            q=[x+y for x,y in zip(a,bmass)]
            M=plus(entropy(a+bmass),scale(entropy(q),-1))
            J=plus(entropy(q),scale(entropy([x*x for x in G]),-(1-p)),scale(entropy([x*x for x in H]),-p))
            ck(J==scale(h2(p),1-w))
            ck(M==plus(J,scale(h2(4*p*(1-p)),b)))
    return True

counts={}; total=0; admitted=0
for n in range(4):
    N=1<<n
    tables=[tuple(1-2*((mask>>x)&1) for x in range(N)) for mask in range(1<<N)]
    ac=0
    for g in tables:
        for h in tables:
            total+=1; ac+=pair(g,h,n,biased=n<=2)
    counts[n]={'pairs':len(tables)**2,'admitted':ac}; admitted+=ac

def quadratic(mask):
    t=[]
    for x in range(8):
        y=[(x>>i)&1 for i in range(3)]
        terms=[1]+y+[y[0]*y[1],y[0]*y[2],y[1]*y[2]]
        t.append(1-2*(sum(((mask>>j)&1)*v for j,v in enumerate(terms))%2))
    return tuple(t)
qt=[quadratic(mask) for mask in range(128)]; qcount=0
for g in qt:
    for h in qt:
        G=spectral(g); H=spectral(h)
        if sum(bool(a) for a in G)==sum(bool(a) for a in H):
            ck(pair(g,h,3)); qcount+=1
g=quadratic(1<<4); h=quadratic(1<<6)
ck(pair(g,h,3,True))
G=spectral(g); H=spectral(h)
ck(sum(a*a for a,b in zip(G,H) if a and b)==Q(1,2))
ck(sum(x!=y for x,y in zip(g,h))==2)
f=list(g)+list(h); P=[a*a for a in spectral(f)]
I=sum(Q(i.bit_count())*p for i,p in enumerate(P))
ck(entropy(P)=={2:Q(3)})
ck(I==Q(5,4))
# Tensor and arbitrary common-factor admission is exact support/magnitude algebra.
for k in [tuple([1,1,1,-1]),tuple([1,-1,-1,-1,1,1,-1,1])]:
    a=tuple(x*y for y in k for x in g); b=tuple(x*y for y in k for x in h)
    ck(pair(a,b,3+(len(k).bit_length()-1)))
# Preserve the original AND repair failure: mean 1/2 overlaps a constant of magnitude 1.
ck(not pair((1,1,1,1),(1,1,1,-1),2))
out={'status':'PASS','all_pair_cases':total,'admitted_pair_cases':admitted,'quadratic_equal_rank_pairs':qcount,'counts':counts,'assertions':checks,'partial_overlap_example':{'H':3,'I':'5/4','selector_influence':'1/4','decrement':1,'w':'1/2'},'runtime_seconds':time.perf_counter()-started}
(ROOT/'out'/'CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
