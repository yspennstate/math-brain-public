#!/usr/bin/env python3
"""Exact verifier for HARD8-01 checkpoint 5.

Standard library only.  No floating point, randomness, SAT solver, or timeout
inference is used.

Checks:
  * witness sets are right cosets of ordered-pair stabilizers;
  * the orbit-size Schreier entrance bound;
  * reset threshold <= minimum orbit-weighted arborescence bound;
  * reset threshold <= minimum leaf-discounted arborescence bound;
  * exhaustive small SI families through n=4;
  * a targeted n=5 S_5 example where both the coarse discounted forest
    certificate and every Hamiltonian defect-path certificate are strictly
    above the Cerny square, while exact subset BFS gives reset threshold 14.
"""

from collections import defaultdict, deque
from itertools import combinations, permutations, product
from math import inf


def compose(a, b):
    """Right-action composition: first a, then b."""
    return tuple(b[a[i]] for i in range(len(a)))


def invperm(a):
    out = [None] * len(a)
    for i, j in enumerate(a):
        out[j] = i
    return tuple(out)


def generate_group(gens, n):
    identity = tuple(range(n))
    seen = {identity}
    q = deque([identity])
    while q:
        g = q.popleft()
        for p in gens:
            h = compose(g, p)
            if h not in seen:
                seen.add(h)
                q.append(h)
    return tuple(seen)


def simple_idempotent(n, s, t):
    a = list(range(n))
    a[s] = t
    return tuple(a)


def alpha(g, edge):
    s, t = edge
    gi = invperm(g)
    return gi[s], gi[t]


def orbit_data(group, edge):
    arcs = defaultdict(list)
    for g in group:
        arcs[alpha(g, edge)].append(g)
    return arcs


def pair_stabilizer(group, edge):
    s, t = edge
    return {g for g in group if g[s] == s and g[t] == t}


def distances_from(start, gens):
    dist = {start: 0}
    q = deque([start])
    while q:
        g = q.popleft()
        for p in gens:
            h = compose(g, p)
            if h not in dist:
                dist[h] = dist[g] + 1
                q.append(h)
    return dist


def apply_subset(S, letter):
    return frozenset(letter[x] for x in S)


def reset_threshold(n, letters):
    start = frozenset(range(n))
    seen = {start}
    q = deque([(start, 0)])
    while q:
        S, d = q.popleft()
        if len(S) == 1:
            return d
        for a in letters:
            T = apply_subset(S, a)
            if T not in seen:
                seen.add(T)
                q.append((T, d + 1))
    return None


def shortest_reset_word(n, letters):
    start = frozenset(range(n))
    prev = {start: (None, None)}
    q = deque([start])
    target = None
    while q:
        S = q.popleft()
        if len(S) == 1:
            target = S
            break
        for i, a in enumerate(letters):
            T = apply_subset(S, a)
            if T not in prev:
                prev[T] = (S, i)
                q.append(T)
    if target is None:
        return None
    word = []
    cur = target
    while prev[cur][0] is not None:
        old, i = prev[cur]
        word.append(i)
        cur = old
    return list(reversed(word))


def verify_cosets_and_entrance(n, P, E):
    G = generate_group(P, n)
    for e in E:
        H = pair_stabilizer(G, e)
        arcs = orbit_data(G, e)
        m = len(arcs)
        assert len(G) // len(H) == m
        all_dist = {f: distances_from(f, P) for f in G}
        for a, witnesses in arcs.items():
            g = witnesses[0]
            right_coset = {compose(g, h) for h in H}
            assert right_coset == set(witnesses)
            for f in G:
                best = min(all_dist[f][w] for w in witnesses)
                assert best <= m - 1


def min_forest_bounds(n, P, E):
    """Brute force n<=5 minimum orbit-weight and leaf-discount bounds."""
    G = generate_group(P, n)
    identity = tuple(range(n))
    dist_identity = distances_from(identity, P)

    options = defaultdict(list)
    for ei, e in enumerate(E):
        arcs = orbit_data(G, e)
        m = len(arcs)
        for a, witnesses in arcs.items():
            eta = min(dist_identity[g] for g in witnesses)
            options[a].append((m, ei, eta))

    best_weight = inf
    best_discount = inf

    for root in range(n):
        vertices = [u for u in range(n) if u != root]
        choices = []
        feasible = True
        for u in vertices:
            c = []
            for (src, dst), vals in options.items():
                if src == u:
                    for m, ei, eta in vals:
                        c.append((dst, m, ei, eta))
            if not c:
                feasible = False
                break
            choices.append(c)
        if not feasible:
            continue

        for selected in product(*choices):
            outgoing = {u: selected[i][0] for i, u in enumerate(vertices)}
            ok = True
            for u in vertices:
                x = u
                seen = set()
                while x != root:
                    if x in seen or x not in outgoing:
                        ok = False
                        break
                    seen.add(x)
                    x = outgoing[x]
                if not ok:
                    break
            if not ok:
                continue

            weight = sum(row[1] for row in selected)
            best_weight = min(best_weight, weight)

            indeg = {u: 0 for u in range(n)}
            for row in selected:
                indeg[row[0]] += 1
            for u, row in zip(vertices, selected):
                dst, m, ei, eta = row
                if indeg[u] == 0:
                    discounted = weight - (m - 1 - eta)
                    best_discount = min(best_discount, discounted)

    return best_weight, best_discount


def minimum_hamiltonian_defect_path_total(n, P, E):
    """Minimum singular+permutation cost among defect arborescences that are paths."""
    G = generate_group(P, n)
    identity = tuple(range(n))
    all_dist = {g: distances_from(g, P) for g in G}
    arcs = {(g, ei): alpha(g, e) for g in G for ei, e in enumerate(E)}

    best_travel = inf

    def extend(cur_g, current_vertex, visited, travel):
        nonlocal best_travel
        if travel >= best_travel:
            return
        if len(visited) == n:
            best_travel = travel
            return
        for h in G:
            step = all_dist[cur_g][h]
            if travel + step >= best_travel:
                continue
            for ei in range(len(E)):
                src, dst = arcs[(h, ei)]
                if src == current_vertex and dst not in visited:
                    visited.add(dst)
                    extend(h, dst, visited, travel + step)
                    visited.remove(dst)

    for g in G:
        initial = all_dist[identity][g]
        for ei in range(len(E)):
            src, dst = arcs[(g, ei)]
            if src == dst:
                continue
            extend(g, dst, {src, dst}, initial)

    return inf if best_travel == inf else (n - 1) + best_travel


def check_family(n, mode):
    identity = tuple(range(n))
    perms = [p for p in permutations(range(n)) if p != identity]
    edges = [(s, t) for s in range(n) for t in range(n) if s != t]

    if mode == "1P1E":
        configs = (((p,), (e,)) for p in perms for e in edges)
    elif mode == "1P2E":
        configs = (((p,), E) for p in perms for E in combinations(edges, 2))
    elif mode == "2P1E":
        configs = ((P, (e,)) for P in combinations(perms, 2) for e in edges)
    else:
        raise ValueError(mode)

    counts = defaultdict(int)
    square = (n - 1) ** 2

    for P, E in configs:
        counts["total"] += 1
        verify_cosets_and_entrance(n, P, E)
        letters = list(P) + [simple_idempotent(n, *e) for e in E]
        rt = reset_threshold(n, letters)
        if rt is None:
            continue
        counts["synchronizing"] += 1

        weight, discounted = min_forest_bounds(n, P, E)
        assert rt <= weight
        assert rt <= discounted
        if weight <= square:
            counts["orbit_weight_square"] += 1
        if discounted <= square:
            counts["leaf_discount_square"] += 1

        # The exact Hamiltonian-path subclass is more expensive to compute;
        # use it for the 2P1E family where it is most informative.
        if mode == "2P1E":
            path_total = minimum_hamiltonian_defect_path_total(n, P, E)
            if path_total <= square:
                counts["path_square"] += 1
            if discounted <= square or path_total <= square:
                counts["discount_or_path_square"] += 1

    return dict(counts)


def targeted_s5_obstruction():
    # Permutations in image-tuple notation.  They generate S_5.
    n = 5
    P = (
        (0, 1, 2, 4, 3),
        (1, 2, 3, 0, 4),
    )
    E = ((0, 2),)
    G = generate_group(P, n)
    assert len(G) == 120
    verify_cosets_and_entrance(n, P, E)

    letters = list(P) + [simple_idempotent(n, 0, 2)]
    rt = reset_threshold(n, letters)
    assert rt == 14
    word = shortest_reset_word(n, letters)
    assert len(word) == 14

    weight, discounted = min_forest_bounds(n, P, E)
    assert weight == 80
    assert discounted == 61

    path_total = minimum_hamiltonian_defect_path_total(n, P, E)
    assert path_total == 21

    # Extract the conjugated defect arcs of one shortest reset word.
    g = tuple(range(n))
    arcs = []
    singular_positions = []
    for pos, letter_index in enumerate(word):
        if letter_index < len(P):
            g = compose(g, P[letter_index])
        else:
            arcs.append(alpha(g, E[0]))
            singular_positions.append(pos)
    assert arcs == [(0, 2), (1, 3), (4, 2), (2, 3)]
    assert singular_positions == [0, 5, 7, 13]

    return {
        "group_order": len(G),
        "reset_threshold": rt,
        "shortest_word_indices": word,
        "conjugated_defect_arcs": arcs,
        "singular_positions": singular_positions,
        "orbit_weight_bound": weight,
        "leaf_discount_bound": discounted,
        "best_hamiltonian_defect_path_total": path_total,
        "cerny_square": 16,
    }


def main():
    summaries = []
    for n in range(2, 5):
        summaries.append((n, "1P1E", check_family(n, "1P1E")))
        if n >= 3:
            summaries.append((n, "1P2E", check_family(n, "1P2E")))
            summaries.append((n, "2P1E", check_family(n, "2P1E")))

    print("EXHAUSTIVE_SMALL_FAMILIES")
    for row in summaries:
        print(row)

    print("TARGETED_S5_OBSTRUCTION")
    print(targeted_s5_obstruction())
    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
