#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
from collections import defaultdict
from math import comb, log2, factorial
import json, math

def fwht(a):
    a=list(map(int,a)); n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def entropy_probs(probs):
    s=0.0
    for p in probs:
        if p:
            x=float(p)
            s -= x*log2(x)
    return s

def h2(x):
    if x<=0 or x>=1:
        return 0.0
    return -x*log2(x)-(1-x)*log2(1-x)

def spectral(vals):
    N=len(vals); W=fwht(vals); den=N*N
    return {i:Fraction(w*w,den) for i,w in enumerate(W) if w}

def influence_phys(vals, i):
    N=len(vals)
    return Fraction(sum(1 for x in range(N) if vals[x]!=vals[x^(1<<i)]),N)

def plaquette(vals,i,j):
    N=len(vals)
    bad=0
    for x in range(N):
        q=vals[x]*vals[x^(1<<i)]*vals[x^(1<<j)]*vals[x^(1<<i)^(1<<j)]
        bad += (q==-1)
    return Fraction(bad,N)

def tensor_addr(m, connector=False):
    n=3*m; N=1<<n; vals=[]
    for x in range(N):
        out=1
        all_zero=True
        for b in range(m):
            a=(x>>(3*b))&1
            u0=(x>>(3*b+1))&1
            u1=(x>>(3*b+2))&1
            if a: all_zero=False
            u=u1 if a else u0
            out *= -1 if u else 1
        if connector and all_zero:
            out *= -1
        vals.append(out)
    return vals

def prefix_law_from_spectrum(p):
    I=sum(Fraction(mask.bit_count())*w for mask,w in p.items())
    law=defaultdict(Fraction)
    for S,w in p.items():
        K=S.bit_count()
        if K==0: continue
        sub=S
        while True:
            if sub != S:
                t=sub.bit_count()
                law[sub] += w / I / comb(K,t)
            if sub==0: break
            sub=(sub-1)&S
    assert sum(law.values(),Fraction(0))==1
    return law,I

def tc_prefix(law,n):
    by_t=defaultdict(dict)
    pt=defaultdict(Fraction)
    for A,w in law.items():
        t=A.bit_count()
        by_t[t][A]=w
        pt[t]+=w
    total=0.0
    for t,dist in by_t.items():
        z=pt[t]
        cond={A:w/z for A,w in dist.items()}
        H=entropy_probs(cond.values())
        sh=0.0
        for i in range(n):
            qi=sum(w for A,w in cond.items() if (A>>i)&1)
            sh += h2(float(qi))
        total += float(z)*(sh-H)
    return total, {t:float(v) for t,v in pt.items()}

def spectral_tv(p,q):
    keys=set(p)|set(q)
    return Fraction(1,2)*sum(abs(p.get(k,0)-q.get(k,0)) for k in keys)

def rectangle_rho(vals,n,A_mask):
    B_mask=((1<<n)-1)^A_mask
    Avec=[u for u in range(1<<n) if u & ~A_mask ==0]
    Bvec=[v for v in range(1<<n) if v & ~B_mask ==0]
    bad=0; tot=0
    for x in range(1<<n):
        for u in Avec:
            for v in Bvec:
                q=vals[x]*vals[x^u]*vals[x^v]*vals[x^u^v]
                bad += (q==-1); tot+=1
    return Fraction(bad,tot)

def cut_Q(vals,n,A_mask):
    B_mask=((1<<n)-1)^A_mask
    return sum((plaquette(vals,i,j)
                for i in range(n) if (A_mask>>i)&1
                for j in range(n) if (B_mask>>j)&1), Fraction(0))

def best_anchor_product_error(vals,n,A_mask):
    B_mask=((1<<n)-1)^A_mask
    N=1<<n
    best=Fraction(1)
    for anchor in range(N):
        a0=anchor&A_mask; b0=anchor&B_mask
        bad=0
        for x in range(N):
            a=x&A_mask; b=x&B_mask
            q=vals[a|b0]*vals[a0|b]*vals[a0|b0]
            bad += (q!=vals[x])
        best=min(best,Fraction(bad,N))
    return best

def connected_from_p(vals,n):
    adj=[set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if plaquette(vals,i,j)>0:
                adj[i].add(j); adj[j].add(i)
    seen={0}; stack=[0]
    while stack:
        i=stack.pop()
        for j in adj[i]:
            if j not in seen:
                seen.add(j); stack.append(j)
    return len(seen)==n

family=[]
for m in range(1,5):
    F=tensor_addr(m,False); G=tensor_addr(m,True); n=3*m
    assert sum(F)==0 and sum(G)==0
    for i in range(n):
        assert influence_phys(F,i)==Fraction(1,2)
        assert influence_phys(G,i)==Fraction(1,2)
    assert connected_from_p(G,n)
    if m>=2:
        for i in range(m):
            for j in range(i+1,m):
                assert plaquette(G,3*i,3*j)==Fraction(1,2**(m-2))
    pF=spectral(F); pG=spectral(G)
    tv=spectral_tv(pF,pG)
    assert pF==pG
    row={"m":m,"n":n,"spectral_tv":float(tv),"spectra_exactly_equal":True,"connected":True}
    if m<=3:
        lawF,IF=prefix_law_from_spectrum(pF)
        lawG,IG=prefix_law_from_spectrum(pG)
        assert IF==Fraction(3*m,2) and IG==Fraction(3*m,2)
        tcF,ptF=tc_prefix(lawF,n)
        tcG,ptG=tc_prefix(lawG,n)
        efactF=sum(w*log2(factorial(S.bit_count())) for S,w in pF.items() if S)
        efactG=sum(w*log2(factorial(S.bit_count())) for S,w in pG.items() if S)
        row.update({
            "TC_prefix_F":tcF,"TC_prefix_G":tcG,
            "R_T_over_I_F":tcF-float(efactF/IF),
            "R_T_over_I_G":tcG-float(efactG/IG),
        })
        for t in range(m):
            assert abs(ptF[t]-2/(3*m))<1e-12
    family.append(row)

cut_checks=0
for mask_truth in range(1<<(1<<3)):
    vals=[-1 if (mask_truth>>x)&1 else 1 for x in range(1<<3)]
    for A_mask in [1,2,4]:
        rho=rectangle_rho(vals,3,A_mask)
        Q=cut_Q(vals,3,A_mask)
        best=best_anchor_product_error(vals,3,A_mask)
        assert best <= rho
        assert rho <= Q/Fraction(4)
        cut_checks += 1

c0=2*h2(1/8)-h2(1/4)-1/4
assert c0>0
def f_lower(m):
    return c0*(m-1)/6 - (4/3)*log2(2*m)
def g_lower(m):
    return f_lower(m)

asym=[{"m":m,"F_lower_R_over_I":f_lower(m),"G_lower_R_over_I":g_lower(m)}
      for m in [100,1000,5000,10000,20000]]
assert asym[-1]["F_lower_R_over_I"]>0
assert asym[-1]["G_lower_R_over_I"]>0

cuts=[]
for m in [4,8,12,20]:
    k=m//2
    Q=Fraction(k*(m-k),2**(m-2))
    cuts.append({
        "m":m,"k":k,
        "Q_cross":float(Q),
        "theorem_product_error_upper_Q_over_4":float(Q/4),
        "actual_known_product_error_to_F":2**(-m),
        "n_sqrt_Q":3*m*math.sqrt(float(Q)),
    })

out={
    "status":"PASS",
    "scope":{
        "exact_mux_connector_truth_table_m":"1..4",
        "exact_prefix_law_m":"1..3",
        "approx_factorization_exhaustive":"all 256 Boolean functions on n=3 and 3 unordered nontrivial cuts",
        "cut_checks":cut_checks,
        "large_m_bounds":"analytic-formula diagnostics only"
    },
    "c0_bits":c0,
    "family":family,
    "asymptotic_lower_bounds":asym,
    "connected_cut_diagnostics":cuts,
    "full_FEI_status":"OPEN_NOT_PROVED"
}
print(json.dumps(out,indent=2,sort_keys=True))
