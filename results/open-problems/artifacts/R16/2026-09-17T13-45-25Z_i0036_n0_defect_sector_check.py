from collections import defaultdict
from math import comb, factorial

# Exact finite self-check for the R16/I0036 n->0 defect-sector discussion.
# The graph is a degree-one terminal path a-p-b together with m disjoint
# hexagons.  We enumerate every edge subset and record (loop_count, edge_count)
# in the empty and {a,b}-defect sectors.  Integer arithmetic only.
#
# This is a finite illustration/certificate for the displayed polynomial
# identities.  The general decomposition theorem is proved on the page.


def build_graph(m):
    edges = [('a', 'p'), ('p', 'b')]
    for j in range(m):
        vs = [f'c{j}_{i}' for i in range(6)]
        for i in range(6):
            edges.append((vs[i], vs[(i + 1) % 6]))
    return edges


def odd_vertices(subset):
    deg = defaultdict(int)
    for u, v in subset:
        deg[u] += 1
        deg[v] += 1
    return frozenset(v for v, d in deg.items() if d % 2)


def loop_components(subset):
    if not subset:
        return 0
    adj = defaultdict(list)
    verts = set()
    for u, v in subset:
        adj[u].append(v)
        adj[v].append(u)
        verts.add(u)
        verts.add(v)
    seen = set()
    loops = 0
    for s in verts:
        if s in seen:
            continue
        stack = [s]
        comp = []
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            comp.append(x)
            stack.extend(adj[x])
        if all(len(adj[x]) == 2 for x in comp):
            loops += 1
    return loops


def sector_coeffs(m, defects):
    edges = build_graph(m)
    ans = defaultdict(int)
    for mask in range(1 << len(edges)):
        subset = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        if odd_vertices(subset) == frozenset(defects):
            ans[(loop_components(subset), len(subset))] += 1
    return dict(sorted(ans.items()))


for m in range(1, 4):
    defect = sector_coeffs(m, {'a', 'b'})
    empty = sector_coeffs(m, set())

    expected_defect = {(j, 2 + 6 * j): comb(m, j) for j in range(m + 1)}
    expected_empty = {(j, 6 * j): comb(m, j) for j in range(m + 1)}

    assert defect == expected_defect
    assert empty == expected_empty

    # n=0 keeps exactly the loop-free term.
    assert defect.get((0, 2), 0) == 1
    assert sum(c for (j, _e), c in defect.items() if j == 0) == 1
    assert empty.get((0, 0), 0) == 1
    assert sum(c for (j, _e), c in empty.items() if j == 0) == 1

    # The j-th derivative at n=0 is j! times the exactly-j-loop coefficient.
    for j in range(m + 1):
        coeff_defect = defect[(j, 2 + 6 * j)]
        coeff_empty = empty[(j, 6 * j)]
        assert factorial(j) * coeff_defect == factorial(j) * comb(m, j)
        assert factorial(j) * coeff_empty == factorial(j) * comb(m, j)

    print(f'm={m}')
    print('  defect coefficients:', defect)
    print('  empty coefficients: ', empty)

print('IDENTITIES:')
print('  Z_defect(m=3) = x^2 (1 + n x^6)^3')
print('  Z_empty(m=3)  =       (1 + n x^6)^3')
print('  at n=0: Z_defect=x^2 and Z_empty=1')
print('  d^j/dn^j at n=0 = j! times the exactly-j-loop coefficient')
print('ALL_EXACT_CHECKS_PASS')
