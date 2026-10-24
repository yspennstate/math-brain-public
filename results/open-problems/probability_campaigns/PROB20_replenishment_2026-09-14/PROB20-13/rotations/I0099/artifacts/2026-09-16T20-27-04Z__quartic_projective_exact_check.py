#!/usr/bin/env python3
from itertools import permutations
from collections import Counter
from math import prod

# Exact self-checks for I0099 run. No floating point.

def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def chi(x,p):
    x%=p
    if x==0:return 0
    z=pow(x,(p-1)//2,p)
    assert z in (1,p-1)
    return 1 if z==1 else -1

def is_clique(C,p):
    return len(set(C))==len(C) and all(chi(C[i]-C[j],p)==1 for i in range(len(C)) for j in range(i))

def cross_ratio(a,b,c,d,p):
    # Convention used in the report.
    return ((b-d)*(c-a)%p)*pow((b-a)*(c-d)%p,-1,p)%p

def legendre_trace(lam,p):
    # a_p(lambda)=p+1-#E_lambda(F_p)=-sum_t chi(t(t-1)(t-lambda))
    return -sum(chi(t*(t-1)*(t-lam),p) for t in range(p))

def quartic_sum(q,p):
    return sum(chi(prod((x-a)%p for a in q),p) for x in range(p))

def check_quartic_formula(p,C):
    assert is_clique(C,p)
    k=len(C)
    S=[sum(chi(x-a,p) for a in C) for x in range(p)]
    M4=sum(s**4 for s in S)
    m=Counter()
    for q in permutations(C,4):
        lam=cross_ratio(*q,p)
        assert lam not in (0,1)
        assert chi(lam,p)==1 and chi(1-lam,p)==1
        ap=legendre_trace(lam,p)
        assert quartic_sum(q,p)==-1-ap
        m[lam]+=1
    P0=-k**4-6*k**3+(3*p+15)*k**2-(2*p+9)*k
    T=sum(mult*legendre_trace(lam,p) for lam,mult in m.items())
    assert M4==P0-T
    H=[lam for lam in range(2,p) if chi(lam,p)==1 and chi(1-lam,p)==1]
    assert len(H)==(p-5)//4
    return M4,P0,T,len(m)

def canonical_matrix(A,B,C,D,p):
    vals=(A%p,B%p,C%p,D%p)
    for z in vals:
        if z:
            iz=pow(z,-1,p)
            return tuple(v*iz%p for v in vals)
    raise AssertionError

def pgl2(p):
    seen=set()
    for A in range(p):
      for B in range(p):
       for C in range(p):
        for D in range(p):
         if (A*D-B*C)%p:
            seen.add(canonical_matrix(A,B,C,D,p))
    assert len(seen)==p*(p*p-1)
    return seen

def mobius(g,x,p):
    A,B,C,D=g
    den=(C*x+D)%p
    if den==0:return None
    return (A*x+B)*pow(den,-1,p)%p

def fall4(n): return n*(n-1)*(n-2)*(n-3)

def check_projective_energy_and_rigidity(p,C):
    C=set(C); assert is_clique(list(C),p)
    m=Counter(cross_ratio(*q,p) for q in permutations(C,4))
    lhs=sum(v*v for v in m.values())
    rhs=0; hist=Counter(); rigid=0
    for g in pgl2(p):
        I=[x for x in C if (mobius(g,x,p) in C)]
        n=len(I); hist[n]+=1; rhs+=fall4(n)
        if n>=3:
            rigid+=1
            A,B,c,D=g
            det=(A*D-B*c)%p
            assert chi(det,p)==1
            if c:
                signs={chi(c*x+D,p) for x in I}
                assert signs <= {-1,1} and len(signs)==1
    assert lhs==rhs
    return lhs,dict(sorted(hist.items())),rigid

def primitive_root(p):
    fac=[]; n=p-1; d=2
    while d*d<=n:
        if n%d==0:
            fac.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:fac.append(n)
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in fac): return g
    raise AssertionError

def quartic_table(p):
    assert p%4==1
    g=primitive_root(p)
    # rho(g)=i, represented as (real,imag)
    vals=[(0,0)]*p
    cyc=[(1,0),(0,1),(-1,0),(0,-1)]
    x=1
    for e in range(p-1):
        vals[x]=cyc[e%4]
        x=x*g%p
    return vals

def cmul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cadd(z,w):return (z[0]+w[0],z[1]+w[1])

def jacobi_lead_check(p):
    rho=quartic_table(p)
    J=(0,0)
    for x in range(p): J=cadd(J,cmul(rho[x],rho[(1-x)%p]))
    J2=cmul(J,J)
    S12=0
    for x in range(p):
      for lam in range(p):
        S12 += chi(x*(x-1)*lam*(lam-1)*(lam-x),p)
    assert S12==2*J2[0]
    # Also verify the elementary H-average reduction.
    H=[lam for lam in range(2,p) if chi(lam,p)==1 and chi(1-lam,p)==1]
    AH=sum(legendre_trace(lam,p) for lam in H)
    assert AH==-(S12+6)//4 and (S12+6)%4==0
    return J,S12,AH

# Finite frontier coverage newly completed by the separate exhaustive solver.
expected=[p for p in range(3542,3582) if p%4==1 and isprime(p)]
assert expected==[3557,3581]
frontier_witnesses={
 3557:[0,1,3542,3379,2565,2995,2948,2486,2446,2383,1460,1273,1214,594,475,151,104],
 3581:[0,1,3551,3546,3100,3203,2946,2819,2651,2465,1661,1445,1277,727,493,406,196],
}
for p,C in frontier_witnesses.items():
    assert len(C)==17 and is_clique(C,p)
print('FRONTIER_PRIME_COVERAGE_3541_TO_3581=PASS', expected)
print('FRONTIER_WITNESSES_OMEGA17=PASS')

small=[(29,[28,27,23,22]),(37,[36,35,32,25]),(41,[40,39,38,30,7])]
for p,C in small:
    out=check_quartic_formula(p,C)
    print('QUARTIC_FORMULA_PASS',p,out)

E,hist,rigid=check_projective_energy_and_rigidity(29,[28,27,23,22])
print('PROJECTIVE_ENERGY_IDENTITY_PASS',29,E,hist)
print('PSL2_DENOMINATOR_RIGIDITY_PASS',29,'overlap_ge_3_transforms',rigid)

# This is recorded as an exact finite lead, NOT as a proved general identity in the report.
for p in [5,13,17,29,37,41,53,61,73,89,97]:
    if p%4==1 and isprime(p):
        J,S12,AH=jacobi_lead_check(p)
        print('JACOBI_LEAD_SMALL_PRIME_MATCH',p,'J=',J,'S12=',S12,'sum_H_ap=',AH)

print('ALL_I0099_QUARTIC_PROJECTIVE_SELF_CHECKS_PASS')
