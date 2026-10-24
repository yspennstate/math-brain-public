from fractions import Fraction as F
from itertools import combinations, permutations

V = range(6)
COLORS = range(3)
EDGES = list(combinations(V, 2))

w = {c: {e: F(0) for e in EDGES} for c in COLORS}

# Synthetic colored edge marginals.  This is deliberately NOT claimed to
# come from an orthogonal decomposition / projection DPP.
w[0][(2, 3)] = F(1, 3)
w[0][(4, 5)] = F(2, 3)

w[1][(0, 2)] = F(1, 3)
w[1][(1, 3)] = F(1, 3)
w[1][(2, 5)] = F(1, 3)

w[2][(0, 1)] = F(2, 3)
w[2][(3, 4)] = F(1, 3)

color_totals = {c: sum(w[c].values(), F(0)) for c in COLORS}
m = {e: sum(w[c][e] for c in COLORS) for e in EDGES}
vertex_degrees = {
    i: sum(m[tuple(sorted((i, j)))] for j in V if j != i)
    for i in V
}
three_set_internal = {
    S: sum(m[e] for e in combinations(S, 2))
    for S in combinations(V, 3)
}


def perfect_matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield []
        return
    a = vertices[0]
    for k in range(1, len(vertices)):
        b = vertices[k]
        rest = vertices[1:k] + vertices[k + 1 :]
        for tail in perfect_matchings(rest):
            yield [(min(a, b), max(a, b))] + tail


matchings = list(perfect_matchings(tuple(V)))
rainbow_supported = []
for matching in matchings:
    for color_assignment in permutations(COLORS):
        if all(w[c][e] > 0 for e, c in zip(matching, color_assignment)):
            rainbow_supported.append((matching, color_assignment))

assert all(x == 1 for x in color_totals.values())
assert all(x == 1 for x in vertex_degrees.values())
assert all(x <= 1 for x in three_set_internal.values())
assert len(matchings) == 15
assert not rainbow_supported

print("color_totals=", color_totals)
print("vertex_degrees=", vertex_degrees)
print("max_three_set_internal=", max(three_set_internal.values()))
print("perfect_matchings=", len(matchings))
print("rainbow_supported_matchings=", len(rainbow_supported))
for S, value in three_set_internal.items():
    if value:
        print("three_set", S, value)
print("ALL_EXACT_CHECKS_PASS")
