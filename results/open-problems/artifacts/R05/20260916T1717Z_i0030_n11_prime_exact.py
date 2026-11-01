#!/usr/bin/env python3
# Exact finite certificate for R05 / Aldous-Fill Open Problem 7.30 metric extension to n=11.
# Finite core: classify all inverse-closed circulant connection sets on F_11 that are
# transitive under their affine multiplier stabilizer. The report supplies the group-theoretic
# reduction (Burnside prime-degree theorem) from every connected arc-transitive graph of order 11
# to either K_11 (2-transitive case) or one of these affine circulants.

p = 11
units = tuple(range(1,p))
pairs = ((1,10),(2,9),(3,8),(4,7),(5,6))

def mulset(a,S):
    return frozenset((a*s) % p for s in S)

def multiplier_stabilizer(S):
    return tuple(a for a in units if mulset(a,S) == S)

def orbit(H,s):
    return frozenset((a*s) % p for a in H)

def matmul(A,B):
    n=len(A); m=len(B); k=len(B[0])
    return [[sum(A[i][r]*B[r][j] for r in range(m)) for j in range(k)] for i in range(n)]

def adjacency(S):
    A=[[0]*p for _ in range(p)]
    for x in range(p):
        for s in S:
            A[x][(x+s)%p]=1
    assert all(A[i][j]==A[j][i] for i in range(p) for j in range(p))
    return A

def walk_identity(S,max_m=30):
    A=adjacency(S); d=len(S)
    M=[[int(i==j) for j in range(p)] for i in range(p)]
    s0=min(S)
    for m in range(max_m+1):
        AM=matmul(A,M)
        diag={M[x][x] for x in range(p)}
        edge={M[x][y] for x in range(p) for y in range(p) if A[x][y]}
        assert len(diag)==1
        assert len(edge)==1
        assert AM[0][0] == d*M[0][s0]
        M=AM
    return True

all_S=[]
for mask in range(1<<len(pairs)):
    S=set()
    for i,pr in enumerate(pairs):
        if (mask>>i)&1:
            S.update(pr)
    all_S.append(frozenset(S))
assert len(all_S)==32

nonempty=[S for S in all_S if S]
affine_arc=[]
for S in nonempty:
    H=multiplier_stabilizer(S)
    s0=min(S)
    if orbit(H,s0)==S:
        affine_arc.append((S,H))

assert len(affine_arc)==6
assert sorted(len(S) for S,H in affine_arc)==[2,2,2,2,2,10]
for S,H in affine_arc:
    assert (p-1) in H
    if len(S)==2:
        a=min(S)
        inv=pow(a,-1,p)
        assert mulset(inv,S)==frozenset((1,p-1))
    else:
        assert S==frozenset(units)
    walk_identity(S,30)

def is_subgroup(H):
    H=set(H)
    if 1 not in H: return False
    for a in H:
        if pow(a,-1,p) not in H: return False
        for b in H:
            if (a*b)%p not in H: return False
    return True
subgroups=[]
for mask in range(1<<len(units)):
    H={units[i] for i in range(len(units)) if (mask>>i)&1}
    if is_subgroup(H): subgroups.append(frozenset(H))
assert sorted(len(H) for H in subgroups)==[1,2,5,10]
minus_one_subgroups=[H for H in subgroups if p-1 in H]
assert sorted(len(H) for H in minus_one_subgroups)==[2,10]

print('R05 I0030 exact n=11 prime-order certificate')
print('p',p)
print('inverse_closed_connection_sets_total',len(all_S))
print('nonempty_inverse_closed_connection_sets',len(nonempty))
print('multiplicative_subgroup_orders',sorted(len(H) for H in subgroups))
print('subgroup_orders_containing_minus_one',sorted(len(H) for H in minus_one_subgroups))
print('affine_arc_transitive_labeled_connection_sets',len(affine_arc))
for S,H in sorted(affine_arc,key=lambda t:(len(t[0]),sorted(t[0]))):
    print('candidate degree',len(S),'S',sorted(S),'H',sorted(H))
print('isomorphism_types',2)
print('types','C11','K11')
print('walk_identity_exact_through_m',30)
print('oeis_A286280_connected_arc_transitive_count_n11_expected',2)
print('metric_largest_fully_certified_vertex_count',11)
print('RESULT PASS')
