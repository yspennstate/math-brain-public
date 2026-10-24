from itertools import combinations
from collections import Counter


def norm(e):
    return tuple(sorted(e))


def is_forest(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    for a, b in edges:
        if not union(a, b):
            return False
    return True


def terminal_state(n, H, a, b, c):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    for x, y in H:
        union(x, y)
    ra, rb, rc = find(a), find(b), find(c)
    if ra == rb == rc:
        return "A"
    if ra == rc and ra != rb:
        return "B"
    if ra == rb and ra != rc:
        return "C"
    if rb == rc and ra != rb:
        return "Q"
    return "D"


def partition_counts(n, K, a, b, c):
    counts = Counter()
    m = len(K)
    for mask in range(1 << m):
        H = [K[i] for i in range(m) if (mask >> i) & 1]
        if is_forest(n, H):
            counts[terminal_state(n, H, a, b, c)] += 1
    return {key: counts[key] for key in "ABCQD"}


def rayleigh_gap(n, edges, e, f):
    edges = [norm(x) for x in edges]
    e, f = norm(e), norm(f)
    ie, jf = edges.index(e), edges.index(f)
    Z = Ze = Zf = Zef = 0
    m = len(edges)
    for mask in range(1 << m):
        H = [edges[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, H):
            continue
        Z += 1
        xe = (mask >> ie) & 1
        xf = (mask >> jf) & 1
        Ze += xe
        Zf += xf
        Zef += xe * xf
    return Z, Ze, Zf, Zef, Ze * Zf - Z * Zef


def verify(max_n=5):
    instances = 0
    identity_failures = 0
    monotonicity_failures = 0
    min_increment = None
    negative_control_triggered = False
    negative_control_witness = None

    for n in range(3, max_n + 1):
        all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
        for a in range(n):
            for b, c in combinations([v for v in range(n) if v != a], 2):
                e = norm((a, b))
                f = norm((a, c))
                h = norm((b, c))
                residual = [g for g in all_edges if g not in {e, f, h}]
                for mask in range(1 << len(residual)):
                    K = [residual[i] for i in range(len(residual)) if (mask >> i) & 1]
                    pc = partition_counts(n, K, a, b, c)
                    A, B, C, Q, D = (pc[key] for key in "ABCQD")
                    G0 = K + [e, f]
                    G1 = K + [e, f, h]
                    d0 = rayleigh_gap(n, G0, e, f)[-1]
                    d1 = rayleigh_gap(n, G1, e, f)[-1]
                    formula0 = B * C - A * D + Q * (B + C + D + Q)
                    increment = 2 * D * (D + Q)
                    instances += 1
                    if d0 != formula0 or d1 - d0 != increment:
                        identity_failures += 1
                    if d1 <= d0:
                        monotonicity_failures += 1
                    if min_increment is None or increment < min_increment:
                        min_increment = increment

                    # Negative control: deliberately omit the D^2 contribution.
                    wrong_increment = 2 * D * Q
                    if not negative_control_triggered and d1 - d0 != wrong_increment:
                        negative_control_triggered = True
                        negative_control_witness = {
                            "n": n,
                            "a_b_c": [a, b, c],
                            "K": K,
                            "A_B_C_Q_D": [A, B, C, Q, D],
                            "true_increment": d1 - d0,
                            "wrong_increment": wrong_increment,
                        }

    n = 4
    all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    witness_G = [g for g in all_edges if g != (2, 3)]
    e, f, h = (0, 1), (0, 2), (1, 2)
    K = [g for g in witness_G if g not in {e, f, h}]
    pc = partition_counts(n, K, 0, 1, 2)
    d0 = rayleigh_gap(n, K + [e, f], e, f)[-1]
    d1 = rayleigh_gap(n, K + [e, f, h], e, f)[-1]
    witness = {
        "K": K,
        "A_B_C_Q_D": [pc[k] for k in "ABCQD"],
        "gap_without_closing_edge": d0,
        "gap_with_closing_edge": d1,
        "increment": d1 - d0,
        "formula_increment": 2 * pc["D"] * (pc["D"] + pc["Q"]),
    }

    print(f"instances={instances}")
    print(f"identity_failures={identity_failures}")
    print(f"strict_monotonicity_failures={monotonicity_failures}")
    print(f"minimum_unit_increment={min_increment}")
    print(f"negative_control_triggered={negative_control_triggered}")
    print(f"negative_control_witness={negative_control_witness}")
    print(f"partner_witness_recheck={witness}")

    assert identity_failures == 0
    assert monotonicity_failures == 0
    assert min_increment >= 2
    assert negative_control_triggered
    assert witness["increment"] == witness["formula_increment"] == 18


if __name__ == "__main__":
    verify()
