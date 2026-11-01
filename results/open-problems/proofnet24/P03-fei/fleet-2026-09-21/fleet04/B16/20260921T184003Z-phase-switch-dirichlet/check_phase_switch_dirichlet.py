#!/usr/bin/env python3
"""Exact/falsification checks for B16 phase-switch Dirichlet reduction."""
from fractions import Fraction
from itertools import product
import math, random, json

def dot2(a,b): return (a & b).bit_count() & 1

def wht(b,m):
    return [sum(v * (-1 if dot2(s,r) else 1) for r,v in enumerate(b))
            for s in range(1<<m)]

def odd_mass(b,m):
    return sum(b[r]*b[r] for r in range(1<<m) if r.bit_count()&1)

def phase_mass(b,m):
    p=wht(b,m); allmask=(1<<m)-1
    return sum((p[s]-p[s^allmask])**2 for s in range(1<<m))/Fraction(1<<(m+2))

odd_checks=0
for m in range(7):
    for seed in range(50):
        rng=random.Random(10000*(m+1)+seed)
        b=[Fraction(rng.randint(-5,5),rng.randint(1,7)) for _ in range(1<<m)]
        assert odd_mass(b,m)==phase_mass(b,m)
        odd_checks+=1

def proj(x,m): return x & ((1<<m)-1)
def C(c,d,de): return sum(c[a]*c[a^de] for a in range(1<<d))
def T(c,d,m,de):
    return sum((-1 if proj(a,m).bit_count()&1 else 1)*c[a]*c[a^de]
               for a in range(1<<d))

corr_checks=0
for d in range(1,7):
    for m in range(d+1):
        for seed in range(15):
            rng=random.Random(100000*d+1000*m+seed)
            c=[Fraction(rng.randint(-3,3),rng.randint(1,5)) for _ in range(1<<d)]
            b=[Fraction(0) for _ in range(1<<m)]
            for a,v in enumerate(c): b[proj(a,m)]+=v
            rhs=Fraction(1,2)*sum(C(c,d,de)-T(c,d,m,de)
                for de in range(1<<d) if proj(de,m)==0)
            assert odd_mass(b,m)==rhs
            corr_checks+=1

def e_full(q,k): return 2*(Fraction(1,q*k)-Fraction(1,q*q))
def e_cen(q,k):
    return 2*Fraction(1,(2**q)*q)*(Fraction(1,(2**k)*k)-Fraction(1,(2**q)*q))

mult_checks=0
max_full=(Fraction(0),None); max_cen=(Fraction(0),None)
for q in range(1,100,2):
    for k in range(1,q+1,2):
        ef=e_full(q,k); ec=e_cen(q,k)
        assert 0<=ef<=Fraction(4,9)
        assert 0<=ec<=Fraction(11,288)
        if ef>max_full[0]: max_full=(ef,(q,k))
        if ec>max_cen[0]: max_cen=(ec,(q,k))
        mult_checks+=1
assert max_full==(Fraction(4,9),(3,1))
assert max_cen==(Fraction(11,288),(3,1))

def affine_masks(n):
    N=1<<n; out=set()
    for a in range(1<<n):
        mask=0
        for x in range(N):
            if dot2(a,x): mask|=1<<x
        out.add(mask); out.add(mask^((1<<N)-1))
    return sorted(out)

def orthogonal(gens,N):
    return [x for x in range(1<<N) if all(dot2(x,g)==0 for g in gens)]

def c0(n):
    return orthogonal(affine_masks(n),1<<n)

def span(vs):
    s={0}
    for v in vs: s |= {x^v for x in list(s)}
    return sorted(s)

def dual(E,N): return orthogonal(E,N)
def mean_sign(mask,N): return 1-2*mask.bit_count()/N

def phi(E,h,s,N):
    P=dual(E,N)
    return (2*N/len(P))*sum(math.cos(s*mean_sign(h^r,N)) for r in P)

def split_corr(ur,g,N,minus):
    mask=g if minus else (((1<<N)-1)^g)
    cnt=mask.bit_count(); neg=(ur&mask).bit_count()
    return (cnt-2*neg)/N

dual_checks=0
retained_checks=0
for n in (2,3):
    N=1<<n; C0=c0(n); nz=[x for x in C0 if x]
    Es=[[0],C0]
    if n==3:
        Es += [span(nz[:k]) for k in range(1,4)]
    for E in Es:
        P=dual(E,N)
        for seed in range(20):
            rng=random.Random(n*10000+len(E)*100+seed)
            h=rng.randrange(1<<N); g=rng.randrange(1<<N); s=3*rng.random()
            lhs=phi(E,h,s,N)-phi(E,h^g,s,N)
            sp=0.0; quad=0.0
            for r in P:
                ap=split_corr(h^r,g,N,False)
                am=split_corr(h^r,g,N,True)
                sp += math.sin(s*ap)*math.sin(s*am)
                quad += ap*am
            rhs=-(4*N/len(P))*sp
            assert abs(lhs-rhs)<1e-9
            assert abs(quad)<1e-9
            pm=g.bit_count()/N; pp=1-pm
            b4=(2/3)*s**4*(pp**2+pm**2)*math.sqrt(pp*pm)
            b2=4*s**2*math.sqrt(pp*pm)
            assert abs(lhs)<=b4+1e-8
            assert abs(lhs)<=b2+1e-8
            dual_checks+=1

    Ds=[[0],C0]
    if n==3: Ds += [span(nz[:k]) for k in range(1,4)]
    for D in Ds:
        L=len(dual(D,N)); rho=2*N/L
        for seed in range(25):
            rng=random.Random(77777+n*1000+len(D)*10+seed)
            h=rng.randrange(1<<N); g=rng.randrange(1<<N); s=3*rng.random()
            psi=lambda z: phi(C0,z,s,N)-phi(D,z,s,N)
            lhs=psi(h)-psi(h^g)
            pm=g.bit_count()/N; pp=1-pm
            b4=(4/3)*s**4*(1-rho)*(pp**2+pm**2)*math.sqrt(pp*pm)
            b2=8*s**2*(1-rho)*math.sqrt(pp*pm)
            assert abs(lhs)<=b4+1e-8
            assert abs(lhs)<=b2+1e-8
            retained_checks+=1

out={
    "status":"PASS",
    "odd_phase_switch_exact_checks":odd_checks,
    "same_syndrome_correlation_exact_checks":corr_checks,
    "multiplier_exact_checks":mult_checks,
    "dual_code_factorization_and_bound_checks":dual_checks,
    "retained_terminal_bound_checks":retained_checks,
    "sharp_full_multiplier":"4/9 at (q,k)=(3,1)",
    "sharp_central_multiplier":"11/288 at (q,k)=(3,1)",
}
print(json.dumps(out,indent=2,sort_keys=True))
