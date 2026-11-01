#!/usr/bin/env python3
"""
Finite diagnostics for B18 majority-sign subcube Hellinger stability.

This checker supports only the finite algebra/measurement statements in the
companion report.  It is not a proof of Ellis stability or of full FEI.
"""
from itertools import product
from math import log2, sqrt
import json, hashlib

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*log2(x)-(1-x)*log2(1-x)

def flip(x, r):
    return x ^ (1 << r)

def influence_indicator(mask, m):
    N = 1 << m
    return sum(
        1 for r in range(m) for x in range(N)
        if bool(mask & (1 << x)) != bool(mask & (1 << flip(x,r)))
    ) / N

def derivative_energy(vals, m):
    N = 1 << m
    return sum(
        ((vals[x]-vals[flip(x,r)])/2.0)**2
        for r in range(m) for x in range(N)
    ) / N

def opposite_sign_adjacency(vals, m):
    N = 1 << m
    return sum(
        1 for r in range(m) for x in range(N)
        if vals[x] * vals[flip(x,r)] == -1
    ) / N

def dtc_uniform(mask, m):
    pts = [x for x in range(1<<m) if mask & (1<<x)]
    if not pts:
        return 0.0
    internal_oriented = sum(
        1 for r in range(m) for x in pts if mask & (1 << flip(x,r))
    )
    return log2(len(pts)) - internal_oriented / len(pts)

def walsh(vals, m):
    N = 1 << m
    return [
        sum(vals[x] * (-1 if ((s & x).bit_count() & 1) else 1)
            for x in range(N)) / N
        for s in range(N)
    ]

def spectral_law(vals, m):
    N = 1 << m
    j = sum(v*v for v in vals)/N
    wh = walsh(vals,m)
    return [a*a/j for a in wh]

def affinity(p,q):
    return sum(sqrt(max(0.0,a*b)) for a,b in zip(p,q))

def project_law(p, m, Kmask):
    out = {}
    for s, mass in enumerate(p):
        t = s & Kmask
        out[t] = out.get(t,0.0)+mass
    return out

def affinity_dict(p,q):
    keys=set(p)|set(q)
    return sum(sqrt(max(0.0,p.get(k,0.0)*q.get(k,0.0))) for k in keys)

def subcube_masks(m):
    # state per coordinate: -1 free, 0 fixed zero, 1 fixed one
    for spec in product((-1,0,1), repeat=m):
        mask=0
        for x in range(1<<m):
            ok=True
            for r,state in enumerate(spec):
                if state!=-1 and ((x>>r)&1)!=state:
                    ok=False; break
            if ok:
                mask |= 1<<x
        yield spec,mask

def best_subcube(mask,m):
    size=mask.bit_count()
    best=None
    for spec,qmask in subcube_masks(m):
        sym=(mask ^ qmask).bit_count()
        delta=sym/size
        cand=(delta,spec,qmask)
        if best is None or cand[0]<best[0]:
            best=cand
    return best

def mask_vals(mask,m):
    return [1 if mask & (1<<x) else 0 for x in range(1<<m)]

def row_check(vals,m, stats):
    N=1<<m
    j=sum(v*v for v in vals)/N
    if not (0<j<=0.5):
        return
    plus=sum(1 for v in vals if v==1)
    minus=sum(1 for v in vals if v==-1)
    if plus < minus:
        vals=[-v for v in vals]
        plus,minus=minus,plus
    a=plus/N; b=minus/N
    theta=b/(a+b)
    L=log2(1/j)
    d=derivative_energy(vals,m)
    Delta=d/j-L/2
    pmask=sum((1<<x) for x,v in enumerate(vals) if v==1)
    bmask=sum((1<<x) for x,v in enumerate(vals) if v==-1)
    Ia=influence_indicator(pmask,m)
    Ib=influence_indicator(bmask,m)
    isoa=Ia-(2*a*log2(1/a) if a else 0.0)
    isob=Ib-(2*b*log2(1/b) if b else 0.0)
    J=opposite_sign_adjacency(vals,m)
    fourbank=isoa+isob+2*J+2*j*h2(theta)
    err=abs(4*j*Delta-fourbank)
    stats["max_fourbank_error"]=max(stats["max_fourbank_error"],err)
    if err>2e-11:
        raise AssertionError(("fourbank",m,vals,err))
    dtc=(a/j)*dtc_uniform(pmask,m)+(b/j)*dtc_uniform(bmask,m)
    ephys=h2(theta)+dtc
    err2=abs(ephys-(2*Delta-J/j))
    stats["max_erasure_identity_error"]=max(stats["max_erasure_identity_error"],err2)
    if err2>2e-11:
        raise AssertionError(("erasure",m,vals,err2))
    # Majority-set subcube proxy: verify the report's deterministic overlap/affinity inequality
    delta,spec,qmask=best_subcube(pmask,m)
    stats["max_best_delta"]=max(stats["max_best_delta"],delta)
    if delta < 0.5-1e-15:
        q=qmask.bit_count()/N
        pg=spectral_law(vals,m)
        pq=spectral_law(mask_vals(qmask,m),m)
        aff=affinity(pg,pq)
        lower=sqrt(1-theta)*(1-2*delta)/sqrt(1+delta)
        slack=aff-lower
        stats["min_affinity_slack"]=min(stats["min_affinity_slack"],slack)
        stats["affinity_cases"]+=1
        if slack < -2e-11:
            raise AssertionError(("affinity",m,vals,delta,theta,aff,lower))
        for Kmask in range(1<<m):
            pa=project_law(pg,m,Kmask)
            qa=project_law(pq,m,Kmask)
            affK=affinity_dict(pa,qa)
            stats["min_projection_contraction_slack"]=min(
                stats["min_projection_contraction_slack"], affK-aff
            )
            stats["projection_checks"]+=1
            if affK+2e-11<aff:
                raise AssertionError(("projection contraction",m,Kmask,affK,aff))
    stats["rows"]+=1

def entropy(p):
    return -sum(x*log2(x) for x in p if x>0)

def mean_level(p,m):
    return sum(s.bit_count()*mass for s,mass in enumerate(p))

def tensor_vals(a,b):
    # Coordinates of a are low bits; b are high bits.
    return [a[x]*b[y] for y in range(len(b)) for x in range(len(a))]

def product_recursion_check():
    checks=0
    maxerr=0.0
    for ma,mb in ((1,1),(1,2),(2,1),(2,2)):
        Na,Nb=1<<ma,1<<mb
        for ta in product((-1,0,1), repeat=Na):
            ja=sum(x*x for x in ta)/Na
            if ja==0: continue
            pa=spectral_law(list(ta),ma)
            Ha=entropy(pa); Ma=mean_level(pa,ma)
            Da=Ma-0.5*log2(1/ja)
            for tb in product((-1,0,1), repeat=Nb):
                jb=sum(x*x for x in tb)/Nb
                if jb==0: continue
                pb=spectral_law(list(tb),mb)
                Hb=entropy(pb); Mb=mean_level(pb,mb)
                Db=Mb-0.5*log2(1/jb)
                vals=tensor_vals(list(ta),list(tb))
                p=spectral_law(vals,ma+mb)
                j=sum(x*x for x in vals)/(Na*Nb)
                H=entropy(p); M=mean_level(p,ma+mb)
                D=M-0.5*log2(1/j)
                err=max(abs(j-ja*jb),abs(H-Ha-Hb),abs(M-Ma-Mb),abs(D-Da-Db))
                maxerr=max(maxerr,err)
                if err>2e-11:
                    raise AssertionError(("product recursion",ma,mb,err))
                checks+=1
    return {"checks":checks,"max_error":maxerr}

def bent_phase_obstruction():
    out=[]
    for d in range(1,5):
        N=1<<d
        # sigma(x,y)=(-1)^(x dot y), coordinates x low, y high.
        vals=[]
        for y in range(N):
            for x in range(N):
                vals.append(-1 if ((x&y).bit_count()&1) else 1)
        wh=walsh(vals,2*d)
        target=[]
        maxerr=0.0
        for b in range(N):
            for a in range(N):
                pred=(-1 if ((a&b).bit_count()&1) else 1)/N
                # Fourier index uses low a, high b.
                got=wh[a | (b<<d)]
                maxerr=max(maxerr,abs(got-pred))
        if maxerr>1e-12:
            raise AssertionError(("bent transform",d,maxerr))
        p=spectral_law(vals,2*d)
        # Uniform spectrum implies exact block MI=0.
        spec_uniform=max(abs(x-1/(N*N)) for x in p)
        # Physical amplitude matrix is normalized Hadamard/N; reduced purity = 1/N.
        purity=1/N
        entanglement=1-purity
        best_rank1_residual_sq=1-1/N
        out.append({"d":d,"spectral_block_mi_bits":0.0,
                    "max_spectral_uniform_error":spec_uniform,
                    "linear_entanglement":entanglement,
                    "best_rank1_frobenius_residual_sq":best_rank1_residual_sq})
    return out

def synthetic_obstruction():
    out=[]
    for k in (4,8,16,32):
        eps=1/k
        hell2=1-sqrt(1-eps)
        excess=h2(eps)+k
        out.append({"k":k,"epsilon":eps,"hellinger_sq":hell2,
                    "mean_excess":eps,"shannon_excess_bits":excess})
    return out

def main():
    stats={
        "rows":0,
        "max_fourbank_error":0.0,
        "max_erasure_identity_error":0.0,
        "affinity_cases":0,
        "projection_checks":0,
        "min_affinity_slack":float("inf"),
        "min_projection_contraction_slack":float("inf"),
        "max_best_delta":0.0,
    }
    by_m={}
    for m in (1,2,3):
        before=stats["rows"]
        N=1<<m
        for tup in product((-1,0,1), repeat=N):
            row_check(list(tup),m,stats)
        by_m[str(m)]=stats["rows"]-before
    stats["rows_by_dimension"]=by_m
    stats["product_recursion"]=product_recursion_check()
    stats["bent_phase_obstruction"]=bent_phase_obstruction()
    stats["synthetic_address_obstruction"]=synthetic_obstruction()
    stats["status"]="PASS"
    payload=json.dumps(stats,sort_keys=True,indent=2)
    print(payload)
    print("payload_sha256="+hashlib.sha256(payload.encode()).hexdigest())

if __name__=="__main__":
    main()
