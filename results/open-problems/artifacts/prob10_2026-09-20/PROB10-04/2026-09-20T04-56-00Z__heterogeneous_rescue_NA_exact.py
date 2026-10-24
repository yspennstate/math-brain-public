from fractions import Fraction
from itertools import combinations, permutations
from math import prod

def falling(x, r):
    z = 1
    for k in range(r):
        z *= x-k
    return z

def brute_case(P,Q,U,B,L,E,centers):
    """Exact exhaustive check of the three-matching completion model.

    ps layer: Q marked/safe target slots among P, represented by a uniform Q-subset
              of source ps copies.
    nu layer: full uniform permutation source->target among U target slots;
              target labels 0,...,B-1 are canonical blocker slots.
    ns1 layer: E marked leaf copies induce a uniform E-subset of L target ns1 slots;
               target labels 0,...,B-1 are the ns1 slots belonging to canonical blockers.

    centers is a list (i,j), with pairwise-disjoint consecutive source blocks.
    """
    ps_blocks, nu_blocks = [], []
    ip = iu = 0
    for i,j in centers:
        ps_blocks.append(tuple(range(ip,ip+i)))
        nu_blocks.append(tuple(range(iu,iu+j)))
        ip += i
        iu += j
    assert ip <= P and iu <= U and B <= L

    total = free = 0
    for ps_tuple in combinations(range(P),Q):
        ps_set = set(ps_tuple)
        A = [all(x in ps_set for x in block) for block in ps_blocks]
        for nu_perm in permutations(range(U)):
            for leaf_tuple in combinations(range(L),E):
                leaf_set = set(leaf_tuple)
                total += 1
                completed = False
                for c,(i,j) in enumerate(centers):
                    if not A[c]:
                        continue
                    labels = [nu_perm[x] for x in nu_blocks[c]]
                    if all(y < B for y in labels) and all(y in leaf_set for y in labels):
                        completed = True
                        break
                if not completed:
                    free += 1

    lhs = Fraction(free,total)
    rhs = Fraction(1,1)
    for i,j in centers:
        a = Fraction(falling(Q,i),falling(P,i)) if Q >= i else Fraction(0,1)
        b = Fraction(falling(B,j),falling(U,j)) if B >= j else Fraction(0,1)
        e = Fraction(falling(E,j),falling(L,j)) if E >= j else Fraction(0,1)
        rhs *= 1-a*b*e
    return lhs,rhs,total

CASES = [
    (3,2,4,3,4,3,[(1,2)]),
    (4,3,5,4,5,4,[(1,2),(1,2)]),
    (5,3,5,4,5,4,[(1,2),(2,2)]),
    (5,4,5,4,5,4,[(1,2),(1,3)]),
    (5,3,6,4,5,3,[(1,2),(2,2)]),
    (5,4,6,5,6,4,[(1,2),(2,2)]),
    (4,2,5,3,5,3,[(1,2),(1,2)]),
    (5,4,5,3,5,4,[(2,2),(1,2)]),
]

checks = 0
for idx,case in enumerate(CASES,1):
    lhs,rhs,total = brute_case(*case)
    ok = lhs <= rhs
    checks += 1
    print(f"CASE {idx}: configurations={total}")
    print(f"  lhs_exact={lhs} ~= {float(lhs):.15g}")
    print(f"  rhs_exact={rhs} ~= {float(rhs):.15g}")
    print(f"  PASS={ok}")
    assert ok

print(f"EXACT_HETEROGENEOUS_CASES_CHECKED = {checks}")
print("ALL_EXACT_NA_RESCUE_CHECKS_PASS = True")
