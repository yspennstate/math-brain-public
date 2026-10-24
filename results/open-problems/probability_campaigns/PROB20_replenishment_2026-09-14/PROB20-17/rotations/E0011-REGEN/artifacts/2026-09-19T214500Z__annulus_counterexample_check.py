#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

DIRS=((1,0),(-1,0),(0,1),(0,-1))

def vacant_edges(V):
    V=set(V)
    return sum(((x+1,y) in V)+((x,y+1) in V) for x,y in V)

def square_annulus(n):
    O=set()
    V=set()
    for x in range(n):
        for y in range(n):
            if x in (0,n-1) or y in (0,n-1):
                V.add((x,y))
            else:
                O.add((x,y))
    return frozenset(O), frozenset(V)

def co_only_poison_probability(O0,V0):
    @lru_cache(None)
    def P(O,V):
        O=set(O); V=set(V)
        if not O and not V:
            return Fraction(1)
        e=vacant_edges(V)
        # Multiply all p=1/2 rates by 4:
        # each CO clock has weight 2, each vacant-vacant O2 clock weight 1.
        total=2*len(V)+e
        assert total>0
        ans=Fraction(0)
        for v in sorted(V):
            neighO=[(v[0]+dx,v[1]+dy) for dx,dy in DIRS
                    if (v[0]+dx,v[1]+dy) in O]
            if neighO:
                # Incoming CO reacts with one adjacent O uniformly.
                # Landing site stays vacant and removed O site becomes vacant.
                for u in neighO:
                    ans += Fraction(2,total*len(neighO))*P(
                        frozenset(O-{u}), frozenset(V|{u}))
            else:
                # Incoming CO survives and fills v.
                ans += Fraction(2,total)*P(frozenset(O),frozenset(V-{v}))
        # Any O2 clock exits the CO-only poisoning subevent, contribution 0.
        return ans
    val=P(O0,V0)
    return val, P.cache_info().currsize

def first_o2_probability_on_square_ring(n):
    O,V=square_annulus(n)
    v=len(V); e=vacant_edges(V)
    # weights after multiplying rates by 4
    return Fraction(e,2*v+e),v,e

def main():
    print("E0011 neutral-annulus exact counterexample screen")
    for n in (3,4):
        O,V=square_annulus(n)
        p,states=co_only_poison_probability(O,V)
        first_o2,v,e=first_o2_probability_on_square_ring(n)
        print(f"n={n} O={len(O)} V={v} E00={e} V-E00={v-e}")
        print(f"  poison={p.numerator}/{p.denominator}")
        print(f"  poison_decimal={float(p):.15f}")
        print(f"  compare_1_64={'GT' if p>Fraction(1,64) else 'LT' if p<Fraction(1,64) else 'EQ'}")
        print(f"  optimistic_M_upper=1-64*poison={float(Fraction(1)-64*p):.15f}")
        print(f"  recursion_states={states}")
        print(f"  first_O2_probability={first_o2.numerator}/{first_o2.denominator}")
        assert v==e==4*(n-1)
        assert first_o2==Fraction(1,3)
    p3,_=co_only_poison_probability(*square_annulus(3))
    p4,_=co_only_poison_probability(*square_annulus(4))
    assert p3>Fraction(1,64)
    assert p4<Fraction(1,64)
    print("CHECKS_PASS")

if __name__=="__main__":
    main()
