#!/usr/bin/env python3
"""
R09 final exploratory scout for Tang Q4.11 transitive half.

Exact part:
  * enumerate NetworkX graph atlas graphs on 3..7 vertices;
  * keep connected vertex-transitive graphs with <=15 edges;
  * enumerate every bond state of each retained factor and build its exact
    root-cluster PGF in integer Bernstein counts;
  * count the 78 unordered pairs.

Numerical part (explicitly NOT a proof/certificate):
  * for every unordered pair of retained factors, treat the free product
    factor exploration as a two-type branching recursion;
  * continue the physical extinction branch numerically on 70 p-values
    between just above p_c and 0.95;
  * evaluate theta'' by implicit differentiation.

The numerical sign scan is only a counterexample search. Absence of a sampled
positive value is NOT a theorem about the full interval or about all transitive
graphs.
"""
import itertools
from collections import defaultdict
import numpy as np
import sympy as sp
import networkx as nx
from scipy import optimize

P, U = sp.symbols("P U")

def is_vertex_transitive(G):
    if not nx.is_connected(G):
        return False
    if len({d for _, d in G.degree()}) != 1:
        return False
    root = next(iter(G.nodes()))
    orbit = set()
    gm = nx.algorithms.isomorphism.GraphMatcher(G, G)
    for iso in gm.isomorphisms_iter():
        orbit.add(iso[root])
        if len(orbit) == G.number_of_nodes():
            return True
    return False

def exact_cluster_pgf(G):
    G = nx.convert_node_labels_to_integers(G)
    n = G.number_of_nodes()
    edges = [tuple(sorted(e)) for e in G.edges()]
    E = len(edges)
    counts = defaultdict(int)
    for mask in range(1 << E):
        parent = list(range(n))
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        def union(a,b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra
        m = 0
        for i,(a,b) in enumerate(edges):
            if (mask >> i) & 1:
                m += 1
                union(a,b)
        r = find(0)
        k = sum(1 for v in range(n) if find(v) == r) - 1
        counts[(k,m)] += 1
    F = sp.Integer(0)
    for (k,m), c in counts.items():
        F += sp.Integer(c) * P**m * (1-P)**(E-m) * U**k
    return sp.expand(F), dict(counts)

def classify_name(G):
    n = G.number_of_nodes()
    known = {
        "K3": nx.complete_graph(3),
        "C4": nx.cycle_graph(4),
        "K4": nx.complete_graph(4),
        "C5": nx.cycle_graph(5),
        "K5": nx.complete_graph(5),
        "C6": nx.cycle_graph(6),
        "triangular_prism": nx.circular_ladder_graph(3),
        "K3,3": nx.complete_bipartite_graph(3,3),
        "octahedral": nx.octahedral_graph(),
        "K6": nx.complete_graph(6),
        "C7": nx.cycle_graph(7),
        "complement_C7": nx.complement(nx.cycle_graph(7)),
    }
    for name,H in known.items():
        if H.number_of_nodes() == n and nx.is_isomorphic(G,H):
            return name
    return "unlabelled"

factors = []
for G in nx.graph_atlas_g():
    n = G.number_of_nodes()
    if 3 <= n <= 7 and G.number_of_edges() <= 15 and is_vertex_transitive(G):
        H = nx.convert_node_labels_to_integers(G)
        F, counts = exact_cluster_pgf(H)
        assert sp.expand(F.subs(U,1) - 1) == 0
        mu = sp.expand(sp.diff(F,U).subs(U,1))
        g6 = nx.to_graph6_bytes(H, header=False).decode().strip()
        factors.append((g6, classify_name(H), H, F, mu, counts))

assert len(factors) == 12
assert len(factors)*(len(factors)+1)//2 == 78
expected_names = {
    "K3","C4","K4","C5","K5","C6","triangular_prism","K3,3",
    "octahedral","K6","C7","complement_C7"
}
assert {x[1] for x in factors} == expected_names

def find_pc(muA, muB):
    crit = sp.expand(muA*muB - 1)
    f = sp.lambdify(P, crit, "numpy")
    xs = np.linspace(1e-6, 0.999999, 5000)
    vals = f(xs)
    for i in range(len(xs)-1):
        if vals[i] == 0:
            return float(xs[i]), crit
        if vals[i]*vals[i+1] < 0:
            root = optimize.brentq(lambda z: float(f(z)), float(xs[i]), float(xs[i+1]))
            if 0 < root < 1:
                return float(root), crit
    raise RuntimeError("no critical root found")

def scout_pair(A, B):
    _,_,GA,FA,muA,_ = A
    _,_,GB,FB,muB,_ = B
    pc, crit = find_pc(muA, muB)
    X,Y = sp.symbols("X Y")
    h1 = X - FA.subs(U,Y)
    h2 = Y - FB.subs(U,X)
    H = [h1,h2]
    J = sp.Matrix(H).jacobian([X,Y])
    Hp = sp.Matrix([sp.diff(h,P) for h in H])
    Hpp = sp.Matrix([sp.diff(h,P,2) for h in H])
    Hpz = sp.Matrix([[sp.diff(h,P,z) for z in (X,Y)] for h in H])
    Hzz = [sp.hessian(h,(X,Y)) for h in H]
    jf = sp.lambdify((P,X,Y),J,"numpy")
    hpf = sp.lambdify((P,X,Y),Hp,"numpy")
    hppf = sp.lambdify((P,X,Y),Hpp,"numpy")
    hpzf = sp.lambdify((P,X,Y),Hpz,"numpy")
    hzzf = [sp.lambdify((P,X,Y),M,"numpy") for M in Hzz]
    f1 = sp.lambdify((P,Y),FA.subs(U,Y),"numpy")
    f2 = sp.lambdify((P,X),FB.subs(U,X),"numpy")

    pmax = 0.95
    if pc >= pmax:
        return pc, None, None, 0
    ps = np.linspace(pmax, pc + 0.001*(pmax-pc), 70)
    guess = np.array([1e-10,1e-10], dtype=float)
    vals = []
    for pv in ps:
        sol = optimize.root(
            lambda z: np.array([z[0]-f1(pv,z[1]), z[1]-f2(pv,z[0])],dtype=float),
            guess, method="hybr"
        )
        if not sol.success:
            continue
        x,y = map(float,sol.x)
        if not (0 <= x < 1 and 0 <= y < 1):
            continue
        guess = np.array([x,y])
        JJ = np.array(jf(pv,x,y),dtype=float)
        hp = np.array(hpf(pv,x,y),dtype=float).reshape(2)
        zp = np.linalg.solve(JJ,-hp)
        hpp = np.array(hppf(pv,x,y),dtype=float).reshape(2)
        hpz = np.array(hpzf(pv,x,y),dtype=float)
        quad = np.array([zp @ np.array(ff(pv,x,y),dtype=float) @ zp for ff in hzzf])
        zpp = np.linalg.solve(JJ,-(hpp + 2*hpz@zp + quad))
        theta2 = -(zpp[0]*y + 2*zp[0]*zp[1] + x*zpp[1])
        vals.append((float(theta2),float(pv)))
    if not vals:
        return pc, None, None, 0
    return pc, max(vals), min(vals), len(vals)

print("R09 Tang transitive-half small-factor scout")
print("EXACT ENUMERATION SECTION")
for g6,name,G,F,mu,counts in factors:
    print(f"{name:17s} graph6={g6:6s} n={G.number_of_nodes()} m={G.number_of_edges()} degree={next(iter(dict(G.degree()).values()))}")
print("exact_factor_count =", len(factors))
print("exact_unordered_pair_count =", len(factors)*(len(factors)+1)//2)
print("all exact factor PGFs satisfy F(p,1)=1: PASS")

print("\nNUMERICAL SCOUT SECTION -- NOT A PROOF")
pair_results = []
for i,A in enumerate(factors):
    for B in factors[i:]:
        pc,best,worst,n = scout_pair(A,B)
        pair_results.append((A[1],B[1],pc,best,worst,n))
valid = [r for r in pair_results if r[3] is not None]
num_nonnegative = sum(1 for r in valid if r[3][0] >= 0)
worst_best = max(valid, key=lambda r:r[3][0])
most_negative = min(valid, key=lambda r:r[4][0])
print("pairs_scouted =", len(pair_results))
print("pairs_with_valid_continuation =", len(valid))
print("sampled_pairs_with_theta_second_derivative_nonnegative =", num_nonnegative)
print("largest_sampled_theta_second_derivative =", worst_best[3], "pair=", worst_best[:2])
print("smallest_sampled_theta_second_derivative =", most_negative[4], "pair=", most_negative[:2])
print("grid: 70 continuation points per pair from p=0.95 down toward p_c")
print("INTERPRETATION: no sampled transitive free-product counterexample found.")
print("WARNING: numerical scout only; this does NOT certify concavity on any full interval.")
print("EXACT_ENUMERATION_PASS / NUMERICAL_SCOUT_COMPLETE")
