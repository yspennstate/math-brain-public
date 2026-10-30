from itertools import permutations


def transitive_closure(n, covers):
    rel = set(map(tuple, covers))
    changed = True
    while changed:
        changed = False
        for a, b in list(rel):
            for c, d in list(rel):
                if b == c and (a, d) not in rel:
                    rel.add((a, d))
                    changed = True
    assert not any(a == b for a, b in rel)
    return rel


def linear_extensions(n, rel):
    out = []
    for perm in permutations(range(n)):
        pos = {x: i for i, x in enumerate(perm)}
        if all(pos[a] < pos[b] for a, b in rel):
            out.append(perm)
    return out


def check_uniform_module(n, covers, module):
    rel = transitive_closure(n, covers)
    exts = linear_extensions(n, rel)
    counts = {}
    for ext in exts:
        restriction = tuple(x for x in ext if x in module)
        counts[restriction] = counts.get(restriction, 0) + 1
    return len(exts), counts, len(set(counts.values())) == 1


examples = [
    (5, [(2, 0), (2, 1), (2, 3)], {0, 1}),
    (6, [(0, 2), (1, 2), (3, 0), (3, 1), (3, 2), (0, 4), (1, 4), (2, 4)], {0, 1, 2}),
    (6, [(3, 0), (3, 1), (3, 2), (0, 4), (1, 4), (2, 4), (3, 4)], {0, 1, 2}),
    (6, [(0, 1), (3, 0), (3, 1), (3, 2), (0, 5), (1, 5), (2, 5)], {0, 1, 2}),
]

for i, example in enumerate(examples, 1):
    total, counts, ok = check_uniform_module(*example)
    print(i, total, counts, ok)
    assert ok

print("POS3_AUTONOMOUS_MODULE_CHECK_PASS")
