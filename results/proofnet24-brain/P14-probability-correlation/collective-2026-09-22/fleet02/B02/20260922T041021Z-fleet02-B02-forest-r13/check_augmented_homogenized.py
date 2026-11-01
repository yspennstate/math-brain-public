from fractions import Fraction
from itertools import combinations


def is_forest(n, edges, mask):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    k = 0
    chosen = []
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            a, b = find(u), find(v)
            if a == b:
                return False, 0, []
            if rank[a] < rank[b]:
                a, b = b, a
            parent[b] = a
            if rank[a] == rank[b]:
                rank[a] += 1
            k += 1
            chosen.append(i)
    return True, k, chosen


def stats(n, edges):
    m = len(edges)
    Z = S1 = S2 = 0
    Ze = [0] * m
    Se = [0] * m
    Zef = [[0] * m for _ in range(m)]
    for mask in range(1 << m):
        ok, k, chosen = is_forest(n, edges, mask)
        if not ok:
            continue
        Z += 1
        S1 += k
        S2 += k * k
        for e in chosen:
            Ze[e] += 1
            Se[e] += k
        for e, f in combinations(chosen, 2):
            Zef[e][f] += 1
            Zef[f][e] += 1
    mu = Fraction(S1, Z)
    var = Fraction(S2, Z) - mu * mu
    p = [Fraction(x, Z) for x in Ze]
    ck = [Fraction(Se[e], Z) - p[e] * mu for e in range(m)]
    cov = [[Fraction(0) for _ in range(m)] for __ in range(m)]
    for e in range(m):
        cov[e][e] = p[e] * (1 - p[e])
        for f in range(e + 1, m):
            x = Fraction(Zef[e][f], Z) - p[e] * p[f]
            cov[e][f] = cov[f][e] = x
    return Z, mu, var, p, ck, cov


graphs = rows = pairs = 0
target_bad = 0
min_det = None
min_ulc = None
min_global = None

for n in range(2, 6):
    universe = list(combinations(range(n), 2))
    for gm in range(1 << len(universe)):
        edges = [universe[i] for i in range(len(universe)) if (gm >> i) & 1]
        m = len(edges)
        graphs += 1
        if m == 0:
            continue
        Z, mu, var, p, ck, cov = stats(n, edges)
        r = Fraction(m, 1) - mu - var
        assert r >= 0, ("r", n, edges, r)

        ulc = mu * (Fraction(m, 1) - mu) / m - var
        assert ulc >= 0, ("ulc", n, edges, ulc)
        min_ulc = ulc if min_ulc is None or ulc < min_ulc else min_ulc

        global_slack = (
            var
            - var * var / (Fraction(m, 1) - mu)
            - sum(ck[e] * ck[e] / p[e] for e in range(m))
        )
        assert global_slack >= 0, ("global", n, edges, global_slack)
        min_global = global_slack if min_global is None or global_slack < min_global else min_global

        for e in range(m):
            pe = p[e]
            lhs = ck[e] * ck[e] / (Fraction(m, 1) - mu)
            lhs += sum(cov[e][f] * cov[e][f] / p[f] for f in range(m) if f != e)
            slack = pe * pe * (1 - pe) - lhs
            assert slack >= 0, ("row", n, edges, e, slack)
            rows += 1

        for e, f in combinations(range(m), 2):
            pairs += 1
            d = -cov[e][f]
            det = (
                r * p[e] * p[e] * p[f] * p[f]
                + 2 * ck[e] * ck[f] * d
                - r * d * d
                - p[f] * p[f] * ck[e] * ck[e]
                - p[e] * p[e] * ck[f] * ck[f]
            )
            assert det >= 0, ("det", n, edges, e, f, det)
            min_det = det if min_det is None or det < min_det else min_det
            if cov[e][f] > 0:
                target_bad += 1

print("AUGMENTED_HOMOGENIZED_FOREST_CHECK")
print("graphs_n2_to_n5 =", graphs)
print("edge_rows_checked =", rows)
print("edge_pairs_checked =", pairs)
print("augmented_row_budget_failures = 0")
print("slack_global_budget_failures = 0")
print("three_by_three_minor_failures = 0")
print("ulc_variance_failures = 0")
print("positive_edge_covariances_in_range =", target_bad)
print("min_three_by_three_det =", min_det)
print("min_ulc_slack =", min_ulc)
print("min_global_slack =", min_global)
print("STATUS=ALL_EXACT_CHECKS_PASS")
