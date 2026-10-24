#!/usr/bin/env python3
"""Exact finite core for the D0072 S3*A5 witness.

This checker verifies only the finite facts used by the written proof:
(1) H=< (12) > is a non-normal index-3 subgroup of S3;
(2) the quotient/coset graph obtained from all nonidentity S3 elements is K3;
(3) [S3,S3]=A3 and [A5,A5]=A5, hence S3^ab=C2 and A5 is perfect.

The infinite free-product and GRR steps are theorem-sized and are proved/cited in the report.
No external packages are used.
"""
from itertools import permutations


def compose(p, q):
    """Composition p∘q for tuple permutations."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    r = [0] * len(p)
    for i, j in enumerate(p):
        r[j] = i
    return tuple(r)


def identity(n):
    return tuple(range(n))


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def subgroup(generators, n):
    e = identity(n)
    gens = list(generators) + [inverse(g) for g in generators]
    out = {e}
    stack = [e]
    while stack:
        x = stack.pop()
        for g in gens:
            y = compose(x, g)
            if y not in out:
                out.add(y)
                stack.append(y)
    return out


def commutator(a, b):
    return compose(compose(compose(inverse(a), inverse(b)), a), b)


S3 = set(permutations(range(3)))
A5 = {p for p in permutations(range(5)) if parity(p) == 0}
transposition_12 = (1, 0, 2)
H = subgroup([transposition_12], 3)

# Exact index / non-normality check.
assert len(S3) == 6
assert len(H) == 2
assert len(S3) // len(H) == 3
conjugates = []
for g in S3:
    gi = inverse(g)
    conjugates.append({compose(compose(g, h), gi) for h in H})
assert any(C != H for C in conjugates)
assert len({tuple(sorted(C)) for C in conjugates}) == 3

# Exact derived subgroups / abelianizations.
D3 = subgroup([commutator(a, b) for a in S3 for b in S3], 3)
D5 = subgroup([commutator(a, b) for a in A5 for b in A5], 5)
assert len(D3) == 3
assert len(D5) == 60
assert len(S3) // len(D3) == 2
assert len(A5) // len(D5) == 1

# Left cosets H g and the simple quotient graph induced by all nonidentity S3 generators.
unseen = set(S3)
cosets = []
while unseen:
    g = next(iter(unseen))
    C = {compose(h, g) for h in H}
    cosets.append(C)
    unseen -= C
assert len(cosets) == 3
assert all(len(C) == 2 for C in cosets)

nonidentity = S3 - {identity(3)}
adj = [[False] * 3 for _ in range(3)]
for i, C in enumerate(cosets):
    for x in C:
        for s in nonidentity:
            y = compose(x, s)
            for j, D in enumerate(cosets):
                if i != j and y in D:
                    adj[i][j] = True
assert all(adj[i][j] for i in range(3) for j in range(3) if i != j)

print("D0072 finite core: PASS")
print(f"|S3|={len(S3)}, |H|={len(H)}, [S3:H]={len(S3)//len(H)}")
print(f"H normal in S3? {all(C == H for C in conjugates)}")
print(f"number of conjugates of H={len({tuple(sorted(C)) for C in conjugates})}")
print(f"|[S3,S3]|={len(D3)}, |S3^ab|={len(S3)//len(D3)}")
print(f"|A5|={len(A5)}, |[A5,A5]|={len(D5)}, |A5^ab|={len(A5)//len(D5)}")
print("left-coset sizes=" + repr([len(C) for C in cosets]))
print("quotient adjacency matrix (loops suppressed):")
for row in adj:
    print(" ".join("1" if x else "0" for x in row))
print("quotient graph=K3: True")
print("ALL_EXACT_CHECKS_PASS")
