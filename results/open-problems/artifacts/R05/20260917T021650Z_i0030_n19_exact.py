#!/usr/bin/env python3
# Exact certificate for R05 / I0030 / order 19.
# Standard library only. All proof-relevant arithmetic is integral.

P = 19

def subgroup_generated(a):
    H = {1}
    x = 1
    while True:
        x = (x*a) % P
        H.add(x)
        if x == 1:
            break
    return frozenset(H)

def matmul(A,B):
    n=len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,a in enumerate(A[i]):
            if a:
                for j,b in enumerate(B[k]):
                    if b:
                        C[i][j]+=a*b
    return C

def cayley_adj(S):
    A=[[0]*P for _ in range(P)]
    for x in range(P):
        for s in S:
            A[x][(x+s)%P]=1
    return A

def connected(A):
    seen={0}
    stack=[0]
    while stack:
        v=stack.pop()
        for w,z in enumerate(A[v]):
            if z and w not in seen:
                seen.add(w); stack.append(w)
    return len(seen)==P

subs = sorted({subgroup_generated(a) for a in range(1,P)}, key=lambda H:(len(H),tuple(sorted(H))))
minus1=P-1
Hs=[H for H in subs if minus1 in H]
assert [len(H) for H in Hs] == [2,6,18]

# Enumerate all labelled affine arc-transitive inverse-closed connection sets H*s.
sets=set()
by_degree={}
for H in Hs:
    for s in range(1,P):
        S=frozenset((h*s)%P for h in H)
        assert frozenset((-x)%P for x in S)==S
        sets.add(S)
        by_degree.setdefault(len(S),set()).add(S)

assert {d:len(v) for d,v in by_degree.items()} == {2:9,6:3,18:1}
assert len(sets)==13

# Collapse by additive-group automorphisms x -> c x: one orbit for each degree.
canonical={}
for d,Ss in by_degree.items():
    reps=[]
    remaining=set(Ss)
    while remaining:
        S=next(iter(remaining))
        orb={frozenset((c*x)%P for x in S) for c in range(1,P)}
        reps.append(min(tuple(sorted(T)) for T in orb))
        remaining -= orb
    assert len(reps)==1
    canonical[d]=frozenset(reps[0])

# Verify each representative is simple, connected, d-regular and explicitly
# arc-transitive under affine maps x -> h*x+b (H transitive on S).
for d,S in sorted(canonical.items()):
    A=cayley_adj(S)
    assert all(A[i][i]==0 for i in range(P))
    assert all(A[i][j]==A[j][i] for i in range(P) for j in range(P))
    assert all(sum(row)==d for row in A)
    assert connected(A)

    Hmatch=None
    for H in Hs:
        if len(H)==d:
            if any(frozenset((h*s)%P for h in H)==S for s in S):
                Hmatch=H; break
    assert Hmatch is not None
    s0=next(iter(S))
    for x in range(P):
        for s in S:
            # h*s0=s and translation by x maps (0,s0) to (x,x+s).
            hs=[h for h in Hmatch if (h*s0)%P==s]
            assert hs

    # Exact walk-count homogeneity and heat-equation coefficient identity.
    M=[[1 if i==j else 0 for j in range(P)] for i in range(P)]
    for m in range(0,45):
        diag={M[i][i] for i in range(P)}
        edge={M[x][(x+s)%P] for x in range(P) for s in S}
        assert len(diag)==1
        assert len(edge)==1
        N=matmul(M,A)
        # (A^{m+1})_xx = d (A^m)_xy on every ordered edge.
        for x in range(P):
            for s in S:
                assert N[x][x] == d*M[x][(x+s)%P]
        M=N

print("prime",P)
print("subgroups_containing_minus1", [(len(H), sorted(H)) for H in Hs])
print("labelled_affine_connection_sets", len(sets))
print("labelled_sets_by_degree", {d:len(v) for d,v in sorted(by_degree.items())})
print("isomorphism_types", len(canonical))
print("valencies", sorted(canonical))
for d,S in sorted(canonical.items()):
    print("representative_degree_%d"%d, sorted(S))
print("walk_identity_checked_through_power",44)
print("metric_largest_fully_certified_vertex_count",19)
print("RESULT PASS")
