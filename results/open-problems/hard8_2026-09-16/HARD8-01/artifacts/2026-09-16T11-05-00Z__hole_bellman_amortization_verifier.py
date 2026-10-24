#!/usr/bin/env python3
"""Exact finite verifier for HARD8-01 checkpoint 6.

Standard library only. No floating point, randomness, external solver, or timeout
inference is used.

It verifies the five-state S_5 obstruction and the five-state classical Cerny
calibration used in the mathematical report:
  * exact subset-BFS reset thresholds 14 and 16;
  * exact one-idempotent hole Bellman values;
  * the unavoidable final S_5 canonical gap lengths 5,5,6;
  * the bounded chain/sibling endpoint profile and hitting levels 5,5,6;
  * exact optimum 19 when every consecutive singular pair is restricted to a
    chain or sibling one-coordinate move;
  * C_5 Bellman travel 12 and Cayley diameter 4, which forces a 4,4,4 travel
    profile in any threshold-16 canonical reset word.
"""

from collections import deque
from functools import lru_cache

INF = 10**9


def compose(a, b):
    """Right-action composition: first a, then b."""
    return tuple(b[a[i]] for i in range(len(a)))


def invperm(a):
    out = [0] * len(a)
    for i, j in enumerate(a):
        out[j] = i
    return tuple(out)


def generate_group(gens, n):
    identity = tuple(range(n))
    queue = deque([identity])
    dist = {identity: 0}
    word = {identity: ()}
    while queue:
        g = queue.popleft()
        for j, p in enumerate(gens):
            h = compose(g, p)
            if h not in dist:
                dist[h] = dist[g] + 1
                word[h] = word[g] + (j,)
                queue.append(h)
    return tuple(dist), dist, word


def simple_idempotent(n, s, t):
    a = list(range(n))
    a[s] = t
    return tuple(a)


def subset_image(S, a):
    return frozenset(a[x] for x in S)


def reset_bfs(n, letters):
    start = frozenset(range(n))
    queue = deque([start])
    dist = {start: 0}
    prev = {}
    while queue:
        S = queue.popleft()
        if len(S) == 1:
            word = []
            cur = S
            while cur != start:
                old, j = prev[cur]
                word.append(j)
                cur = old
            return dist[S], tuple(reversed(word))
        for j, a in enumerate(letters):
            T = subset_image(S, a)
            if T not in dist:
                dist[T] = dist[S] + 1
                prev[T] = (S, j)
                queue.append(T)
    return None, None


def hole_bellman(n, gens, s, t):
    group, group_dist, group_word = generate_group(gens, n)
    goal = frozenset(set(range(n)) - {t})
    choice = {}

    @lru_cache(None)
    def F(H):
        if H == goal:
            return 0
        best = INF
        best_data = None
        for u in group:
            Hu = subset_image(H, u)
            if s in Hu or t in Hu:
                continue
            H2 = frozenset(set(Hu) | {s})
            value = group_dist[u] + F(H2)
            if value < best:
                best = value
                best_data = (u, H2)
        choice[H] = best_data
        return best

    start = frozenset({s})
    start_value = F(start)
    values = {}
    for mask in range(1 << n):
        H = frozenset(i for i in range(n) if (mask >> i) & 1)
        if s in H and t not in H:
            value = F(H)
            if value < INF:
                values[H] = value
    return start_value, values, choice, group, group_dist, group_word


def alpha(g, s, t):
    gi = invperm(g)
    return gi[s], gi[t]


def local_one_coordinate_optimum(n, gens, s, t):
    """Exact best reset length if every arc transition is chain or sibling."""
    group, group_dist, group_word = generate_group(gens, n)
    identity = tuple(range(n))
    start_holes = frozenset({s})
    start_arc = (s, t)
    goal = frozenset(set(range(n)) - {t})
    next_choice = {}

    @lru_cache(None)
    def F(H, g, last_src, last_dst):
        if H == goal:
            return 0
        best = INF
        best_data = None
        for u in group:
            Hu = subset_image(H, u)
            if s in Hu or t in Hu:
                continue
            H2 = frozenset(set(Hu) | {s})
            g2 = compose(g, u)
            arc2 = alpha(g2, s, t)
            if last_dst == arc2[0]:
                mode = "chain"
            elif last_dst == arc2[1]:
                mode = "sibling"
            else:
                continue
            value = group_dist[u] + F(H2, g2, arc2[0], arc2[1])
            if value < best:
                best = value
                best_data = (u, H2, g2, arc2, mode)
        next_choice[(H, g, last_src, last_dst)] = best_data
        return best

    travel = F(start_holes, identity, *start_arc)
    path = []
    state = (start_holes, identity, *start_arc)
    while state[0] != goal:
        data = next_choice[state]
        assert data is not None
        u, H2, g2, arc2, mode = data
        path.append((group_dist[u], group_word[u], arc2, mode, H2))
        state = (H2, g2, *arc2)
    return (n - 1) + travel, path


def verify_s5():
    n = 5
    p = (0, 1, 2, 4, 3)
    q = (1, 2, 3, 0, 4)
    gens = (p, q)
    s, t = 0, 2

    group, group_dist, group_word = generate_group(gens, n)
    assert len(group) == 120

    reset_threshold, reset_word = reset_bfs(
        n, [p, q, simple_idempotent(n, s, t)]
    )
    assert reset_threshold == 14
    assert len(reset_word) == 14

    start_value, values, _, group, group_dist, group_word = hole_bellman(
        n, gens, s, t
    )
    assert start_value == 10
    expected_values = {
        frozenset({0}): 10,
        frozenset({0, 1}): 10,
        frozenset({0, 3}): 7,
        frozenset({0, 4}): 6,
        frozenset({0, 1, 3}): 5,
        frozenset({0, 1, 4}): 5,
        frozenset({0, 3, 4}): 6,
        frozenset({0, 1, 3, 4}): 0,
    }
    assert values == expected_values
    assert (n - 1) + start_value == reset_threshold

    target_pre_final_holes = frozenset({1, 3, 4})
    final = {}
    size_three_states = [
        frozenset({0, 1, 3}),
        frozenset({0, 1, 4}),
        frozenset({0, 3, 4}),
    ]
    for H in size_three_states:
        candidates = [
            (group_dist[u], group_word[u])
            for u in group
            if subset_image(H, u) == target_pre_final_holes
        ]
        final[H] = min(candidates)

    assert [final[H][0] for H in size_three_states] == [5, 5, 6]
    assert final[size_three_states[0]][1] == (1, 1, 1, 0, 1)
    assert final[size_three_states[1]][1] == (1, 0, 1, 0, 1)
    assert final[size_three_states[2]][1] == (1, 1, 0, 1, 0, 1)

    profile_rows = []
    for L in range(max(group_dist.values()) + 1):
        chain = set()
        sibling = set()
        for u in group:
            if group_dist[u] > L:
                continue
            ui = invperm(u)
            if u[t] == s:
                chain.add(ui[t])
            if u[t] == t:
                sibling.add(ui[s])
        profile_rows.append((L, len(chain), len(sibling), len(chain | sibling)))

    assert profile_rows[:8] == [
        (0, 0, 1, 1),
        (1, 0, 1, 1),
        (2, 1, 1, 1),
        (3, 1, 1, 1),
        (4, 1, 1, 1),
        (5, 2, 2, 3),
        (6, 3, 4, 4),
        (7, 4, 4, 4),
    ]
    mu = {L: m for L, _, _, m in profile_rows}
    hitting_levels = [
        min(L for L, m in mu.items() if m > h) for h in range(1, n - 1)
    ]
    assert hitting_levels == [5, 5, 6]

    local_total, local_path = local_one_coordinate_optimum(n, gens, s, t)
    assert local_total == 19
    assert [row[0] for row in local_path] == [5, 5, 5]
    assert [row[2] for row in local_path] == [(4, 2), (2, 3), (1, 3)]
    assert [row[3] for row in local_path] == ["sibling", "chain", "sibling"]

    return {
        "reset_threshold": reset_threshold,
        "bellman_start": start_value,
        "final_stage_distances": [final[H][0] for H in size_three_states],
        "profile_0_to_7": profile_rows[:8],
        "mixed_hitting_levels": hitting_levels,
        "one_coordinate_local_total": local_total,
    }


def verify_c5():
    n = 5
    cycle = (1, 2, 3, 4, 0)
    s, t = 0, 1

    reset_threshold, reset_word = reset_bfs(
        n, [cycle, simple_idempotent(n, s, t)]
    )
    assert reset_threshold == 16
    assert len(reset_word) == 16

    start_value, values, _, _, _, _ = hole_bellman(n, (cycle,), s, t)
    assert start_value == 12
    assert values[frozenset({0})] == 12
    assert values[frozenset({0, 4})] == 8
    assert values[frozenset({0, 3, 4})] == 4

    _, group_dist, _ = generate_group((cycle,), n)
    assert max(group_dist.values()) == 4

    # A canonical threshold-16 reset word has three inter-singular blocks.
    # Each induced group element can be represented in at most 4 generator
    # letters, while their total must be 12 by exact threshold extremality;
    # hence all three shortest block lengths must be 4.
    assert (n - 1) + start_value == reset_threshold

    return {
        "reset_threshold": reset_threshold,
        "bellman_start": start_value,
        "positive_generator_diameter": max(group_dist.values()),
    }


def main():
    s5 = verify_s5()
    c5 = verify_c5()
    print("S5_RESET_THRESHOLD", s5["reset_threshold"])
    print("S5_BELLMAN_START", s5["bellman_start"])
    print("S5_FINAL_STAGE_DISTANCES", s5["final_stage_distances"])
    print("S5_PROFILE_0_TO_7", s5["profile_0_to_7"])
    print("S5_MIXED_HITTING_LEVELS", s5["mixed_hitting_levels"])
    print("S5_ONE_COORDINATE_LOCAL_TOTAL", s5["one_coordinate_local_total"])
    print("C5_RESET_THRESHOLD", c5["reset_threshold"])
    print("C5_BELLMAN_START", c5["bellman_start"])
    print("C5_POSITIVE_GENERATOR_DIAMETER", c5["positive_generator_diameter"])
    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
