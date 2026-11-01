#!/usr/bin/env python3
"""Finite self-checks for the mass-weighted erasure composition identity.

These tests are diagnostics for the algebraic theorem in REPORT.md.  They do not
prove FEI and do not replace the proof.
"""
from __future__ import annotations
import itertools, json, math, random, hashlib

def inputs(n):
    return list(itertools.product((-1,1), repeat=n))

def walsh(vals):
    n=len(next(iter(vals)))
    z={}
    for mask in range(1<<n):
        s=0.0
        for x,v in vals.items():
            chi=1
            for i in range(n):
                if mask>>i & 1:
                    chi*=x[i]
            s += v*chi
        z[mask]=s/(1<<n)
    return z

def E(a,b):
    s=a+b
    if s==0: return 0.0
    out=0.0
    if a>0: out += a*math.log2(s/a)
    if b>0: out += b*math.log2(s/b)
    return out

def spectral_metrics(vals):
    c=walsh(vals); n=len(next(iter(vals)))
    p={m:v*v for m,v in c.items()}
    B=[]; inf=[]
    for i in range(n):
        bit=1<<i
        B.append(sum(E(p[T],p[T|bit]) for T in range(1<<n) if not (T&bit)))
        inf.append(sum(p[T] for T in range(1<<n) if T&bit))
    I=sum(inf)
    W=sum(c[1<<i]**2 for i in range(n))
    T=sum((c[1<<i]**2)*math.log2(1/(c[1<<i]**2))
          for i in range(n) if c[1<<i])
    return c,p,B,inf,I,W,T

def mean(vals):
    return sum(vals.values())/len(vals)

def compose(G, gs):
    ns=[len(next(iter(g))) for g in gs]
    off=[0]
    for n in ns: off.append(off[-1]+n)
    out={}
    for x in inputs(sum(ns)):
        z=tuple(gs[j][tuple(x[off[j]:off[j+1]])] for j in range(len(gs)))
        out[x]=G[z]
    return out

def biased_outer_q(G,mus):
    m=len(mus); q={}
    for mask in range(1<<m):
        coeff=0.0
        for z in inputs(m):
            pr=1.0; psi=1.0
            for j,mu in enumerate(mus):
                pr *= (1+mu*z[j])/2
                if mask>>j & 1:
                    V=1-mu*mu
                    psi *= (z[j]-mu)/math.sqrt(V)
            coeff += pr*G[z]*psi
        q[mask]=coeff*coeff
    return q

def q_metrics(q,m):
    B=[]; a=[]
    for j in range(m):
        bit=1<<j
        B.append(sum(E(q[C],q[C|bit]) for C in range(1<<m) if not(C&bit)))
        a.append(sum(q[C] for C in range(1<<m) if C&bit))
    return B,a

def R(q,m,j,x):
    bit=1<<j
    return sum(E(q[C],x*q[C|bit]) for C in range(1<<m) if not(C&bit))

def random_bool(n,rng,balanced=False):
    xs=inputs(n)
    if balanced:
        idx=list(range(len(xs))); rng.shuffle(idx); pos=set(idx[:len(xs)//2])
        return {x:(1 if k in pos else -1) for k,x in enumerate(xs)}
    return {x:rng.choice((-1,1)) for x in xs}

def nonconstant(n,rng,balanced=False):
    while True:
        f=random_bool(n,rng,balanced)
        if abs(mean(f))<1:
            return f

def main():
    rng=random.Random(20260921151112)
    max_general=0.0; general_checks=0
    for _ in range(80):
        m=rng.choice((2,3))
        G=random_bool(m,rng,False)
        ns=[rng.choice((1,2)) for _ in range(m)]
        gs=[nonconstant(n,rng,False) for n in ns]
        mus=[mean(g) for g in gs]
        q=biased_outer_q(G,mus); _,alpha=q_metrics(q,m)
        F=compose(G,gs); _,_,BF,_,_,_,_=spectral_metrics(F)
        off=[0]
        for n in ns: off.append(off[-1]+n)
        for j,g in enumerate(gs):
            cg,_,Bg,_,_,_,_=spectral_metrics(g)
            V=1-mus[j]*mus[j]
            for k in range(ns[j]):
                e=cg[1<<k]**2
                rhs=(alpha[j]/V)*(Bg[k]-E(mus[j]**2,e))+R(q,m,j,e/V)
                err=abs(BF[off[j]+k]-rhs)
                max_general=max(max_general,err); general_checks+=1
                assert err < 2e-12, (err,j,k)
    min_scalar=1e100
    for a,b,e in [(0,1,0),(0,1,1),(1,0,.3),(1,1,.5)]:
        lhs=E(a,e*b)
        rhs=e*E(a,b)+(e*b*math.log2(1/e) if e not in (0,1) and b else 0.0)
        min_scalar=min(min_scalar,rhs-lhs)
    for _ in range(20000):
        a=10**rng.uniform(-8,2); b=10**rng.uniform(-8,2); e=rng.random()
        lhs=E(a,e*b)
        rhs=e*E(a,b)+(e*b*math.log2(1/e) if e>0 else 0.0)
        min_scalar=min(min_scalar,rhs-lhs)
        assert rhs+2e-11*max(1,a,b) >= lhs
    max_balanced=0.0; balanced_checks=0; min_global_slack=1e100
    for _ in range(50):
        m=rng.choice((2,3)); n=rng.choice((1,2))
        G=nonconstant(m,rng,True); g=nonconstant(n,rng,True)
        F=compose(G,[g]*m)
        _,_,_,_,IF,WF,TF=spectral_metrics(F)
        _,_,BG,_,IG,WG,TG=spectral_metrics(G)
        _,_,Bg,_,Ig,Wg,Tg=spectral_metrics(g)
        q=biased_outer_q(G,[0.0]*m); Bq,alpha=q_metrics(q,m)
        BF=spectral_metrics(F)[2]
        directB=sum(BF)
        upper=IG*sum(Bg)+sum(Bq)*Wg+IG*Tg
        min_global_slack=min(min_global_slack,upper-directB)
        assert upper+2e-12>=directB
        rerr=abs(WF/IF-(WG/IG)*(Wg/Ig))
        terr=abs(TF/IF-((Wg/Ig)*(TG/IG)+(WG/IG)*(Tg/Ig)))
        max_balanced=max(max_balanced,rerr,terr); balanced_checks+=1
        assert rerr<2e-12 and terr<2e-12
    c0=2/(math.e*math.log(2))
    max_c_ratio=0.0
    for _ in range(20000):
        p=rng.random()
        e=(p*p)*rng.random()
        ratio=(e*math.log2(1/e)/p) if e>0 and p>0 else 0.0
        max_c_ratio=max(max_c_ratio,ratio)
        assert ratio<=c0+1e-12
    result={
        "status":"PASS",
        "scope":"finite diagnostics only; analytic proof is in REPORT.md; not FEI closure",
        "general_unbalanced_composition_local_identity_checks":general_checks,
        "max_abs_general_identity_error":max_general,
        "scalar_concavity_checks":20004,
        "minimum_scalar_inequality_slack":min_scalar,
        "balanced_global_state_checks":balanced_checks,
        "max_abs_r_or_t_recursion_error":max_balanced,
        "minimum_global_upper_bound_slack":min_global_slack,
        "universal_T_over_I_constant_2_over_e_ln2":c0,
        "largest_sampled_pointwise_ratio":max_c_ratio
    }
    print(json.dumps(result,sort_keys=True,indent=2))
if __name__=="__main__":
    main()
