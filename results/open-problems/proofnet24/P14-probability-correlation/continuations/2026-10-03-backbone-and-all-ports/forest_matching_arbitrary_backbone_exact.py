"""Exact arbitrary-backbone matching law / conditioning verification.

The backbone is enumerated literally; each new terminal is added by actual
spoke-subset cycle tests. Alpha/gamma appear only in the independent forced-OR
comparison. The small case also enumerates the full uncontracted graph.
The existing general finite-cube event checker is reused explicitly.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
from forest_matching_negative_association_exact import (
    canonical, terminal, clear_denominators, conditional_na_check,
    forced_bernoulli_table)


def backbone_records(n, edges, ports=(0, 1, 2)):
    records = []
    for mask in range(1 << len(edges)):
        parent = list(range(n)); weight = F(1)
        def root(u):
            while parent[u] != u: u = parent[u]
            return u
        for j, (u, v, w) in enumerate(edges):
            if mask >> j & 1:
                u, v = root(u), root(v)
                if u == v: break
                parent[u] = v; weight *= w
        else:
            records.append((mask, canonical(tuple(root(i) for i in ports)), weight))
    return records


def row_for_condition(records, status):
    row = defaultdict(F)
    for mask, state, weight in records:
        if all(v == -1 or (mask >> j & 1) == v for j, v in enumerate(status)):
            row[state] += weight
    return dict(row)


def direct_matching_table(backbone, rows, columns, activities):
    weights = []
    for mask in range(1 << len(activities)):
        row = backbone; weight = F(1)
        for i, w in enumerate(activities):
            a, b = rows[2*i:2*i+2]
            if mask >> i & 1:
                row = terminal(row, a+b, columns); weight *= w
            else:
                row = terminal(terminal(row, a, columns), b, columns)
        weights.append(weight * sum(row.values(), F(0)))
    return weights


def baseline_parameters(backbone, rows, columns):
    row = backbone
    for a in rows: row = terminal(row, a, columns)
    pairs = ((0, 1), (0, 2), (1, 2))
    A = [sum((mass for state, mass in row.items() if state[i] != state[j]), F(0))
         for i, j in pairs]
    r = sum((mass for state, mass in row.items() if len(set(state)) == 3), F(0))
    Z = sum(row.values(), F(0)); B = sum(columns, F(0))
    M = sum((A[k]*columns[i]*columns[j] for k, (i, j) in enumerate(pairs)), F(0))
    J = r * columns[0]*columns[1]*columns[2]
    H = [[A[i]*A[j] - (r*Z if i != j else 0) for j in range(3)] for i in range(3)]
    minors = [H[i][i] for i in range(3)]
    minors += [H[i][i]*H[j][j]-H[i][j]**2 for i, j in combinations(range(3), 2)]
    determinant = (H[0][0]*(H[1][1]*H[2][2]-H[1][2]**2)
                   -H[0][1]*(H[0][1]*H[2][2]-H[1][2]*H[0][2])
                   +H[0][2]*(H[0][1]*H[1][2]-H[1][1]*H[0][2]))
    minors.append(determinant)
    assert min(minors) >= 0
    assert M*M >= 2*B*J*Z and B*M >= 9*J
    return Z, M, J, minors


def forced_table(backbone, rows, columns, activities):
    Z, M, J, minors = baseline_parameters(backbone, rows, columns)
    B = sum(columns, F(0)); theta = []; t = []; h = []
    if B == 0:
        weights = [F(1)] * (1 << len(activities))
        for mask in range(len(weights)):
            for i, w in enumerate(activities):
                if mask >> i & 1: weights[mask] *= w
        return [v/sum(weights) for v in weights], (Z, M, J, minors)
    d = lambda x: 1+B*x
    alpha = lambda x: x*x/d(x)
    gamma = lambda x: x**3/d(x)**2
    for i, w in enumerate(activities):
        a, b = rows[2*i:2*i+2]
        delta = alpha(a+b)-alpha(a)-alpha(b)
        epsilon = gamma(a+b)-gamma(a)-gamma(b)
        c = d(a+b)/(d(a)*d(b)); theta.append(c*w/(1+c*w))
        if delta == 0:
            assert epsilon == 0
            t.append(F(0)); h.append(M)
        else:
            assert 0 < delta < 1/(B*B) and 0 < epsilon/delta < 2/B
            t.append(delta*theta[-1]); h.append(M+J*epsilon/delta+B*J*delta)
    if M:
        assert min(h)**2 >= 2*B*J*Z and max(h) < 2*min(h)
    else:
        assert J == 0 and not any(h)
    represented, forced = forced_bernoulli_table(Z, 2*B*J, theta, t, h)
    return represented, (Z, M, J, minors)


def literal_joint_graph(n, edges, rows, columns, activities):
    """Whole original graph; neither marked contraction nor port transfer."""
    k = len(activities); h = len(edges)
    all_edges = list(edges) + [(n+j, i, a*b) for j, a in enumerate(rows)
                              for i, b in enumerate(columns) if a*b]
    weights = [F(0)] * (1 << (k+h)); counts = [0] * (1 << k)
    def root(parent, u):
        while parent[u] != u: u = parent[u]
        return u
    def visit(j, parent, mass, bgmask):
        if j < len(all_edges):
            visit(j+1, parent, mass, bgmask)
            u, v, w = all_edges[j]; u, v = root(parent, u), root(parent, v)
            if u != v:
                copy = parent.copy(); copy[u] = v
                visit(j+1, copy, mass*w, bgmask | ((1 << j) if j < h else 0))
            return
        for matching in range(1 << k):
            copy = parent.copy(); value = mass
            for i, w in enumerate(activities):
                if matching >> i & 1:
                    u, v = root(copy, n+2*i), root(copy, n+2*i+1)
                    if u == v: break
                    copy[u] = v; value *= w
            else:
                weights[matching+(bgmask << k)] += value; counts[matching] += 1
    visit(0, list(range(n+len(rows))), F(1), 0)
    return weights, counts


def main():
    cases = [
        {'name':'nonuniform_K4_two_matching', 'n':4,
         'edges':[(i,j,F(i+2*j+1,3)) for i in range(4) for j in range(i+1,4)],
         'rows':[F(1,3),F(2,5),F(3,7),F(4,9)],
         'columns':[F(1,2),F(2,3),F(3,4)], 'activities':[F(2,3),F(3,5)], 'literal':True},
        {'name':'extra_vertex_nonuniform_backbone_four_matching', 'n':5,
         'edges':[(0,3,F(2)),(1,3,F(3)),(2,4,F(5)),(3,4,F(7)),(0,2,F(11))],
         'rows':[F(i+1,i+2) for i in range(8)],
         'columns':[F(2,3),F(3,4),F(5,7)], 'activities':[F(2,3),F(3,5),F(5,7),F(7,11)]},
        {'name':'five_matching_triangle_backbone', 'n':3,
         'edges':[(0,1,F(2)),(0,2,F(3)),(1,2,F(5))],
         'rows':[F(1,100)]*10, 'columns':[F(1),F(1),F(1)],
         'activities':[F(1),F(2),F(3),F(5),F(7)]},
        {'name':'zero_endpoint_and_column', 'n':4,
         'edges':[(0,3,F(2)),(1,3,F(3)),(2,3,F(5)),(0,1,F(7))],
         'rows':[F(0),F(2),F(1),F(3),F(2),F(4)],
         'columns':[F(1),F(0),F(2)], 'activities':[F(2),F(3),F(5)]},
        {'name':'single_column_independence', 'n':3,
         'edges':[(0,1,F(2)),(1,2,F(3))],
         'rows':[F(1),F(2),F(3),F(4)],
         'columns':[F(0),F(2),F(0)], 'activities':[F(3),F(5)]},
        {'name':'zero_columns_independence', 'n':3,
         'edges':[(0,1,F(2))], 'rows':[F(1),F(2),F(3),F(4)],
         'columns':[F(0),F(0),F(0)], 'activities':[F(3),F(5)]},
    ]
    report = {'arithmetic':'exact Fraction and denominator-cleared integer', 'cases':[]}
    for case in cases:
        n, edges, rows, columns, activities = [case[key] for key in ('n','edges','rows','columns','activities')]
        k, h = len(activities), len(edges); records = backbone_records(n, edges)
        literal = None
        if case.get('literal'):
            literal, counts = literal_joint_graph(n, edges, rows, columns, activities)
            direct_joint = [F(0)]*len(literal)
            for mask, state, weight in records:
                table = direct_matching_table({state:weight}, rows, columns, activities)
                for outcome, mass in enumerate(table): direct_joint[outcome+(mask << k)] = mass
            assert literal == direct_joint
        valid = laws = event_checks = 0; first = None
        for status in product((-1,0,1), repeat=h):
            backbone = row_for_condition(records, status)
            if not sum(backbone.values(), F(0)): continue
            actual = direct_matching_table(backbone, rows, columns, activities)
            represented, params = forced_table(backbone, rows, columns, activities)
            assert represented == [value/sum(actual) for value in actual]
            conditional_laws, tested = conditional_na_check(clear_denominators(actual))
            valid += 1; laws += conditional_laws; event_checks += tested
            if first is None: first = params
        report['cases'].append({'name':case['name'], 'matching_edges':k,
            'backbone_vertices':n, 'backbone_edges':h, 'positive_backbone_conditionings':valid,
            'total_matching_conditional_laws':laws, 'ordered_increasing_event_checks':event_checks,
            'full_OR_law_every_backbone_conditioning':True, 'hessian_all_principal_minors_nonnegative':True,
            'unconditional_F_M_J':list(map(str,first[:3])),
            'unconditional_hessian_principal_minors':list(map(str,first[3])),
            'literal_uncontracted_graph_match':literal is not None,
            'literal_marked_configuration_forest_counts':counts if literal is not None else None})
        print(case['name'], 'PASS;', valid, 'backbone conditions,', laws,
              'matching laws,', event_checks, 'event checks.', flush=True)
    Path(__file__).with_name('forest_matching_arbitrary_backbone_exact_results.json').write_text(json.dumps(report,indent=2)+'\n')
    print('All arbitrary-backbone matching NA / full law checks PASS.',flush=True)


if __name__ == '__main__': main()
