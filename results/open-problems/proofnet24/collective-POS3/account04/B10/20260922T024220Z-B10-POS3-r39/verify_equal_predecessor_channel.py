from itertools import combinations
from collections import Counter


def closure_from_edges(n, edges):
    reach = [[False] * n for _ in range(n)]
    for i, j in edges:
        reach[i][j] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    if reach[k][j]:
                        reach[i][j] = True
    assert not any(reach[i][i] for i in range(n))
    return tuple(tuple(row) for row in reach)


def all_forward_closures(n):
    pairs = list(combinations(range(n), 2))
    seen = {}
    for mask in range(1 << len(pairs)):
        edges = [pairs[k] for k in range(len(pairs)) if (mask >> k) & 1]
        reach = closure_from_edges(n, edges)
        seen[reach] = None
    return list(seen)


def incomparable(reach, a, b):
    return a != b and not reach[a][b] and not reach[b][a]


def pred_succ(reach):
    n = len(reach)
    pred = [set() for _ in range(n)]
    succ = [set() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if reach[i][j]:
                succ[i].add(j)
                pred[j].add(i)
    return pred, succ


def width(reach):
    n = len(reach)
    best = 0
    for mask in range(1 << n):
        S = [i for i in range(n) if (mask >> i) & 1]
        if len(S) <= best:
            continue
        if all(incomparable(reach, i, j) for i, j in combinations(S, 2)):
            best = len(S)
    return best


def linear_extensions(reach, nodes=None):
    n = len(reach)
    nodes = tuple(range(n)) if nodes is None else tuple(nodes)
    preds = {v: {u for u in nodes if reach[u][v]} for v in nodes}
    ans = []

    def rec(prefix, remaining):
        if not remaining:
            ans.append(tuple(prefix))
            return
        rem = set(remaining)
        for v in sorted(remaining):
            if preds[v].isdisjoint(rem):
                rec(prefix + [v], tuple(w for w in remaining if w != v))

    rec([], nodes)
    return ans


def pair_count(exts, a, b):
    A = sum(L.index(a) < L.index(b) for L in exts)
    return A, len(exts) - A


def admissible_interval(reach, tau, v):
    pos = {x: i + 1 for i, x in enumerate(tau)}
    m = len(tau)
    ell = max([pos[u] for u in tau if reach[u][v]], default=0)
    upper = min([pos[w] - 1 for w in tau if reach[v][w]], default=m)
    assert ell <= upper
    return ell, upper


def minimal_positive_blockers(reach, a, b):
    n = len(reach)
    S = [z for z in range(n) if reach[a][z] and incomparable(reach, z, b)]
    return tuple(
        sorted(
            z
            for z in S
            if not any(w != z and w in S and reach[w][z] for w in S)
        )
    )


def is_cover(reach, a, z):
    n = len(reach)
    return reach[a][z] and not any(
        w != a and w != z and reach[a][w] and reach[w][z] for w in range(n)
    )


def analyze_pair(reach, a, b):
    n = len(reach)
    pred, _ = pred_succ(reach)
    assert incomparable(reach, a, b) and pred[a] == pred[b]
    taus = linear_extensions(reach, [v for v in range(n) if v not in (a, b)])
    plus = Counter()
    minus = Counter()
    A_sum = B_sum = 0
    Cplus = Cminus = 0
    for tau in taus:
        la, ua = admissible_interval(reach, tau, a)
        lb, ub = admissible_interval(reach, tau, b)
        assert la == lb
        r, s = ua - la + 1, ub - lb + 1

        A = B = 0
        for i in range(la, ua + 1):
            for j in range(lb, ub + 1):
                if i < j:
                    A += 1
                elif i > j:
                    B += 1
                else:
                    A += 1
                    B += 1
        assert A - B == min(r, s) * (s - r)
        assert A + B == min(r, s) * (max(r, s) + 1)
        A_sum += A
        B_sum += B

        if s > r:
            mass = r * (s - r)
            assert ua < len(tau)
            z = tau[ua]
            assert reach[a][z] and incomparable(reach, z, b)
            assert z in minimal_positive_blockers(reach, a, b)
            plus[z] += mass
            Cplus += mass
        elif r > s:
            mass = s * (r - s)
            assert ub < len(tau)
            z = tau[ub]
            assert reach[b][z] and incomparable(reach, z, a)
            assert z in minimal_positive_blockers(reach, b, a)
            minus[z] += mass
            Cminus += mass

    full = linear_extensions(reach)
    A, B = pair_count(full, a, b)
    assert (A_sum, B_sum) == (A, B)
    assert Cplus - Cminus == A - B
    return len(full), A, B, plus, minus


def main():
    totals = Counter()
    by_n = {}
    for n in range(2, 7):
        stat = Counter()
        for reach in all_forward_closures(n):
            stat["closures"] += 1
            if width(reach) > 3:
                continue
            stat["width_le_3"] += 1
            pred, _ = pred_succ(reach)
            full = None
            for a in range(n):
                for b in range(n):
                    if not incomparable(reach, a, b) or pred[a] != pred[b]:
                        continue
                    stat["equal_pred_ordered_pairs"] += 1
                    M = minimal_positive_blockers(reach, a, b)
                    assert len(M) <= 2
                    assert all(is_cover(reach, a, z) for z in M)

                    E, A, B, plus, minus = analyze_pair(reach, a, b)
                    if 3 * A > 2 * E:
                        stat["p_gt_2_3"] += 1
                        if full is None:
                            full = linear_extensions(reach)
                        all_after = True
                        for z in M:
                            bz, _ = pair_count(full, b, z)
                            if 3 * bz <= 2 * E:
                                all_after = False
                                break
                        if all_after:
                            stat["fork_escalation_cases"] += 1
                            assert len(M) == 2
                            assert 3 * sum(plus.values()) > E
                            assert 6 * max(plus.values()) > E
        by_n[n] = stat
        totals.update(stat)

    print("POS3_EQUAL_PREDECESSOR_CHANNEL_CHECK_PASS")
    for n in range(2, 7):
        s = by_n[n]
        print(
            "n=%d closures=%d width_le_3=%d equal_pred_pairs=%d p_gt_2_3=%d fork_escalation=%d"
            % (
                n,
                s["closures"],
                s["width_le_3"],
                s["equal_pred_ordered_pairs"],
                s["p_gt_2_3"],
                s["fork_escalation_cases"],
            )
        )
    print(
        "TOTAL closures=%d width_le_3=%d equal_pred_pairs=%d p_gt_2_3=%d fork_escalation=%d"
        % (
            totals["closures"],
            totals["width_le_3"],
            totals["equal_pred_ordered_pairs"],
            totals["p_gt_2_3"],
            totals["fork_escalation_cases"],
        )
    )


if __name__ == "__main__":
    main()
