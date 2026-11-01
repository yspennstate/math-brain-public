from fractions import Fraction


def is_forest(n, edges, mask):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, (u, v) in enumerate(edges):
        if not ((mask >> i) & 1):
            continue
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[rv] = ru
    return True


def stats(n, edges, ei, fi):
    Z = Ze = Zf = Zef = 0
    for mask in range(1 << len(edges)):
        if not is_forest(n, edges, mask):
            continue
        Z += 1
        a = (mask >> ei) & 1
        b = (mask >> fi) & 1
        Ze += a
        Zf += b
        Zef += a * b
    gap = Ze * Zf - Z * Zef
    cov = Fraction(Zef, Z) - Fraction(Ze, Z) * Fraction(Zf, Z)
    return Z, Ze, Zf, Zef, gap, cov

# Two parallel physical edges: a smallest loopless-multigraph regression.
multigraph = [(0, 1), (0, 1)]
ms = stats(2, multigraph, 0, 1)
assert ms[:5] == (3, 1, 1, 0, 1)
assert ms[5] == Fraction(-1, 9)

# Replace each physical edge by three internally disjoint length-two paths.
simple_edges = []
representatives = []
next_vertex = 2
for _ in range(2):
    for path_index in range(3):
        w = next_vertex
        next_vertex += 1
        left_index = len(simple_edges)
        simple_edges.extend([(0, w), (w, 1)])
        if path_index == 0:
            representatives.append(left_index)

ss = stats(next_vertex, simple_edges, representatives[0], representatives[1])
assert ss[:5] == (2187, 891, 891, 351, 26244)
assert ss[5] == Fraction(-4, 729)
assert ss[5] / ms[5] == Fraction(4, 81)

print("MULTIGRAPH_STATS", ms)
print("THETA3_SIMPLE_STATS", ss)
print("COVARIANCE_RATIO", ss[5] / ms[5])
print("STATUS=THETA3_SCALING_EXACT_PASS")
