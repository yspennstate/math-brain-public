#!/usr/bin/env python3
from itertools import combinations

def transitive_closure(n, covers):
    rel = set(covers)
    changed = True
    while changed:
        changed = False
        add = set()
        for a, b in rel:
            for c, d in rel:
                if b == c and (a, d) not in rel:
                    add.add((a, d))
        if add:
            before = len(rel)
            rel |= add
            changed = len(rel) != before
    return frozenset(rel)

def incomparable(rel, a, b):
    return (a, b) not in rel and (b, a) not in rel

def is_cover(n, rel, a, b):
    if (a, b) not in rel:
        return False
    return not any(
        z not in (a, b) and (a, z) in rel and (z, b) in rel
        for z in range(n)
    )

def width_le_three(n, rel):
    return not any(
        all(incomparable(rel, a, b) for a, b in combinations(S, 2))
        for S in combinations(range(n), 4)
    )

def linear_extensions(n, rel):
    preds = [0] * n
    for a, b in rel:
        preds[b] |= 1 << a
    out = []

    def rec(mask, order):
        if mask == (1 << n) - 1:
            out.append(tuple(order))
            return
        for v in range(n):
            if ((mask >> v) & 1) == 0 and (preds[v] & ~mask) == 0:
                rec(mask | (1 << v), order + [v])

    rec(0, [])
    return out

def count_before(exts, a, b):
    return sum(L.index(a) < L.index(b) for L in exts)

def relation(rel, v, w):
    if (v, w) in rel:
        return "<"
    if (w, v) in rel:
        return ">"
    return "||"

def distinguishers(n, rel, a, b):
    return [
        v for v in range(n)
        if v not in (a, b) and relation(rel, v, a) != relation(rel, v, b)
    ]

def balanced_pairs(n, rel, exts):
    E = len(exts)
    ans = []
    for a, b in combinations(range(n), 2):
        if incomparable(rel, a, b):
            c = count_before(exts, a, b)
            if 3 * min(c, E - c) >= E:
                ans.append((a, b, c, E - c))
    return ans

def orientation_count(exts, a, b):
    return count_before(exts, a, b)

def verify_case(name, n, cover_edges, state, mode):
    x, y, a, s, u = state
    rel = transitive_closure(n, cover_edges)
    assert width_le_three(n, rel)
    for p, q in cover_edges:
        assert is_cover(n, rel, p, q)

    # Same-right-ray canonical geometry:
    # x<.y and x<.s are the two F1 sibling upper covers;
    # a<.u is the F3 cover.
    assert is_cover(n, rel, x, y)
    assert is_cover(n, rel, x, s)
    assert is_cover(n, rel, a, u)
    assert incomparable(rel, a, x)
    assert incomparable(rel, a, y)
    assert incomparable(rel, a, s)
    assert incomparable(rel, y, s)
    assert incomparable(rel, y, u)

    if mode == "nested":
        assert (s, u) in rel
    elif mode == "saturated":
        assert incomparable(rel, s, u)
    else:
        raise AssertionError(mode)

    exts = linear_extensions(n, rel)
    E = len(exts)
    counts = {
        "x<a": orientation_count(exts, x, a),
        "y<a": orientation_count(exts, y, a),
        "y<s": orientation_count(exts, y, s),
        "y<u": orientation_count(exts, y, u),
        "a<s": orientation_count(exts, a, s),
    }

    # Heavy-edge / same-right-ray directions all mimic a no-balanced branch.
    assert 3 * counts["x<a"] > 2 * E
    assert 3 * counts["y<a"] < E
    assert 3 * counts["y<s"] > 2 * E
    assert 3 * counts["y<u"] > 2 * E
    assert 3 * counts["a<s"] > 2 * E

    # None of the five local key pairs closes POS3.
    for label, c in counts.items():
        assert 3 * min(c, E - c) < E, (name, label, c, E)

    D_as = distinguishers(n, rel, a, s)
    D_ys = distinguishers(n, rel, y, s)
    core = {x, y, a, s, u}

    if mode == "nested":
        # Exactly one core distinguisher of (a,s): x.
        assert set(D_as) & core == {x}
    else:
        # Width-saturating gate: zero core distinguishers of (y,s).
        assert set(D_ys) & core == set()
        # Sharpness of the two-external-distinguisher requirement in this witness.
        assert len(D_ys) == 2

    bal = balanced_pairs(n, rel, exts)
    # These are counterexamples only to the stronger LOCAL closure claim,
    # not to POS3: each whole poset still has balanced pairs elsewhere.
    assert bal

    print(name)
    print("  n =", n, "E =", E)
    print("  state (x,y,a,s,u) =", state)
    print("  covers =", sorted(cover_edges))
    print("  key_counts =", counts)
    print("  D(a,s) =", D_as, "D(y,s) =", D_ys)
    print("  balanced_pairs_elsewhere =", bal)
    return E, counts, D_as, D_ys, bal

nested = verify_case(
    "RIGHT_NESTED_LOCAL_CLOSURE_COUNTEREXAMPLE",
    8,
    [(0,5),(0,7),(1,2),(1,4),(2,5),(3,4),(3,6),(4,7),(5,6)],
    (1,2,0,4,7),
    "nested",
)
assert nested[0] == 128
assert nested[1] == {"x<a":89, "y<a":42, "y<s":90, "y<u":120, "a<s":105}

saturated = verify_case(
    "RIGHT_WIDTH_SATURATING_LOCAL_CLOSURE_COUNTEREXAMPLE",
    7,
    [(0,2),(0,3),(0,4),(1,4),(1,5),(2,5),(5,6)],
    (0,2,1,3,4),
    "saturated",
)
assert saturated[0] == 62
assert saturated[1] == {"x<a":42, "y<a":18, "y<s":45, "y<u":51, "a<s":52}
assert saturated[3] == [5, 6]

print("POS3_B19_SAME_RAY_EXPORT_CERTIFICATE_PASS")
