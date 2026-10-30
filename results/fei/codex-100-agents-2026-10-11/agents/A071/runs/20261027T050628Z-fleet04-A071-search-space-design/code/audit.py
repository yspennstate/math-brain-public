from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations
import json,time
R=Path(__file__).resolve().parents[1]; start=time.monotonic(); count=0
def ck(p):
    global count
    count+=1; assert p
    if time.monotonic()-start>55:raise TimeoutError('frozen55s')
def rawln(t):
    z=(t-1)/(t+1); s=Q(0)
    for j in range(40):s+=2*z**(2*j+1)/(2*j+1)
    return s,s+2*z**81/(81*(1-z*z))
L2=rawln(Q(2))
@lru_cache(None)
def log2(t):
    e=0
    while t<1:t*=2;e-=1
    while t>=2:t/=2;e+=1
    a,b=rawln(t)
    return a/L2[1]+e,b/L2[0]+e
def entropy(probs):
    lo=hi=Q(0)
    for p in probs:
        if not p:continue
        a,b=log2(p);lo-=p*b;hi-=p*a
    return lo,hi
def spectrum(f):
    M=len(f)
    return [Q(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(f))**2,M*M) for s in range(M)]
encodings=[]
for k in range(2,7):
    values=[]
    classes=[min(z.bit_count(),2) for z in range(1<<k)]
    for code in permutations(range(4),3):
        # Direct physical-edge cost of BOTH outputs, not a spectral proxy.
        edges=sum((code[classes[z]]^code[classes[z^(1<<i)]]).bit_count() for z in range(1<<k) for i in range(k))
        cost=Q(edges,1<<k);values.append(cost)
        ck(cost>=Q(k*k,1<<(k-1)))
    ck(min(values)==Q(k*k,1<<(k-1)))
    encodings.append(dict(k=k,count=24,minimum=str(min(values)),minimizers=values.count(min(values))))
functions=0
for n in [1,2]:
    for mask in range(1<<(1<<n)):
        g=[1-2*((mask>>x)&1) for x in range(1<<n)]
        pg=spectrum(g); hg=entropy(pg)
        for k in [2,3]:
            N=n+k; f=[g[x% (1<<n)]*(-1 if x.bit_count()<=1 else 1) for x in range(1<<N)]
            pf=spectrum(f); hf=entropy(pf)
            padded=pg+[Q(0)]*((1<<N)-(1<<n))
            d=sum(abs(a-b) for a,b in zip(pf,padded))/2
            eps=Q(N+1,1<<N)
            ck(d*d<=4*eps)
            if d:
                hb=entropy([d,1-d]);bound=hb[0]+N*d
                ck(max(hf[1]-hg[0],hg[1]-hf[0])<bound)
            else:ck(hf==hg)
            functions+=1
out=dict(status='PASS',assertions=count,entropy_functions=functions,encodings=encodings,seconds=time.monotonic()-start,arithmetic='exact rational directed logarithm intervals')
(R/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
