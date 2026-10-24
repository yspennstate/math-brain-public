#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict


def is_forest(n, F):
    p = list(range(n))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    for u, v in F:
        a, b = find(u), find(v)
        if a == b:
            return False
        p[a] = b
    return True


def comp_index(n, F):
    p = list(range(n))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    for u, v in F:
        a, b = find(u), find(v)
        if a != b:
            p[a] = b
    return {x: find(x) for x in range(n)}


def path_edges(n, F, s, t):
    adj = defaultdict(list)
    for g in F:
        u, v = g
        adj[u].append((v, g))
        adj[v].append((u, g))
    stack = [s]
    prev = {s: (None, None)}
    while stack:
        x = stack.pop()
        if x == t:
            break
        for y, g in adj[x]:
            if y not in prev:
                prev[y] = (x, g)
                stack.append(y)
    assert t in prev
    out = set()
    x = t
    while x != s:
        x0, g = prev[x]
        out.add(g)
        x = x0
    return out


def all_forests(n, edges):
    out = []
    for mask in range(1 << len(edges)):
        F = frozenset(edges[i] for i in range(len(edges)) if (mask >> i) & 1)
        if is_forest(n, F):
            out.append(F)
    return out


def kappa(K, ci, mark):
    a, b = ci[mark[0]], ci[mark[1]]
    assert a != b
    target = frozenset((a, b))
    return sum(
        frozenset((ci[g[0]], ci[g[1]])) == target
        for g in K
    )


def transport_sums(n, G, e, f):
    K = tuple(g for g in G if g not in (e, f))
    classes = defaultdict(list)
    Q = set()
    for H in all_forests(n, K):
        ci = comp_index(n, H)
        xe = int(ci[e[0]] != ci[e[1]])
        yf = int(ci[f[0]] != ci[f[1]])
        classes[(xe, yf)].append(H)
        if xe and yf:
            pe = frozenset((ci[e[0]], ci[e[1]]))
            pf = frozenset((ci[f[0]], ci[f[1]]))
            if pe == pf:
                Q.add(H)

    A00 = classes[(0, 0)]
    A10 = classes[(1, 0)]
    A01 = classes[(0, 1)]
    A11 = classes[(1, 1)]
    D = [H for H in A11 if H not in Q]

    lhs1 = lhs2 = lhs3 = 0
    for R in A00:
        pe = path_edges(n, R, *e)
        pf = path_edges(n, R, *f)
        lhs1 += len(pe - pf)
        lhs2 += len(pf - pe)
        lhs3 += len(pe & pf)

    rhs1 = sum(kappa(K, comp_index(n, H), e) for H in A10)
    rhs2 = sum(kappa(K, comp_index(n, H), f) for H in A01)
    rhs3 = sum(kappa(K, comp_index(n, H), e) for H in Q)

    lhs4 = sum(len(path_edges(n, R, *e)) for R in A01)
    lhs5 = sum(len(path_edges(n, R, *f)) for R in A10)
    rhs4 = sum(kappa(K, comp_index(n, H), e) for H in D)
    rhs5 = sum(kappa(K, comp_index(n, H), f) for H in D)

    return (
        (lhs1, rhs1),
        (lhs2, rhs2),
        (lhs3, rhs3),
        (lhs4, rhs4),
        (lhs5, rhs5),
        classes,
        Q,
    )


# Exhaustive audit of the five path-cut transport identities through 5 vertices.
pair_instances = 0
transport_failures = 0
for n in range(2, 6):
    allE = tuple(combinations(range(n), 2))
    for gm in range(1 << len(allE)):
        G = tuple(allE[i] for i in range(len(allE)) if (gm >> i) & 1)
        for e, f in combinations(G, 2):
            pair_instances += 1
            result = transport_sums(n, G, e, f)
            pairs = result[:5]
            if any(a != b for a, b in pairs):
                transport_failures += 1
                raise AssertionError((n, G, e, f, pairs))

# K4 obstruction to every edge-multiplicity-preserving direct coupling.
n = 4
E = tuple(combinations(range(n), 2))
e = (0, 1)
f = (2, 3)
F = all_forests(n, E)

cell = Counter((int(e in A), int(f in A)) for A in F)
M00, M10, M01, M11 = (
    cell[(0, 0)],
    cell[(1, 0)],
    cell[(0, 1)],
    cell[(1, 1)],
)
Delta_full = M10 * M01 - M00 * M11


def mult_sig(A, B):
    return tuple(int(g in A) + int(g in B) for g in E)


domain_by_sig = Counter()
target_by_sig = Counter()
domain_pairs = defaultdict(list)
target_pairs = defaultdict(list)
for A in F:
    for B in F:
        sig = mult_sig(A, B)
        if e in A and f in A and e not in B and f not in B:
            domain_by_sig[sig] += 1
            domain_pairs[sig].append((A, B))
        if e in A and f not in A and e not in B and f in B:
            target_by_sig[sig] += 1
            target_pairs[sig].append((A, B))

ones = (1,) * len(E)
assert domain_by_sig[ones] == 4
assert target_by_sig[ones] == 2

K = tuple(g for g in E if g not in (e, f))
KF = all_forests(n, K)
state = Counter()
Q = set()
D = set()
for H in KF:
    ci = comp_index(n, H)
    xe = int(ci[e[0]] != ci[e[1]])
    yf = int(ci[f[0]] != ci[f[1]])
    state[(xe, yf)] += 1
    if xe and yf:
        pe = frozenset((ci[e[0]], ci[e[1]]))
        pf = frozenset((ci[f[0]], ci[f[1]]))
        if pe == pf:
            Q.add(H)
        else:
            D.add(H)

N = len(KF)
n00, n10, n01, n11 = (
    state[(0, 0)],
    state[(1, 0)],
    state[(0, 1)],
    state[(1, 1)],
)
q = len(Q)
d = len(D)
Delta_partner = n10 * n01 - n00 * n11 + N * q
Delta_reduced = n10 * n01 + q * (N - n00) - n00 * d

assert M00 == N
assert M10 == n10 + n11
assert M01 == n01 + n11
assert M11 == d
assert Delta_full == Delta_partner == Delta_reduced == 6

for A, B in domain_pairs[ones]:
    assert frozenset(set(A) - {e, f}) in D
    ci = comp_index(n, B)
    assert ci[e[0]] == ci[e[1]] and ci[f[0]] == ci[f[1]]
for A, B in target_pairs[ones]:
    assert frozenset(set(A) - {e}) in Q
    assert frozenset(set(B) - {f}) in Q

print(f"transport_pair_instances={pair_instances}")
print(f"transport_identity_failures={transport_failures}")
print("K4 marks=e01,f23")
print(f"full_cells M00={M00} M10={M10} M01={M01} M11={M11}")
print(f"full_Rayleigh={Delta_full}")
print(
    "partner_state "
    f"N={N} n00={n00} n10={n10} n01={n01} n11={n11} q={q} d={d}"
)
print(f"partner_identity={n10*n01}-{n00*n11}+{N*q}={Delta_partner}")
print(
    "reduced_residual "
    f"domain=n00*d={n00*d} "
    f"target=n10*n01+q*(N-n00)={n10*n01+q*(N-n00)} "
    f"slack={Delta_reduced}"
)
print(
    "all_singleton_multiplicity_fiber "
    f"domain={domain_by_sig[ones]} target={target_by_sig[ones]} deficit=2"
)
print("same-fiber injection negative control=REJECTED")
print("universal multiplicity-preserving pure color-swap coupling=REFUTED")
