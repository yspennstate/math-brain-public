"""Exact finite verification of affine child releases and adaptive ownership."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, product
from math import comb
import json,sys,time,hashlib
R=Path(__file__).resolve().parents[1]
PILOT='--pilot' in sys.argv
START=time.monotonic(); COUNT=0
def ck(b):
    global COUNT
    COUNT+=1
    assert b,COUNT
    if COUNT%1024==0 and time.monotonic()-START>55: raise RuntimeError('frozen55s cap')
def norm(d): return {p:c for p,c in d.items() if c}
def plus(*ds):
    r={}
    for d in ds:
        for p,c in d.items(): r[p]=r.get(p,F(0))+c
    return norm(r)
def scale(c,d): return norm({p:c*v for p,v in d.items()})
def const(c): return norm({2:F(c)})
def sub(a,b): return plus(a,scale(-1,b))
def factor(x):
    d={}; p=2
    while p*p<=x:
        while x%p==0: d[p]=d.get(p,0)+1; x//=p
        p+=1
    if x>1:d[x]=1
    return d
def entropy(ms,den):
    assert sum(ms)==den
    r=const(den.bit_length()-1)
    for z in ms:
        if z:
            r=plus(r,{p:-F(z*e,den) for p,e in factor(z).items()})
    return r
def ln_series(x):
    z=(x-1)/(x+1); z2=z*z; power=z; a=F(0)
    for j in range(32): a+=2*power/(2*j+1); power*=z2
    return a,a+2*power/(65*(1-z2))
LN2=ln_series(F(2))
@lru_cache(None)
def logprime(p):
    if p==2:return F(1),F(1)
    k=p.bit_length()-1; a,b=ln_series(F(p,1<<k))
    return k+a/LN2[1],k+b/LN2[0]
def interval(d):
    lo=hi=F(0)
    for p,c in d.items():
        a,b=logprime(p)
        if c<0:a,b=b,a
        lo+=c*a;hi+=c*b
    return lo,hi
def nonneg(d): return not d or interval(d)[0]>0
def positive(d): return bool(d) and interval(d)[0]>0
def enc(d):return {str(p):str(c) for p,c in d.items()}
def par(x):return x.bit_count()%2
def span(vs):
    S={0}
    for v in vs:S|={u^v for u in tuple(S)}
    return S
def fwht(f):
    a=list(f);h=1
    while h<len(a):
        for q in range(0,len(a),2*h):
            for j in range(q,q+h):
                u,v=a[j],a[j+h]; a[j],a[j+h]=u+v,u-v
        h*=2
    return tuple(a)
@lru_cache(None)
def bases(n):
    return tuple(vs for vs in permutations(range(1,1<<n),n) if len(span(vs))==1<<n) if n else ((),)
def table(n,t):return tuple(1-2*((t>>x)&1) for x in range(1<<n))
@lru_cache(None)
def stats(f):
    N=len(f);n=N.bit_length()-1;a=fwht(f);den=N*N
    p=tuple(F(sum(a[s]**2 for s in range(N) if (s>>i)&1),den) for i in range(n))
    w=tuple(F(sum(f[x]!=f[x^v] for x in range(N)),N) for v in range(N))
    ck(all(w[v]==F(sum(a[s]**2 for s in range(N) if par(v&s)),den) for v in range(N)))
    ck(sum(p)==sum(w[1<<i] for i in range(n)))
    m=tuple(min(q,1-q) for q in w)
    rows=[];S={0}
    for v in sorted(range(1,N),key=lambda v:(m[v],v)):
        if v not in S:
            rows.append(v);S|={u^v for u in tuple(S)}
    minimum=sum((m[v] for v in rows),F(0))
    # Independent full-basis enumeration, not the greedy exchange algorithm.
    ck(minimum==min(sum((m[v] for v in vs),F(0)) for vs in bases(n)))
    b=sum((w[v]>F(1,2))<<i for i,v in enumerate(rows))
    canonical=[]
    for y in range(N):
        x=0
        for i,v in enumerate(rows):
            if (y>>i)&1:x^=v
        canonical.append(f[x]*(-1 if par(b&y) else 1))
    canonical=tuple(canonical);ca=fwht(canonical)
    ck(sorted(z*z for z in a)==sorted(z*z for z in ca))
    ck(F(sum(s.bit_count()*ca[s]**2 for s in range(N)),den)==minimum)
    return dict(n=n,N=N,a=a,p=p,w=w,m=m,H=entropy([z*z for z in a],den),I=sum(p),amin=minimum,canonical=canonical)
def child(f,A,u):
    n=len(f).bit_length()-1;B=[i for i in range(n) if i not in A];g=[]
    for y in range(1<<len(B)):
        x=sum(((u>>j)&1)<<i for j,i in enumerate(A))
        x+=sum(((y>>j)&1)<<i for j,i in enumerate(B))
        g.append(f[x])
    return tuple(g)
def block(f,A):
    s=stats(f);a=len(A);cs=[stats(child(f,A,u)) for u in range(1<<a)]
    avh=plus(*(scale(F(1,1<<a),c['H']) for c in cs))
    avi=sum((c['I'] for c in cs),F(0))/(1<<a)
    avm=sum((c['amin'] for c in cs),F(0))/(1<<a)
    ia=sum(s['p'][i] for i in A);rho=avi-avm
    ck(avi+ia==s['I']);ck(rho>=0)
    masses={};mask=sum(1<<i for i in A)
    for t,z in enumerate(s['a']):masses[t&~mask]=masses.get(t&~mask,0)+z*z
    margH=entropy(list(masses.values()),s['N']**2)
    L=sub(s['H'],avh);B=sub(s['H'],margH);J=sub(L,B)
    ck(nonneg(J))
    return dict(A=A,children=cs,avh=avh,avi=avi,avm=avm,IA=ia,rho=rho,L=L,B=B,J=J)

roots=[table(n,t) for n in range(3 if PILOT else 4) for t in range(1<<(1<<n))]
allstats=[stats(f) for f in roots]
blocks_count=0;directional=0;minimal_count=0;critical_count=0
maxima={}
for K in [1,2,3,4]:
    for n in range(3 if PILOT else 4):
        ds=[sub(s['H'],const(K*s['I'])) for s in allstats if s['n']==n]
        best=ds[0]
        for d in ds[1:]:
            if positive(sub(d,best)):best=d
        maxima[K,n]=best

for f,s in zip(roots,allstats):
    n=s['n'];minimal=s['I']==s['amin'];minimal_count+=minimal
    bs=[]
    for mask in range(1,1<<n):
        A=tuple(i for i in range(n) if (mask>>i)&1);z=block(f,A);bs.append(z);blocks_count+=1
        for K in [1,2,3,4]:
            D=sub(s['H'],const(K*s['I']))
            star=sub(const(K*z['avm']),z['avh'])
            orig=sub(const(K*z['avi']),z['avh'])
            ck(orig==plus(star,const(K*z['rho'])))
            ck(plus(D,star)==sub(z['L'],const(K*(z['IA']+z['rho']))))
    for i in range(n):
        z=next(q for q in bs if q['A']==(i,))
        coords=[j for j in range(n) if j!=i]
        delta=s['I']-s['amin']
        ck(z['rho']<=sum((min(s['p'][j],s['p'][i]+delta) for j in coords),F(0)))
        for b,c in enumerate(z['children']):
            for v in range(1<<len(coords)):
                lifted=sum(((v>>t)&1)<<j for t,j in enumerate(coords))
                ck(abs(c['w'][v]-s['w'][lifted])<=s['p'][i]);directional+=1
            if minimal:
                ck(c['amin']>=sum((max(F(0),s['p'][j]-s['p'][i]) for j in coords),F(0)))
        if minimal:ck(z['rho']<=sum((min(s['p'][j],s['p'][i]) for j in coords),F(0)))
    for k in range(1,n+1):
        group=[z for z in bs if len(z['A'])==k];M=comb(n,k);t=comb(n-1,k-1)
        T=sub(scale(t,s['H']),plus(*(z['B'] for z in group)))
        Jsum=plus(*(z['J'] for z in group));rhos=sum((z['rho'] for z in group),F(0))
        ck(nonneg(T));ck(not Jsum or interval(Jsum)[1]<=2*t*s['I']/LN2[1])
        for K in [1,2,3,4]:
            D=sub(s['H'],const(K*s['I']))
            stars=[sub(const(K*z['avm']),z['avh']) for z in group]
            ck(plus(T,scale(M-t,D),*stars,const(K*rhos))==Jsum)
            critical=positive(D) and maxima[K,n]==D and all(nonneg(scale(-1,maxima[K,j])) for j in range(n))
            if critical:
                ck(all(nonneg(q) for q in stars))
                lhs=plus(scale(M-t,D),const(K*rhos))
                ck(interval(lhs)[1]<=2*t*s['I']/LN2[1]);critical_count+=1

@lru_cache(None)
def policies(f):
    s=stats(f);n=s['n']
    if n==0:return ((F(0),F(0),{}),)
    ans=[]
    for i in range(n):
        z=block(f,(i,));cs=[q['canonical'] for q in z['children']]
        for a,b in product(policies(cs[0]),policies(cs[1])):
            q=z['IA']+(a[0]+b[0])/2
            r=z['rho']+(a[1]+b[1])/2
            L=plus(z['L'],scale(F(1,2),a[2]),scale(F(1,2),b[2]))
            ck(q+r==s['I']);ck(L==s['H']);ans.append((q,r,L))
    return tuple(ans)
policy_count=0
for f in roots:
    for q,r,L in policies(f):
        ck(q+r==stats(f)['I']);ck(L==stats(f)['H']);policy_count+=1

point=(-1,1,1,1);s=stats(point);z=block(point,(0,))
ck(s['I']==1 and s['amin']==1 and z['rho']==F(1,2) and z['IA']==F(1,2))
ck(z['L']==const(2))
ck(z['L']==const(2*(z['IA']+z['rho'])))
ck(z['L']!=const(2*z['IA'])) # negative arm: physical-only price2 fails.
q,r,L=policies(point)[0]
ck(q+r+z['rho']!=s['I']) # double-booking the old reset violates conservation.
dummy=tuple((-1)**(((x>>1)&1)+((x>>2)&1)) for x in range(8))
s0=stats(dummy);zd=block(dummy,(0,))
ck(s0['p'][0]==0 and zd['rho']==2 and s0['I']!=s0['amin'])
ck(zd['rho']>sum(min(s0['p'][j],s0['p'][0]) for j in [1,2]))

result={'status':'PASS','pilot':PILOT,'assertions':COUNT,'root_tables':len(roots),'physical_blocks':blocks_count,'directional_fiber_checks':directional,'affine_minimal_roots':minimal_count,'critical_block_budget_checks':critical_count,'complete_adaptive_policies':policy_count,'point2':{'I':'1','query_I':'1/2','full_affine_release':'1/2','physical_only_price':'4','reset_price':'2'},'negative_controls':['dummy parity violates release bound without affine-minimality','point2 physical-only rate2 fails','double-booked reset violates energy telescope'],'arithmetic':'integer Walsh, independent physical translations, Fraction, exact prime-log forms and32-term rational atanh tails','runtime_seconds':time.monotonic()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out'/('PILOT.json' if PILOT else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
