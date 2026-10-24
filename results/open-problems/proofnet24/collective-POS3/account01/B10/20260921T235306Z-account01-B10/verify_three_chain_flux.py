#!/usr/bin/env python3
from itertools import product, combinations
from collections import Counter


def closure(n, rel):
    m = [[False] * n for _ in range(n)]
    for a, b in rel:
        m[a][b] = True
    for k in range(n):
        for i in range(n):
            if m[i][k]:
                for j in range(n):
                    if m[k][j]:
                        m[i][j] = True
    assert not any(m[i][i] for i in range(n))
    return {(i, j) for i in range(n) for j in range(n) if m[i][j]}


def width(n, rel):
    def incomparable(a, b):
        return (a, b) not in rel and (b, a) not in rel
    ans = 1
    for r in range(2, n + 1):
        if any(all(incomparable(a, b) for a, b in combinations(S, 2))
               for S in combinations(range(n), r)):
            ans = r
    return ans


def enumerate_extensions(n, rel):
    pred = [set() for _ in range(n)]
    for a, b in rel:
        pred[b].add(a)
    out = []

    def rec(seq, rem):
        S = set(seq)
        if not rem:
            out.append(tuple(seq))
            return
        for x in sorted(rem):
            if pred[x] <= S:
                rec(seq + [x], rem - {x})

    rec([], set(range(n)))
    return out


def state_set(chains, u):
    S = set()
    for C, k in zip(chains, u):
        S.update(C[:k])
    return S


def ideal_states(chains, rel):
    dims = [len(C) for C in chains]
    out = set()
    for u in product(*[range(d + 1) for d in dims]):
        S = state_set(chains, u)
        if all(not (b in S and a not in S) for a, b in rel):
            out.add(u)
    return out


def path_counts(chains, rel):
    O = ideal_states(chains, rel)
    z = tuple(0 for _ in chains)
    t = tuple(len(C) for C in chains)
    F = {u: 0 for u in O}
    F[z] = 1
    for u in sorted(O, key=sum):
        if u == z:
            continue
        total = 0
        for r in range(len(chains)):
            if u[r]:
                v = list(u)
                v[r] -= 1
                v = tuple(v)
                if v in O:
                    total += F[v]
        F[u] = total
    R = {u: 0 for u in O}
    R[t] = 1
    for u in sorted(O, key=lambda x: -sum(x)):
        if u == t:
            continue
        total = 0
        for r, C in enumerate(chains):
            if u[r] < len(C):
                v = list(u)
                v[r] += 1
                v = tuple(v)
                if v in O:
                    total += R[v]
        R[u] = total
    return O, F, R


def edge_flux(chains, rel, chain_of_x, pos_x_1based, other_chain):
    O, F, R = path_counts(chains, rel)
    top = tuple(len(C) for C in chains)
    E = F[top]
    q = Counter()
    for u in O:
        if u[chain_of_x] != pos_x_1based - 1:
            continue
        v = list(u)
        v[chain_of_x] += 1
        v = tuple(v)
        if v in O:
            q[u[other_chain]] += F[u] * R[v]
    return E, dict(sorted(q.items()))


def insertion_counts_by_enumeration(exts, x, C):
    q = Counter()
    for L in exts:
        p = {z: i for i, z in enumerate(L)}
        q[sum(p[c] < p[x] for c in C)] += 1
    return dict(sorted(q.items()))


def projected_weights(exts, A, B):
    As, Bs = set(A), set(B)
    out = Counter()
    for L in exts:
        w = ''.join('A' if x in As else 'B'
                    for x in L if x in As or x in Bs)
        out[w] += 1
    return dict(sorted(out.items()))


def pair_count(exts, x, y):
    return sum(L.index(x) < L.index(y) for L in exts)


chains = [[0, 1], [2, 3], [4, 5]]

# Example A: true width three, and projecting away the third chain gives
# nonconstant lift multiplicities.
relA = closure(6, {(0, 1), (2, 3), (4, 5), (0, 2), (2, 4)})
extA = enumerate_extensions(6, relA)
EA, fluxA = edge_flux(chains, relA, 0, 2, 1)
enumA = insertion_counts_by_enumeration(extA, 1, chains[1])
weightsA = projected_weights(extA, chains[0], chains[1])
assert width(6, relA) == 3
assert len(extA) == EA == 15
assert fluxA == enumA == {0: 3, 1: 6, 2: 6}
assert weightsA == {'AABB': 3, 'ABAB': 6, 'ABBA': 6}
assert pair_count(extA, 1, 3) == 9
assert pair_count(extA, 1, 2) == 3
print('EXAMPLE_A width=3 extensions=15')
print('EXAMPLE_A projected_AB_lift_weights', weightsA)
print('EXAMPLE_A flux_x=1_vs_B', fluxA)
print('EXAMPLE_A P(1<3)=9/15=3/5; P(1<2)=3/15=1/5')

# Example B: insertion-slice counts need not be log-concave even in width three.
relB = closure(6, {(0, 1), (2, 3), (4, 5), (0, 3), (1, 3)})
extB = enumerate_extensions(6, relB)
EB, fluxB = edge_flux(chains, relB, 2, 1, 0)
enumB = insertion_counts_by_enumeration(extB, 4, chains[0])
assert width(6, relB) == 3
assert len(extB) == EB == 45
assert fluxB == enumB == {0: 19, 1: 14, 2: 12}
assert 14 * 14 < 19 * 12
assert pair_count(extB, 0, 4) == 26
print('EXAMPLE_B width=3 extensions=45')
print('EXAMPLE_B flux_x=4_vs_A', fluxB)
print('EXAMPLE_B log_concavity_fails: 14^2=196 < 19*12=228')
print('EXAMPLE_B P(0<4)=26/45; minority=19/45>1/3')

print('POS3_THREE_CHAIN_FLUX_CHECK_PASS')
