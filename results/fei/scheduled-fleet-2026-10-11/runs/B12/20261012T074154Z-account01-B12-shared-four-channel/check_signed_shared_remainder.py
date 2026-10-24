#!/usr/bin/env python3
"""Exact checks for the shared-coordinate four-channel decomposition.

Walsh coefficients and coefficients of logarithms of primes are exact
Fractions. Decimal evaluations are display only. No randomness is used.
"""

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product

getcontext().prec = 80


def walsh(values):
    a = [Fraction(x) for x in values]
    n = len(a)
    step = 1
    while step < n:
        for base in range(0, n, 2 * step):
            for j in range(base, base + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return tuple(x / n for x in a)


def restrict(values, dimension, coordinate, bit):
    return tuple(values[j] for j in range(1 << dimension)
                 if ((j >> coordinate) & 1) == bit)


def split(values, dimension, coordinate):
    plus = restrict(values, dimension, coordinate, 0)
    minus = restrict(values, dimension, coordinate, 1)
    return (tuple((x + y) / 2 for x, y in zip(plus, minus)),
            tuple((x - y) / 2 for x, y in zip(plus, minus)))


def factor_integer(n):
    n = abs(n)
    out = defaultdict(int)
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] += 1
            n //= p
        p += 1
    if n > 1:
        out[n] += 1
    return out


def entropy_vector_from_hat(coefficients):
    out = defaultdict(Fraction)
    for coefficient in coefficients:
        if coefficient == 0:
            continue
        mass = coefficient * coefficient
        for p, exponent in factor_integer(mass.denominator).items():
            out[p] += mass * exponent
        for p, exponent in factor_integer(mass.numerator).items():
            out[p] -= mass * exponent
    return {p: c for p, c in out.items() if c}


def entropy_vector(values):
    return entropy_vector_from_hat(walsh(values))


def add_vectors(*terms):
    out = defaultdict(Fraction)
    for scalar, vector in terms:
        for p, coefficient in vector.items():
            out[p] += scalar * coefficient
    return {p: c for p, c in out.items() if c}


def decimal(vector):
    return sum(Decimal(c.numerator) / Decimal(c.denominator) * Decimal(p).ln()
               for p, c in vector.items())


def source_data(gp, gm):
    bhat = walsh(tuple(Fraction(x-y, 2) for x,y in zip(gp,gm)))
    return sum(x*x for x in bhat), entropy_vector_from_hat(bhat)


def child_data(h):
    hhat = walsh(h)
    return (1-hhat[0]*hhat[0],
            sum(j.bit_count()*x*x for j,x in enumerate(hhat)))


def potential_drops(gp, gm, h, dimension, coordinate):
    q,z=source_data(gp,gm)
    v,j=child_data(h)
    children=[]
    for bit in (0,1):
        gbp=restrict(gp,dimension,coordinate,bit)
        gbm=restrict(gm,dimension,coordinate,bit)
        hb=restrict(h,dimension,coordinate,bit)
        qb,zb=source_data(gbp,gbm)
        vb,jb=child_data(hb)
        children.append((qb,zb,vb,jb))
    dqi=q*j-sum(x[0]*x[3] for x in children)/2
    dvz=add_vectors((v,z),(-children[0][2]/2,children[0][1]),
                    (-children[1][2]/2,children[1][1]))
    return dqi,dvz


def kernel_form(p, q):
    return add_vectors((1, entropy_vector(p)), (1, entropy_vector(q)),
                       (Fraction(-1, 2), entropy_vector(tuple(x+y for x,y in zip(p,q)))),
                       (Fraction(-1, 2), entropy_vector(tuple(x-y for x,y in zip(p,q)))))


def decomposition(gp, gm, h, dimension, coordinate):
    a = tuple(Fraction(x+y, 2) for x,y in zip(gp,gm))
    b = tuple(Fraction(x-y, 2) for x,y in zip(gp,gm))
    a0,a1 = split(a,dimension,coordinate)
    b0,b1 = split(b,dimension,coordinate)
    r,s = split(h,dimension,coordinate)
    A=tuple(x+y*z for x,y,z in zip(a0,r,b0))
    B=tuple(x+y*z for x,y,z in zip(a1,r,b1))
    C=tuple(x*y for x,y in zip(s,b1))
    D=tuple(x*y for x,y in zip(s,b0))
    u=tuple(x+y for x,y in zip(A,C))
    v=tuple(x+y for x,y in zip(B,D))
    source=kernel_form(A,B)
    crossed=kernel_form(C,D)
    total=kernel_form(u,v)
    omega=add_vectors((1,total),(-1,source),(-1,crossed))
    qmass=sum(x*x for x in walsh(b))
    child=kernel_form(r,s)
    remainder=add_vectors((1,omega),(-qmass,child))
    reconstructed=add_vectors((1,source),(1,crossed),(qmass,child),(1,remainder))
    F=tuple(gp[j] if h[j]==1 else gm[j] for j in range(1<<dimension))
    direct=add_vectors((1,entropy_vector(F)),
                       (Fraction(-1,2),entropy_vector(restrict(F,dimension,coordinate,0))),
                       (Fraction(-1,2),entropy_vector(restrict(F,dimension,coordinate,1))))
    assert total == direct == reconstructed
    return source,crossed,child,remainder,total,qmass


def bits(mask,N):
    return tuple(1 if (mask>>j)&1 else -1 for j in range(N))


def main():
    # Exhaustively verify the exact identity for all Boolean triples through n=2.
    checked=0
    for n in (1,2):
        N=1<<n
        for x,y,z in product(range(1<<N),repeat=3):
            gp,gm,h=bits(x,N),bits(y,N),bits(z,N)
            for i in range(n):
                decomposition(gp,gm,h,n,i)
                checked+=1

    # Previously archived activation-irreducible constant-output witness.
    gp=(1,1,-1,1,-1,1,-1,-1)
    gm=(-1,1,1,1,1,1,1,1)
    h=(1,-1,-1,-1,-1,-1,-1,-1)
    terms=decomposition(gp,gm,h,3,0)
    assert terms[4] == {}
    assert add_vectors((1,terms[0]),(1,terms[1]),(terms[5],terms[2]),(1,terms[3])) == {}

    # Disjoint child-query control: source branches are independent of both
    # child bits.  Then the source and crossed channels vanish and R_sh is
    # exactly D_i(F)-qD_i(h), the prior biased coherent remainder.
    gp_d=(-1,-1,-1,-1,1,1,1,1)
    gm_d=(1,1,1,1,1,1,1,1)
    h_d=(-1,1,1,-1,-1,1,1,-1)
    disjoint=decomposition(gp_d,gm_d,h_d,3,0)
    assert disjoint[0] == disjoint[1] == {}

    # Activation-irreducible falsifier for the tempting Bellman inequality
    # R_sh <= Delta{C_*qI+VZ}.  Both selector signs occur on disagreement.
    gp2=(-1,-1,1,1,-1,-1,1,-1)
    gm2=(-1,-1,-1,1,-1,-1,-1,-1)
    h2=(-1,-1,1,-1,-1,1,-1,1)
    source,crossed,child,remainder,total,qmass=decomposition(gp2,gm2,h2,3,1)
    support=[j for j in range(8) if gp2[j] != gm2[j]]
    assert support == [2,6] and {h2[j] for j in support} == {-1,1}
    assert source == {2:Fraction(15,4),5:Fraction(-25,32),3:Fraction(-9,32)}
    assert crossed == {2:Fraction(1,4)}
    assert child == {2:Fraction(3),3:Fraction(-9,8)}
    assert remainder == {2:Fraction(-11,4),5:Fraction(25,32),3:Fraction(9,16)}
    assert total == {2:Fraction(2)} and qmass == Fraction(1,4)
    delta_qi,delta_vz=potential_drops(gp2,gm2,h2,3,1)
    assert delta_qi == Fraction(-1,16)
    assert delta_vz == {2:Fraction(7,16)}

    # Rigorous separation.  Since e>sum_{k=0}^5 1/k!=163/60 and
    # 163*5^25*3^18 > 60*2^88, we have 32R_sh=ln(5^25 3^18/2^88)>-1.
    num=5**25*3**18
    den=2**88
    assert 163*num > 60*den
    # Also exp(7/10)>sum_{k=0}^4(7/10)^k/k!>2, hence ln2<7/10.
    # Write the factorials explicitly to keep the certificate transparent.
    exp_partial=(Fraction(1)+Fraction(7,10)+Fraction(49,200)
                 +Fraction(343,6000)+Fraction(2401,240000))
    assert exp_partial > 2
    # Therefore R_sh>-1/32, while for C_*=4+2ln2+2/e,
    # Delta P=-1/4-1/(8e)+(5/16)ln2<-1/32.
    rdec=decimal(remainder)
    cstar=Decimal(4)+2*Decimal(2).ln()+2/Decimal(1).exp()
    installed_drop=-cstar/Decimal(16)+Decimal(7)*Decimal(2).ln()/Decimal(16)
    assert rdec > -Decimal(1)/32 > installed_drop

    print('PASS')
    print('exhaustive_identity_cases=',checked)
    print('archived_constant_output_total=0')
    print('archived_terms_decimal=',*[str(decimal(v)) for v in terms[:5]])
    print('disjoint_source_and_crossed_channels=0')
    print('falsifier_disagreement_support=',support)
    print('falsifier_selector_signs=',sorted({h2[j] for j in support}))
    print('falsifier_source_decimal=',decimal(source))
    print('falsifier_crossed_decimal=',decimal(crossed))
    print('falsifier_child_decimal=',decimal(child))
    print('falsifier_Rsh_decimal=',rdec)
    print('falsifier_Delta_qI=-1/16')
    print('falsifier_Delta_VZ=(7/16)ln2')
    print('installed_potential_drop=',installed_drop)
    print('Rsh_minus_installed_drop=',rdec-installed_drop)
    print('exact_separation=Rsh>-1/32>installed_drop')
    print('integer_certificate=163*5^25*3^18 > 60*2^88')
    print('random_seed=NONE')


if __name__=='__main__':
    main()
