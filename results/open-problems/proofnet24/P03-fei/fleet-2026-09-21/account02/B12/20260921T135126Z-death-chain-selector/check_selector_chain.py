#!/usr/bin/env python3
"""Self-checks for B12 random-order spectral-sample decomposition.

Finite checks support, but do not prove, the universal lemmas in REPORT.md.
All Walsh/shadow identities are checked with fractions; logarithmic identities
are checked numerically after exact probabilities are constructed.
"""
from fractions import Fraction
from math import comb, factorial, log, log2

def bitlist(x,n): return [(x>>i)&1 for i in range(n)]

def parity(n):
    return [1 if sum(bitlist(x,n))%2==0 else -1 for x in range(1<<n)]

def and_fn(n):
    return [1 if x==(1<<n)-1 else -1 for x in range(1<<n)]

def majority(n):
    return [1 if sum(bitlist(x,n))>n//2 else -1 for x in range(1<<n)]

def addressing(k):
    n=k+(1<<k)
    vals=[]
    for x in range(1<<n):
        j=sum(((x>>i)&1)<<i for i in range(k))
        vals.append(1 if ((x>>(k+j))&1) else -1)
    return vals,n

def tribes(w,m):
    n=w*m
    vals=[]
    for x in range(1<<n):
        hit=any(all((x>>(j*w+l))&1 for l in range(w)) for j in range(m))
        vals.append(1 if hit else -1)
    return vals,n

def walsh(vals,n):
    N=1<<n
    out=[]
    for A in range(N):
        total=0
        for x,fx in enumerate(vals):
            total += fx*(-1 if ((A&x).bit_count()&1) else 1)
        out.append(Fraction(total,N))
    return out

def entropy(probs):
    return -sum(float(q)*log2(float(q)) for q in probs if q>0)

def analyze(name,vals,n):
    c=walsh(vals,n)
    p=[z*z for z in c]
    assert sum(p)==1
    N=1<<n
    v=[Fraction(0) for _ in range(N)]
    for A in range(N):
        a=A.bit_count()
        for B in range(N):
            if A & ~B == 0:
                v[A] += p[B]/comb(B.bit_count(),a)

    recurrence_checks=0
    green_checks=0
    for A in range(N):
        a=A.bit_count()
        lhs=sum(v[A|(1<<i)] for i in range(n) if not ((A>>i)&1))
        assert lhs==(a+1)*(v[A]-p[A])
        recurrence_checks += 1
        if a:
            via_green=Fraction(0)
            for B in range(N):
                if A & ~B == 0:
                    d=B.bit_count()-a
                    # a * integral_0^1 s^(a-1)(1-s)^d ds
                    weight=Fraction(a*factorial(a-1)*factorial(d),factorial(a+d))
                    via_green += p[B]*weight
            assert via_green==v[A]
            green_checks += 1

    I=sum(Fraction(A.bit_count())*p[A] for A in range(N))
    assert sum(v)==1+I
    H=entropy(p)
    level=[Fraction(0) for _ in range(n+1)]
    for A in range(N):
        level[A.bit_count()] += p[A]
    HK=entropy(level)

    hazard=0.0
    selector=0.0
    for A in range(N):
        if not v[A]:
            continue
        a=A.bit_count()
        t=float(p[A]/v[A])
        u=1.0-t
        if 0.0<t<1.0:
            hazard += float(v[A])*(-t*log2(t)-u*log2(u))
        if v[A]>p[A]:
            denom=(a+1)*(v[A]-p[A])
            r=[v[A|(1<<i)]/denom for i in range(n) if not ((A>>i)&1)]
            Hr=entropy(r)
            residual_log=0.0
            norm=v[A]-p[A]
            for B in range(N):
                if B!=A and A & ~B == 0 and p[B]:
                    w=(p[B]/comb(B.bit_count(),a))/norm
                    residual_log += float(w)*log2(B.bit_count()-a)
            j=Hr-residual_log
            assert j>=-1e-12
            selector += float(v[A]-p[A])*j

    assert abs(H-(hazard+selector))<2e-10
    assert hazard<=HK+2e-10
    assert HK<=3*float(I)+2e-10
    print(f"{name}: n={n} I={float(I):.12g} H={H:.12g} "
          f"H(K)={HK:.12g} hazard={hazard:.12g} selector={selector:.12g} "
          f"rec={recurrence_checks} green={green_checks}")

def h2(x):
    if x==0.0 or x==1.0: return 0.0
    return -x*log2(x)-(1-x)*log2(1-x)

def and_root(n):
    alpha=2.0**(-n)
    V=4*alpha*(1-alpha)
    return V,h2(V)/V

def tribes_root_lb(w):
    base=1-2.0**(-w)
    m=max(1,round(log(0.5)/log(base)))
    q=base**m
    V=4*q*(1-q)
    I=m*w*2.0**(-(w-1))*base**(m-1)
    n=m*w
    jlb=log2(n*V/I)
    return m,n,q,V,I,jlb

if __name__=="__main__":
    cases=[
        ("parity5",parity(5),5),
        ("and6",and_fn(6),6),
        ("majority5",majority(5),5),
    ]
    vals,n=addressing(2); cases.append(("address2",vals,n))
    vals,n=tribes(2,2); cases.append(("tribes2x2",vals,n))
    for case in cases:
        analyze(*case)

    print("AND root local hazard h2(V)/V:")
    for n in (4,8,12,16,20,32):
        V,r=and_root(n)
        print(f"  n={n:2d} V={V:.12g} ratio={r:.12g}")

    print("balanced-tribes root selector lower bound log2(n V / I):")
    for w in (4,6,8,10,12,16,20):
        m,n,q,V,I,jlb=tribes_root_lb(w)
        print(f"  w={w:2d} m={m:7d} n={n:9d} q={q:.12g} "
              f"I={I:.12g} lower={jlb:.12g}")
    print("PASS")
