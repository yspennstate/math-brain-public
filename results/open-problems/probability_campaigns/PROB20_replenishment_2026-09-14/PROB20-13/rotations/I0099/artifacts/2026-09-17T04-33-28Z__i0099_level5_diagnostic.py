#!/usr/bin/env python3
from itertools import combinations

MAXP=229

def primes_upto(n):
    out=[]
    for p in range(2,n+1):
        ok=True
        d=2
        while d*d<=p:
            if p%d==0:
                ok=False; break
            d+=1
        if ok: out.append(p)
    return out

def qrset(p):
    return {x*x%p for x in range(1,p)}

def chi(a,p,Q):
    a%=p
    if a==0: return 0
    return 1 if a in Q else -1

def q4bit(a,p):
    a%=p
    assert pow(a,(p-1)//2,p)==1
    v=pow(a,(p-1)//4,p)
    assert v in (1,p-1)
    return 0 if v==1 else 1

def is_clique(C,p,Q):
    return all((a-b)%p in Q for a,b in combinations(C,2))

def common_neighbors(C,p,Q):
    S=set(C)
    return sum(1 for x in range(p) if x not in S and all((x-a)%p in Q for a in C))

def common_nonneighbors(C,p,Q):
    S=set(C)
    return sum(1 for x in range(p) if x not in S and all((x-a)%p not in Q and (x-a)%p!=0 for a in C))

def curve_count(C,p,Q):
    s=0
    for x in range(p):
        f=1
        for a in C:
            f=f*((x-a)%p)%p
        s += chi(f,p,Q)
    # odd degree: one rational point at infinity; even degree, monic: two.
    return p + (1 if len(C)%2 else 2) + s

def normalized_five_cliques(p,Q):
    H=[x for x in range(2,p) if x in Q and (x-1)%p in Q]
    out=[]
    for a_i,c in enumerate(H):
        for b_i in range(a_i+1,len(H)):
            d=H[b_i]
            if (d-c)%p not in Q: continue
            for e in H[b_i+1:]:
                if (e-c)%p in Q and (e-d)%p in Q:
                    out.append((0,1,c,d,e))
    return out

# B3: the naive mod-4 lift is not determined by p mod 16 plus all five
# normalized quartic edge-class bits.
p=89; Q=qrset(p)
C1=(0,1,5,21); C2=(0,1,9,10)
assert is_clique(C1,p,Q) and is_clique(C2,p,Q)
def five_q4_bits(C,p):
    _,_,c,d=C
    return tuple(q4bit(a,p) for a in (c,1-c,d,1-d,d-c))
b1=five_q4_bits(C1,p); b2=five_q4_bits(C2,p)
t1=common_neighbors(C1,p,Q); t2=common_neighbors(C2,p,Q)
assert b1==b2==(1,0,1,1,0)
assert t1==3 and t2==5 and t1%4!=t2%4
print("B3_SAME_PRIME_LEVEL4_COUNTEREXAMPLE=PASS")
print(f"p=89 bits={b1} C1={C1} t4={t1} C2={C2} t4={t2}")

# Abstract parity linear system: proper intersections through size four leave
# the five-fold intersection bit z free. We verify the Möbius inversion.
subs=[]
for r in range(6):
    subs += [frozenset(s) for s in combinations(range(5),r)]

def atom_parities(eps,z):
    I={}
    for J in subs:
        r=len(J)
        if r==0: I[J]=0               # p-5 is even
        elif r==1: I[J]=0             # (p-1)/2 even
        elif r in (2,3,4): I[J]=eps
        else: I[J]=z
    atoms={}
    for J in sorted(subs,key=lambda S:-len(S)):
        v=I[J]
        for S,w in atoms.items():
            if len(S)>len(J) and J.issubset(S):
                v ^= w
        atoms[J]=v
    # Recover every intersection by zeta summation.
    for J in subs:
        rec=0
        for S,w in atoms.items():
            if J.issubset(S): rec ^= w
        assert rec==I[J]
    assert atoms[frozenset()] == (eps^z)  # t5 parity
    return atoms

for eps in (0,1):
    for z in (0,1):
        atom_parities(eps,z)
print("B12_LOW_ORDER_PARITY_SYSTEM_HAS_ONE_FREE_BIT=PASS")

# B29 exact five-clique cover identity and low-order intersection hierarchy.
total5=0
primes_with5=0
empirical_t5_even=True
max_t5=0
for p in [r for r in primes_upto(MAXP) if r%4==1]:
    Q=qrset(p)
    cliques=normalized_five_cliques(p,Q)
    if not cliques:
        continue
    primes_with5 += 1
    eps=((p-1)//4)&1
    local=0
    for C in cliques:
        assert is_clique(C,p,Q)
        # Proper nonneighbor intersection parities.
        for r in (1,2,3,4):
            for J in combinations(C,r):
                val=common_nonneighbors(J,p,Q)
                expected=0 if r==1 else eps
                assert val%2==expected, (p,C,J,val,expected)
        t5=common_neighbors(C,p,Q)
        i5=common_nonneighbors(C,p,Q)
        assert (t5&1)==(eps^(i5&1))

        # The 15 elliptic quotients (10 cubics + 5 quartics) plus the
        # genus-two quintic quotient give the exact genus-17 cover count.
        sum3=sum(curve_count(T,p,Q) for T in combinations(C,3))
        sum4=sum(curve_count(D,p,Q) for D in combinations(C,4))
        n5=curve_count(C,p,Q)
        assert 32*t5 == sum3+sum4+n5-15*p-111

        # Consequence of the previously established mod-8 XOR-weight law,
        # independently checked here by direct point count.
        assert (n5-(15-p))%16==0

        empirical_t5_even &= (t5%2==0)
        max_t5=max(max_t5,t5)
        local+=1
    total5 += local
    print(f"p={p} normalized_five_cliques={local} cover_identity=PASS proper_parities=PASS t5_even_observed={all(common_neighbors(C,p,Q)%2==0 for C in cliques)}")

assert empirical_t5_even
print(f"PRIMES_WITH_FIVE_CLIQUES={primes_with5}")
print(f"TOTAL_NORMALIZED_FIVE_CLIQUES={total5}")
print(f"MAX_T5_OBSERVED={max_t5}")
print("GENUS17_FIVE_CLIQUE_COVER_IDENTITY_ALL=PASS")
print("PROPER_INTERSECTION_PARITY_HIERARCHY_ALL=PASS")
print("GENUS2_POINT_COUNT_MOD16_ALL=PASS")
print("T5_EVEN_THROUGH_229=EMPIRICAL_PASS_NOT_THEOREM")
print("ALL_I0099_LEVEL5_DIAGNOSTIC_SELF_CHECKS_PASS")
