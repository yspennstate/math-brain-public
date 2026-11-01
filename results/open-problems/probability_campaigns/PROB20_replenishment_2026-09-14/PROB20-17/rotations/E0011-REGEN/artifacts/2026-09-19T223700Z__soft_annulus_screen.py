#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

DIRS=((1,0),(-1,0),(0,1),(0,-1))

def vacant_edges(V):
    V=set(V)
    return sum(((x+1,y) in V)+((x,y+1) in V) for x,y in V)

def rect_annulus(a,b):
    O=set(); V=set()
    for x in range(a):
        for y in range(b):
            if x in (0,a-1) or y in (0,b-1):
                V.add((x,y))
            else:
                O.add((x,y))
    return frozenset(O),frozenset(V)

def poison_probability(a,b):
    O0,V0=rect_annulus(a,b)
    @lru_cache(None)
    def P(O,V):
        O=set(O); V=set(V)
        if not O and not V:
            return Fraction(1)
        e=vacant_edges(V)
        total=2*len(V)+e
        ans=Fraction(0)
        for v in sorted(V):
            neighO=[(v[0]+dx,v[1]+dy) for dx,dy in DIRS
                    if (v[0]+dx,v[1]+dy) in O]
            if neighO:
                for u in neighO:
                    ans += Fraction(2,total*len(neighO))*P(
                        frozenset(O-{u}),frozenset(V|{u}))
            else:
                ans += Fraction(2,total)*P(frozenset(O),frozenset(V-{v}))
        return ans
    val=P(O0,V0)
    return val,P.cache_info().currsize

def immediate_retry(P):
    r_adj=Fraction(8,(3*P+7)*(3*P+3))
    r_sep=Fraction(8,(3*P+6)*(3*P+3))
    R=Fraction(P-4,3*P)*r_adj + Fraction(4,3*P)*r_sep
    return r_adj,r_sep,R

def main():
    print('E0011 exact soft-annulus rectangle screen')
    vals={}
    for a,b in ((3,3),(3,4),(3,5),(4,4)):
        O,V=rect_annulus(a,b)
        Pn=len(V)
        assert vacant_edges(V)==Pn==2*a+2*b-4
        poison,states=poison_probability(a,b)
        vals[(a,b)]=poison
        radj,rsep,R=immediate_retry(Pn)
        print(f'{a}x{b}: P={Pn} O={len(O)} states={states}')
        print(f'  poison={poison.numerator}/{poison.denominator}')
        print(f'  poison_decimal={float(poison):.15f}')
        print(f'  poison_vs_1_64={"LT" if poison<Fraction(1,64) else "GT" if poison>Fraction(1,64) else "EQ"}')
        print(f'  r_adj={radj.numerator}/{radj.denominator}')
        print(f'  r_sep={rsep.numerator}/{rsep.denominator}')
        print(f'  immediate_retry={R.numerator}/{R.denominator}')
        print(f'  immediate_retry_decimal={float(R):.15f}')
    assert vals[(3,3)]>Fraction(1,64)
    assert vals[(3,4)]>Fraction(1,64)
    assert vals[(3,5)]<Fraction(1,64)
    assert vals[(4,4)]<Fraction(1,64)
    assert vals[(4,4)]<vals[(3,5)]
    assert immediate_retry(12)[2]==Fraction(508,316953)
    ratio=vals[(3,5)]/vals[(4,4)]
    print(f'perimeter12_poison_ratio_3x5_over_4x4={float(ratio):.15f}')
    print('CHECKS_PASS')

if __name__=='__main__':
    main()
