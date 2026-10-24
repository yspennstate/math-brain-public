from collections import defaultdict

# Exact finite self-check for the first n-derivative identity in the
# two-defect loop O(n) sector.
#
# Graph: terminals a,b joined through one edge of a hexagon.
# There are two loop-free a-b SAWs (length 3 and length 7) and one empty-sector
# loop (the length-6 hexagon).  The hexagon intersects both SAWs, so the
# one-loop coefficient in the defect sector is zero.  Integer arithmetic only.

EDGES = [
    ('a', 'u'), ('u', 'v'), ('v', 'b'),
    ('u', 'w1'), ('w1', 'w2'), ('w2', 'w3'), ('w3', 'w4'), ('w4', 'v')
]


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


def sector_coeffs(defects):
    ans = defaultdict(int)
    for mask in range(1 << len(EDGES)):
        subset = [EDGES[i] for i in range(len(EDGES)) if (mask >> i) & 1]
        if odd_vertices(subset) == frozenset(defects):
            ans[(loop_components(subset), len(subset))] += 1
    return dict(sorted(ans.items()))


defect = sector_coeffs({'a', 'b'})
empty = sector_coeffs(set())

assert defect == {(0, 3): 1, (0, 7): 1}
assert empty == {(0, 0): 1, (1, 6): 1}

# Hence A0=x^3+x^7, A1=0, B0=1, B1=x^6.  For R(n)=A(n)/B(n),
# R'(0)=A1-A0*B1=-(x^9+x^13), exactly the negative weight of the two
# (SAW,hexagon) pairs whose members intersect.
# We certify this symbolically by exponent->coefficient dictionaries.
A0 = {3: 1, 7: 1}
A1 = {}
B1 = {6: 1}

product = defaultdict(int)
for ea, ca in A0.items():
    for eb, cb in B1.items():
        product[ea + eb] += ca * cb

Rprime = {e: -c for e, c in sorted(product.items())}
assert Rprime == {9: -1, 13: -1}

print('defect coefficients:', defect)
print('empty coefficients: ', empty)
print("A0 = x^3 + x^7; A1 = 0; B1 = x^6")
print("R'(0) = -(x^9 + x^13)")
print('This equals minus the total weight of the two intersecting (SAW,hexagon) pairs.')
print('ALL_EXACT_CHECKS_PASS')
