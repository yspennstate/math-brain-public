#!/usr/bin/env python3
"""Finite falsification checks for B16 two-cell phase-switch Mobius/RKHS identities.
This is not a proof of unrestricted FEI.
"""
from __future__ import annotations
import itertools, math, random, json


def rm1_code(n: int):
    N=1<<n
    out=[]
    for a in range(1<<n):
        for b in (0,1):
            row=[]
            for x in range(N):
                bit=b ^ ((a & x).bit_count() & 1)
                row.append(-1 if bit else 1)
            out.append(row)
    return out


def dual_relations(code):
    N=len(code[0]); out=[]
    for mask in range(1<<N):
        good=True
        for row in code:
            p=1
            for x in range(N):
                if (mask>>x)&1: p*=row[x]
            if p!=1:
                good=False; break
        if good: out.append(mask)
    return out


def prod_mask(f, mask):
    p=1
    for x,z in enumerate(f):
        if (mask>>x)&1: p*=z
    return p


def direct_components(n,f,Q,theta):
    code=rm1_code(n); N=1<<n
    U=[x for x in range(N) if x not in Q]
    V=list(Q)
    G=LU=LV=OV=0.0
    sarg=N*theta
    for eps in code:
        uf=sum(f[x]*eps[x] for x in U)/N
        u0=sum(eps[x] for x in U)/N
        vf=sum(f[x]*eps[x] for x in V)/N
        v0=sum(eps[x] for x in V)/N
        a=math.sin(sarg*uf); a0=math.sin(sarg*u0)
        b=math.sin(sarg*vf); b0=math.sin(sarg*v0)
        G += a*b-a0*b0
        LU += (a-a0)*b0
        LV += a0*(b-b0)
        OV += (a-a0)*(b-b0)
    L=len(code)
    return tuple(z/L for z in (G,LU,LV,OV))


def relation_components(n,f,Q,theta):
    code=rm1_code(n); D=dual_relations(code); N=1<<n
    Qmask=sum(1<<x for x in Q); allmask=(1<<N)-1; Umask=allmask^Qmask
    s=math.sin(theta); c=math.cos(theta)
    G=LU=LV=OV=0.0
    coefficient_cases=0; overlap_cases=0; source_cases=0
    for A in D:
        AU=A&Umask; AV=A&Qmask
        a=AU.bit_count(); b=AV.bit_count(); q=a+b
        if a%2!=1 or b%2!=1: continue
        rU=(1-prod_mask(f,AU))//2
        rV=(1-prod_mask(f,AV))//2
        rF=(1-prod_mask(f,A))//2
        assert rF == rU+rV-2*rU*rV
        sign=(-1)**(q//2); amp=(s**q)*(c**(N-q))
        g=2*sign*rF*amp
        lu=2*sign*rU*amp
        lv=2*sign*rV*amp
        ov=-4*sign*rU*rV*amp
        assert abs(g-(lu+lv+ov)) < 1e-30
        if rU*rV:
            overlap_cases += 1
            assert rF==0
        if rF:
            source_cases += 1
            assert rU*rV==0
        coefficient_cases += 1
        G+=g; LU+=lu; LV+=lv; OV+=ov
    return (G,LU,LV,OV), coefficient_cases, overlap_cases, source_cases


def one_subcube_Q(n,c,pattern):
    N=1<<n; F=list(range(c)); Q=[]
    for x in range(N):
        ok=True
        for j in F:
            if ((x>>j)&1) != ((pattern>>j)&1): ok=False; break
        if ok: Q.append(x)
    return Q


def run():
    random.seed(20260921)
    direct_checks=0; coeff_checks=0; overlap=0; source=0; maxerr=0.0
    for n in (2,3):
        N=1<<n
        for c in range(1,n+1):
            for pattern in range(1<<c):
                Q=one_subcube_Q(n,c,pattern)
                for trial in range(25):
                    f=[random.choice((-1,1)) for _ in range(N)]
                    for theta in (0.03125,0.137,0.311):
                        d=direct_components(n,f,Q,theta)
                        r,cc,oo,ss=relation_components(n,f,Q,theta)
                        err=max(abs(x-y) for x,y in zip(d,r))
                        maxerr=max(maxerr,err)
                        assert err < 2e-12
                        assert abs(d[0]-(d[1]+d[2]+d[3])) < 2e-12
                        direct_checks += 1; coeff_checks += cc; overlap += oo; source += ss
    pattern_checks=0
    for r0,r1 in itertools.product((0,1),repeat=2):
        xor=r0^r1; both=r0*r1
        gross=2*(r0+r1); refund=4*both; net=gross-refund
        assert net==2*xor
        p=xor; o=both; kappa=p+4*o
        assert gross <= 2*p+4*o <= 2*kappa
        pattern_checks += 1
    return {
        'status':'PASS',
        'full_FEI':'OPEN_NOT_PROVED',
        'direct_RKHS_vs_relation_checks':direct_checks,
        'exact_relation_coefficient_checks':coeff_checks,
        'overlap_support_cases_checked':overlap,
        'frustrated_source_cases_checked':source,
        'two_bit_orientation_pattern_checks':pattern_checks,
        'max_float_error':maxerr,
        'scope':'finite RM(1,n) truth-table checks for n=2,3 plus exact coefficient algebra; all-dimensional statements are symbolic proofs'
    }

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
