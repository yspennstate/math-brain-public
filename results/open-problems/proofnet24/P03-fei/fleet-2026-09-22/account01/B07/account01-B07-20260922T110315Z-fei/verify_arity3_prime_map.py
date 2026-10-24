#!/usr/bin/env python3
import itertools
import sympy as sp

p=sp.symbols("p")
PTS=list(itertools.product([0,1], repeat=3))
NONEMPTY=[frozenset(s) for r in range(1,4) for s in itertools.combinations(range(3),r)]

def value(mask,idx):
    return 1 if (mask>>idx)&1 else -1

def essential(mask,i):
    for idx,y in enumerate(PTS):
        yy=list(y); yy[i]=1-yy[i]
        j=PTS.index(tuple(yy))
        if value(mask,idx)!=value(mask,j): return True
    return False

def composition_prime(mask):
    # Exact project cofactor criterion specialized to n=3.
    for A in itertools.combinations(range(3),2):
        b=({0,1,2}-set(A)).pop()
        cofs=set()
        for a in itertools.product([0,1],repeat=2):
            yy=[0,0,0]
            for j,i in enumerate(A): yy[i]=a[j]
            vals=[]
            for xb in [0,1]:
                yy[b]=xb
                vals.append(value(mask,PTS.index(tuple(yy))))
            cofs.add(tuple(vals))
        if len(cofs)<=2: return False
    return True

def coeff_sq(mask,S):
    q=1-p
    num=0
    for idx,y in enumerate(PTS):
        prob=sp.prod(p if bit else q for bit in y)
        cen=sp.prod(y[i]-p for i in S)
        num += value(mask,idx)*prob*cen
    return sp.factor(sp.cancel(num**2/(p*q)**len(S)))

def torics(mask):
    w={S:coeff_sq(mask,S) for S in NONEMPTY}
    S=lambda *xs:frozenset(xs)
    es=[
      w[S(0,1)]*w[S(2)]-w[S(0,2)]*w[S(1)],
      w[S(0,1)]*w[S(2)]-w[S(1,2)]*w[S(0)],
      w[S(0,1,2)]*w[S(0)]-w[S(0,1)]*w[S(0,2)],
    ]
    nums=[sp.factor(sp.fraction(sp.cancel(e))[0]) for e in es]
    return w,nums

def divisible(poly,fac):
    if sp.expand(poly)==0: return True
    return sp.rem(sp.Poly(poly,p,domain=sp.QQ),sp.Poly(fac,p,domain=sp.QQ)).as_expr()==0

essential_masks=[m for m in range(256) if all(essential(m,i) for i in range(3))]
assert len(essential_masks)==218

factors=[
  2*p-1,
  8*p**2-8*p+1,
  2*p**2-1,
  2*p**2-4*p+1,
  18*p**2-24*p+7,
  2*p**2-6*p+3,
  18*p**2-12*p+1,
  2*p**2+2*p-1,
]

expected_prime={
 "2*p - 1":[],
 "8*p**2 - 8*p + 1":[23,232],
 "2*p**2 - 1":[61,91,103,152,164,194],
 "2*p**2 - 4*p + 1":[25,37,67,188,218,230],
 "18*p**2 - 24*p + 7":[22,233],
 "2*p**2 - 6*p + 3":[62,94,118,137,161,193],
 "18*p**2 - 12*p + 1":[104,151],
 "2*p**2 + 2*p - 1":[110,122,124,131,133,145],
}

for fac in factors:
    key=str(sp.factor(fac))
    candidates=[]
    for m in essential_masks:
        w,nums=torics(m)
        if all(divisible(e,fac) for e in nums):
            candidates.append(m)
            if key!="2*p - 1":
                # Each listed nonbalanced factor is irreducible over QQ.
                # If a Fourier square vanished at its algebraic root, its rational
                # numerator would be divisible by that factor. Assert this never occurs.
                for csq in w.values():
                    num=sp.fraction(sp.cancel(csq))[0]
                    assert not divisible(num,fac)
    primes=[m for m in candidates if composition_prime(m)]
    assert primes==expected_prime[key]
    print(key, "candidate_masks=",candidates)
    print(key, "composition_prime_masks=",primes)

print("PASS")
