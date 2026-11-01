#!/usr/bin/env python3
"""Exact combinatorial verifier for a 23-cell obstruction found in HARD8-08.

Geometry encoded by this graph:
- Tile the plane by regular hexagons of side s=1/4.
- Centers are indexed by (a,b) in Z^2 with basis
      u=(sqrt(3)/4, 0), v=(sqrt(3)/8, 3/8).
- For two cells whose index difference is (da,db), set
      Q=da^2+da*db+db^2.
- For Q in {3,4,7,9}, there are points in the interiors of the two
  hexagons at distance <1 and points in the interiors at distance >1;
  by continuity there is an interior pair at distance exactly 1.

The exact witnesses are described in the accompanying report.  Therefore
cells joined by an edge in this finite graph must receive different colors
in any coloring that makes every hexagon interior monochromatic.

This script exhaustively verifies that the 23-vertex graph is not
6-colorable and supplies a 7-coloring witness.  It uses only Python's
standard library and exact integer arithmetic for the graph itself.
"""

NODES = [
    (-2,0), (-2,2),
    (-1,0), (-1,1), (-1,2), (-1,3),
    (0,-2), (0,-1), (0,0), (0,1), (0,2),
    (1,-2), (1,-1), (1,0), (1,1), (1,2),
    (2,-3), (2,-2), (2,-1), (2,0), (2,1),
    (3,-2), (3,-1),
]
FORBIDDEN_Q = {3, 4, 7, 9}


def qnorm(p, q):
    a = q[0] - p[0]
    b = q[1] - p[1]
    return a*a + a*b + b*b


def build_graph():
    adj = {v: set() for v in NODES}
    for i, p in enumerate(NODES):
        for q in NODES[i+1:]:
            if qnorm(p, q) in FORBIDDEN_Q:
                adj[p].add(q)
                adj[q].add(p)
    return adj


def search_coloring(adj, k):
    """Exhaustive DSATUR-style backtracking. Returns (coloring_or_None, calls)."""
    nodes = list(NODES)
    colors = {}
    saturation = {v: set() for v in nodes}
    degree = {v: len(adj[v]) for v in nodes}
    calls = 0

    def choose_vertex():
        remaining = [v for v in nodes if v not in colors]
        return max(remaining, key=lambda v: (len(saturation[v]), degree[v], v))

    def recurse():
        nonlocal calls
        calls += 1
        if len(colors) == len(nodes):
            return dict(colors)

        v = choose_vertex()
        used = {colors[w] for w in adj[v] if w in colors}
        for c in range(k):
            if c in used:
                continue
            colors[v] = c
            changed = []
            for w in adj[v]:
                if w not in colors and c not in saturation[w]:
                    saturation[w].add(c)
                    changed.append(w)

            # If an uncolored vertex already sees all k colors, this branch is dead.
            if all(len(saturation[w]) < k for w in nodes if w not in colors):
                ans = recurse()
                if ans is not None:
                    return ans

            for w in changed:
                saturation[w].remove(c)
            del colors[v]
        return None

    return recurse(), calls


def verify_coloring(adj, coloring, k):
    assert coloring is not None
    assert set(coloring) == set(NODES)
    assert all(0 <= coloring[v] < k for v in NODES)
    for v in NODES:
        for w in adj[v]:
            assert coloring[v] != coloring[w]


def main():
    adj = build_graph()
    m = sum(len(adj[v]) for v in NODES) // 2
    assert len(NODES) == 23
    assert m == 143

    six, calls6 = search_coloring(adj, 6)
    assert six is None

    seven, calls7 = search_coloring(adj, 7)
    verify_coloring(adj, seven, 7)

    print("vertices:", len(NODES))
    print("edges:", m)
    print("forbidden Q shells:", sorted(FORBIDDEN_Q))
    print("6-colorable: NO")
    print("6-color search calls:", calls6)
    print("7-colorable: YES")
    print("7-color search calls:", calls7)
    print("7-coloring witness:")
    for v in sorted(NODES):
        print(v, seven[v])


if __name__ == "__main__":
    main()
