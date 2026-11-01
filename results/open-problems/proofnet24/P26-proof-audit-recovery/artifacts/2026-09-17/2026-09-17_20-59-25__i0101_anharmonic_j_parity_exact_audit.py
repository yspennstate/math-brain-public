#!/usr/bin/env python3
"""Independent exact P26 audit checker for P04-I0101-ANHARMONIC-J-PARITY-23.

Purpose:
  * verify the polynomial factorization over Z[x,y];
  * verify the free S3 orbit/J-label/parity theorem for every prime p<1000
    with p == 5 (mod 24), using exact finite-field arithmetic;
  * deliberately break the symmetry at p=73 == 1 (mod 24) and exhibit the
    exceptional size-2 and size-3 orbits, confirming the congruence hypothesis
    is doing real work;
  * distinguish k (per-vertex cross-orbit valency) from the total number 6k
    of cross-orbit edges.

No floating-point arithmetic is used.
"""
import sympy as sp

x, y = sp.symbols("x y")
N = lambda z: (z*z-z+1)**3
D = lambda z: z*z*(1-z)**2
rhs = ((x-y)*(x*y-1)*(x+y-1)*(x*y-x+1)*(x*y-x-y)*(x*y-y+1))
assert sp.Poly(sp.expand(N(x)*D(y)-N(y)*D(x)-rhs), x, y).is_zero

def chi(a,p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a,(p-1)//2,p) == 1 else -1

def J(a,p):
    num = pow((a*a-a+1) % p, 3, p)
    den = (a*a*(1-a)*(1-a)) % p
    return num * pow(den,-1,p) % p

def orbit(a,p):
    seen=set()
    stack=[a]
    while stack:
        z=stack.pop()
        if z in seen:
            continue
        seen.add(z)
        stack.append((1-z) % p)
        stack.append(pow(z,-1,p))
    return seen

def Vset(p):
    return {a for a in range(2,p) if chi(a,p)==1 and chi(a-1,p)==1}

def partition(V,p):
    seen=set()
    out=[]
    for a in sorted(V):
        if a in seen:
            continue
        o=orbit(a,p)
        assert o <= V
        seen |= o
        out.append(o)
    assert seen == V
    return out

good=[]
for p in list(sp.primerange(5,1000)):
    if p % 24 != 5:
        continue
    V=Vset(p)
    O=partition(V,p)
    assert len(V) == (p-5)//4
    assert all(len(o)==6 for o in O)
    assert len(O) == (p-5)//24
    reps=[min(o) for o in O]
    labels=[J(a,p) for a in reps]
    assert len(set(labels)) == len(labels)
    for a,o in zip(reps,O):
        assert all(J(z,p)==J(a,p) for z in o)
    for i,a in enumerate(reps):
        for j,b in enumerate(reps):
            if i >= j:
                continue
            signs=[chi(a-z,p) for z in O[j]]
            assert all(s in (-1,1) for s in signs)
            k=sum(s==1 for s in signs)
            prod=sp.prod(signs)
            lhs=chi(J(a,p)-J(b,p),p)
            assert lhs == prod == (-1)**k

            # Since the S3 action is by Paley automorphisms, every vertex of
            # O[i] has the same k neighbors in O[j]; total cross-block edges
            # are therefore 6*k.  Check this directly.
            kvals=[]
            for u in O[i]:
                kvals.append(sum(chi(u-v,p)==1 for v in O[j]))
            assert len(set(kvals)) == 1 and kvals[0] == k
            total=sum(chi(u-v,p)==1 for u in O[i] for v in O[j])
            assert total == 6*k
    good.append((p,len(V),len(O)))

# Symmetry-breaking falsification outside the theorem's congruence class.
p=73
assert p % 24 == 1
V=Vset(p)
O=partition(V,p)
sizes=sorted(len(o) for o in O)
exceptional=[sorted(o) for o in O if len(o)<6]
assert sizes == [2,3,6,6]
assert sorted(exceptional) == [[2,37,72],[9,65]]

print("P26-I0101-ANHARMONIC-J-PARITY-INDEPENDENT-EXACT-AUDIT: PASS")
print("POLYNOMIAL_FACTOR_IDENTITY: PASS")
print("GOOD_PRIMES_LT_1000:", good)
print("P73_SYMMETRY_BREAK_ORBIT_SIZES:", sizes)
print("P73_EXCEPTIONAL_ORBITS:", exceptional)
print("K_IS_ROW_VALENCY_TOTAL_CROSS_EDGES_IS_6K: PASS")
print("FLOATING_POINT_USED: NO")
