from fractions import Fraction
from itertools import combinations


def is_forest(n, edges, mask):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            parent[ru] = rv
    return True


def rank_graph(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
    return n - len({find(i) for i in range(n)})


def check_graph(n, edges):
    m = len(edges)
    forests = [s for s in range(1 << m) if is_forest(n, edges, s)]
    N = len(forests)
    rank = rank_graph(n, edges)
    counts = [sum((s >> i) & 1 for s in forests) for i in range(m)]
    p = [Fraction(c, N) for c in counts]
    mean = sum(p, Fraction(0))
    variances = [x * (1 - x) for x in p]
    varK = Fraction(0)
    sizes = [s.bit_count() for s in forests]
    EK2 = sum(Fraction(k * k, N) for k in sizes)
    varK = EK2 - mean * mean
    sumv = sum(variances, Fraction(0))
    maxcov = Fraction(0)
    for i, j in combinations(range(m), 2):
        pij = Fraction(sum(((s >> i) & 1) and ((s >> j) & 1) for s in forests), N)
        cov = pij - p[i] * p[j]
        maxcov = max(maxcov, cov)
    assert all(x <= Fraction(1, 2) for x in p)
    assert mean >= Fraction(rank, 2)
    assert maxcov <= 0
    assert varK <= sumv
    return mean - Fraction(rank, 2), max(p, default=Fraction(0)), varK - sumv


for n in range(2, 6):
    all_edges = list(combinations(range(n), 2))
    min_mean_gap = None
    max_p = Fraction(0)
    max_var_gap = None
    graph_count = 0
    for gm in range(1, 1 << len(all_edges)):
        edges = [all_edges[i] for i in range(len(all_edges)) if (gm >> i) & 1]
        mean_gap, pmax, var_gap = check_graph(n, edges)
        min_mean_gap = mean_gap if min_mean_gap is None else min(min_mean_gap, mean_gap)
        max_p = max(max_p, pmax)
        max_var_gap = var_gap if max_var_gap is None else max(max_var_gap, var_gap)
        graph_count += 1
    print(f"n={n} graphs={graph_count} min(mean-r/2)={min_mean_gap} max_p={max_p} max(VarK-sumv)={max_var_gap}")
print("violations=0")
