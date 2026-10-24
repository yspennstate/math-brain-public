#!/usr/bin/env python3
import math, json, itertools, random

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def entropy(vals):
    N=len(vals); H=0.0
    for z in fwht(vals):
        if z:
            p=(z/N)**2
            H-=p*math.log2(p)
    return H

def inf(vals,k):
    N=len(vals); b=1<<k
    return sum(vals[x]!=vals[x^b] for x in range(N))/N

def derivative_support(f,n,i):
    others=[k for k in range(n) if k!=i]; E=[]
    for z in range(1<<(n-1)):
        x0=x1=0
        for t,k in enumerate(others):
            bit=(z>>t)&1; x0|=bit<<k; x1|=bit<<k
        x1|=1<<i
        E.append(1 if f[x0]!=f[x1] else 0)
    return E,others

def set_inf(E,k):
    N=len(E); b=1<<k
    return sum(E[x]!=E[x^b] for x in range(N))/N

def exact_subcube(E,m):
    pts=[x for x,v in enumerate(E) if v]
    if not pts:return None
    fixed={}
    for k in range(m):
        bits={(x>>k)&1 for x in pts}
        if len(bits)==1:fixed[k]=next(iter(bits))
    if len(pts)!=(1<<(m-len(fixed))):return None
    for x in range(1<<m):
        q=all(((x>>k)&1)==a for k,a in fixed.items())
        if bool(E[x])!=q:return None
    return fixed

def child(f,n,i,b):
    others=[k for k in range(n) if k!=i]; out=[]
    for z in range(1<<(n-1)):
        x=b<<i
        for t,k in enumerate(others):x|=((z>>t)&1)<<k
        out.append(f[x])
    return out

def functions(n):
    N=1<<n
    if n<=3:
        masks=range(1<<(N-1))
    else:
        rng=random.Random(20260921)
        masks=[rng.randrange(1<<(N-1)) for _ in range(1500)]
        masks += [0,(1<<(N-1))-1]
    for mask in masks:
        yield [1]+[1 if ((mask>>(x-1))&1)==0 else -1 for x in range(1,N)]

edge_checks=exact_cases=0; max_ratio=0.0; worst=None
for n in range(1,5):
    for f in functions(n):
        Hf=None
        for i in range(n):
            E,others=derivative_support(f,n,i); j=sum(E)/len(E)
            if not (0<j<=0.5):continue
            for t,k in enumerate(others):
                qk=min(inf(f,k),1-inf(f,k))
                assert qk+1e-12>=set_inf(E,t)/2; edge_checks+=1
            fixed=exact_subcube(E,n-1)
            if fixed is None or len(fixed)==0:continue
            if Hf is None:Hf=entropy(f)
            dH=Hf-(entropy(child(f,n,i,0))+entropy(child(f,n,i,1)))/2
            trans=sum(min(inf(f,others[t]),1-inf(f,others[t])) for t in fixed)
            assert dH<=4*trans+2e-11; exact_cases+=1
            if trans and dH/trans>max_ratio:
                max_ratio=dH/trans; worst=(n,i,j,len(fixed),dH,trans)

def subcubes(m):
    for r in range(1,m+1):
        for F in itertools.combinations(range(m),r):
            for a in range(1<<r):
                Q=[]
                for x in range(1<<m):
                    Q.append(int(all(((x>>k)&1)==((a>>t)&1) for t,k in enumerate(F))))
                yield F,a,Q

geom=post=0
rng=random.Random(918273)
for m in range(1,5):
    N=1<<m
    if m<=3:
        masks=range(1,1<<N)
    else:
        masks=[rng.randrange(1,1<<N) for _ in range(1200)]
    cubes=list(subcubes(m))
    for mask in masks:
        E=[(mask>>x)&1 for x in range(N)]
        for F,a,Q in cubes:
            q=sum(Q)/N; eps=sum(e!=z for e,z in zip(E,Q))/N
            for k in F:
                assert set_inf(E,k)/2+1e-12>=q-eps; geom+=1
            dens=[]
            for c in range(1<<len(F)):
                pts=[x for x in range(N) if all(((x>>k)&1)==((c>>t)&1) for t,k in enumerate(F))]
                dens.append(sum(E[x] for x in pts)/len(pts))
            avg=sum(min(p,1-p) for p in dens)/(1<<len(F))
            assert avg<=eps+1e-12; post+=1

def bent(m):
    return [-1 if sum(((x>>k)&1)&((x>>(k+1))&1) for k in range(0,m,2))%2 else 1 for x in range(1<<m)]
brows=[]
for m in range(2,13,2):
    h=bent(m); hp=h[:]; hp[0]*=-1; f=h+hp; j=2**(-m)
    dH=entropy(f)-(entropy(h)+entropy(hp))/2
    tq=sum(min(inf(f,k),1-inf(f,k)) for k in range(m))
    brows.append({"m":m,"j":j,"dH_over_j":dH/j,"sum_transverse_q":tq,"dH_over_transverse":dH/tq})

print(json.dumps({
 "edge_parity_folded_influence_checks":edge_checks,
 "exact_subcube_payment_cases":exact_cases,
 "max_exact_dH_over_transverse_q":max_ratio,
 "worst_exact_case":worst,
 "near_subcube_boundary_checks":geom,
 "postF_residual_checks":post,
 "bent_flip_family":brows,
 "all_checks_pass":True},sort_keys=True,indent=2))
