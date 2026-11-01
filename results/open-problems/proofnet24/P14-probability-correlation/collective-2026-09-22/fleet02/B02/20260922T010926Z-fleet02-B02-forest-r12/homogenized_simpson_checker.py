from fractions import Fraction
from itertools import combinations


def forest(mask, n, edges):
    p = list(range(n))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    k = 0
    for i, (a, b) in enumerate(edges):
        if (mask >> i) & 1:
            a, b = find(a), find(b)
            if a == b:
                return False, 0
            p[a] = b
            k += 1
    return True, k


def graph_rank(n, edges):
    p = list(range(n))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    for a, b in edges:
        a, b = find(a), find(b)
        if a != b:
            p[a] = b
    return n - len({find(i) for i in range(n)})


graphs = 0
pairs = 0
positive_cov_pairs = 0
size_bound_fail = 0
pair_psd_fail = 0
support_fail = 0
rank_mean_fail = 0
p_half_fail = 0
sum_u_fail = 0
min_size_slack = None
min_support_slack = None

for n in range(2, 6):
    all_edges = list(combinations(range(n), 2))
    for gm in range(1 << len(all_edges)):
        edges = [all_edges[i] for i in range(len(all_edges)) if (gm >> i) & 1]
        m = len(edges)
        graphs += 1
        Z = 0
        sumK = 0
        sumK2 = 0
        Ze = [0] * m
        sumKe = [0] * m
        Zef = [[0] * m for _ in range(m)]
        for mask in range(1 << m):
            ok, k = forest(mask, n, edges)
            if not ok:
                continue
            Z += 1
            sumK += k
            sumK2 += k * k
            inc = [i for i in range(m) if (mask >> i) & 1]
            for i in inc:
                Ze[i] += 1
                sumKe[i] += k
            for a in range(len(inc)):
                i = inc[a]
                for b in range(a + 1, len(inc)):
                    j = inc[b]
                    Zef[i][j] += 1
                    Zef[j][i] += 1

        mu = Fraction(sumK, Z)
        varK = Fraction(sumK2, Z) - mu * mu
        t = Fraction(m, 1) - mu - varK
        size_slack = mu * (m - mu) - m * varK
        if size_slack < 0:
            size_bound_fail += 1
        if min_size_slack is None or size_slack < min_size_slack:
            min_size_slack = size_slack

        r = graph_rank(n, edges)
        if mu < Fraction(r, 2):
            rank_mean_fail += 1

        probs = [Fraction(z, Z) for z in Ze]
        u = [Fraction(Z * sumKe[i] - sumK * Ze[i], Z * Z) for i in range(m)]
        if any(q > Fraction(1, 2) for q in probs):
            p_half_fail += 1
        if sum(u, Fraction()) != varK:
            sum_u_fail += 1

        for i in range(m):
            for j in range(i + 1, m):
                pairs += 1
                C = Fraction(Z * Zef[i][j] - Ze[i] * Ze[j], Z * Z)
                if C > 0:
                    positive_cov_pairs += 1
                if C * C > probs[i] * probs[i] * probs[j] * probs[j]:
                    pair_psd_fail += 1
                support_slack = (
                    t * (probs[i] * probs[i] + probs[j] * probs[j] - 2 * C)
                    - (u[i] + u[j]) ** 2
                )
                if support_slack < 0:
                    support_fail += 1
                if min_support_slack is None or support_slack < min_support_slack:
                    min_support_slack = support_slack

print(f"graphs={graphs}")
print(f"present_edge_pairs={pairs}")
print(f"positive_covariance_pairs={positive_cov_pairs}")
print(f"size_variance_bound_failures={size_bound_fail}")
print(f"edge_pair_psd_failures={pair_psd_fail}")
print(f"homogenized_support_bound_failures={support_fail}")
print(f"rank_half_mean_failures={rank_mean_fail}")
print(f"edge_marginal_half_failures={p_half_fail}")
print(f"sum_u_identity_failures={sum_u_fail}")
print(f"minimum_size_slack={min_size_slack}")
print(f"minimum_support_slack={min_support_slack}")
print(
    "ALL_EXACT_CHECKS_PASSED"
    if not any(
        [
            size_bound_fail,
            pair_psd_fail,
            support_fail,
            rank_mean_fail,
            p_half_fail,
            sum_u_fail,
        ]
    )
    else "CHECK_FAILURE"
)
