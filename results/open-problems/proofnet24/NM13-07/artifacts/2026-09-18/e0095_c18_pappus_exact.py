#!/usr/bin/env python3
"""
NM13-07 / E0095 C18 exact self-check.

Proof-critical computations use exact integer/symbolic or finite combinatorial
enumeration. There is no floating-point spectral comparison in this checker.
"""
from fractions import Fraction
from math import factorial
import sympy as sp
import networkx as nx

N = 18
M0 = {
    (0,5), (1,8), (2,13), (3,10), (4,15),
    (6,11), (7,14), (9,16), (12,17),
}
M0 = {tuple(sorted(e)) for e in M0}
CYCLE = {tuple(sorted((i, (i+1) % N))) for i in range(N)}

# Exact validity of the fixed-C18 matching construction.
assert len(M0) == N // 2
assert not (M0 & CYCLE)
assert sorted(v for e in M0 for v in e) == list(range(N))

G = nx.Graph()
G.add_nodes_from(range(N))
G.add_edges_from(CYCLE | M0)
assert nx.is_connected(G)
assert all(d == 3 for _, d in G.degree())

# Exact characteristic polynomial of the candidate.
x = sp.symbols("x")
A = sp.zeros(N)
for u, v in G.edges():
    A[u, v] = A[v, u] = 1
charpoly = sp.factor(A.charpoly(x).as_expr())
expected = sp.expand(x**4 * (x-3) * (x+3) * (x**2-3)**6)
assert sp.expand(charpoly - expected) == 0

# The competitor in Cioaba-Koolen-Nozaki-Vermette Thm. 4.7 has
# lambda_2 = gamma, the largest real root of f. This exact evaluation
# suffices to show gamma > sqrt(3), since f(sqrt(3)) < 0 and f -> +infty.
f = x**3 + 2*x**2 - 4*x - 6
at_sqrt3 = sp.simplify(f.subs(x, sp.sqrt(3)))
assert at_sqrt3 == -sp.sqrt(3)

# Fixed-cycle dihedral orbit of the candidate matching.
def transform_matching(M, shift, reflect):
    def phi(v):
        return ((-v if reflect else v) + shift) % N
    return frozenset(tuple(sorted((phi(u), phi(v)))) for u, v in M)

orbit = {
    transform_matching(M0, shift, reflect)
    for shift in range(N)
    for reflect in (False, True)
}
assert len(orbit) == 6

# Exact finite Hamilton-cycle count in the Pappus graph.
# We fix start vertex 0. Each undirected Hamilton cycle is traversed twice.
adj = {v: tuple(sorted(G.neighbors(v))) for v in G.nodes()}
directed_from_zero = 0

def dfs(path, used):
    global directed_from_zero
    v = path[-1]
    if len(path) == N:
        if 0 in adj[v]:
            directed_from_zero += 1
        return
    for w in adj[v]:
        if w == 0 or w in used:
            continue
        used.add(w)
        path.append(w)
        dfs(path, used)
        path.pop()
        used.remove(w)

dfs([0], {0})
assert directed_from_zero == 72
undirected_hamilton_cycles = directed_from_zero // 2
assert undirected_hamilton_cycles == 36

# Exact finite automorphism count by graph-isomorphism backtracking.
aut_count = sum(
    1 for _ in nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter()
)
assert aut_count == 216

# Double-count labeled Pappus graphs and labeled Hamilton cycles.
# # labeled Pappus copies = 18!/|Aut(Pappus)|.
# Each has 36 undirected Hamilton cycles.
# # labeled undirected C18 cycles = 17!/2.
# S_18 acts transitively on labeled Hamilton cycles, so the number of
# Pappus copies containing a fixed labeled C18 is the quotient below.
copies_through_fixed_cycle = (
    Fraction(factorial(N), aut_count)
    * undirected_hamilton_cycles
    / Fraction(factorial(N-1), 2)
)
assert copies_through_fixed_cycle == 6

# Every dihedral orbit member is a valid matching and has the same
# characteristic polynomial, giving six explicit equality cases.
for M in orbit:
    assert len(M) == N // 2
    assert not (set(M) & CYCLE)
    assert sorted(v for e in M for v in e) == list(range(N))
    H = nx.Graph()
    H.add_nodes_from(range(N))
    H.add_edges_from(CYCLE | set(M))
    B = sp.zeros(N)
    for u, v in H.edges():
        B[u, v] = B[v, u] = 1
    assert sp.expand(B.charpoly(x).as_expr() - expected) == 0

print("candidate_matching =", sorted(M0))
print("characteristic_polynomial =", sp.factor(charpoly))
print("f(sqrt(3)) =", at_sqrt3)
print("fixed_cycle_dihedral_orbit_size =", len(orbit))
print("directed_hamilton_traversals_from_0 =", directed_from_zero)
print("undirected_hamilton_cycles =", undirected_hamilton_cycles)
print("automorphism_group_order =", aut_count)
print("pappus_copies_through_fixed_C18 =", copies_through_fixed_cycle)
print("ALL_EXACT_CHECKS_PASS")
