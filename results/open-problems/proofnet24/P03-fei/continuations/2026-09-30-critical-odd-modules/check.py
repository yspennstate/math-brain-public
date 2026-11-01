#!/usr/bin/env python3
"""Finite regression checks, not an all-dimensional proof."""
import itertools
import json
import math
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent
LN2 = math.log(2)

def walsh(f):
    a = np.array(f, dtype=np.int64, copy=True)
    N = len(a)
    k = 1
    while k < N:
        for start in range(0, N, 2*k):
            x, y = a[start:start+k].copy(), a[start+k:start+2*k].copy()
            a[start:start+k], a[start+k:start+2*k] = x+y, x-y
        k *= 2
    return a.astype(float)/N

def ent(p):
    p = np.asarray(p)
    p = p[p>0]
    return float(-np.sum(p*np.log2(p)))

def scalarE(a,b):
    if a == 0 or b == 0:
        return 0.0
    return (a*math.log1p(b/a)+b*math.log1p(a/b))/LN2

def quantities(f):
    a=walsh(f); p=a*a
    n=(len(f)-1).bit_length()
    inf=np.array([sum(p[s] for s in range(len(p)) if (s>>i)&1) for i in range(n)])
    return a,p,ent(p),inf

def coordinate(f,i):
    a,p,H,inf=quantities(f)
    masks=[s for s in range(len(f)) if not (s>>i)&1]
    u=a[masks]; v=a[np.array(masks)+(1<<i)]
    B=sum(scalarE(float(x*x),float(y*y)) for x,y in zip(u,v))
    pplus=(u+v)**2; pminus=(u-v)**2
    JS=ent((pplus+pminus)/2)-(ent(pplus)+ent(pminus))/2
    Delta=H-(ent(pplus)+ent(pminus))/2
    return B,JS,Delta,float(inf[i])

def compose(G,gs):
    widths=[(len(g)-1).bit_length() for g in gs]
    n=sum(widths); out=np.empty(1<<n,dtype=np.int64)
    for x in range(1<<n):
        offset=0; y=0
        for j,(g,w) in enumerate(zip(gs,widths)):
            value=g[(x>>offset)&((1<<w)-1)]
            if value==-1: y|=1<<j
            offset+=w
        out[x]=G[y]
    return out

def odd_tables(n):
    N=1<<n
    for bits in itertools.product((-1,1),repeat=N//2):
        f=np.empty(N,dtype=np.int64)
        for x,v in enumerate(bits):
            f[x]=v; f[N-1-x]=-v
        yield f

def balanced_tables(n):
    N=1<<n
    for plus in itertools.combinations(range(N),N//2):
        f=-np.ones(N,dtype=np.int64)
        f[list(plus)]=1
        yield f

def activation(h,g,r):
    nh=(len(h)-1).bit_length(); ng=(len(g)-1).bit_length()
    f=[]
    for x in range(1<<(nh+r*ng)):
        active=all(g[(x>>(nh+j*ng))&((1<<ng)-1)]==1 for j in range(r))
        f.append(h[x&((1<<nh)-1)] if active else 1)
    return np.array(f,dtype=np.int64)

def main():
    result={"scope":"finite numerical regression; analytic proofs are in REPORT.md",
            "odd_module_coordinate_cases":0,"activation_cases":0,"scalar_cases":0,
            "max_identity_error":0.0,"max_inequality_violation":0.0}
    def identity(x,y):
        error=abs(x-y)
        result["max_identity_error"]=max(result["max_identity_error"],error)
        assert error<2e-10,(x,y,error)
    def leq(x,y):
        error=max(0.0,x-y)
        result["max_inequality_violation"]=max(result["max_inequality_violation"],error)
        assert error<2e-10,(x,y,error)
    # Every outer gate of arity 3; every odd three-variable child;
    # other children are balanced dictators on distinct blocks.
    for signs in itertools.product((-1,1),repeat=8):
        G=np.array(signs)
        a,_,_,infl=quantities(G); q=float(infl[0])
        if not q: continue
        T=[s for s in range(8) if not s&1]
        Bouter=sum(scalarE(float(a[s]**2),float(a[s+1]**2)) for s in T)
        for g in odd_tables(3):
            ag,_,_,dg=quantities(g)
            f=compose(G,[g,np.array([1,-1]),np.array([1,-1])])
            for i in range(3):
                d=float(dg[i]); c=float(ag[1<<i])
                if not d: continue
                B,JS,Delta,D=coordinate(f,i)
                direct=sum(scalarE(float(a[s]**2),float(c*c*a[s+1]**2)) for s in T)
                identity(D,q*d); identity(B,direct); identity(Delta,B+JS)
                leq(B,scalarE(1-q,c*c*q))
                leq(JS,2/LN2*c*c*q)
                leq(Delta/D,d*(math.log2(1/(q*d*d))+3/LN2))
                leq(B/D,Bouter/q+.5)
                leq(Delta/D,Bouter/q+.5+2/LN2*d)
                result["odd_module_coordinate_cases"]+=1
    # Exact activation identities for all balanced 1--3 variable h,
    # all balanced 1--2 variable controls, and one or two control blocks.
    for nh in range(1,4):
        for h in balanced_tables(nh):
            _,_,Hh,dh=quantities(h)
            for ng in range(1,3):
                for g in balanced_tables(ng):
                    _,_,Hg,dg=quantities(g)
                    for r in (1,2):
                        p=2.0**(-r); f=activation(h,g,r)
                        af,pf,Hf,df=quantities(f)
                        I=sum(df); expectedH=p*Hh+p*r*Hg+4*p*r-ent([p*p])+ent([(1-p)**2])
                        identity(af[0],1-p)
                        identity(1-af[0]**2,2*p-p*p)
                        identity(Hf,expectedH)
                        identity(I,p*(sum(dh)+r*sum(dg)))
                        identity(max(df),p*max(max(dh),max(dg)))
                        result["activation_cases"]+=1
    for t in np.r_[np.geomspace(1e-9,1,91),np.linspace(.01,1,100)]:
        for x in np.geomspace(1e-15,1e15,301):
            leq(scalarE(x,t*t),t*scalarE(x,1)+t/2)
            result["scalar_cases"]+=1
    # Explicit single-sequence parameters for f=AND_2 (H=2,J=1).
    # F_k uses G_k=Maj_3 times k copies of f, composed k times,
    # and r=k^2 controls which are depth-k recursive majority.
    asymptotic=[]
    for k in (2,4,8,16,32,64):
        a=k+1.5; Hseed=2*k+2; Ih=a**k
        Hh=Hseed*(Ih-1)/(a-1); Ig=1.5**k; Hg=4*(Ig-1)
        r=k*k; denom=Ih+r*Ig
        # Constant-packet correction / p tends to 2/ln2;
        # its exact stable value is retained when representable.
        p=2.0**(-r) if r<1075 else 0.0
        corr=(-(1-p)**2*2*math.log1p(-p)/LN2/p-2*r*p) if p else 2/LN2
        ratio=(Hh+r*Hg+4*r+corr)/denom
        asymptotic.append({"k":k,"H_over_I":ratio,
                          "log2_I":-r+math.log2(denom),
                          "log2_variance":-r+math.log2(2-p),
                          "relative_maxInf":2**(-k)/(2-p),
                          "control_debit_ratio_upper":2**(-k)*(r+2*k+3/LN2)})
    result["asymptotic_parameter_checks"]=asymptotic
    result["status"]="PASS"
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    (ROOT/"verification.json").write_text(text)
    print(text,end="")

if __name__=="__main__": main()
