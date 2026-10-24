from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
from functools import lru_cache
import json, time

RUN = Path(__file__).resolve().parents[1]
START = time.perf_counter()
COUNTS = {'cases': 0, 'assertions': 0, 'rank_cut_checks': 0, 'entropy_intervals': 0}

def ck(b):
    COUNTS['assertions'] += 1
    assert b

def walsh(f):
    a = list(f)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return a

def sign_table(n, code):
    return [1-2*((code>>x)&1) for x in range(1<<n)]

def chi(s, x):
    return (-1)**((s&x).bit_count())

def influences(f):
    n = len(f).bit_length()-1
    return [Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(n)]

def plaquette(f,i,j):
    return Q(sum(f[x]*f[x^(1<<i)]*f[x^(1<<j)]*f[x^(1<<i)^(1<<j)] == -1 for x in range(len(f))),len(f))

def not_factorable_by_cut(f, mask):
    full = len(f)-1
    rows=[x for x in range(len(f)) if x&mask==x]
    cols=[x for x in range(len(f)) if x&(full^mask)==x]
    return any(f[0]*f[r|c] != f[r]*f[c] for r in rows for c in cols)

@lru_cache(maxsize=1024)
def log2_interval(x, terms=40):
    assert x>0
    shift=0
    while x>=2:
        x/=2; shift+=1
    while x<1:
        x*=2; shift-=1
    def ln_interval(y):
        z=(y-1)/(y+1)
        lo=2*sum((z**(2*k+1))/Q(2*k+1) for k in range(terms))
        err=2*z**(2*terms+1)/Q(2*terms+1)/(1-z*z)
        return lo,lo+err
    a,b=ln_interval(x)
    c,d=ln_interval(Q(2))
    return Q(shift)+a/d, Q(shift)+b/c

def entropy_interval(probs):
    lo=hi=Q(0)
    for p in probs:
        if p:
            a,b=log2_interval(1/p)
            lo+=p*a; hi+=p*b
    return lo,hi

def verify(f, a, cross=None, prime=False):
    if time.perf_counter()-START > 55:
        (RUN/'out'/'PILOT_TIMEOUT.json').write_text(json.dumps(COUNTS,indent=2),encoding='utf-8')
        raise TimeoutError('Frozen 55-second internal stopping bound reached')
    n=len(f).bit_length()-1
    N=len(f); p=Q(1,N)
    g=list(f); g[a]*=-1
    F,G=walsh(f),walsh(g)
    old=[Q(v*v,N*N) for v in F]
    new=[Q(v*v,N*N) for v in G]
    inf0,inf1=influences(f),influences(g)
    ck(sum(old)==sum(new)==1)
    for s in range(N):
        ck(G[s]==F[s]-2*f[a]*chi(s,a))
    for i in range(n):
        ri=f[a]*f[a^(1<<i)]
        ck(inf1[i]-inf0[i]==2*p*ri)
        ck(sum(new[s] for s in range(N) if s&(1<<i))==inf1[i])
    for i,j in combinations(range(n),2):
        ri=f[a]*f[a^(1<<i)]; rj=f[a]*f[a^(1<<j)]
        rij=f[a]*f[a^(1<<i)^(1<<j)]
        k0=sum(old[s] for s in range(N) if s&(1<<i) and s&(1<<j))
        k1=sum(new[s] for s in range(N) if s&(1<<i) and s&(1<<j))
        ck(k1-k0==p*(ri+rj-rij))
        # Independent physical derivative computation.
        phys=Q(sum((g[x]-g[x^(1<<i)]-g[x^(1<<j)]+g[x^(1<<i)^(1<<j)])**2 for x in range(N)),16*N)
        ck(phys==k1)
        c0,c1=plaquette(f,i,j),plaquette(g,i,j)
        sigma=f[a]*f[a^(1<<i)]*f[a^(1<<j)]*f[a^(1<<i)^(1<<j)]
        ck(c1-c0==4*p*sigma)
        if cross is not None and bool(cross&(1<<i))!=bool(cross&(1<<j)):
            ck(c0==0 and c1==4*p)
            ck(k0==inf0[i]*inf0[j])
            ck(rij==ri*rj)
            cov1=k1-inf1[i]*inf1[j]
            expected=p*(ri+rj-ri*rj)-2*p*(ri*inf0[j]+rj*inf0[i])-4*p*p*ri*rj
            ck(cov1==expected)
            ck(abs(cov1)<=7*p+4*p*p)
    tv=sum(abs(x-y) for x,y in zip(old,new))/2
    ck(tv*tv<=4*p*(1-p))
    if prime:
        ck(sum(x==-1 for x in g)%2==1)
        ck(all(v%4==2 for v in G))
        for mask in range(1,N-1):
            if mask&1:
                ck(not_factorable_by_cut(g,mask))
                COUNTS['rank_cut_checks']+=1
    COUNTS['cases']+=1
    return old,new,tv

for n in (1,2,3):
    for code in range(1<<(1<<n)):
        f=sign_table(n,code)
        verify(f,0)

for c in range(16):
    for d in range(16):
        h,k=sign_table(2,c),sign_table(2,d)
        f=[h[x&3]*k[x>>2] for x in range(16)]
        verify(f,0,cross=3,prime=True)

for d in (1,2):
    for code in range(1<<(1<<d)):
        h=sign_table(d,code)
        for t in (1,2,3):
            n=t*d+1
            f=[]
            for x in range(1<<n):
                v=(-1)**((x>>(n-1))&1)
                for j in range(t):
                    v*=h[(x>>(j*d))&((1<<d)-1)]
                f.append(v)
            old,new,tv=verify(f,0,cross=(1<<(n-1))-1,prime=True)
            # Spectrum product identity for balanced tensor; no logarithm needed.
            hp=[Q(v*v,1<<(2*d)) for v in walsh(h)]
            for s in range(1<<n):
                expected=Q((s>>(n-1))&1)
                for j in range(t):
                    expected*=hp[(s>>(j*d))&((1<<d)-1)]
                ck(old[s]==expected)
            if n>=4:
                u=Q(2)**(1-n//2)
                ck(tv<=u<=Q(1,2))
                a,b=entropy_interval(old)
                c,e=entropy_interval(new)
                h0,h1=entropy_interval([u,1-u])
                bound=h0+n*u
                ck(max(e-a,b-c)<=bound)
                COUNTS['entropy_intervals']+=1

ck(COUNTS['cases']==592)
COUNTS['runtime_seconds']=time.perf_counter()-START
COUNTS['status']='PASS'
COUNTS['arithmetic']='integer Walsh and physical truth tables; exact Fraction identities and atanh logarithm intervals'
(RUN/'out'/'EXACT_CHECK.json').write_text(json.dumps(COUNTS,indent=2)+'\n',encoding='utf-8')
print(json.dumps(COUNTS,indent=2))
