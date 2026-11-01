"""Exact verifier for HARD8-02, 2026-09-16 second checkpoint.

No floating point and no external solver are used.

The script verifies:
1. A 9-vertex non-caterpillar base tree is graceful.
2. Exhaustive enumeration of all of its graceful labelings finds that the
   designated root is never labeled 0 or 8 (so endpoint/0-rotatable extension
   at that root is unavailable for this base tree).
3. The displayed labeling has an interior one-gap certificate (L,k)=(4,1),
   high-root branch.
4. The closed-form labeling after attaching t pendant leaves at that same
   root is graceful for t=0,...,50.  The accompanying report proves the
   formula for every t>=0 symbolically.
"""

from itertools import permutations

BASE_VERTICES = tuple(range(9))
BASE_EDGES = (
    (0, 1), (0, 4), (0, 7), (1, 2),
    (2, 3), (4, 5), (4, 6), (7, 8),
)
ROOT = 3

BASE_LABEL = {
    0: 0,
    4: 1,
    8: 2,
    2: 3,
    5: 4,
    3: 5,
    6: 6,
    1: 7,
    7: 8,
}
L = 4
K = 1


def edge_differences(edges, lab):
    return sorted(abs(lab[u] - lab[v]) for u, v in edges)


def is_graceful(vertices, edges, lab):
    n = len(vertices)
    return (
        sorted(lab.values()) == list(range(n))
        and edge_differences(edges, lab) == list(range(1, n))
    )


def crossing_vector(edges, lab, L):
    by_diff = {}
    for u, v in edges:
        d = abs(lab[u] - lab[v])
        assert d not in by_diff
        by_diff[d] = (u, v)
    m = len(edges)
    ans = []
    for d in range(1, m + 1):
        u, v = by_diff[d]
        ans.append(int((lab[u] < L) != (lab[v] < L)))
    return ans


def exhaustive_graceful_labelings():
    """Backtracking enumeration of every graceful labeling of the base tree."""
    n = len(BASE_VERTICES)
    adjacency = {v: [] for v in BASE_VERTICES}
    for u, v in BASE_EDGES:
        adjacency[u].append(v)
        adjacency[v].append(u)

    # High-degree-first order is only a speed choice; search remains exhaustive.
    order = sorted(BASE_VERTICES, key=lambda v: (-len(adjacency[v]), v))
    used_labels = [False] * n
    used_diffs = [False] * n
    lab = {}
    all_labelings = []

    def rec(i):
        if i == n:
            all_labelings.append(dict(lab))
            return
        v = order[i]
        for a in range(n):
            if used_labels[a]:
                continue
            new_diffs = []
            ok = True
            for u in adjacency[v]:
                if u not in lab:
                    continue
                d = abs(a - lab[u])
                if d == 0 or used_diffs[d] or d in new_diffs:
                    ok = False
                    break
                new_diffs.append(d)
            if not ok:
                continue
            lab[v] = a
            used_labels[a] = True
            for d in new_diffs:
                used_diffs[d] = True
            rec(i + 1)
            for d in new_diffs:
                used_diffs[d] = False
            used_labels[a] = False
            del lab[v]

    rec(0)
    return all_labelings


def amplified_tree(t):
    """Attach t new leaves to ROOT and return vertices, edges, exact labeling."""
    assert t >= 0
    leaves = tuple(range(9, 9 + t))
    vertices = BASE_VERTICES + leaves
    edges = list(BASE_EDGES) + [(ROOT, z) for z in leaves]

    # High-root branch of the pendant-star amplification theorem.
    lab = {}
    for v in BASE_VERTICES:
        a = BASE_LABEL[v]
        lab[v] = a if a < L else a + t
    for j, z in enumerate(leaves):
        lab[z] = L + j
    return vertices, tuple(edges), lab


def is_caterpillar(vertices, edges):
    deg = {v: 0 for v in vertices}
    nbr = {v: [] for v in vertices}
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
        nbr[u].append(v)
        nbr[v].append(u)
    core = [v for v in vertices if deg[v] > 1]
    core_set = set(core)
    core_deg = {v: sum(1 for u in nbr[v] if u in core_set) for v in core}
    if not core:
        return True
    # A connected induced core is a path iff all core degrees are <=2.
    return max(core_deg.values(), default=0) <= 2


def main():
    assert is_graceful(BASE_VERTICES, BASE_EDGES, BASE_LABEL)
    cv = crossing_vector(BASE_EDGES, BASE_LABEL, L)
    assert cv == [0] * K + [1] * (len(BASE_EDGES) - K), cv
    assert BASE_LABEL[ROOT] == L + K  # high-root branch

    labs = exhaustive_graceful_labelings()
    assert len(labs) == 248, len(labs)
    root_values = sorted({lab[ROOT] for lab in labs})
    assert 0 not in root_values and 8 not in root_values, root_values

    # Exact finite checks of the symbolic all-t formula.
    for t in range(51):
        vertices, edges, lab = amplified_tree(t)
        assert is_graceful(vertices, edges, lab), t
        if t >= 1:
            assert not is_caterpillar(vertices, edges), t

    print("base graceful labelings:", len(labs))
    print("root labels attained:", root_values)
    print("interior certificate crossing vector:", cv)
    print("verified amplified graceful family for t=0..50")
    print("for t>=1 the checked family is non-caterpillar")


if __name__ == "__main__":
    main()
