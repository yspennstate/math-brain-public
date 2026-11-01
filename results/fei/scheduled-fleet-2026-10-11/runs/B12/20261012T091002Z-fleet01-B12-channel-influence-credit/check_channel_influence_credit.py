#!/usr/bin/env python3
"""Exact checks for the B12/A057 selector-channel collision credit.

All arithmetic is rational.  No randomness is used.
"""

from fractions import Fraction
from itertools import permutations, product


def walsh(values):
    a=[Fraction(x) for x in values]
    n=len(a)
    step=1
    while step<n:
        for base in range(0,n,2*step):
            for j in range(base,base+step):
                u,v=a[j],a[j+step]
                a[j],a[j+step]=u+v,u-v
        step*=2
    return tuple(x/n for x in a)


def influence(values):
    return sum(mask.bit_count()*x*x for mask,x in enumerate(walsh(values)))


def restrict(values,dimension,coordinate,bit):
    return tuple(values[j] for j in range(1<<dimension)
                 if ((j>>coordinate)&1)==bit)


def split(values,dimension,coordinate):
    plus=restrict(values,dimension,coordinate,0)
    minus=restrict(values,dimension,coordinate,1)
    return (tuple((Fraction(x)+Fraction(y))/2 for x,y in zip(plus,minus)),
            tuple((Fraction(x)-Fraction(y))/2 for x,y in zip(plus,minus)))


def full_block_stats(gp,gm,h,n):
    b=tuple(Fraction(x-y,2) for x,y in zip(gp,gm))
    bh=walsh(b)
    hh=walsh(h)
    N=1<<n
    q=sum(x*x for x in bh)
    variance=sum(hh[a]*hh[a] for a in range(1,N))
    selector_influence=sum(a.bit_count()*hh[a]*hh[a] for a in range(1,N))
    source_influence=sum(beta.bit_count()*bh[beta]*bh[beta]
                         for beta in range(N))
    overlap=sum((a&beta).bit_count()*hh[a]*hh[a]*bh[beta]*bh[beta]
                for a in range(1,N) for beta in range(N))
    channel_energy=sum(hh[a]*hh[a]*q for a in range(1,N))
    channel_influence=sum(
        hh[a]*hh[a]*sum((beta^a).bit_count()*bh[beta]*bh[beta]
                        for beta in range(N))
        for a in range(1,N)
    )
    gross=(variance*source_influence+selector_influence*q)
    assert channel_energy == variance*q
    assert channel_influence == gross-2*overlap
    assert channel_energy <= q
    assert channel_influence <= source_influence+selector_influence
    return {
        "q":q,
        "variance":variance,
        "selector_influence":selector_influence,
        "source_influence":source_influence,
        "overlap":overlap,
        "gross":gross,
        "channel_energy":channel_energy,
        "channel_influence":channel_influence,
    }


def local_singleton_channel_influence(b,h,n,coordinate):
    b0,_=split(b,n,coordinate)
    _,h1=split(h,n,coordinate)
    return sum((x*y)*(x*y) for x,y in zip(h1,b0))/len(b0)


def hierarchy_channel_influence(b,h,n,order):
    states=[(Fraction(1),b,h,n,tuple(range(n)))]
    total=Fraction(0)
    for original_coordinate in order:
        new_states=[]
        for weight,bv,hv,dimension,remaining in states:
            local_coordinate=remaining.index(original_coordinate)
            total += weight*local_singleton_channel_influence(
                bv,hv,dimension,local_coordinate)
            next_remaining=tuple(x for x in remaining if x!=original_coordinate)
            for bit in (0,1):
                new_states.append((
                    weight/2,
                    restrict(bv,dimension,local_coordinate,bit),
                    restrict(hv,dimension,local_coordinate,bit),
                    dimension-1,
                    next_remaining,
                ))
        states=new_states
    return total


def bits(mask,N):
    return tuple(1 if (mask>>j)&1 else -1 for j in range(N))


def universality_check(k):
    # Add a fresh fastest coordinate x.  Set h=x and b=x*k, so the unique
    # nonzero selector channel is x*b=k lifted independently of x.
    N=len(k)
    h=tuple(1 if (j&1)==0 else -1 for j in range(2*N))
    b=tuple(h[j]*k[j>>1] for j in range(2*N))
    hh=walsh(h)
    bh=walsh(b)
    assert hh[1]==1 and all(x==0 for j,x in enumerate(hh) if j!=1)
    channel_hat=tuple(bh[gamma^1] for gamma in range(2*N))
    lifted=tuple(k[j>>1] for j in range(2*N))
    assert channel_hat==walsh(lifted)
    assert influence(lifted)==influence(k)


def main():
    functions=list(product((-1,1),repeat=4))
    triples=0
    strict_refund=0
    full_refund=0
    hierarchy_checks=0
    hierarchy_equalities=0
    for gp in functions:
        for gm in functions:
            b=tuple(Fraction(x-y,2) for x,y in zip(gp,gm))
            for h in functions:
                triples+=1
                stats=full_block_stats(gp,gm,h,2)
                if stats["overlap"]>0:
                    strict_refund+=1
                if stats["gross"]>0 and stats["channel_influence"]==0:
                    full_refund+=1
                budget=influence(b)+influence(h)
                for order in permutations(range(2)):
                    hierarchy_checks+=1
                    value=hierarchy_channel_influence(b,h,2,order)
                    assert value<=budget
                    if value==budget:
                        hierarchy_equalities+=1

    # Exact parity-erasure control: b=h is one character.  The selector
    # shift moves its only source frequency to zero, refunding all gross
    # block influence.
    gp=(-1,-1,1,1)
    gm=(1,1,-1,-1)
    h=(-1,-1,1,1)
    witness=full_block_stats(gp,gm,h,2)
    assert witness=={
        "q":Fraction(1),
        "variance":Fraction(1),
        "selector_influence":Fraction(1),
        "source_influence":Fraction(1),
        "overlap":Fraction(1),
        "gross":Fraction(2),
        "channel_energy":Fraction(1),
        "channel_influence":Fraction(0),
    }

    universal_functions=0
    for n in range(4):
        N=1<<n
        for mask in range(1<<N):
            universality_check(bits(mask,N))
            universal_functions+=1

    print("PASS")
    print("exhaustive_n2_boolean_triples=",triples)
    print("strict_overlap_refund=",strict_refund)
    print("complete_parity_erasure=",full_refund)
    print("adaptive_two_order_checks=",hierarchy_checks)
    print("adaptive_budget_equalities=",hierarchy_equalities)
    print("parity_witness_g_plus=",gp)
    print("parity_witness_g_minus=",gm)
    print("parity_witness_h=",h)
    print("parity_witness_stats=",witness)
    print("universality_boolean_functions_through_n3=",universal_functions)
    print("random_seed=NONE")


if __name__=="__main__":
    main()
