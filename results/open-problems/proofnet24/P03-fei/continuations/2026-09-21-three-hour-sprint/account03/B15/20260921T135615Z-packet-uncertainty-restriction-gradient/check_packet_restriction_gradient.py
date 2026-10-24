#!/usr/bin/env python3
"""B15 exact/finite checks for packet-geometry and restriction magnitude-gradient lemmas.

Analytic statements are proved in REPORT.md. This checker provides finite exact
Walsh sanity checks and exploratory logarithmic measurements. Full FEI remains open.
"""
from __future__ import annotations
from fractions import Fraction
import hashlib, json, math

def fwht(a):
    a=list(map(int,a)); h=1; n=len(a)
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def v2(z):
    z=abs(int(z))
    if not z: raise ValueError("v2(0)")
    return (z & -z).bit_length()-1

def truth(mask,n):
    return [1 if (mask>>x)&1 else -1 for x in range(1<<n)]

def packet_geometry(mask,n):
    N=1<<n; W=fwht(truth(mask,n))
    packets={}
    for s,w in enumerate(W):
        if w:
            packets.setdefault(abs(w),[]).append((s,1 if w>0 else -1))
    out=[]
    for mag,items in packets.items():
        eps=[0]*N
        for s,sgn in items: eps[s]=sgn
        V=fwht(eps)
        r=min(v2(x) for x in V if x)
        p=Fraction(len(items)*mag*mag,N*N)
        b=Fraction(mag*(1<<r),N)
        rhs=b*b/Fraction(1<<r,1)
        out.append((p,b,r,rhs))
    return out

def z2log2(z):
    return 0.0 if z==0.0 else z*z*math.log2(z)

def gkernel(t):
    if t<0: t=-t
    return z2log2(t+1.0)+z2log2(abs(t-1.0))-2.0*z2log2(t)

def kernel_metrics_from_walsh(W,n):
    N=1<<n
    kappas=[]; rhos=[]; rows=[]
    for i in range(n):
        bit=1<<i; inf=L=delta=0.0
        for s in range(N):
            if s&bit: continue
            u=abs(W[s]); v=abs(W[s|bit])
            pv=(v/N)**2
            inf += pv
            if v:
                t=u/v
                delta += pv*gkernel(t)
                if u>v:
                    L += pv*math.log2(u/v)
        if inf:
            kappas.append(L/inf); rhos.append(delta/inf)
            rows.append({"i":i,"Inf":inf,"L":L,"kappa":L/inf,"rho":delta/inf})
    return {"min_kappa":min(kappas) if kappas else None,
            "min_rho":min(rhos) if rhos else None,
            "rows":rows}

def exhaustive_small():
    data={}
    for n in range(1,5):
        packet_count=bad=integral=eq=0
        max_k=(-1.0,None); max_rho=(-1.0,None)
        for mask in range(1<<(1<<n)):
            for p,b,r,rhs in packet_geometry(mask,n):
                packet_count+=1
                if p<rhs: bad+=1
                if b==1:
                    integral+=1
                    if p==Fraction(1,1<<r): eq+=1
            km=kernel_metrics_from_walsh(fwht(truth(mask,n)),n)
            if km["min_kappa"] is not None and km["min_kappa"]>max_k[0]:
                max_k=(km["min_kappa"],mask)
            if km["min_rho"] is not None and km["min_rho"]>max_rho[0]:
                max_rho=(km["min_rho"],mask)
        data[str(n)]={"packets":packet_count,"uncertainty_failures":bad,
                      "integral_packets":integral,"integral_equality_packets":eq,
                      "max_min_kappa":max_k[0],"max_min_kappa_mask":hex(max_k[1]) if max_k[1] is not None else None,
                      "max_min_rho":max_rho[0],"max_min_rho_mask":hex(max_rho[1]) if max_rho[1] is not None else None}
    return data

CORE_HEX=("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
          "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000")
HOSTS=[[78,79],[113,121],[228,484],[170,186],[149,151],[338,466],[284,316],[291,295],[393,457]]
EXPECTED="f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"

def external_seed():
    base=int(CORE_HEX,16)
    core=[-1 if (base>>x)&1 else 1 for x in range(512)]
    table=[]
    for aux in range(1<<len(HOSTS)):
        row=core.copy()
        for j,cells in enumerate(HOSTS):
            if aux>>j & 1:
                for c in cells: row[c]=-1
        table.extend(row)
    digest=hashlib.sha256(','.join(map(str,table)).encode()).hexdigest()
    if digest!=EXPECTED: raise AssertionError((digest,EXPECTED))
    W=fwht(table)
    km=kernel_metrics_from_walsh(W,18)
    p=[(w/len(W))**2 for w in W]
    I=sum(s.bit_count()*p[s] for s in range(len(W)))
    H=sum(-x*math.log2(x) for x in p if x)
    core_rows=km["rows"][:9]; aux_rows=km["rows"][9:]
    return {"truth_sha256":digest,"I":I,"H":H,"H_over_I":H/I,
            "min_kappa":km["min_kappa"],"min_rho":km["min_rho"],
            "core_coordinate":{"Inf":core_rows[0]["Inf"],"kappa":core_rows[0]["kappa"],"rho":core_rows[0]["rho"]},
            "aux_coordinate":{"Inf":aux_rows[0]["Inf"],"kappa":aux_rows[0]["kappa"],"rho":aux_rows[0]["rho"]}}

def kernel_envelope_grid():
    c0=3/math.log(2)
    worst=None; arg=None
    for k in range(-2000,2001):
        t=2**(k/200.0)
        slack=c0+2*max(0.0,math.log2(t))-gkernel(t)
        if worst is None or slack<worst:
            worst=slack;arg=t
    return {"c0":c0,"sampled_min_slack":worst,"arg":arg}

if __name__=="__main__":
    result={"small_exhaustive":exhaustive_small(),
            "external_seed":external_seed(),
            "kernel_envelope_grid":kernel_envelope_grid()}
    print(json.dumps(result,indent=2,sort_keys=True))
