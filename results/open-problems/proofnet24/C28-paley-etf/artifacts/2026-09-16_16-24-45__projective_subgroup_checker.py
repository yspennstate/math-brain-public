#!/usr/bin/env python3
import itertools, math
import sympy as sp

INF = None

def legendre(a,p):
    a %= p
    if a == 0:
        return 0
    v = pow(a,(p-1)//2,p)
    return 1 if v == 1 else -1

def canon_vec(P,p):
    return (1,0) if P is INF else (P%p,1)

def det2(u,v,p):
    return (u[0]*v[1]-u[1]*v[0])%p

def C_entry(P,Q,p):
    if P == Q:
        return 0
    return legendre(det2(canon_vec(P,p),canon_vec(Q,p),p),p)

def mat_vec(A,v,p):
    a,b,c,d=A
    return ((a*v[0]+b*v[1])%p,(c*v[0]+d*v[1])%p)

def canonicalize(w,p):
    r,s=w
    if s%p:
        inv=pow(s,-1,p)
        P=(r*inv)%p
        lam=inv
        return P,lam
    assert r%p
    inv=pow(r,-1,p)
    return INF,inv

def sl2_mats(p):
    for a,b,c,d in itertools.product(range(p), repeat=4):
        if (a*d-b*c)%p==1:
            yield (a,b,c,d)

def check_projective_switching(p=13):
    assert p%4==1 and sp.isprime(p)
    points=list(range(p))+[INF]
    total=0
    for A in sl2_mats(p):
        image={}
        sign={}
        for P in points:
            Q,lam=canonicalize(mat_vec(A,canon_vec(P,p),p),p)
            image[P]=Q
            sign[P]=legendre(lam,p)
            assert sign[P] in (-1,1)
        assert len(set(image.values()))==p+1
        for P in points:
            for Q in points:
                lhs=C_entry(image[P],image[Q],p)
                rhs=sign[P]*sign[Q]*C_entry(P,Q,p)
                assert lhs==rhs
                total += 1
    # explicit map sending any chosen outside point z to infinity
    for z in points:
        if z is INF:
            A=(1,0,0,1)
        else:
            A=(0,p-1,1,(-z)%p)  # [[0,-1],[1,-z]], det=1
        Q,_=canonicalize(mat_vec(A,canon_vec(z,p),p),p)
        assert Q is INF
    return total

def primitive_root(p):
    return int(sp.primitive_root(p))

def subgroup(p,m):
    assert (p-1)%m==0
    g=primitive_root(p)
    step=(p-1)//m
    H=[pow(g,step*k,p) for k in range(m)]
    assert len(set(H))==m
    return H

def seidel_subset(p,S):
    return sp.Matrix([[0 if i==j else legendre(S[i]-S[j],p) for j in range(len(S))] for i in range(len(S))])

def ceil_three_fifths_exact(p,m):
    return (m-1)**5 < p**3 <= m**5

def subgroup_checks():
    x=sp.symbols('x')
    cases=[]
    expected={
      97: (16, (x-3)*(x+1)**2*(x+5)*(x**2-6*x+1)**2*(x**4+4*x**3-26*x**2+4*x+1)**2),
      193:(24, (x-7)**2*(x-3)**2*(x+5)**4*(x**2-6*x-39)**2*(x**2+2*x-7)**6),
    }
    for p,(m,fac) in expected.items():
        assert p%4==1 and sp.isprime(p)
        assert ceil_three_fifths_exact(p,m)
        assert ((p-1)//2)%m==0  # H lies in quadratic residues
        H=subgroup(p,m)
        assert all(legendre(h,p)==1 for h in H)
        M=seidel_subset(p,H)
        # circulant in multiplicative-group ordering: entry depends only on H[i]/H[j]
        for i in range(m):
            for j in range(m):
                ratio=(H[i]*pow(H[j],-1,p))%p
                expected_entry=0 if ratio==1 else legendre(ratio-1,p)
                assert M[i,j]==expected_entry
        cp=sp.factor(M.charpoly(x).as_expr())
        assert sp.expand(cp-fac)==0
        cases.append((p,m,sp.factor(cp)))
    return cases

if __name__=='__main__':
    total=check_projective_switching(13)
    print('PROJECTIVE_SWITCHING_P13_ALL_SL2_PASS')
    print('checked_pair_identities=', total)
    cases=subgroup_checks()
    for p,m,cp in cases:
        print(f'SUBGROUP_CASE p={p} m={m} charpoly={cp}')
    print('ALL_EXACT_CHECKS_PASS')
