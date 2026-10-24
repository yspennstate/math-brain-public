#!/usr/bin/env python3
"""
Exact certificate for R06 / Romero split reliability / first source-new
max-minus-four class T_{9,32}.

Terminals are 0,1.  By the terminal-edge swap lemma, it is enough to
consider graphs whose missing-edge set contains {0,1}.  The other three
missing edges form D.  Since D has at most six nonterminal endpoints,
all terminal-isomorphism types stabilize already on vertices 0,...,7.
We quotient D by S_6 on nonterminals and swapping the two terminals,
then compute the complete exact split-reliability coefficient vector
for one representative of each type at n=9.

All arithmetic is integer arithmetic.
"""
from itertools import combinations, permutations
from math import comb
from collections import Counter

CORE_N = 8
N = 9
S,T = 0,1

def all_edges(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def norm_edge(a,b):
    return (a,b) if a<b else (b,a)

CORE_EDGES = all_edges(CORE_N)
CORE_ALLOWED = [e for e in CORE_EDGES if e != (0,1)]

# S_6 acting on vertices 2,...,7, together with optional swap 0<->1.
NONTERMS = list(range(2,8))
ACTIONS = []
for perm in permutations(NONTERMS):
    base = {0:0,1:1}
    base.update({NONTERMS[i]:perm[i] for i in range(6)})
    ACTIONS.append(base)
    sw = dict(base)
    sw[0], sw[1] = 1,0
    ACTIONS.append(sw)

def act_D(D, mp):
    return tuple(sorted(norm_edge(mp[a],mp[b]) for a,b in D))

def canon_D(D):
    D = tuple(sorted(D))
    return min(act_D(D,mp) for mp in ACTIONS)

# Exhaust all 3-edge defects D not using st on the stable 8-vertex core.
classes = {}
for D in combinations(CORE_ALLOWED,3):
    c = canon_D(D)
    classes[c] = classes.get(c,0)+1

assert sum(classes.values()) == comb(27,3) == 2925
assert len(classes) == 21

def deg_signature(D):
    deg = Counter()
    for a,b in D:
        deg[a]+=1; deg[b]+=1
    vals = sorted((v for v in deg.values() if v), reverse=True)
    # classify the abstract 3-edge graph
    if vals == [3,1,1,1]:
        return "S3"
    if vals == [2,2,1,1]:
        return "P4"
    if vals == [2,1,1,1,1]:
        return "P3+K2"
    if vals == [2,2,2]:
        return "K3"
    if vals == [1,1,1,1,1,1]:
        return "3K2"
    raise AssertionError((D,vals))

shape_counts = Counter(deg_signature(D) for D in classes)
assert shape_counts == Counter({"P3+K2":7,"P4":5,"S3":4,"3K2":3,"K3":2})

# Candidate: total missing graph is a 4-star centered at terminal 0.
Dstar = canon_D(((0,2),(0,3),(0,4)))
assert Dstar in classes

def graph_edges(n, missing):
    miss=set(map(tuple,missing))
    return [e for e in all_edges(n) if e not in miss]

def split_coeffs(n, missing, s=0, t=1):
    """
    Return N_j where N_j is the number of j-edge spanning subgraphs
    having exactly two connected components separating s and t.

    Exact recurrence for connected spanning-subgraph polynomial C_A(z):
      C_A(z) = (1+z)^{e(A)}
               - sum_{B proper subset A, r in B}
                   C_B(z) (1+z)^{e(A minus B)}.
    """
    E = graph_edges(n, missing)
    # internal edge counts for every vertex subset
    ecount = [0]*(1<<n)
    for mask in range(1<<n):
        c=0
        for a,b in E:
            if (mask>>a)&1 and (mask>>b)&1:
                c += 1
        ecount[mask]=c

    C = [None]*(1<<n)
    for size in range(1,n+1):
        for A in range(1,1<<n):
            if A.bit_count()!=size:
                continue
            eA=ecount[A]
            poly=[comb(eA,j) for j in range(eA+1)]
            r=(A & -A).bit_length()-1
            root=1<<r
            rest=A^root
            sub=rest
            while True:
                B=root|sub
                if B!=A:
                    U=A^B
                    cb=C[B]
                    eU=ecount[U]
                    need=len(cb)+eU
                    if len(poly)<need:
                        poly += [0]*(need-len(poly))
                    for i,ci in enumerate(cb):
                        if ci:
                            for j in range(eU+1):
                                poly[i+j] -= ci*comb(eU,j)
                if sub==0: break
                sub=(sub-1)&rest
            assert all(x>=0 for x in poly)
            while len(poly)>1 and poly[-1]==0:
                poly.pop()
            C[A]=poly

    ans=[0]*(len(E)+1)
    full=(1<<n)-1
    for A in range(1,full):
        if ((A>>s)&1) and not ((A>>t)&1):
            B=full^A
            ca,cb=C[A],C[B]
            for i,x in enumerate(ca):
                if x:
                    for j,y in enumerate(cb):
                        if y:
                            ans[i+j]+=x*y
    return ans

candidate_missing=((0,1),)+Dstar
cand=split_coeffs(N,candidate_missing)

violations=0
ties=0
min_pos=None
min_where=None
rows=[]
for D,multiplicity in sorted(classes.items()):
    vec=split_coeffs(N, ((0,1),)+D)
    bad=[j for j,(a,b) in enumerate(zip(cand,vec)) if b>a]
    if bad:
        violations += 1
    if vec==cand:
        ties += 1
    gaps=[(a-b,j) for j,(a,b) in enumerate(zip(cand,vec)) if a-b>0]
    if D!=Dstar and gaps:
        g,j=min(gaps)
        if min_pos is None or g<min_pos:
            min_pos,min_where=g,(D,j)
    rows.append((D,multiplicity,deg_signature(D),bad,vec==cand))

assert violations==0
assert ties==1
assert min_pos is not None

print("ROMERO max-minus-four exact certificate: first source-new class T_{9,32}")
print(f"stable_core_labeled_D={comb(27,3)}")
print(f"terminal_isomorphism_types={len(classes)}")
print("host_shape_type_counts=" +
      ",".join(f"{k}:{shape_counts[k]}" for k in ["S3","P4","P3+K2","K3","3K2"]))
print(f"candidate_D={Dstar}")
print(f"candidate_missing={candidate_missing}")
print(f"types_checked={len(rows)} coefficientwise_violations={violations} exact_ties={ties}")
print(f"smallest_positive_coefficient_gap={min_pos} at_j={min_where[1]} competitor_D={min_where[0]}")
print("candidate_split_coefficients=" + ",".join(map(str,cand)))
print("PASS: for every terminal-isomorphism type in T_{9,32},")
print("the 4-star-defect candidate dominates the exact split coefficient vector coefficientwise.")
print("Therefore K_9-{st,su,sv,sw} is uniformly most split reliable in T_{9,32}.")
