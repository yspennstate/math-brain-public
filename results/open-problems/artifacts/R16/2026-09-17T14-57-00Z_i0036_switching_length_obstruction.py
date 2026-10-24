#!/usr/bin/env python3
"""
R16 / I0036 exact finite obstruction for same-total-length four-terminal SAW switching.

The base planar subcubic graph has vertices 0,...,6 and edges
    01, 04, 12, 23, 25, 36, 45, 56.
An explicit planar face certificate is
    outer: 0-4-5-6-3-2-1-0
    inner: 0-1-2-5-4-0
    inner: 2-3-6-5-2.
Pendant terminals a,b,c,d are attached respectively at 0,4,6,3,
so they appear in cyclic order around the outer face.

For S_uv(x)=sum_{simple u-v paths P} x^{|P|}, this checker proves:
    [x^15] S_ac S_bd = 1,
    [x^15] (S_ab S_cd + S_ad S_bc) = 0.
Hence no universal switching injection from opposite-pair path pairs
to the union of adjacent-pair path pairs can preserve total path length.

All computations are integer-exact.
"""

from collections import defaultdict, Counter

BASE_EDGES = [
    (0, 1), (0, 4), (1, 2), (2, 3),
    (2, 5), (3, 6), (4, 5), (5, 6),
]
FACES = [
    (0, 4, 5, 6, 3, 2, 1),  # outer
    (0, 1, 2, 5, 4),
    (2, 3, 6, 5),
]
ANCHOR = {"a": 0, "b": 4, "c": 6, "d": 3}

def norm_edge(u, v):
    return tuple(sorted((u, v), key=lambda z: (str(type(z)), str(z))))

def verify_planar_face_certificate():
    edge_mult = Counter()
    for face in FACES:
        for i, u in enumerate(face):
            v = face[(i + 1) % len(face)]
            edge_mult[norm_edge(u, v)] += 1
    expected = {norm_edge(u, v) for u, v in BASE_EDGES}
    assert set(edge_mult) == expected
    assert all(edge_mult[e] == 2 for e in expected)
    V = 7
    E = len(BASE_EDGES)
    F = len(FACES)
    assert V - E + F == 2
    deg = Counter()
    for u, v in BASE_EDGES:
        deg[u] += 1
        deg[v] += 1
    assert max(deg.values()) <= 3
    outer = FACES[0]
    positions = [outer.index(ANCHOR[t]) for t in ("a", "b", "c", "d")]
    assert positions == sorted(positions)

def build_adjacency():
    adj = defaultdict(list)
    for u, v in BASE_EDGES:
        adj[u].append(v)
        adj[v].append(u)
    for terminal, u in ANCHOR.items():
        adj[terminal].append(u)
        adj[u].append(terminal)
    return adj

ADJ = build_adjacency()

def path_polynomial(src, dst):
    counts = defaultdict(int)
    def dfs(u, visited, length):
        if u == dst:
            counts[length] += 1
            return
        for v in ADJ[u]:
            if v not in visited:
                visited.add(v)
                dfs(v, visited, length + 1)
                visited.remove(v)
    dfs(src, {src}, 0)
    return dict(sorted(counts.items()))

def path_list(src, dst):
    paths = []
    def dfs(u, visited, path):
        if u == dst:
            paths.append(tuple(path))
            return
        for v in ADJ[u]:
            if v not in visited:
                visited.add(v)
                path.append(v)
                dfs(v, visited, path)
                path.pop()
                visited.remove(v)
    dfs(src, {src}, [src])
    return paths

def poly_mul(p, q):
    r = defaultdict(int)
    for i, a in p.items():
        for j, b in q.items():
            r[i + j] += a * b
    return dict(sorted(r.items()))

def poly_add(p, q):
    r = defaultdict(int)
    for k, v in p.items():
        r[k] += v
    for k, v in q.items():
        r[k] += v
    return dict(sorted((k, v) for k, v in r.items() if v))

def poly_sub(p, q):
    r = defaultdict(int)
    for k, v in p.items():
        r[k] += v
    for k, v in q.items():
        r[k] -= v
    return dict(sorted((k, v) for k, v in r.items() if v))

def fmt_poly(p):
    terms = []
    for k, c in sorted(p.items()):
        if c == 1:
            terms.append(f"x^{k}")
        else:
            terms.append(f"{c}*x^{k}")
    return " + ".join(terms) if terms else "0"

def main():
    verify_planar_face_certificate()

    pairs = [("a","b"), ("a","c"), ("a","d"),
             ("b","c"), ("b","d"), ("c","d")]
    P = {pair: path_polynomial(*pair) for pair in pairs}

    expected = {
        ("a","b"): {3:1, 6:1, 8:1},
        ("a","c"): {5:1, 6:2, 7:1},
        ("a","d"): {5:1, 6:2, 7:1},
        ("b","c"): {4:1, 6:1, 7:2},
        ("b","d"): {5:2, 6:1, 8:1},
        ("c","d"): {3:1, 5:1, 8:1},
    }
    assert P == expected

    lhs = poly_mul(P[("a","c")], P[("b","d")])
    rhs = poly_add(
        poly_mul(P[("a","b")], P[("c","d")]),
        poly_mul(P[("a","d")], P[("b","c")]),
    )
    diff = poly_sub(rhs, lhs)

    expected_lhs = {10:2, 11:5, 12:4, 13:2, 14:2, 15:1}
    expected_rhs = {6:1, 8:1, 9:2, 10:2, 11:5, 12:4, 13:6, 14:3, 16:1}
    expected_diff = {6:1, 8:1, 9:2, 13:4, 14:1, 15:-1, 16:1}
    assert lhs == expected_lhs
    assert rhs == expected_rhs
    assert diff == expected_diff
    assert lhs.get(15, 0) == 1
    assert rhs.get(15, 0) == 0

    source15 = []
    for p in path_list("a", "c"):
        for q in path_list("b", "d"):
            if (len(p)-1) + (len(q)-1) == 15:
                source15.append((p, q))
    assert len(source15) == 1
    assert source15[0] == (
        ("a",0,4,5,2,3,6,"c"),
        ("b",4,0,1,2,5,6,3,"d"),
    )

    # The witness does NOT refute the weighted C=1 inequality on 0<=x<=1:
    # RHS-LHS = x^6+x^8+2x^9+4x^13+x^14(1-x)+x^16 >= 0.
    assert diff == {6:1, 8:1, 9:2, 13:4, 14:1, 15:-1, 16:1}

    print("PLANAR_FACE_CERTIFICATE_PASS")
    for pair in pairs:
        print(f"S_{pair[0]}{pair[1]} = {fmt_poly(P[pair])}")
    print("LHS = S_ac*S_bd =", fmt_poly(lhs))
    print("RHS = S_ab*S_cd + S_ad*S_bc =", fmt_poly(rhs))
    print("RHS-LHS =", "x^6 + x^8 + 2*x^9 + 4*x^13 + x^14 - x^15 + x^16")
    print("[x^15] LHS =", lhs.get(15, 0))
    print("[x^15] RHS =", rhs.get(15, 0))
    print("UNIQUE_SOURCE_LENGTH_15 =", source15[0])
    print("WEIGHTED_DIFFERENCE_ON_0_1 = x^6+x^8+2*x^9+4*x^13+x^14*(1-x)+x^16 >= 0")
    print("ALL_EXACT_CHECKS_PASS")

if __name__ == "__main__":
    main()
