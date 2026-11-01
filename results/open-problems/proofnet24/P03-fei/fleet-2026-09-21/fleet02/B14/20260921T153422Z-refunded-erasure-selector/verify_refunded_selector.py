#!/usr/bin/env python3
import math, json

def E(a,b):
    if a <= 0.0 or b <= 0.0:
        return 0.0
    s=a+b
    return a*math.log2(s/a)+b*math.log2(s/b)

def fwht(vals):
    a=list(map(float,vals))
    n=len(a); h=1
    while h<n:
        for j in range(0,n,2*h):
            for k in range(j,j+h):
                x=a[k]; y=a[k+h]
                a[k]=x+y; a[k+h]=x-y
        h*=2
    return [x/n for x in a]

def stats(vals,n):
    hats=fwht(vals)
    m=[x*x for x in hats]
    c=m[0]
    ps=[]; es=[]; Bs=[]
    for i in range(n):
        bit=1<<i
        p=sum(m[s] for s in range(1<<n) if s&bit)
        b=sum(E(m[t],m[t|bit]) for t in range(1<<n) if not(t&bit))
        ps.append(p); es.append(m[bit]); Bs.append(b)
    I=sum(ps); W1=sum(es)
    H=sum(-x*math.log2(x) for x in m if x>0)
    return m,c,ps,es,Bs,I,W1,H

def Gamma(r):
    return E((1-r)/r,1-r)

def tensor_spectrum(m,k):
    cur=[1.0]
    for _ in range(k):
        cur=[a*b for a in cur for b in m]
    return cur

tol=2e-11
nonconstant=0
positive_r=0
group_worst=0.0
selector_worst=0.0
raw_selector_worst=0.0
purity_worst=0.0
zero_r_count=0

for n in range(1,5):
    N=1<<n
    for mask in range(1<<N):
        vals=[1 if (mask>>x)&1 else -1 for x in range(N)]
        m,c,ps,es,Bs,I,W1,H=stats(vals,n)
        if I <= tol:
            continue
        nonconstant += 1
        V=1-c
        for i in range(n):
            p=ps[i]
            if p <= tol:
                continue
            residual=Bs[i]-E(c,es[i])
            grouped=E(V-p,p-es[i])
            group_worst=max(group_worst,residual-grouped)
            purity_worst=max(purity_worst,es[i]-p*p)
        r=W1/I
        if r <= tol:
            zero_r_count += 1
            continue
        positive_r += 1
        relevant=[i for i,p in enumerate(ps) if p>tol]
        residual_min=min((Bs[i]-E(c,es[i]))/ps[i] for i in relevant)
        selector_worst=max(selector_worst,residual_min-Gamma(r))
        raw_min=min(Bs[i]/ps[i] for i in relevant)
        raw_selector_worst=max(raw_selector_worst,
            raw_min-(Gamma(r)+2*math.sqrt(1-r)))

pad_worst_H=0.0
pad_worst_I=0.0
pad_worst_W1=0.0
pad_cases=0
for n in range(1,4):
    N=1<<n
    for mask in range(1<<N):
        vals=[1 if (mask>>x)&1 else -1 for x in range(N)]
        m,c,ps,es,Bs,I,W1,H=stats(vals,n)
        if I<=tol: continue
        for k in (1,2,3):
            mk=tensor_spectrum(m,k)
            Hpad=sum(-x*math.log2(x) for x in mk if x>0)
            Ipad=k*I+2
            W1pad=0.0
            pad_worst_H=max(pad_worst_H,abs(Hpad-k*H))
            degdist=[(0,1.0)]
            base=[(s.bit_count(),m[s]) for s in range(len(m))]
            for _ in range(k):
                nd={}
                for da,pa in degdist:
                    for db,pb in base:
                        nd[da+db]=nd.get(da+db,0.0)+pa*pb
                degdist=list(nd.items())
            direct=sum((deg+2)*prob for deg,prob in degdist)
            pad_worst_I=max(pad_worst_I,abs(direct-Ipad))
            pad_worst_W1=max(pad_worst_W1,W1pad)
            pad_cases += 1

out={
    "status":"PASS" if max(group_worst,selector_worst,raw_selector_worst,purity_worst,
                           pad_worst_H,pad_worst_I,pad_worst_W1)<=tol else "FAIL",
    "enumeration_nonconstant_n_le_4":nonconstant,
    "positive_singleton_fraction_cases":positive_r,
    "zero_singleton_fraction_cases":zero_r_count,
    "max_grouped_refund_violation":group_worst,
    "max_residual_selector_violation":selector_worst,
    "max_raw_selector_violation":raw_selector_worst,
    "max_boolean_purity_violation":purity_worst,
    "parity_padding_cases":pad_cases,
    "max_padding_entropy_identity_error":pad_worst_H,
    "max_padding_influence_identity_error":pad_worst_I,
    "max_padding_level1_mass":pad_worst_W1
}
print(json.dumps(out,indent=2,sort_keys=True))
