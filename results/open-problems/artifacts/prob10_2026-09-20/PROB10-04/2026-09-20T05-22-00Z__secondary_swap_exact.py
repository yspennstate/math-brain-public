from fractions import Fraction
from itertools import combinations, permutations

def falling(x,r):
    z=1
    for k in range(r): z*=x-k
    return z

def brute(P,Q,U,B,L,E,centers):
    ps_blocks=[]; nu_blocks=[]; ip=iu=0
    for i,j in centers:
        ps_blocks.append(tuple(range(ip,ip+i))); ip+=i
        nu_blocks.append(tuple(range(iu,iu+j))); iu+=j
    assert ip<=P and iu<=U and B<=L
    total=free=0
    for safe in combinations(range(P),Q):
        safe=set(safe)
        A=[all(x in safe for x in block) for block in ps_blocks]
        for perm in permutations(range(U)):
            for leaves in combinations(range(L),E):
                leaves=set(leaves); total+=1; completed=False
                for c,(i,j) in enumerate(centers):
                    if not A[c]: continue
                    labels=[perm[x] for x in nu_blocks[c]]
                    if all(y<B for y in labels) and all(y in leaves for y in labels):
                        completed=True; break
                if not completed: free+=1
    lhs=Fraction(free,total)
    rhs=Fraction(1,1)
    for i,j in centers:
        a=Fraction(falling(Q,i),falling(P,i)) if Q>=i else Fraction(0,1)
        b=Fraction(falling(B,j),falling(U,j)) if B>=j else Fraction(0,1)
        e=Fraction(falling(E,j),falling(L,j)) if E>=j else Fraction(0,1)
        rhs*=1-a*b*e
    return lhs,rhs,total

CASES=[
    (3,2,3,2,3,2,[(1,1)]),
    (4,3,4,3,4,2,[(1,1),(1,1)]),
    (5,4,4,3,4,3,[(1,1),(2,1)]),
    (6,4,5,3,5,3,[(1,1),(2,1),(1,1)]),
]
for n,case in enumerate(CASES,1):
    lhs,rhs,total=brute(*case)
    print(f"CASE {n}: configurations={total} lhs={lhs} rhs={rhs} PASS={lhs<=rhs}")
    assert lhs<=rhs
print(f"EXACT_SECONDARY_SWAP_CASES_CHECKED = {len(CASES)}")
print("ALL_EXACT_SECONDARY_SWAP_CHECKS_PASS = True")
