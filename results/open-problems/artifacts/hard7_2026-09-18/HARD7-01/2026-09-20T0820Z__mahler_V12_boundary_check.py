#!/usr/bin/env python3
"""
Exact finite core for HARD7-01, 2026-09-20.

It checks the two V=F=12 / no-six-vertex-facet shadow-rigid corners:
(1) five opposite 5-vertex facet pairs + one tetrahedral pair, with the
    forced dual degree pattern (5,5,5,5,5,4): no oriented incidence-sign
    pattern satisfies the square-pyramid/tetrahedron ridge constraints;
(2) six opposite 5-vertex facet pairs with all vertex degrees five:
    exactly 30 spanning-tree-gauge sign patterns survive, all in one orbit.
    For a canonical orbit representative, a 5x5 minor of the cube-section
    coordinate matrix factors into four linear factors nonzero for all
    unsaturated coordinates in (-1,1), so rank <= 4 is impossible.

All enumeration is exact over {+1,-1}; the symbolic determinant is exact.
"""
from itertools import permutations
from collections import deque
import sympy as sp

N = 6
PERMS = list(permutations(range(N)))

def saturated_edges(missing):
    missing = set(missing)
    return [(i,j) for i in range(N) for j in range(N) if (i,j) not in missing]

def spanning_tree(edges):
    adj = [[] for _ in range(2*N)]
    for i,j in edges:
        u, v = i, N+j
        adj[u].append((v,(i,j)))
        adj[v].append((u,(i,j)))
    seen = {0}
    q = deque([0])
    tree = []
    while q:
        u = q.popleft()
        for v,e in adj[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
                tree.append(e)
    assert len(seen) == 2*N and len(tree) == 2*N-1
    return tree

def gauge_to_tree(S, missing, tree):
    """Row/column sign flips making every spanning-tree incidence +1."""
    r = [None]*N
    c = [None]*N
    r[0] = 1
    changed = True
    while changed:
        changed = False
        for i,j in tree:
            if r[i] is not None and c[j] is None:
                c[j] = r[i]*S[i][j]
                changed = True
            elif c[j] is not None and r[i] is None:
                r[i] = c[j]*S[i][j]
                changed = True
    assert all(x is not None for x in r+c)
    U = [[0]*N for _ in range(N)]
    for i,j in saturated_edges(missing):
        U[i][j] = r[i]*c[j]*S[i][j]
    assert all(U[i][j] == 1 for i,j in tree)
    return U

def shape_ok(S, missing):
    """
    Every support-5 facet must be a square pyramid:
      across the other five opposite facet pairs its ridge common-vertex
      counts are exactly 4,3,3,3,3.
    Every support-4 facet is a tetrahedron:
      exactly four of the other five opposite facet pairs give a triangular
      ridge (common-vertex count 3), and none gives 4.
    Apply the same test to columns (the polar facets).
    """
    missing = set(missing)
    row_support = [[j for j in range(N) if (i,j) not in missing] for i in range(N)]
    col_support = [[i for i in range(N) if (i,j) not in missing] for j in range(N)]

    def one_side(supports, transpose=False):
        for a in range(N):
            vals = []
            for b in range(N):
                if a == b:
                    continue
                common = sorted(set(supports[a]).intersection(supports[b]))
                if transpose:
                    same = sum(S[k][a] == S[k][b] for k in common)
                else:
                    same = sum(S[a][k] == S[b][k] for k in common)
                vals.append(max(same, len(common)-same))
            if len(supports[a]) == 5:
                if sorted(vals) != [3,3,3,3,4]:
                    return False
            elif len(supports[a]) == 4:
                if sum(v == 3 for v in vals) != 4 or any(v > 3 for v in vals):
                    return False
            else:
                raise AssertionError("unexpected facet support size")
        return True

    return one_side(row_support, False) and one_side(col_support, True)

def enumerate_tree_gauge(missing):
    edges = saturated_edges(missing)
    tree = spanning_tree(edges)
    tree_set = set(tree)
    chords = [e for e in edges if e not in tree_set]
    out = []
    for mask in range(1 << len(chords)):
        S = [[0]*N for _ in range(N)]
        for i,j in tree:
            S[i][j] = 1
        for bit,(i,j) in enumerate(chords):
            S[i][j] = -1 if ((mask >> bit) & 1) else 1
        if shape_ok(S, missing):
            out.append(S)
    return out, tree, chords

# x=5.  The unique degree-2 omitted row and column may either be
# incident or nonincident; these are the only two missing-graph types.
missing_x5_incident = [
    (0,0),(0,1),(1,0),(2,2),(3,3),(4,4),(5,5)
]
missing_x5_nonincident = [
    (0,1),(0,2),(1,0),(2,0),(3,3),(4,4),(5,5)
]
sol_A, tree_A, chords_A = enumerate_tree_gauge(missing_x5_incident)
sol_B, tree_B, chords_B = enumerate_tree_gauge(missing_x5_nonincident)
assert len(chords_A) == 18 and len(chords_B) == 18
assert len(sol_A) == 0 and len(sol_B) == 0

# x=6 and all six vertex-pair degrees are five.
# Missing incidence is a perfect matching; put it on the diagonal.
missing_diag = [(i,i) for i in range(N)]
sol_6, tree_6, chords_6 = enumerate_tree_gauge(missing_diag)
assert len(chords_6) == 19
assert len(sol_6) == 30

def permute_simultaneous(S,p):
    U = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                U[i][j] = S[p[i]][p[j]]
    return U

def chord_key(S, chords):
    return tuple(0 if S[i][j] == 1 else 1 for i,j in chords)

def canonical_key(S):
    candidates = []
    for p in PERMS:
        U = permute_simultaneous(S,p)
        G = gauge_to_tree(U, missing_diag, tree_6)
        candidates.append(chord_key(G,chords_6))
    return min(candidates)

orbit_keys = {canonical_key(S) for S in sol_6}
assert len(orbit_keys) == 1

# Reconstruct the canonical representative from its tree-gauge chord key.
rep_key = min(orbit_keys)
rep = [[0]*N for _ in range(N)]
for i,j in tree_6:
    rep[i][j] = 1
for bit,(i,j) in zip(rep_key,chords_6):
    rep[i][j] = 1 if bit == 0 else -1
assert shape_ok(rep, missing_diag)

# Six section vertices are rows of Q=S+diag(t_i), with |t_i|<1.
# If they lie in one 4D central cube section then rank Q <= 4, so every
# 5x5 minor must vanish.  This one never does in the open cube.
t = sp.symbols("t0:6")
Q = sp.Matrix([[t[i] if i == j else rep[i][j] for j in range(N)] for i in range(N)])
minor = sp.factor(Q.minor_submatrix(0,3).det())
target = (t[1]-1)*(t[2]+1)*(t[4]+1)*(t[5]+1)
assert sp.expand(minor-target) == 0

print("X5_INCIDENT_MISSING_GRAPH_CHORD_BITS =", len(chords_A))
print("X5_INCIDENT_SIGN_SOLUTIONS =", len(sol_A))
print("X5_NONINCIDENT_MISSING_GRAPH_CHORD_BITS =", len(chords_B))
print("X5_NONINCIDENT_SIGN_SOLUTIONS =", len(sol_B))
print("X6_PERFECT_MATCHING_CHORD_BITS =", len(chords_6))
print("X6_TREE_GAUGE_SIGN_SOLUTIONS =", len(sol_6))
print("X6_SIMULTANEOUS_RELABEL_ORBITS =", len(orbit_keys))
print("X6_CANONICAL_REPRESENTATIVE =")
for row in rep:
    print(" ".join(f"{x:+d}" if x else " ." for x in row))
print("X6_MINOR_DELETE_ROW0_COL3 =", minor)
print("For every t_i in (-1,1), each of t1-1,t2+1,t4+1,t5+1 is nonzero.")
print("Hence the displayed 5x5 minor is nonzero and rank(Q) >= 5.")
print("ALL_EXACT_CHECKS_PASS = True")
