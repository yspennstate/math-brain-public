#!/usr/bin/env python3
"""Exact finite sanity checks for D0067 run 6 contact-fugacity pattern families.

The infinite claims (prefix-freeness for all k and joint properness of every
fixed two-end pair) are proved algebraically in the report. This script checks:
  * T_k/U_k/V_k are lattice SAWs for 1 <= k <= K;
  * their D4 orbits have size 8;
  * the union of all oriented patterns is prefix-free in this range;
  * root contact guarantees are at least 3,1,2 respectively.
"""
K = 30

D4 = (
    lambda x,y:( x, y),
    lambda x,y:(-y, x),
    lambda x,y:(-x,-y),
    lambda x,y:( y,-x),
    lambda x,y:(-x, y),
    lambda x,y:( x,-y),
    lambda x,y:( y, x),
    lambda x,y:(-y,-x),
)

def apply(path, g):
    f = D4[g]
    return tuple(f(x,y) for x,y in path)

def T(k):
    p=[(0,0)]
    p += [(j,0) for j in range(1,k+1)]
    p.append((k,1))
    p += [(j,1) for j in range(k-1,-1,-1)]
    p += [(-1,1),(-1,0),(-1,-1),(0,-1)]
    return tuple(p)

def U(k):
    p=[(0,0),(1,0),(1,1),(0,1),(0,2)]
    p += [(j,2) for j in range(1,k+1)]
    p.append((k,3))
    return tuple(p)

def V(k):
    p=[(0,0),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
    p += [(-j,0) for j in range(2,k+2)]
    p.append((-(k+1),1))
    return tuple(p)

def is_saw(p):
    return len(set(p)) == len(p) and all(
        abs(a-c)+abs(b-d)==1
        for (a,b),(c,d) in zip(p,p[1:])
    )

def root_extra_contacts(p):
    root=p[0]
    first=p[1]
    nbrs={(1,0),(-1,0),(0,1),(0,-1)}
    assert root==(0,0) and first in nbrs
    return len((set(p) & nbrs) - {first})

families=(("U",U,1),("V",V,2),("T",T,3))
items=[]
for name,fam,need in families:
    for k in range(1,K+1):
        p=fam(k)
        assert is_saw(p), (name,k,"not SAW")
        assert root_extra_contacts(p) >= need, (name,k,"contact failure")
        orb={apply(p,g) for g in range(8)}
        assert len(orb)==8, (name,k,"orbit not size 8")
        for g in range(8):
            items.append((name,k,g,apply(p,g)))

for i,(n1,k1,g1,p1) in enumerate(items):
    for j,(n2,k2,g2,p2) in enumerate(items):
        if i==j:
            continue
        m=min(len(p1),len(p2))
        assert p1[:m] != p2[:m], (
            "prefix collision",(n1,k1,g1),(n2,k2,g2)
        )

print("PASS")
print(f"K={K}")
print(f"oriented_patterns={len(items)}")
print("contact_guarantees=U:1,V:2,T:3")
print("all_SAW=True")
print("all_D4_orbits_size_8=True")
print("union_prefix_free=True")
