#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
from itertools import combinations

getcontext().prec = 100
LN2 = Decimal(2).ln()

def dlog2(x: Decimal) -> Decimal:
    return x.ln() / LN2

def h2(x: Decimal) -> Decimal:
    if x == 0 or x == 1:
        return Decimal(0)
    return -x*dlog2(x) - (Decimal(1)-x)*dlog2(Decimal(1)-x)

def wht_coeffs(vals):
    N=len(vals)
    out=[]
    for s in range(N):
        total=0
        for x,v in enumerate(vals):
            total += v * (-1 if ((s & x).bit_count() & 1) else 1)
        out.append(Fraction(total,N))
    return out

def project(p,n,Bmask):
    bits=[i for i in range(n) if (Bmask>>i)&1]
    out=[Fraction(0) for _ in range(1<<len(bits))]
    for S,ps in enumerate(p):
        R=0
        for j,i in enumerate(bits):
            if (S>>i)&1:
                R |= 1<<j
        out[R]+=ps
    return out

def exact_small():
    spectral_checks=0
    parity_checks=0
    projection_checks=0
    cap_equalities=0
    for n in range(2,9):
        N=1<<n
        vals=[-1]+[1]*(N-1)
        coeff=wht_coeffs(vals)
        p=[c*c for c in coeff]
        p0=Fraction((N-2)**2,N*N)
        c=Fraction(4,N*N)
        assert p[0]==p0
        for S in range(1,N):
            assert p[S]==c
            spectral_checks += 1
        alpha=Fraction(N-2,N)
        assert p0 == alpha*alpha
        for J in range(1,N):
            even=sum(p[S] for S in range(N) if ((S&J).bit_count()&1)==0)
            assert even==alpha
            parity_checks += 1
            assert p[0] == even*even
            cap_equalities += 1
            # Every odd atom saturates the odd raw cap.
            odd_target=(1-even)*(1-even)
            for T in range(N):
                if ((T&J).bit_count()&1)==1:
                    assert p[T]==odd_target
                    cap_equalities += 1
            q=J.bit_count()
            marginal=project(p,n,J)
            M=1<<q
            zero=Fraction(1,1)-Fraction(4,N)+Fraction(4,N*M)
            nonzero=Fraction(4,N*M)
            assert marginal[0]==zero
            projection_checks += 1
            for R in range(1,M):
                assert marginal[R]==nonzero
                projection_checks += 1
    return spectral_checks,parity_checks,projection_checks,cap_equalities

def profile_decimal(n,q):
    N=Decimal(2) ** n
    M=Decimal(2) ** q
    vq=Decimal(4)/N*(Decimal(1)-Decimal(1)/M)
    vn=Decimal(4)/N*(Decimal(1)-Decimal(1)/N)
    Hq=h2(vq)+vq*dlog2(M-Decimal(1))
    Hn=h2(vn)+vn*dlog2(N-Decimal(1))
    eps=Decimal(2)/N
    T=Decimal(n)*h2(eps)-Hn
    K=Decimal(n)/Decimal(q)*Hq-Hn
    I=Decimal(2*n)/N
    return Hq,Hn,T,K,I

def main():
    a,b,c,d=exact_small()
    print('exact_spectral_atom_checks',a)
    print('exact_nonempty_block_parity_checks',b)
    print('exact_projection_atom_checks',c)
    print('exact_block_cap_saturation_equalities',d)
    print('n q T_over_I K_over_I K_over_T asymptotic_K_over_I')
    for n in (20,40,80,160):
        q=n//2
        Hq,Hn,T,K,I=profile_decimal(n,q)
        target=Decimal(2)*(Decimal(n)/Decimal(q)-Decimal(1))
        print(n,q,
              f'{T/I:.30f}',
              f'{K/I:.30f}',
              f'{K/T:.30f}',
              f'{target:.30f}')
    print('PASS')

if __name__=='__main__':
    main()
