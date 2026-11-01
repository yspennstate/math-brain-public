#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict


def is_forest(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        a, b = find(u), find(v)
        if a == b:
            return False
        parent[a] = b
    return True


def all_forests(n, edges):
    E = list(edges)
    ans = []
    for mask in range(1 << len(E)):
        S = frozenset(E[i] for i in range(len(E)) if mask >> i & 1)
        if is_forest(n, S):
            ans.append(S)
    return ans


def state(n, H, e, f):
    return (
        int(is_forest(n, list(H) + [e])),
        int(is_forest(n, list(H) + [f])),
    )


def jointly_addable(n, H, e, f):
    return is_forest(n, list(H) + [e, f])


def path_edges(n, H, a, b):
    adj = [[] for _ in range(n)]
    for u, v in H:
        ed = (u, v) if u < v else (v, u)
        adj[u].append((v, ed))
        adj[v].append((u, ed))
    stack = [(a, [])]
    seen = set()
    while stack:
        x, path = stack.pop()
        if x == b:
            return path
        if x in seen:
            continue
        seen.add(x)
        for y, ed in adj[x]:
            if y not in seen:
                stack.append((y, path + [ed]))
    return None


def components(n, H):
    adj = [[] for _ in range(n)]
    for u, v in H:
        adj[u].append(v)
        adj[v].append(u)
    ans = []
    seen = set()
    for v in range(n):
        if v in seen:
            continue
        stack = [v]
        seen.add(v)
        C = set()
        while stack:
            x = stack.pop()
            C.add(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        ans.append(C)
    return ans


def analyze(n, G, e, f):
    B = tuple(g for g in G if g not in (e, f))
    forests = all_forests(n, B)
    cells = defaultdict(list)
    Q = []
    for H in forests:
        s = state(n, H, e, f)
        cells[s].append(H)
        if s == (1, 1) and not jointly_addable(n, H, e, f):
            Q.append(H)

    N = len(forests)
    n00, n10, n01, n11 = (
        len(cells[(0, 0)]),
        len(cells[(1, 0)]),
        len(cells[(0, 1)]),
        len(cells[(1, 1)]),
    )
    q = len(Q)
    Delta = n10 * n01 + q * N - n00 * n11

    def signature(A, H):
        return tuple(int(g in A) + int(g in H) for g in B)

    domain = Counter(
        signature(A, H) for A in cells[(0, 0)] for H in cells[(1, 1)]
    )
    ordinary = Counter(
        signature(C, D) for C in cells[(1, 0)] for D in cells[(0, 1)]
    )
    qchannel = Counter(signature(K, H) for K in Q for H in forests)
    codomain = ordinary + qchannel
    violations = {
        s: (domain[s], codomain[s]) for s in domain if domain[s] > codomain[s]
    }

    d = o = I_left = 0
    for H in cells[(0, 0)]:
        pe = set(path_edges(n, H, *e))
        pf = set(path_edges(n, H, *f))
        s = len(pe & pf)
        if s:
            o += 1
            I_left += s
        else:
            d += 1

    I_right = 0
    for K in Q:
        comps = components(n, K)

        def ci(v):
            return next(i for i, C in enumerate(comps) if v in C)

        i, j = ci(e[0]), ci(e[1])
        assert {i, j} == {ci(f[0]), ci(f[1])}
        C1, C2 = comps[i], comps[j]
        c = sum(
            1
            for u, v in B
            if (u in C1 and v in C2) or (v in C1 and u in C2)
        )
        I_right += c

    assert I_left == I_right
    E_O = I_left - o
    E_Q = I_right - q
    terms = (
        n10 * n01 - d * n11,
        q * (N - n11),
        n11 * E_O,
        -n11 * E_Q,
    )
    assert sum(terms) == Delta

    return dict(
        N=N,
        n00=n00,
        n10=n10,
        n01=n01,
        n11=n11,
        q=q,
        Delta=Delta,
        B=B,
        domain=domain,
        ordinary=ordinary,
        qchannel=qchannel,
        codomain=codomain,
        violations=violations,
        d=d,
        o=o,
        I_left=I_left,
        I_right=I_right,
        E_O=E_O,
        E_Q=E_Q,
        terms=terms,
    )


G = tuple(combinations(range(4), 2))
e = (0, 1)
f = (2, 3)
r = analyze(4, G, e, f)
print(
    "K4_DISJOINT_COUNTS",
    r["N"],
    r["n00"],
    r["n10"],
    r["n01"],
    r["n11"],
    r["q"],
    r["Delta"],
)
sigma = (1, 1, 1, 1)
print(
    "ALL_ONES_SIGNATURE",
    list(r["B"]),
    "domain",
    r["domain"][sigma],
    "ordinary",
    r["ordinary"][sigma],
    "q_channel",
    r["qchannel"][sigma],
    "fiber_deficit",
    r["domain"][sigma] - r["codomain"][sigma],
)
assert r["domain"][sigma] == 4
assert r["ordinary"][sigma] == 0
assert r["qchannel"][sigma] == 2
assert r["codomain"][sigma] == 2

print(
    "B03_DECOMPOSITION",
    "d",
    r["d"],
    "o",
    r["o"],
    "I",
    r["I_left"],
    r["I_right"],
    "E_O",
    r["E_O"],
    "E_Q",
    r["E_Q"],
    "terms",
    r["terms"],
    "sum",
    sum(r["terms"]),
)

rows = []
first = None
for n in range(2, 5):
    allE = list(combinations(range(n), 2))
    instances = bad = 0
    for mask in range(1 << len(allE)):
        H = tuple(allE[i] for i in range(len(allE)) if mask >> i & 1)
        if len(H) < 2:
            continue
        for a, b in combinations(H, 2):
            instances += 1
            rr = analyze(n, H, a, b)
            if rr["violations"]:
                bad += 1
                if first is None:
                    first = (n, H, a, b)
    rows.append((n, instances, bad))

print(
    "SMALL_GRAPH_AUDIT",
    rows,
    "first_violation_n",
    first[0],
    "first_graph_edges",
    first[1],
    "marks",
    first[2],
    first[3],
)
assert rows == [(2, 0, 0), (3, 6, 0), (4, 240, 3)]
assert first == (4, G, e, f)
print("ALL_EXACT_ASSERTIONS_PASSED")
