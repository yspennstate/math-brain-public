#!/usr/bin/env python3
"""
R12 / I0102 exact-arithmetic self-check for the spike/Mellin reduction.

Finite checks only. They verify the integer character identities used in the
written all-prime proof; they do not prove a sub-square-root SOS bound.

Checked for p=5,13,17,29,37 and every nonzero xi:
  1. the quartic Fourier-kernel cross-ratio identity on the generic set;
  2. the unique doubly-degenerate (eta,zeta)=(0,0) value p-2;
  3. the special eta=+-xi or zeta=+-xi entries have absolute value <=2;
  4. the multiplicative-convolution Gram identity
       M M^T = p^2 I - (p+1)(J + chi chi^T),
     where M[a,b]=L(a/b) and
       L(lambda)=sum_x chi(x(x-1)(x-lambda)).
"""

PRIMES=(5,13,17,29,37)

def chi(a,p):
    a%=p
    if a==0:
        return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def L(p,lam):
    return sum(chi(x*(x-1)*(x-lam),p) for x in range(p))

def quartic_T(p,xi,eta,zeta):
    inv2=pow(2,-1,p)
    roots=(
        ((xi+eta-zeta)*inv2)%p,
        ((-zeta)*inv2)%p,
        (eta*inv2)%p,
        (xi*inv2)%p,
    )
    total=0
    for s in range(p):
        prod=1
        for r in roots:
            prod=(prod*(s-r))%p
        total+=chi(prod,p)
    return total

def matmul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][r]*B[r][j] for r in range(k))
             for j in range(m)] for i in range(n)]

for p in PRIMES:
    for xi in range(1,p):
        special={xi%p,(-xi)%p}
        for eta in range(p):
            A=(xi*xi-eta*eta)%p
            for zeta in range(p):
                B=(xi*xi-zeta*zeta)%p
                T=quartic_T(p,xi,eta,zeta)
                if eta not in special and zeta not in special:
                    if eta==0 and zeta==0:
                        assert T==p-2, (p,xi,eta,zeta,T)
                    else:
                        lam=(A*pow(B,-1,p))%p
                        rhs=chi(B,p)*L(p,lam)-1
                        assert T==rhs, (p,xi,eta,zeta,T,rhs)
                else:
                    assert abs(T)<=2, (p,xi,eta,zeta,T)

    elems=list(range(1,p))
    n=p-1
    M=[[L(p,(a*pow(b,-1,p))%p) for b in elems] for a in elems]
    MT=[list(row) for row in zip(*M)]
    MM=matmul(M,MT)
    ch=[chi(a,p) for a in elems]
    for i in range(n):
        for j in range(n):
            rhs=(p*p if i==j else 0) - (p+1)*(1+ch[i]*ch[j])
            assert MM[i][j]==rhs, (p,i,j,MM[i][j],rhs)
    print(f"p={p}: quartic cross-ratio + Mellin Gram identities PASS")

print("ALL_EXACT_CHECKS_PASS")
