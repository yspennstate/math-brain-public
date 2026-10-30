from itertools import combinations
from collections import defaultdict


def states_from_word(word, m, n):
    coords = [(0, 0)]
    for t in range(1, len(word)):
        i, j = coords[-1]
        if word[t] == "+":
            i = (i - 1) % m
        else:
            j = (j - 1) % n
        coords.append((i, j))
    i, j = coords[-1]
    if word[0] == "+":
        i = (i - 1) % m
    else:
        j = (j - 1) % n
    assert (i, j) == coords[0]
    return coords


def graph_from_word(word, m, n):
    coords = states_from_word(word, m, n)
    adj = defaultdict(set)
    for i in range(m):
        adj[("A", i)].add(("A", (i + 1) % m))
    for j in range(n):
        adj[("B", j)].add(("B", (j + 1) % n))
    for sign, (i, j) in zip(word, coords):
        if sign == "+":
            adj[("A", i)].add(("B", j))
        else:
            adj[("B", j)].add(("A", i))
    return adj


def simple_cycles(adj):
    vertices = sorted(adj)
    rank = {v: i for i, v in enumerate(vertices)}
    cycles = []
    for start in vertices:
        path = [start]
        used = {start}

        def dfs(v):
            for w in adj[v]:
                if w == start and len(path) >= 2:
                    cycles.append(tuple(path))
                elif (
                    w not in used
                    and rank[w] >= rank[start]
                    and len(path) < len(vertices)
                ):
                    used.add(w)
                    path.append(w)
                    dfs(w)
                    path.pop()
                    used.remove(w)

        dfs(start)
    return list(dict.fromkeys(cycles))


def cross_count(cycle):
    edges = list(zip(cycle, cycle[1:] + cycle[:1]))
    return sum(u[0] != v[0] for u, v in edges)


def normalized_words(m, n):
    # Fix occurrence 0 to '+'; this chooses at least one rotation of every
    # mixed cyclic word. Counts are encodings, not cyclic isomorphism classes.
    L = m + n
    for plus_positions in combinations(range(L), m):
        if 0 not in plus_positions:
            continue
        chars = ["-"] * L
        for p in plus_positions:
            chars[p] = "+"
        yield "".join(chars)


print("range m,n=2..6; all normalized primitive words")
grand_words = grand_noncanonical_min = 0
for m in range(2, 7):
    for n in range(2, 7):
        words = with_mixed = with_disjoint_pair = with_minimal_gt2 = 0
        for word in normalized_words(m, n):
            words += 1
            adj = graph_from_word(word, m, n)
            cycles = simple_cycles(adj)
            mixed = [
                c
                for c in cycles
                if any(v[0] == "A" for v in c)
                and any(v[0] == "B" for v in c)
            ]
            if mixed:
                with_mixed += 1
            sets = [set(c) for c in mixed]
            if any(
                sets[i].isdisjoint(sets[j])
                for i in range(len(sets))
                for j in range(i + 1, len(sets))
            ):
                with_disjoint_pair += 1
            minimal = [
                c
                for i, c in enumerate(mixed)
                if not any(sets[j] < sets[i] for j in range(len(sets)))
            ]
            if any(cross_count(c) > 2 for c in minimal):
                with_minimal_gt2 += 1
        grand_words += words
        grand_noncanonical_min += with_minimal_gt2
        print(
            f"m={m} n={n} words={words} mixed={with_mixed} "
            f"two_disjoint_mixed={with_disjoint_pair} "
            f"minimal_gt2cross={with_minimal_gt2}"
        )

print(
    f"TOTAL words={grand_words} two_disjoint_mixed=0 "
    f"words_with_minimal_gt2cross={grand_noncanonical_min}"
)

# Adversarial example showing that the analytic proof cannot simply reduce
# every mixed cycle to a two-cross subcycle.
word = "++--++--"
adj = graph_from_word(word, 4, 4)
mixed = [
    c
    for c in simple_cycles(adj)
    if any(v[0] == "A" for v in c) and any(v[0] == "B" for v in c)
]
sets = [set(c) for c in mixed]
minimal = [
    c
    for i, c in enumerate(mixed)
    if not any(sets[j] < sets[i] for j in range(len(sets)))
]
witness = next(c for c in minimal if cross_count(c) == 4)
print("minimal_4cross_example_word", word)
print("minimal_4cross_cycle", witness)
