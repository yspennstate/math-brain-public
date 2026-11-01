"""Frozen finite domain in ../out/SPEC.json; no external writes or imports."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(v):
    global checks
    checks+=1
    assert v, checks

def walsh(f):
    a=list(f); d=1
    while d<len(a):
        for j in range(0,len(a),2*d):
            for k in range(j,j+d):
                u,v=a[k],a[k+d]; a[k],a[k+d]=u+v,u-v
        d*=2
    return a

@lru_cache(None)
def log2_bounds(z):
    z=Q(z); k=0
    while z>=2: z/=2; k+=1
    while z<1: z*=2; k-=1
    def ln_bounds(a):
        t=(a-1)/(a+1); s=Q(0)
        for j in range(28): s+=2*t**(2*j+1)/(2*j+1)
        return s,s+2*t**57/(57*(1-t*t))
    lo,hi=ln_bounds(z); ll,lh=ln_bounds(Q(2))
    return Q(k)+lo/lh,Q(k)+hi/ll

def entropy(f):
    N=len(f); lo=hi=Q(0)
    for w in walsh(f):
        if w:
            p=Q(w*w,N*N); a,b=log2_bounds(1/p)
            lo+=p*a; hi+=p*b
    return lo,hi

def influences(f):
    n=(len(f)-1).bit_length()
    return [Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(n)]

def direct_walsh(f):
    return [sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(f)) for s in range(len(f))]

def certificate_fei2(f):
    # Exact integer-product comparison: N^2(H-2I)<=0.
    N=len(f); n=(N-1).bit_length(); w=walsh(f)
    exponent=int(N*N*(2*n-2*sum(influences(f))))
    product=1
    for a in w:
        if a: product*=pow(a*a,a*a)
    return pow(2,exponent)<=product if exponent>=0 else True

def txt(q): return str(q)

start=time.perf_counter()
h=[-1]+[1]*7
hl,hu=entropy(h); I=sum(influences(h)); gaplo=hl-2*I; gaphi=hu-2*I
ck(gaplo>0); ck(I==Q(3,4)); ck(not certificate_fei2(h))
all3=[]; certified=[]
for mask in range(256):
    f=[-1 if mask>>x&1 else 1 for x in range(8)]
    ck(walsh(f)==direct_walsh(f))
    ck(sum(w*w for w in walsh(f))==64)
    good=certificate_fei2(f)
    if good: certified.append(f)
    all3.append((f,good))
r=min(sum(a!=b for a,b in zip(h,f)) for f in certified)
ck(r==1)
repair_points=[]
for x in range(8):
    f=h.copy(); f[x]*=-1
    ck(certificate_fei2(f)); repair_points.append(x)

# Exhaustive original-core repair and full signed-bank bound, on all 256 tables.
# q=8, rho=1/8, mu=D(h), M=K*m=6.
for f,good in all3:
    e=sum(a!=b for a,b in zip(h,f)); lo,hi=entropy(f)
    Dlo,Dhi=lo-2*sum(influences(f)),hi-2*sum(influences(f))
    ck(not good or e>=r)
    # e=0 uses equality; e>=1 uses universal D>=-6.
    if e==0: ck(Dlo==gaplo and Dhi==gaphi)
    else: ck(Dlo>=-6)

families=[]
for t in (1,2,3):
    n=3*t; N=1<<n; f=[]; g=[]; edits=[]
    for x in range(N):
        v=1; parity=0
        for j in range(t):
            a=(x>>(3*j))&7; parity^=a; v*=h[a]
        f.append(v); g.append(-v if parity==0 else v)
        if parity==0: edits.append(x)
    ck(len(edits)==8**(t-1))
    ck(sum(w*w for w in walsh(g))==N*N)
    ck(walsh(g)==direct_walsh(g))
    fibres=0
    if t>=2:
        for j in range(t):
            others=[k for k in range(t) if k!=j]
            for y in range(8**(t-1)):
                base=sum(((y>>(3*k))&7)<<(3*b) for k,b in enumerate(others))
                child=[g[base|(a<<(3*j))] for a in range(8)]
                seed=[f[base|(a<<(3*j))] for a in range(8)]
                ck(sum(a!=b for a,b in zip(child,seed))==1)
                ck(certificate_fei2(child)); fibres+=1
    lo,hi=entropy(g); infl=influences(g)
    families.append(dict(t=t,n=n,edits=len(edits),density="1/8",certified_core_fibres=fibres,
                         H_lower=txt(lo),H_upper=txt(hi),I=txt(sum(infl)),
                         D2_lower=txt(lo-2*sum(infl)),D2_upper=txt(hi-2*sum(infl))))
    if t==2:
        g2=g; ck(lo>2*sum(infl))
    if t==3:
        child=g[:64]
        ck(child==[-v for v in g2])
        ck(entropy(child)[0]>2*sum(influences(child)))

# Independent reconstruction of A054's exact bank, actual critical three-bit guard.
f=h; F=[-1 if x in (0,5) else 1 for x in range(8)]
ck(sum(influences(F))==Q(3,2)); ck(entropy(F)==(Q(2),Q(2)))
cost=lambda v: Q(sum(F[x]!=F[x^v] for x in range(8)),8)
W=[0,4]; mW=cost(4)
b=[min(cost(q^v) for v in W) for q in (1,2,3)]
J=mW+sum(sorted(b)[:2]); R=sum(influences(F))-J
ck(J==1); ck(R==Q(1,2))
Omega_lo=hl-2+2*(Q(3,2)-I); Omega_hi=hu-2+2*(Q(3,2)-I)
ck(Omega_lo-2*R==gaplo); ck(Omega_hi-2*R==gaphi)
# Both u=0 and fully booked u=R retain Pi_u and the same positive deficit.
for u in (Q(0),Q(1,4),R):
    ck(Q(2)-2*(J+u)+(Omega_lo-2*(R-u))==gaplo)

result=dict(status="PASS",checks=checks,seconds=time.perf_counter()-start,
            core_repair_radius_vertices=r,all_single_vertex_repairs=repair_points,
            exhaustive_core_tables=256,core_gap_lower=txt(gaplo),core_gap_upper=txt(gaphi),
            families=families,review_A054="scoped analytic bank and n3 fixture reconstructed; no source census adopted")
(ROOT/'out'/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('families','core_gap_lower','core_gap_upper')},indent=2))
