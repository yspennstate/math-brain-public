#!/usr/bin/env python3
"""Exact verifier for HARD8-08 checkpoint 7.

Reconstructs the 33-vertex {1,sqrt(3)} graph from the integer coordinate
quadruples in Table 1 of De Neve et al., counts distance types exactly,
checks an explicit 6-colouring, proves non-5-colourability by deterministic
DSATUR backtracking, and validates explicit 5-colour witnesses after deleting
each of the 32 sqrt(3)-edges.

No floating point, randomness, external solver, or timeout inference.
"""

COORDS = [(0, 0, 0, 0), (0, 0, 0, 4), (1, 3, -1, 1), (1, 3, 1, 3), (-1, 3, 1, 1), (-1, 3, -1, 3), (1, -3, 1, 1), (1, -3, -1, 3), (2, 0, 0, 2), (0, 0, 2, 2), (0, 0, -2, 2), (-1, -3, 1, 3), (-2, 0, 0, 2), (-2, 0, 2, 4), (-1, 3, 3, 3), (-3, 3, -1, 1), (-3, 3, 1, 3), (3, 3, -1, 3), (1, 3, 3, 1), (3, -3, 1, 3), (3, -3, -1, 1), (4, 0, 0, 4), (4, 0, 0, 0), (-3, -3, -1, 3), (-3, -3, 1, 1), (-2, 0, -2, 4), (-2, 0, 2, 0), (-4, 0, 0, 4), (-4, 0, 0, 0), (1, -3, 3, 3), (1, -3, -3, 1), (-1, -3, -3, 3), (-1, -3, 3, 1)]
DELETION_WITNESSES = [(1, 1, 17, '311212230003014432342342233411414'), (2, 1, 18, '411232230003012324412341431413244'), (3, 1, 20, '311212230003014422332444233311414'), (4, 1, 24, '311212230003014422342343243411314'), (5, 2, 16, '132121320002014333244132133444421'), (6, 2, 21, '132121320002014433243142133434421'), (7, 2, 25, '132131320032013224424133302444141'), (8, 3, 7, '122121230003012333444122133444421'), (9, 3, 22, '123121230023014432341344103122434'), (10, 3, 26, '123121230003014432331444133122244'), (11, 3, 31, '123121230023014432331444103122344'), (12, 4, 8, '132121310002014433242142133434421'), (13, 4, 23, '132121320002014433244112133434421'), (14, 4, 27, '132421310002014433244122134431423'), (15, 4, 30, '132121320002014433241142133431424'), (16, 5, 28, '132121320032014433241144103232424'), (17, 5, 33, '132121320002014433241142133434422'), (18, 6, 12, '122121330001024333121444433122144'), (19, 6, 29, '122323310001023134424122411434343'), (20, 6, 32, '122123330011024433121444304122433'), (21, 7, 14, '132231310032031223422444401133144'), (22, 7, 19, '132131320032014223321444402133144'), (23, 7, 22, '132131320032013224421344402133144'), (24, 8, 23, '132121320002014433244122133434421'), (25, 12, 15, '132131320032012223421444402133144'), (26, 12, 29, '132121320002014433244132133424421'), (27, 14, 19, '132131320032014223121444402133144'), (28, 16, 25, '132131320032014423221444402133144'), (29, 17, 24, '132121320032014433241143103432424'), (30, 18, 20, '132121320002013234444132133444421'), (31, 26, 31, '132121320032014433221444103132044'), (32, 27, 30, '132121320002014433241142133433424')]
SIX_COLORING = "132121320002014233521142133434455"

def distance_repr(c, d):
    # If c-d=(p,q,r,s), then
    # 64*distance^2 = A + B*sqrt(5).
    p, q, r, s = (c[i]-d[i] for i in range(4))
    A = p*p + 5*q*q + 3*r*r + 15*s*s
    B = 2*p*q + 6*r*s
    return A, B

def build_edges():
    unit, root3 = [], []
    for i in range(len(COORDS)):
        for j in range(i+1, len(COORDS)):
            z = distance_repr(COORDS[i], COORDS[j])
            if z == (64, 0):
                unit.append((i,j))
            elif z == (192, 0):
                root3.append((i,j))
    return unit, root3

def valid_coloring(n, edges, text, k):
    if len(text) != n:
        return False
    col = [int(ch) for ch in text]
    if any(c < 0 or c >= k for c in col):
        return False
    return all(col[a] != col[b] for a,b in edges)

def find_k_coloring(n, edges, k):
    # Deterministic DSATUR backtracking with canonical colour introduction.
    adj = [set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    colors = [-1]*n

    def choose_vertex():
        best = None
        best_key = None
        for v in range(n):
            if colors[v] >= 0:
                continue
            sat = len({colors[w] for w in adj[v] if colors[w] >= 0})
            key = (sat, len(adj[v]), -v)
            if best is None or key > best_key:
                best, best_key = v, key
        return best

    def rec():
        v = choose_vertex()
        if v is None:
            return tuple(colors)
        forbidden = {colors[w] for w in adj[v] if colors[w] >= 0}
        used = {c for c in colors if c >= 0}
        if not used:
            candidates = [0]
        else:
            next_new = len(used)
            candidates = [c for c in range(k)
                          if c not in forbidden and (c in used or c == next_new)]
        for c in candidates:
            colors[v] = c
            ans = rec()
            if ans is not None:
                return ans
            colors[v] = -1
        return None

    return rec()

def main():
    assert len(COORDS) == 33
    unit, root3 = build_edges()
    assert len(unit) == 81, len(unit)
    assert len(root3) == 32, len(root3)
    edges = unit + root3
    assert len(edges) == 113
    assert valid_coloring(33, edges, SIX_COLORING, 6)

    # Exhaustive deterministic non-5-colourability check.
    assert find_k_coloring(33, edges, 5) is None

    root3_one_based = [(a+1,b+1) for a,b in root3]
    assert len(DELETION_WITNESSES) == 32
    for idx, a1, b1, text in DELETION_WITNESSES:
        assert root3_one_based[idx-1] == (a1,b1)
        e = (a1-1,b1-1)
        remaining = [f for f in edges if f != e]
        assert valid_coloring(33, remaining, text, 5)
        col = [int(ch) for ch in text]
        # The deleted edge is necessarily monochromatic in the witness.
        assert col[e[0]] == col[e[1]]

    print("VERTICES", len(COORDS))
    print("UNIT_EDGES", len(unit))
    print("SQRT3_EDGES", len(root3))
    print("TOTAL_EDGES", len(edges))
    print("FULL_6_COLORING_VALID", True)
    print("FULL_5_COLORABLE", False)
    print("SQRT3_DELETION_WITNESSES_VALID", len(DELETION_WITNESSES))
    print("ALL_CHECKS_PASSED")

if __name__ == "__main__":
    main()
