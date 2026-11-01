from itertools import combinations


def is_forest(n, edges, mask):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            parent[ru] = rv
    return True


def forest_masks(n, edges):
    return [m for m in range(1 << len(edges)) if is_forest(n, edges, m)]


n = 4
simple_edges = list(combinations(range(n), 2))
# Multiplicities on 01,02,03,12,13,23.
mult = [2, 3, 1, 2, 1, 1]
mark_e_class, mark_f_class = 0, 1

# Actual labelled multigraph.
multiedges = []
classes = []
for edge, k in zip(simple_edges, mult):
    cls = []
    for _ in range(k):
        cls.append(len(multiedges))
        multiedges.append(edge)
    classes.append(cls)
me, mf = classes[mark_e_class][0], classes[mark_f_class][0]
M = forest_masks(n, multiedges)
Z = Ze = Zf = Zef = 0
for mask in M:
    Z += 1
    xe = (mask >> me) & 1
    xf = (mask >> mf) & 1
    Ze += xe
    Zf += xf
    Zef += xe & xf
multigraph_counts = (Z, Ze, Zf, Zef)
multigraph_gap = Ze * Zf - Z * Zef

# Collapsed simple graph with class activities.  A fixed copy of a marked
# class corresponds to the derivative in that class variable.
S = forest_masks(n, simple_edges)
WZ = WZe = WZf = WZef = 0
for mask in S:
    w = 1
    for i, k in enumerate(mult):
        if (mask >> i) & 1:
            w *= k
    WZ += w
    if (mask >> mark_e_class) & 1:
        WZe += w // mult[mark_e_class]
    if (mask >> mark_f_class) & 1:
        WZf += w // mult[mark_f_class]
    if ((mask >> mark_e_class) & 1) and ((mask >> mark_f_class) & 1):
        WZef += w // (mult[mark_e_class] * mult[mark_f_class])
weighted_counts = (WZ, WZe, WZf, WZef)
weighted_gap = WZe * WZf - WZ * WZef

print('MULTIGRAPH_COLLAPSE_AUDIT')
print('edge_labels =', len(multiedges))
print('forest_count =', len(M))
print('multigraph_counts =', multigraph_counts)
print('weighted_derivative_counts =', weighted_counts)
print('multigraph_gap =', multigraph_gap)
print('weighted_gap =', weighted_gap)
print('identity =', multigraph_counts == weighted_counts and multigraph_gap == weighted_gap)

assert multigraph_counts == weighted_counts
assert multigraph_gap == weighted_gap
