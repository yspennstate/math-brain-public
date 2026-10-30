#!/usr/bin/env python3
import math, json

def E(a,b):
    if a <= 0.0 or b <= 0.0:
        return 0.0
    s=a+b
    return a*math.log2(s/a)+b*math.log2(s/b)

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

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

def Gamma(t):
    return E((1-t)/t,1-t)

tol=5e-10
counts={"nonconstant":0,"positive_r":0,"zero_r":0,"relevant_coordinates":0}
mx={
 "grouped_refund":0.0,
 "purity":0.0,
 "autocorrelation":0.0,
 "coord_residual":0.0,
 "coord_raw_refunded":0.0,
 "coord_raw_entropy":0.0,
 "exist_residual":0.0,
 "exist_raw":0.0,
}
for n in range(1,5):
    N=1<<n
    for mask in range(1<<N):
        vals=[1 if (mask>>x)&1 else -1 for x in range(N)]
        hats=fwht(vals)
        mu=[x*x for x in hats]
        c=mu[0]
        ps=[]; es=[]; Bs=[]
        for i in range(n):
            bit=1<<i
            p=sum(mu[s] for s in range(N) if s&bit)
            e=mu[bit]
            B=sum(E(mu[t],mu[t|bit]) for t in range(N) if not(t&bit))
            ps.append(p); es.append(e); Bs.append(B)
        I=sum(ps)
        if I <= tol:
            continue
        counts["nonconstant"] += 1
        W1=sum(es)
        r=W1/I
        relevant=[]
        for i,p in enumerate(ps):
            if p <= tol:
                continue
            counts["relevant_coordinates"] += 1
            e=es[i]; B=Bs[i]
            residual=B-E(c,e)
            grouped=E(max(0.0,1-c-p),max(0.0,p-e))
            mx["grouped_refund"]=max(mx["grouped_refund"],residual-grouped)
            mx["purity"]=max(mx["purity"],e-p*p)
            mx["autocorrelation"]=max(mx["autocorrelation"],c*e-(1-c-p)*(p-e))
            t=e/p
            if t>tol:
                mx["coord_residual"]=max(mx["coord_residual"],residual/p-Gamma(t))
                mx["coord_raw_refunded"]=max(mx["coord_raw_refunded"],B/p-(Gamma(t)+2*(1-t)))
                mx["coord_raw_entropy"]=max(mx["coord_raw_entropy"],B/p-h2(t)/t)
            relevant.append((i,p,t,residual/p,B/p))
        if r>tol:
            counts["positive_r"] += 1
            eligible=[x for x in relevant if x[2]+tol>=r]
            for _,p,t,rr,br in eligible:
                mx["exist_residual"]=max(mx["exist_residual"],rr-Gamma(r))
                mx["exist_raw"]=max(mx["exist_raw"],br-(Gamma(r)+2*(1-r)))
        else:
            counts["zero_r"] += 1

status="PASS" if max(mx.values()) <= tol else "FAIL"
print(json.dumps({"status":status,"tolerance":tol,"counts":counts,"max_positive_violation":mx},
                 indent=2,sort_keys=True))
