from fractions import Fraction
from math import ceil, log


def bundle_graph(lengths):
    edges = []
    nxt = 2
    for a in lengths:
        if a < 1:
            raise ValueError("positive path length required")
        if a == 1:
            edges.append((0, 1))
            continue
        prev = 0
        for _ in range(a - 1):
            v = nxt
            nxt += 1
            edges.append((prev, v))
            prev = v
        edges.append((prev, 1))
    return nxt, edges


def forest_and_connected(n, edges, mask):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            if not union(u, v):
                return False, False
    return True, find(0) == find(1)


def exact_counts(lengths):
    n, edges = bundle_graph(lengths)
    D = C = 0
    for mask in range(1 << len(edges)):
        ok, conn = forest_and_connected(n, edges, mask)
        if ok:
            if conn:
                C += 1
            else:
                D += 1
    return D, C


def formula_counts(lengths):
    ds = [2 ** a - 1 for a in lengths]
    D = 1
    for x in ds:
        D *= x
    C = sum(Fraction(D, x) for x in ds)
    assert C.denominator == 1
    return D, C.numerator


def greedy_below(r, eps):
    r = Fraction(r)
    eps = Fraction(eps)
    if not (0 < eps < r <= 1):
        raise ValueError("need 0 < eps < r <= 1")
    initial = r
    terms = []
    while r > eps:
        a = 1
        while Fraction(1, 2 ** a - 1) > r:
            a += 1
        old = r
        r -= Fraction(1, 2 ** a - 1)
        assert r >= 0
        assert 3 * r < 2 * old
        terms.append(a)
    K = ceil(log(float(initial / eps), 1.5))
    A = ceil(log(1.0 + 1.0 / float(eps), 2.0))
    assert len(terms) <= K
    assert sum(terms) <= K * A
    return terms, initial - r, r, K, A


def responses_up_to_cost(max_cost):
    dp = [set() for _ in range(max_cost + 1)]
    dp[0].add(Fraction(0))
    for c in range(max_cost + 1):
        for s in tuple(dp[c]):
            for a in range(1, max_cost - c + 1):
                dp[c + a].add(s + Fraction(1, 2 ** a - 1))
    out = set()
    for s in dp:
        out |= s
    return out


bundle_tests = [(2,), (3,), (2, 3), (1, 2, 3), (2, 2, 3), (3, 4)]
print("MIXED_THETA_BUNDLE_TESTS")
for lengths in bundle_tests:
    got = exact_counts(lengths)
    want = formula_counts(lengths)
    assert got == want
    D, C = got
    print(lengths, "cost", sum(lengths), "D", D, "C", C, "response", Fraction(C, D))

print("GREEDY_EPS_NET_TESTS")
examples = [
    (Fraction(1, 2), Fraction(1, 100)),
    (Fraction(5, 7), Fraction(1, 1000)),
    (Fraction(13, 29), Fraction(1, 10000)),
    (Fraction(1, 10), Fraction(1, 100000)),
]
for r, eps in examples:
    terms, s, rem, K, A = greedy_below(r, eps)
    print("r", r, "eps", eps, "terms", terms, "cost", sum(terms),
          "residual", rem, "bound_KA", K * A)

R = sorted(x for x in responses_up_to_cost(12) if 0 <= x <= 1)
gaps = [(R[i + 1] - R[i], R[i], R[i + 1]) for i in range(len(R) - 1)]
gap, left, right = max(gaps)
print("COST_LE_12_DISTINCT_RESPONSES_[0,1]", len(R))
print("COST_LE_12_MAX_GAP_[0,1]", gap, "between", left, right)
print("STATUS=MIXED_THETA_EXACT_PASS")
