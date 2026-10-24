#!/usr/bin/env python3
# Exact finite self-check for I0099 Selberg-centering report.
# All arithmetic is integer / modular; quartic-character values are Gaussian integer pairs.

def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

def factors(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1: out.append(n)
    return out

def primitive_root(p):
    fac=factors(p-1)
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in fac):
            return g
    raise RuntimeError

I4=[(1,0),(0,1),(-1,0),(0,-1)]
def add(z,w): return (z[0]+w[0],z[1]+w[1])
def conj(z): return (z[0],-z[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])

def data(p):
    g=primitive_root(p)
    log=[None]*p
    x=1
    for e in range(p-1):
        log[x]=e
        x=(x*g)%p
    def rho(x):
        x%=p
        if x==0:return (0,0)
        return I4[log[x]%4]
    def chi(x):
        x%=p
        if x==0:return 0
        return 1 if log[x]%2==0 else -1

    S=0
    for x in range(p):
        for lam in range(p):
            S += chi(x*(x-1)*lam*(lam-1)*(lam-x))

    L=(0,0)
    Lb=(0,0)
    for s in range(p):
        for t in range(p):
            w=chi(t)*chi(1-s+t)
            if not w: continue
            D=(s*s-4*t)%p
            r=rho(D)
            L=add(L,(w*r[0],w*r[1]))
            rb=conj(r)
            Lb=add(Lb,(w*rb[0],w*rb[1]))

    J=(0,0)
    for u in range(p):
        J=add(J,mul(rho(u),rho(1-u)))

    H=[lam for lam in range(2,p) if chi(lam)==1 and chi(1-lam)==1]
    suma=0
    for lam in H:
        cubic=sum(chi(x*(x-1)*(x-lam)) for x in range(p))
        a=-cubic
        suma += a

    assert len(H)==(p-5)//4
    assert (S,0)==add(L,Lb), (p,S,L,Lb)
    assert Lb==conj(L)
    assert L[0]*L[0]+L[1]*L[1]==p*p, (p,L)
    assert suma == -(S+6)//4 and (S+6)%4==0
    assert abs(suma)*4 <= 2*p+6

    # Diagnostic phase identity only: not used as a proved input in the report.
    J2=mul(J,J)
    phase=2*J2[0]
    assert S==phase, (p,S,J,J2)

    return p,g,len(H),S,L,J,suma,2*(p+3),p-5

ps=[p for p in range(13,198) if p%4==1 and isprime(p)]
for row in map(data,ps):
    p,g,h,S,L,J,suma,bn,bd=row
    print(f"p={p} primitive={g} H={h} Sigma12={S} Lrho={L[0]}{L[1]:+d}i "
          f"J={J[0]}{J[1]:+d}i sum_H_a={suma} b={bn}/{bd}")
print(f"PRIMES_CHECKED={len(ps)} FIRST={ps[0]} LAST={ps[-1]}")
print("SELBERG_REDUCTION_DIRECT_FINITE_CHECK=PASS")
print("EVANS_MODULUS_SPECIALIZATION_ABS_L2_EQ_P=PASS")
print("H_MEAN_IDENTITY_FINITE_CHECK=PASS")
print("PHASE_IDENTITY_DIAGNOSTIC_ONLY_MATCHES_ALL_TESTED=PASS")
print("ALL_I0099_SELBERG_CENTERING_SELF_CHECKS_PASS")
