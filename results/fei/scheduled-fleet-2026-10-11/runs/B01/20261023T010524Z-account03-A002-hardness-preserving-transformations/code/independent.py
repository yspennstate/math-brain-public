from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from functools import lru_cache
import time,json
START=time.monotonic();checks=0;out=Path(__file__).resolve().parents[1]/'out'
def ck(b):
    global checks
    checks+=1;assert b
    if time.monotonic()-START>55:raise RuntimeError('55s cap')
def rank(vs):
    rows=[]
    for x in vs:
        for p in rows:x=min(x,x^p)
        if x:rows.append(x);rows.sort(reverse=True)
    return len(rows)
@lru_cache(None)
def bases(n):return tuple(b for b in combinations(range(1,1<<n),n) if rank(b)==n)
@lru_cache(None)
def measure(f):
    n=(len(f)-1).bit_length();D=len(f)
    w=[sum(f[x]!=f[x^v] for x in range(D)) for v in range(D)]
    ell=Q(min(sum(w[v] for v in b) for b in bases(n)),D)
    a=Q(min(sum(min(w[v],D-w[v]) for v in b) for b in bases(n)),D)
    I=sum((Q(w[1<<i],D) for i in range(n)),Q(0))
    # Direct character sums independently compare with physical translation.
    c=[sum(y*(-1)**((x&s).bit_count()%2) for x,y in enumerate(f)) for s in range(D)]
    for v in range(D):ck(Q(w[v],D)==Q(sum(c[s]**2 for s in range(D) if (s&v).bit_count()%2),D*D))
    return dict(n=n,ell=ell,a=a,I=I,w=w,mu=Q(sum(f),D),c=c)
def act(f,k):return tuple(f)+(1,)*(len(f)*((1<<k)-1))
def child(f,i,b):
    n=(len(f)-1).bit_length();others=[j for j in range(n) if j!=i]
    return tuple(f[(b<<i)+sum(((x>>r)&1)<<j for r,j in enumerate(others))] for x in range(1<<(n-1)))
fixtures=0;childpairs=0
for n in range(3):
    for mask in range(1<<(1<<n)):
        f=tuple(1-2*((mask>>x)&1) for x in range(1<<n));F=act(f,2)
        s=measure(f);t=measure(F);p=Q(1,4)
        ck(t['a']==t['ell']==p*(s['ell']+2*(1-s['mu'])))
        for i in range(n):
            cs=[measure(child(f,i,b)) for b in [0,1]];cts=[measure(child(F,i,b)) for b in [0,1]]
            source=s['I']-Q(s['w'][1<<i],len(f))-sum(c['a'] for c in cs)/2
            loss=sum(c['ell']-c['a'] for c in cs)/2
            rho=t['I']-Q(t['w'][1<<i],len(F))-sum(c['a'] for c in cts)/2
            ck(rho==p*(source-loss));childpairs+=1
        fixtures+=1
bent=(1,1,1,-1);s=measure(bent);t=measure(act(bent,2))
cs=[measure(child(bent,0,b)) for b in [0,1]];cts=[measure(child(act(bent,2),0,b)) for b in [0,1]]
ck(s['a']==s['I']==1);ck(t['a']==t['I']==Q(1,2))
ck(s['I']-Q(1,2)-sum(c['a'] for c in cs)/2==Q(1,2))
ck(t['I']-Q(1,8)-sum(c['a'] for c in cts)/2==0)
ck(sorted(c['a'] for c in cts)==[Q(0),Q(3,4)])
# Source K2 query/reset bill is zero. Activated K2 bill is strictly positive:
# (120+18log2(3)-49log2(7))/32, certified without logarithm evaluation.
ck(2**120*3**18>7**49)
ck(sorted(x*x for x in t['c'])==[4]*15+[196])
result={'status':'PASS','assertions':checks,'seeds':fixtures,'singleton_child_pairs':childpairs,'seconds':time.monotonic()-START,'arithmetic':'physical disagreement counts, direct characters, exhaustive all independent bases n<=4; no main-helper import','guard':'2^120*3^18>7^49; activated K2 signed bill positive though source query/reset bill zero','max_dimension':4}
(out/'INDEPENDENT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
