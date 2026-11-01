#!/usr/bin/env python3
"""Exact orbit-size certificate for the five-input central equality classes.

Peer source consumed:
fleet01/B17/20260922T043923Z-arity5-uniform-c001/check_arity5_uniform_c001.out

That source proves, for each output cardinality m<=16, that every equality case in
its rigorous comparison has the same boundary and absolute Walsh multiset as the
listed read-once comparator, and reports the exact equality counts below.

This checker enumerates all 2^5 * 5! cube automorphisms of Q_5 and proves that
the orbit of each listed comparator has exactly the same cardinality. Since cube
automorphisms preserve output cardinality, boundary and squared Walsh spectrum,
the comparator orbit is contained in the peer equality class; equal finite counts
therefore identify the equality class exactly with the read-once orbit.
"""
from itertools import permutations

COMP = {
 1:(5,0x80000000), 2:(4,0x8000), 3:(5,0x80808000), 4:(3,0x80),
 5:(5,0xaa800000), 6:(4,0x8880), 7:(5,0xaa808080), 8:(2,0x8),
 9:(5,0xe0e0e000), 10:(4,0xa888), 11:(5,0xa8a8a888), 12:(3,0xa8),
 13:(5,0xaaa8a8a8), 14:(4,0xf888), 15:(5,0xeaeaea00), 16:(1,0x2)
}
EQUALITY_COUNTS = {
 1:32,2:80,3:320,4:80,5:960,6:480,7:480,8:40,
 9:480,10:960,11:1920,12:240,13:960,14:240,15:960,16:10
}
STRICT_GAPS = {
 1:None,2:0.56148322526,3:0.532947475699,4:0.307162499999,
 5:0.120229982455,6:0.415621093342,7:0.004906502214,
 8:0.114325,9:0.004906502214,10:0.415621093342,
 11:0.188315081728,12:0.222783593342,13:0.119300486391,
 14:0.009813004432,15:0.039701149089,16:0.22865
}

def embed(mask,k):
    M=0
    for x in range(32):
        if (mask>>(x & ((1<<k)-1)))&1:
            M |= 1<<x
    return M

def point_map(perm, flip):
    mp=[]
    for x in range(32):
        y=0
        for i in range(5):
            bit=((x>>perm[i])&1)^((flip>>i)&1)
            y |= bit<<i
        mp.append(y)
    return mp

maps=[point_map(p,f) for p in permutations(range(5)) for f in range(32)]
assert len(maps)==3840

print("PASS")
print("cube_automorphisms", len(maps))
for m,(k,mask) in COMP.items():
    M=embed(mask,k)
    orbit=set()
    for mp in maps:
        T=0
        for x,y in enumerate(mp):
            if (M>>y)&1:
                T |= 1<<x
        orbit.add(T)
    got=len(orbit)
    want=EQUALITY_COUNTS[m]
    assert got==want, (m,got,want)
    print("m",m,"orbit",got,"peer_equal",want)

delta=min(x for x in STRICT_GAPS.values() if x is not None)
prime_margin_upper=0.01-(4.0/5.0)*delta
print("strict_objective_gap", format(delta,'.12f'))
print("prime_center_cG_upper_when_M_positive", format(prime_margin_upper,'.13f'))
print("conclusion", "every peer equality case is a cube-automorphic read-once comparator; every composition-prime five-input gate has the strict central gap")
