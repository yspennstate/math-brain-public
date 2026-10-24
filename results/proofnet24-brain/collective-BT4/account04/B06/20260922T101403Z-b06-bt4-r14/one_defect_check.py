from itertools import combinations
from collections import defaultdict


def states_from_word(word, m, n):
    coords = [(0, 0)]
    for t in range(1, len(word)):
        i, j = coords[-1]
        if word[t] == '+':
            i = (i - 1) % m
        else:
            j = (j - 1) % n
        coords.append((i, j))
    i, j = coords[-1]
    if word[0] == '+':
        i = (i - 1) % m
    else:
        j = (j - 1) % n
    assert (i, j) == coords[0]
    return coords


def graph_from_word(word, m, n):
    coords = states_from_word(word, m, n)
    adj = defaultdict(set)
    for i in range(m):
        adj[('A', i)].add(('A', (i + 1) % m))
    for j in range(n):
        adj[('B', j)].add(('B', (j + 1) % n))
    for sign, (i, j) in zip(word, coords):
        if sign == '+':
            adj[('A', i)].add(('B', j))
        else:
            adj[('B', j)].add(('A', i))
    return adj, coords


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
                elif w not in used and rank[w] >= rank[start] and len(path) < len(vertices):
                    used.add(w)
                    path.append(w)
                    dfs(w)
                    path.pop()
                    used.remove(w)

        dfs(start)
    return list(dict.fromkeys(cycles))


def disjoint_mixed_pair(adj):
    mixed = []
    for c in simple_cycles(adj):
        kinds = {v[0] for v in c}
        if 'A' in kinds and 'B' in kinds:
            mixed.append(c)
    sets = [set(c) for c in mixed]
    for i in range(len(mixed)):
        for j in range(i + 1, len(mixed)):
            if sets[i].isdisjoint(sets[j]):
                return mixed[i], mixed[j]
    return None


def normalized_words(m, n):
    L = m + n
    for plus_positions in combinations(range(L), m):
        if 0 not in plus_positions:
            continue
        chars = ['-'] * L
        for p in plus_positions:
            chars[p] = '+'
        yield ''.join(chars)


total = success = 0
print('single-defect audit; normalized primitive words; 2<=m,n<=5')
for m in range(2, 6):
    for n in range(2, 6):
        tests = hits = 0
        for word in normalized_words(m, n):
            adj, coords = graph_from_word(word, m, n)
            trace_plus = {c for s, c in zip(word, coords) if s == '+'}
            trace_minus = {c for s, c in zip(word, coords) if s == '-'}
            for i in range(m):
                for j in range(n):
                    for sign, trace in (('+', trace_plus), ('-', trace_minus)):
                        if (i, j) in trace:
                            continue
                        tests += 1
                        aug = defaultdict(set, {u: set(vs) for u, vs in adj.items()})
                        if sign == '+':
                            aug[('A', i)].add(('B', j))
                        else:
                            aug[('B', j)].add(('A', i))
                        if disjoint_mixed_pair(aug) is not None:
                            hits += 1
        total += tests
        success += hits
        print(f'm={m} n={n} one_defect_tests={tests} two_disjoint_mixed={hits}')
print(f'TOTAL one_defect_tests={total} two_disjoint_mixed={success}')

# Sharpness: two defects suffice, even in the same direction.
word = '+-+-'
m = n = 2
adj, coords = graph_from_word(word, m, n)
adj[('A', 0)].add(('B', 1))
adj[('A', 1)].add(('B', 0))
witness = disjoint_mixed_pair(adj)
print('sharp_word', word)
print('states', list(zip(word, coords)))
print('added_defects', [(('A', 0), ('B', 1)), (('A', 1), ('B', 0))])
print('sharp_disjoint_pair', witness)
