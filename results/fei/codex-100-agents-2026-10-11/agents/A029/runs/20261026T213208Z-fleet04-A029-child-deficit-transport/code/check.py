import json, sys, time, itertools, math
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache

ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic(); MODE=sys.argv[1]; LIMIT=55 if MODE=='pilot' else 240
checks=0; states=0; edges=0; roots=0
def ck(x):
    global checks
    checks+=1
    if not x: raise AssertionError(checks)
    if checks%1000==0 and time.monotonic()-START>LIMIT: raise TimeoutError('frozen runtime cap')
def add(*vs):
    z={}
    for v in vs:
        for p,c in v.items(): z[p]=z.get(p,F(0))+c
    return {p:c for p,c in z.items() if c}
def mul(v,c): return {p:a*c for p,a in v.items() if a*c}
@lru_cache(maxsize=8192)
def factors(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def logv(x):
    ck(x>0); z={p:F(k) for p,k in factors(x.numerator).items()}
    return add(z,{p:F(-k) for p,k in factors(x.denominator).items()})
def kl(p,q):
    ck(len(p)==len(q))
    z={}
    for a,b in zip(p,q):
        if a: ck(b>0); z=add(z,mul(logv(a/b),a))
    return z
@lru_cache(maxsize=2048)
def lnprime(p):
    k=p.bit_length()-1; r=F(p,2**k)
    def series(r):
        z=(r-1)/(r+1); z2=z*z; term=z; s=F(0)
        for j in range(20): s+=term/F(2*j+1); term*=z2
        return 2*s,2*s+2*term/(41*(1-z2))
    l,u=series(r); l2,u2=series(F(2))
    return l+k*l2,u+k*u2
def bounds(v):
    lo=hi=F(0)
    for p,c in v.items():
        a,b=lnprime(p)
        lo+=c*(a if c>=0 else b); hi+=c*(b if c>=0 else a)
    l2,u2=lnprime(2)
    return (lo/u2 if lo>=0 else lo/l2),(hi/l2 if hi>=0 else hi/u2)
def bern(k): return (1-k,k)
@lru_cache(maxsize=8192)
def spec(t):
    a=list(t); n=len(a); step=1
    while step<n:
        for s in range(0,n,2*step):
            for j in range(step): x,y=a[s+j],a[s+j+step]; a[s+j],a[s+j+step]=x+y,x-y
        step*=2
    return tuple(F(x,n) for x in a)
def restrict(t,i,b):
    return tuple(v for x,v in enumerate(t) if (x>>i)&1==b)
def merge(p,i):
    out=[F(0)]*(len(p)//2)
    for x,v in enumerate(p): out[(x&((1<<i)-1))|((x>>(i+1))<<i)]+=v
    return tuple(out)
def tables(n):
    return [tuple(1 if m>>x&1 else -1 for x in range(2**n)) for m in range(2**(2**n))]
def full(a,g,h):
    return tuple((g[x//len(a)] if a[x%len(a)]==1 else h[x//len(a)]) for x in range(len(a)*len(g)))
def child(s,i,b):
    a,g,h=s; nc=len(a).bit_length()-1
    return (restrict(a,i,b),g,h) if i<nc else (a,restrict(g,i-nc,b),restrict(h,i-nc,b))
@lru_cache(maxsize=4096)
def node(a,g,h,e):
    global states
    states+=1
    nc=len(a).bit_length()-1; t=full(a,g,h); f=spec(t); P=tuple(x*x for x in f)
    av=F(sum(a),len(a)); V=1-av*av; gamma=F(sum(x!=y for x,y in zip(g,h)),len(g)); eta=V*gamma
    A=spec(a); B=tuple(x*x/V if V else F(0) for x in A)
    q=tuple(sum(P[u+v*len(a)] for u in range(len(a))) for v in range(len(g)))
    k=tuple(sum(P[u+v*len(a)] for u in range(1,len(a)))/q[v] if q[v] else F(0) for v in range(len(g)))
    ell=tuple((1-e)*x+e*eta for x in k)
    Q=[F(0)]*len(P); C={}
    for v,qt in enumerate(q):
        if not qt: continue
        ck(e*eta<=ell[v]<=1-e*(1-eta))
        Q[v*len(a)]=qt*(1-ell[v])
        for u in range(1,len(a)): Q[u+v*len(a)]=qt*ell[v]*B[u]
        C=add(C,mul(kl(bern(k[v]),bern(ell[v])),qt))
        chord=add(mul(logv(1/(1-e*eta)),1-k[v]),mul(logv(1/(1-e*(1-eta))),k[v]))
        if k[v] in (0,1): ck(C is not None)
        else: ck(bounds(add(chord,mul(kl(bern(k[v]),bern(ell[v])),-1)))[0]>=0 or e==0)
    ck(sum(P)==sum(Q)==1); ck(sum(q[v]*k[v] for v in range(len(q)))==eta)
    ck(sum(q[v]*ell[v] for v in range(len(q)))==eta)
    ck(kl(P,Q)==C)
    if C: ck(bounds(C)[1]<=F(31,160)*eta)
    else: ck(C=={})
    return t,P,tuple(Q),eta,gamma,V,C
def edge(s,i,e):
    global edges
    edges+=1; t,P,Q,eta,gamma,V,C=node(*s,e)
    cs=[child(s,i,b) for b in (0,1)]; ns=[node(*c,e) for c in cs]
    M=merge(P,i); N=merge(Q,i)
    raw=[]; inherited=[]; r=[]
    for z in ns:
        pc=z[1]; rq=tuple(N[j]*pc[j]/(2*M[j]) if M[j] else N[j]/2 for j in range(len(M)))
        rb=sum(rq); ck(rb>0); qc=tuple(x/rb for x in rq)
        r.append(rb); inherited.append(kl(pc,qc)); raw.append(add(z[6],mul(inherited[-1],-1)))
    ck(sum(r)==1)
    erase=add(C,mul(kl(M,N),-1)); outcome=kl((F(1,2),F(1,2)),r)
    ck(C==add(erase,outcome,mul(add(*inherited),F(1,2))))
    sigma=add(mul(add(ns[0][6],ns[1][6]),F(1,2)),mul(C,-1))
    ck(mul(add(*raw),F(1,2))==add(sigma,erase,outcome))
    release=eta-(ns[0][3]+ns[1][3])/2
    nc=len(s[0]).bit_length()-1
    expected=gamma*spec(s[0])[1<<i]**2 if i<nc else F(0)
    ck(release==expected>=0)
    # Exact child allowance conservation: Cchild-Cparent + release/2 + mean(Schild)-Sparent=0.
    Spar=add({2:eta/2},mul(C,-1))
    Sc=add({2:(ns[0][3]+ns[1][3])/4},mul(add(ns[0][6],ns[1][6]),F(-1,2)))
    ck(add(sigma,{2:release/2},Sc,mul(Spar,-1))=={})

domains=[(1,1)] if MODE=='pilot' else [(1,1),(2,1),(1,2)]
for nc,nd in domains:
    for a,g,h in itertools.product(tables(nc),tables(nd),tables(nd)):
        roots+=1; s=(a,g,h)
        for e in (F(0),F(1,32),F(1,16)):
            node(*s,e)
        for i in range(nc+nd): edge(s,i,F(1,16))
guards=[]
for n in range(1,11):
    d=F(1,2**n); q=1-2*d+2*d*d; k=d*d/q; ell=F(15,16)*k+d/16
    odds=ell*(1-k)/(k*(1-ell))
    if n>=6: ck(odds>2)
    if n>=7: ck(d/(16*k)>2)
    guards.append({'n':n,'eta':str(d),'odds_factor':str(odds)})
result={'status':'PASS','mode':MODE,'mux_representations':roots,'unique_cached_states':states,'physical_split_checks':edges,'exact_assertions':checks,'seconds':time.monotonic()-START,'rare_guards':guards,'scope':'finite validation; continuum/all-dimensional argument is in DERIVATION.md; no peer or Lean acceptance implied'}
(ROOT/'out'/f'{MODE}.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rare_guards'}))
