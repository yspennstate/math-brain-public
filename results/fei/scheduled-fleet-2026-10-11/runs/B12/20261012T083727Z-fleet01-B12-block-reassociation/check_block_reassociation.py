#!/usr/bin/env python3
"""Exact checks for the B12/A057 block-channel and reassociation laws.

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


def kernel_form(p, q):
    return add_vectors((1, entropy_vector(p)), (1, entropy_vector(q)),
                       (Fraction(-1, 2), entropy_vector(tuple(x+y for x,y in zip(p,q)))),
                       (Fraction(-1, 2), entropy_vector(tuple(x-y for x,y in zip(p,q)))))


def one_step_decomposition(gp, gm, h, dimension, coordinate):
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
    assert add_vectors((1,source),(1,crossed),(qmass,child),(1,remainder)) == total
    return source,crossed,child,remainder,total,qmass


def block_coeff_functions(values, dimension, coordinates):
    coordinates=tuple(coordinates)
    rest=tuple(i for i in range(dimension) if i not in coordinates)
    m=len(coordinates)
    out=[[Fraction(0) for _ in range(1<<len(rest))] for _ in range(1<<m)]
    for ridx in range(1<<len(rest)):
        for bmask in range(1<<m):
            idx=0
            for k,c in enumerate(rest):
                idx |= ((ridx>>k)&1)<<c
            for k,c in enumerate(coordinates):
                idx |= ((bmask>>k)&1)<<c
            value=Fraction(values[idx])
            for gamma in range(1<<m):
                sign=-1 if (gamma&bmask).bit_count()%2 else 1
                out[gamma][ridx] += sign*value/Fraction(1<<m)
    return tuple(tuple(x) for x in out)


def block_form(channels):
    m=(len(channels)).bit_length()-1
    total=add_vectors(*[(1,entropy_vector(x)) for x in channels])
    for bmask in range(1<<m):
        restricted=tuple(sum(((-1 if (gamma&bmask).bit_count()%2 else 1)
                              *channels[gamma][j])
                             for gamma in range(1<<m))
                         for j in range(len(channels[0])))
        total=add_vectors((1,total),(Fraction(-1,1<<m),entropy_vector(restricted)))
    return total


def block_decomposition(gp,gm,h,n,coordinates):
    a=tuple(Fraction(x+y,2) for x,y in zip(gp,gm))
    b=tuple(Fraction(x-y,2) for x,y in zip(gp,gm))
    av=block_coeff_functions(a,n,coordinates)
    bv=block_coeff_functions(b,n,coordinates)
    hv=block_coeff_functions(h,n,coordinates)
    N=len(av)
    source=tuple(tuple(av[g][j]+hv[0][j]*bv[g][j]
                       for j in range(len(av[0]))) for g in range(N))
    selector_channels=[]
    for alpha in range(1,N):
        selector_channels.append(tuple(tuple(hv[alpha][j]*bv[g^alpha][j]
                                                    for j in range(len(av[0])))
                                             for g in range(N)))
    fchannels=tuple(tuple(source[g][j]+sum(c[g][j] for c in selector_channels)
                          for j in range(len(av[0]))) for g in range(N))
    S=block_form(source)
    Xs=[block_form(c) for c in selector_channels]
    total=block_form(fchannels)
    omega=add_vectors((1,total),(-1,S),*[(-1,x) for x in Xs])
    q=sum(x*x for x in walsh(b))
    child=block_form(hv)
    R=add_vectors((1,omega),(-q,child))
    assert add_vectors((1,S),*[(1,x) for x in Xs],(q,child),(1,R)) == total
    return S,Xs,child,R,total,q


def sequential_two(gp,gm,h,n,i,j):
    root=one_step_decomposition(gp,gm,h,n,i)
    source_crossed=add_vectors((1,root[0]),(1,root[1]))
    qchild=add_vectors((root[5],root[2]))
    remainder=root[3]
    total=root[4]
    jj=j-1 if j>i else j
    for bit in (0,1):
        gp1=restrict(gp,n,i,bit)
        gm1=restrict(gm,n,i,bit)
        h1=restrict(h,n,i,bit)
        child=one_step_decomposition(gp1,gm1,h1,n-1,jj)
        source_crossed=add_vectors((1,source_crossed),
                                   (Fraction(1,2),child[0]),
                                   (Fraction(1,2),child[1]))
        qchild=add_vectors((1,qchild),(child[5]/2,child[2]))
        remainder=add_vectors((1,remainder),(Fraction(1,2),child[3]))
        total=add_vectors((1,total),(Fraction(1,2),child[4]))
    return source_crossed,qchild,remainder,total


def composed_values(gp,gm,h):
    return tuple(Fraction(x+y,2)+Fraction(z*(x-y),2)
                 for x,y,z in zip(gp,gm,h))


def main():
    functions=list(product((-1,1),repeat=4))
    triples=0
    nonzero_transfer=0
    order_dependent=0
    activation_irreducible_order_dependent=0
    for gp in functions:
        for gm in functions:
            for h in functions:
                triples += 1
                block=block_decomposition(gp,gm,h,2,(0,1))
                block_sc=add_vectors((1,block[0]),*[(1,x) for x in block[1]])
                block_cr=add_vectors((block[5],block[2]),(1,block[3]))
                transfers=[]
                for order in ((0,1),(1,0)):
                    seq=sequential_two(gp,gm,h,2,*order)
                    assert seq[3] == block[4]
                    transfer=add_vectors((1,seq[0]),(-1,block_sc))
                    assert add_vectors((1,seq[1]),(1,seq[2]),
                                       (-1,block_cr),(1,transfer)) == {}
                    transfers.append(transfer)
                if any(transfers):
                    nonzero_transfer += 1
                if transfers[0] != transfers[1]:
                    order_dependent += 1
                    disagreement=[k for k,(x,y) in enumerate(zip(gp,gm)) if x != y]
                    if disagreement and {h[k] for k in disagreement} == {-1,1}:
                        activation_irreducible_order_dependent += 1

    gp=(-1,-1,-1,-1)
    gm=(-1,-1,1,1)
    h=(-1,-1,-1,1)
    block=block_decomposition(gp,gm,h,2,(0,1))
    block_sc=add_vectors((1,block[0]),*[(1,x) for x in block[1]])
    seq01=sequential_two(gp,gm,h,2,0,1)
    seq10=sequential_two(gp,gm,h,2,1,0)
    transfer01=add_vectors((1,seq01[0]),(-1,block_sc))
    transfer10=add_vectors((1,seq10[0]),(-1,block_sc))
    tau={2:Fraction(-2),3:Fraction(9,8)}
    assert composed_values(gp,gm,h) == (-1,-1,1,-1)
    assert [k for k in range(4) if gp[k] != gm[k]] == [2,3]
    assert {h[2],h[3]} == {-1,1}
    assert block[0] == {2:Fraction(9,4),3:Fraction(-9,8)}
    assert block[1] == [{2:Fraction(1,4)}]*3
    assert block[2] == {2:Fraction(2)} and block[5] == Fraction(1,2)
    assert block[3] == tau and block[4] == {2:Fraction(2)}
    assert seq01[0] == {2:Fraction(1)}
    assert seq01[1] == {2:Fraction(1)} and seq01[2] == {}
    assert seq10[0] == block_sc
    assert seq10[1] == {2:Fraction(1)} and seq10[2] == tau
    assert transfer01 == tau and transfer10 == {}
    assert 3**9 < 2**16  # tau=(1/8)ln(3^9/2^16)<0.

    print('PASS')
    print('exhaustive_n2_boolean_triples=',triples)
    print('nonzero_reassociation_transfer=',nonzero_transfer)
    print('order_dependent_transfer=',order_dependent)
    print('activation_irreducible_order_dependent=',activation_irreducible_order_dependent)
    print('witness_g_plus=',gp)
    print('witness_g_minus=',gm)
    print('witness_h=',h)
    print('witness_F=',composed_values(gp,gm,h))
    print('witness_disagreement_support=[2, 3]')
    print('witness_selector_signs=[-1, 1]')
    print('block_source=',block[0])
    print('block_selector_channels=',block[1])
    print('block_child=',block[2],'q=',block[5])
    print('block_remainder=',block[3],'decimal=',decimal(block[3]))
    print('block_total=',block[4],'decimal=',decimal(block[4]))
    print('order_01_transfer=',transfer01,'decimal=',decimal(transfer01))
    print('order_10_transfer=',transfer10,'decimal=',decimal(transfer10))
    print('sign_certificate=3^9 < 2^16')
    print('random_seed=NONE')


if __name__=='__main__':
    main()
