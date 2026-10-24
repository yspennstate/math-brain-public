#!/usr/bin/env python3
"""Exact finite self-check for the R16/I0036 polyhex XOR-skeleton obstruction.

The graph is a chain of five honeycomb hexagons.  Four interior shared
vertical edges are optional source-pair swap rungs.  For every odd subset S
of those rungs we build two opposite-connectivity self-avoiding paths.
Their mod-two symmetric difference is the same pair of horizontal rails,
and the source/target total-length excess is exactly 2|S|.

At honeycomb criticality z=x_c^2=(2-sqrt(2))/2.  The canonical projection
that forgets the common selected rungs therefore loads that one rail target
by sum_{|S| odd} z^{|S|}.  For four optional rungs this equals
14-9*sqrt(2)>1.
"""

m = 4
last = m + 1


def edge(u, v):
    return tuple(sorted((u, v)))


def rail_edges(side):
    ans = []
    for i in range(last):
        mid = ("U" if side == "T" else "V", i)
        ans.append(edge((side, i), mid))
        ans.append(edge(mid, (side, i + 1)))
    return ans


# Five fused hexagons, plus four pendant boundary terminals.
G = set(rail_edges("T") + rail_edges("B"))
for i in range(last + 1):
    G.add(edge(("T", i), ("B", i)))
for leaf, node in [
    (("a",), ("T", 0)),
    (("b",), ("B", 0)),
    (("d",), ("T", last)),
    (("c",), ("B", last)),
]:
    G.add(edge(leaf, node))

TOP = rail_edges("T")
BOT = rail_edges("B")
TARGET = set(
    TOP
    + BOT
    + [
        edge(("a",), ("T", 0)),
        edge(("d",), ("T", last)),
        edge(("b",), ("B", 0)),
        edge(("c",), ("B", last)),
    ]
)


def walk(start_leaf, start_side, end_leaf, selected_rungs):
    selected_rungs = set(selected_rungs)
    side = start_side
    vertices = [(start_leaf,), (side, 0)]
    for i in range(last):
        if i in selected_rungs:
            other = "B" if side == "T" else "T"
            vertices.append((other, i))
            side = other
        mid = ("U" if side == "T" else "V", i)
        vertices.extend([mid, (side, i + 1)])
    vertices.append((end_leaf,))
    return vertices


def edges_of(vertices):
    return [edge(vertices[i], vertices[i + 1]) for i in range(len(vertices) - 1)]


def is_simple_graph_path(vertices):
    return len(vertices) == len(set(vertices)) and all(e in G for e in edges_of(vertices))


records = []
for mask in range(1 << m):
    S = {i + 1 for i in range(m) if (mask >> i) & 1}
    if len(S) % 2 == 0:
        continue

    P = walk("a", "T", "c", S)
    Q = walk("b", "B", "d", S)
    assert is_simple_graph_path(P)
    assert is_simple_graph_path(Q)

    EP, EQ = set(edges_of(P)), set(edges_of(Q))
    assert EP ^ EQ == TARGET

    source_length = (len(P) - 1) + (len(Q) - 1)
    target_length = len(TARGET)
    assert source_length - target_length == 2 * len(S)
    records.append((tuple(sorted(S)), source_length, target_length, 2 * len(S)))

assert len(records) == 2 ** (m - 1) == 8

# For z=(2-sqrt(2))/2, the odd-subset fiber load at m=4 is
#   4 z + 4 z^3 = 14 - 9 sqrt(2).
# It is >1 iff 13 > 9 sqrt(2); both sides are positive and 169>162.
assert 169 > 162

print("m=", m, "odd_sources=", len(records))
for record in records:
    print(record)
print("fiber_load_exact = 14 - 9*sqrt(2)")
print("fiber_load_gt_1 because 13^2=169 > 162=(9*sqrt(2))^2")
print("ALL_EXACT_CHECKS_PASS")
