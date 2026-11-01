#!/usr/bin/env python3
from itertools import combinations

MAXP=197

def primes_upto(n):
    out=[]
    for p in range(2,n+1):
        if all(p%d for d in range(2,int(p**0.5)+1)):
            out.append(p)
    return out

def qrset(p):
    return {x*x%p for x in range(1,p)}

def chi(a,p,Q):
    a%=p
    if a==0: return 0
    return 1 if a in Q else -1

def beta(a,p,Q):
    c=chi(a,p,Q)
    assert c in (-1,1)
    return 0 if c==1 else 1

def inv(a,p):
    return pow(a%p,p-2,p)

def sqrt_det(a,p):
    a%=p
    for x in range(p):
        if x*x%p==a:
            return x
    raise AssertionError(("nonsquare",a,p))

def point_count_legendre(lam,p,Q):
    return p+1+sum(chi(x*(x-1)*(x-lam),p,Q) for x in range(p))

grand=0
per=[]
for p in [q for q in primes_upto(MAXP) if q%4==1]:
    Q=qrset(p)
    H=[x for x in range(p) if x not in (0,1) and x in Q and (x-1)%p in Q]
    pairs=[(c,d) for c,d in combinations(H,2) if (d-c)%p in Q]
    if not pairs:
        continue
    ii=sqrt_det(-1,p)
    eps=beta(2,p,Q)
    assert eps==beta(ii,p,Q)
    local=0
    for c,d in pairs:
        U=sqrt_det(c,p); V=sqrt_det(1-c,p)
        S=sqrt_det(d,p); T=sqrt_det(1-d,p); W=sqrt_det(d-c,p)
        pairs5=[
            (U,V),
            (S,T),
            (S*inv(U,p)%p, ii*W*inv(U,p)%p),
            (T*inv(V,p)%p, W*inv(V,p)%p),
            (ii*T*U*inv(W,p)%p, S*V*inv(W,p)%p),
        ]
        assert all((u*u+v*v)%p==1 for u,v in pairs5)

        # Exact square factorization from Lemma 7.1 of the report.
        x=V*inv(1+U,p)%p
        y=T*inv(1+S,p)%p
        R=W*(1+x*x)%p*(1+y*y)%p*inv(2,p)%p
        assert R*R%p == ((x*x-y*y)*(1-x*x*y*y))%p
        kap=sqrt_det((-2*ii)%p,p)
        prod=1
        for u,v in pairs5:
            prod=prod*(1+u)%p
        lhs=prod*inv(2*U*V*W,p)%p
        fac=(x*x+1)*inv(x*(x*x-1)*(y*y+1),p)%p
        fac=fac*(R-ii*(x-y)*(1+x*y))%p*inv(kap*(x-y),p)%p
        assert lhs == fac*fac%p

        ns=[]; ds=[]; rs=[]; ss=[]
        for u,v in pairs5:
            lam=u*u%p
            N=point_count_legendre(lam,p,Q)
            assert N%16==0
            n=(N//16)&1
            r=beta(u,p,Q); s=beta(v,p,Q); dd=beta(1+u,p,Q)
            assert n == (((1+eps)*dd + r*s)&1)
            ns.append(n); ds.append(dd); rs.append(r); ss.append(s)
        assert sum(ns)%2==0

        alpha=beta(U,p,Q); nu=beta(V,p,Q); omega=beta(W,p,Q)
        assert sum(ds)%2 == (eps+alpha+nu+omega)%2
        assert sum((r*s) for r,s in zip(rs,ss))%2 == ((1+eps)*(alpha+nu+omega))%2

        common=0
        for z in range(p):
            if z in (0,1,c,d): continue
            if all((z-a)%p in Q for a in (0,1,c,d)):
                common += 1
        expected=1 if p%8==1 else 0
        assert common%2==expected
        grand+=1; local+=1
    per.append((p,local))
    print(f"p={p} normalized_four_cliques={local} parity=PASS five_factor=PASS square_identity=PASS")

print("PRIMES_CHECKED="+str(len(per)))
print("TOTAL_NORMALIZED_FOUR_CLIQUES="+str(grand))
print("LEGENDRE_PARITY_FORMULA_ALL=PASS")
print("FIVE_FACTOR_NORMALIZED_ORDER_PARITY_ALL=PASS")
print("FIVE_FACTOR_SQUARE_CLASS_PRODUCT_ALL=PASS")
print("FOUR_CLIQUE_EXTENSION_PARITY_ALL=PASS")
print("ALL_I0099_FOUR_CLIQUE_PARITY_SELF_CHECKS_PASS")
