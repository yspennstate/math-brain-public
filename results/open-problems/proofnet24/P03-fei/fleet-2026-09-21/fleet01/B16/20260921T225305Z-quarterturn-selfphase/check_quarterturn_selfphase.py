#!/usr/bin/env python3
from fractions import Fraction
import json, math, random

def par(x): return x.bit_count() & 1

def rm1(n):
    N=1<<n
    out=[]
    for a in range(1<<n):
        for b in (0,1):
            m=0
            for x in range(N):
                if par(a & x)^b: m |= 1<<x
            out.append(m)
    return sorted(set(out))

def span(gens):
    S={0}
    for g in gens:
        S |= {x^g for x in list(S)}
    return sorted(S)

def perp(M,N):
    return [A for A in range(1<<N) if all(par(A&m)==0 for m in M)]

def beta(b,m,N):
    s=0
    for x in range(N):
        s += -1 if (((b>>x)&1)^((m>>x)&1)) else 1
    return Fraction(s,N)

def fA(b,A): return -1 if par(b&A) else 1

def poly_average(M,b,N):
    ans=[(Fraction(0),Fraction(0)) for _ in range(N+1)]
    for m in M:
        p=[(Fraction(1),Fraction(0))]
        for x in range(N):
            sg=-1 if (((b>>x)&1)^((m>>x)&1)) else 1
            q=[(Fraction(0),Fraction(0)) for _ in range(len(p)+1)]
            for k,(re,im) in enumerate(p):
                q[k]=(q[k][0]+re,q[k][1]+im)
                rr,ii=q[k+1]
                q[k+1]=(rr-im*sg,ii+re*sg)
            p=q
        for k,(re,im) in enumerate(p):
            rr,ii=ans[k]
            ans[k]=(rr+re/Fraction(len(M)),ii+im/Fraction(len(M)))
    return ans

def poly_dual(M,b,N):
    ans=[(Fraction(0),Fraction(0)) for _ in range(N+1)]
    for A in perp(M,N):
        k=A.bit_count()
        ir,ii=((1,0),(0,1),(-1,0),(0,-1))[k&3]
        rr,qq=ans[k]
        ans[k]=(rr+fA(b,A)*ir,qq+fA(b,A)*ii)
    return ans

def psi(q):
    x=float(abs(q))
    if x==0.0 or x==1.0: return 0.0
    return -(x*x)*math.log(x*x)

def theta(M,b,N):
    return N*(sum(psi(beta(b,m,N)) for m in M)/len(M)
              -sum(psi(beta(0,m,N)) for m in M)/len(M))

def Hnat(b,n):
    N=1<<n
    H=0.0
    for a in range(N):
        s=0
        for x in range(N):
            s += (-1 if (b>>x)&1 else 1) * (-1 if par(a&x) else 1)
        p=(s/N)**2
        if p: H -= p*math.log(p)
    return H

stats={"macwilliams_polynomials":0,"matched_second_moments":0,
       "self_phase_distribution_kills":0,"rm1_entropy_identities":0,
       "self_phase_dual_classifications":0}
for n in (2,3):
    N=1<<n
    base=rm1(n)
    rng=random.Random(20260921+n)
    for _ in range(12):
        b=rng.randrange(1<<N)
        M=span(base+[rng.randrange(1<<N),rng.randrange(1<<N)])
        assert poly_average(M,b,N)==poly_dual(M,b,N)
        stats["macwilliams_polynomials"]+=1
        e_f=sum(beta(b,m,N)**2 for m in M)/len(M)
        e_1=sum(beta(0,m,N)**2 for m in M)/len(M)
        assert e_f==e_1==Fraction(1,N)
        stats["matched_second_moments"]+=1
        Ms=span(M+[b])
        assert sorted(beta(b,m,N) for m in Ms)==sorted(beta(0,m,N) for m in Ms)
        stats["self_phase_distribution_kills"]+=1
        D0=set(perp(base,N)); Ds=set(perp(span(base+[b]),N))
        assert Ds=={A for A in D0 if fA(b,A)==1}
        stats["self_phase_dual_classifications"]+=1
        assert abs(theta(base,b,N)-Hnat(b,n))<2e-12
        stats["rm1_entropy_identities"]+=1
stats["total_checks"]=sum(stats.values())
print(json.dumps(stats,sort_keys=True))
