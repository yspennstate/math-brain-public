#!/usr/bin/env python3
"""Exact finite checks for The maximal Kemeny constant of an n-vertex graph.
These checks do not prove the all-graph asymptotic theorem or novelty.
Requires Python 3.10+, networkx and sympy. Run: python check_kemeny.py
"""
from __future__ import annotations
import json
from functools import lru_cache
from pathlib import Path
import networkx as nx
import sympy as sp

@lru_cache(maxsize=None)
def resistance_data(n: int, edges: tuple[tuple[int, int], ...]):
    if n < 2:
        raise ValueError('At least two vertices required')
    g = nx.Graph(); g.add_nodes_from(range(n)); g.add_edges_from(edges)
    if not nx.is_connected(g):
        raise ValueError('Connected graphs only')
    degrees = [g.degree(i) for i in range(n)]
    lap = sp.diag(*degrees)
    for u, v in edges:
        lap[u, v] -= 1; lap[v, u] -= 1
    grounded_inverse = lap[:n-1, :n-1].inv()
    def entry(i: int, j: int):
        return grounded_inverse[i, j] if i < n-1 and j < n-1 else sp.S.Zero
    resistance = sp.Matrix(n, n, lambda i,j: entry(i,i)+entry(j,j)-2*entry(i,j))
    m = len(edges)
    k = sum(degrees[i]*degrees[j]*resistance[i,j] for i in range(n) for j in range(i+1,n))/(2*m)
    return g, degrees, lap, resistance, k


def canonical_edges(g: nx.Graph):
    return tuple(sorted(tuple(sorted(e)) for e in g.edges()))


def main() -> None:
    counts = {'graphs':0, 'bridge_identities':0, 'fundamental_matrix_identities':0,
              'connected_deletion_comparisons':0, 'refined_internal_resistance_bounds':0,
              'incident_energy_bounds':0, 'turan_capacity_bounds':0}
    for base in nx.graph_atlas_g():
        n = len(base)
        if n < 2 or not nx.is_connected(base):
            continue
        base = nx.convert_node_labels_to_integers(base)
        edges = canonical_edges(base)
        g, deg, lap, resistance, k = resistance_data(n, edges)
        m = len(edges)
        counts['graphs'] += 1
        # A second exact definition, via the Markov-chain fundamental matrix.
        if n <= 6 or counts['graphs'] % 53 == 0:
            P = sp.eye(n) - sp.diag(*[sp.Rational(1,d) for d in deg])*lap
            stationary = sp.Matrix(1,n,[sp.Rational(d,2*m) for d in deg])
            Pi = sp.ones(n,1)*stationary
            k_fundamental = sp.trace((sp.eye(n)-P+Pi).inv())-1
            assert k_fundamental == k
            counts['fundamental_matrix_identities'] += 1
        # Compute the bridge contribution directly from cut-side degrees.
        bridges = list(nx.bridges(g))
        direct = sp.S.Zero
        for u,v in bridges:
            cut = g.copy(); cut.remove_edge(u,v)
            side = nx.node_connected_component(cut,u)
            vol = sum(deg[i] for i in side)
            direct += sp.Rational(vol*(2*m-vol),2*m)
        # Independently compute the same quantity from the weighted quotient tree.
        core = g.copy(); core.remove_edges_from(bridges)
        blocks = list(nx.connected_components(core))
        index = {v:i for i,block in enumerate(blocks) for v in block}
        qtree = nx.Graph(); qtree.add_nodes_from(range(len(blocks)))
        qtree.add_edges_from((index[u],index[v]) for u,v in bridges)
        weights = [g.subgraph(block).number_of_edges()+1 for block in blocks]
        W = sum(weights)
        assert W == m+1
        dist = dict(nx.all_pairs_shortest_path_length(qtree))
        raw = sum(weights[i]*weights[j]*dist[i][j] for i in qtree for j in qtree)
        quotient = sp.Rational(raw,m)-sp.Rational((2*m+1)*len(bridges),2*m)
        assert quotient == direct
        assert 0 <= direct <= k
        counts['bridge_identities'] += 1
        # The improved error uses that a nontrivial epsilon-resistance component
        # needs at least 1 + 1/epsilon vertices. Test with actual bridge blocks.
        block_diameters = []
        for block in blocks:
            if len(block) == 1:
                block_diameters.append(sp.S.Zero)
            else:
                induced = nx.convert_node_labels_to_integers(g.subgraph(block))
                rr = resistance_data(len(induced), canonical_edges(induced))[3]
                block_diameters.append(max(rr))
        epsilon = max(block_diameters)
        nontrivial = sum(len(block)>1 for block in blocks)
        internal_bound = n * epsilon**2 / (1+epsilon)
        assert sum(block_diameters) <= internal_bound
        assert k <= direct + m*internal_bound
        if epsilon:
            assert nontrivial <= n*epsilon/(1+epsilon)
        counts['refined_internal_resistance_bounds'] += 1
        for u in range(n):
            for v in range(n):
                if u != v:
                    assert resistance[u,v] >= sp.Rational(1,deg[u])
                    counts['incident_energy_bounds'] += 1
        omega = max(map(len, nx.find_cliques(g)))
        gamma = sp.Rational(omega-1,omega)
        assert m <= gamma*n*n/2
        counts['turan_capacity_bounds'] += 1
        # A tree retains connectivity while potentially deleting many edges.
        h = nx.minimum_spanning_tree(g)
        if h.number_of_edges() < m:
            mh = h.number_of_edges(); removed = m-mh
            kh = resistance_data(n,canonical_edges(h))[-1]
            upper = sp.Rational(mh,m)*kh + sp.Rational((n-1)*(2*removed*mh+removed**2),m)
            assert k <= upper
            assert k <= kh + 2*removed*(n-1)
            counts['connected_deletion_comparisons'] += 1
        # Independently test one nonbridge single-edge deletion when possible.
        for e in edges:
            if e in bridges or (e[1],e[0]) in bridges:
                continue
            h = g.copy(); h.remove_edge(*e)
            kh = resistance_data(n,canonical_edges(h))[-1]
            upper = sp.Rational(m-1,m)*kh + sp.Rational((n-1)*(2*m-1),m)
            assert k <= upper
            counts['connected_deletion_comparisons'] += 1
            break
    s = sp.symbols('s',real=True)
    factor = sp.factor(sp.Rational(1,54)-s**2*(1-s)/8)
    assert sp.expand(factor-(3*s-2)**2*(3*s+1)/216) == 0
    # Refined exponent balance, independent of a numerical asymptotic fit.
    a = sp.Rational(2,7)
    errors = [3-a,1+6*a,sp.Rational(5,2)]
    assert errors[0] == errors[1] == sp.Rational(19,7)
    assert max(errors) == sp.Rational(19,7)
    barbells = []
    for q in (3,4,6,8,10):
        for r in (2,3,q):
            sizes = [q//r + (i<q%r) for i in range(r)]
            block = nx.complete_multipartite_graph(*sizes)
            e = block.number_of_edges()
            g = nx.disjoint_union(block,block)
            internal = list(range(2*q,3*q))
            route = [0]+internal+[q]
            g.add_edges_from(zip(route,route[1:]))
            n = len(g); ell = len(route)-1
            _, deg, _, _, kval = resistance_data(n,canonical_edges(g))
            f = {i:sp.Integer(-1) for i in range(q)}
            f.update({i:sp.Integer(1) for i in range(q,2*q)})
            f.update({v:-1+sp.Rational(2*j,ell) for j,v in enumerate(route)})
            assert sum(deg[v]*f[v] for v in g) == 0
            energy = sum((f[u]-f[v])**2 for u,v in g.edges())
            variance_numerator = sum(deg[v]*f[v]**2 for v in g)
            rayleigh_lower = variance_numerator/energy
            claimed_lower = sp.Rational((2*e+1)*ell,2)
            assert kval >= rayleigh_lower >= claimed_lower
            if r == 2:
                assert nx.is_bipartite(g)
            assert max(map(len,nx.find_cliques(g))) <= r
            barbells.append({'n':n,'parts':r,'block_order':q,'path_length':ell,
                             'K_exact':str(kval),'relaxation_lower':str(claimed_lower)})
    counts['multipartite_barbell_tests'] = len(barbells)
    result = {'status':'ALL_FINITE_CHECKS_PASS', 'counts':counts,
              'scalar_gap_factorization':str(factor), 'error_exponents':[str(v) for v in errors],
              'barbell_examples':barbells, 'scope':'Exact finite arithmetic only. Not a proof of asymptotic limits, published decomposition, or novelty.'}
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
