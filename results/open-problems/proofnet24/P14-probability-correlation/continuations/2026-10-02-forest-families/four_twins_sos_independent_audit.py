"""Independent audit: enumerate subsets of the full graph, no transfer formulas."""
from fractions import Fraction as Q
from itertools import combinations
import json


def det(a):
    if not a:
        return Q(1)
    return sum((-1) ** j * a[0][j] * det([row[:j] + row[j+1:] for row in a[1:]])
               for j in range(len(a)))


def independent_sos(a, core):
    s = len(a)
    mat = [[Q(0) for _ in a] for _ in a]
    for i, v in enumerate(a):
        mat[i][i] = 4*v
    for u, v, w in core:
        mat[u][u] += w
        mat[v][v] += w
        mat[u][v] -= w
        mat[v][u] -= w
    W, d = det(mat), sum(a)
    adj = [[(-1)**(i+j)*det([row[:i]+row[i+1:] for k, row in enumerate(mat) if k != j])
            for j in range(s)] for i in range(s)]
    answer = sum(a[i]*a[j]*(4*d*adj[i][j]-W)**2 for i in range(s) for j in range(s))/64
    return answer, W


def polys_full_graph(a, core):
    s = len(a)
    # Matching edges first; their inclusion is recorded but not in lambda degree.
    edges = [(0, 1, Q(1)), (2, 3, Q(1))]
    edges += [(i, v+4, weight) for i in range(4) for v, weight in enumerate(a)]
    edges += [(u+4, v+4, weight) for u, v, weight in core]
    polynomials = [{} for _ in range(4)]
    accepted = 0
    for mask in range(1 << len(edges)):
        parent = list(range(s+4))
        weight, degree = Q(1), 0
        def root(u):
            while parent[u] != u:
                u = parent[u]
            return u
        for j, (u, v, w) in enumerate(edges):
            if not (mask >> j & 1):
                continue
            ru, rv = root(u), root(v)
            if ru == rv:
                break
            parent[ru] = rv
            weight *= w
            degree += int(j >= 2)
        else:
            accepted += 1
            poly = polynomials[mask & 3]
            poly[degree] = poly.get(degree, Q(0)) + weight
    return polynomials, accepted


def mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i+j] = out.get(i+j, Q(0)) + x*y
    return out


def test(label, a, core):
    polys, accepted = polys_full_graph(a, core)
    A, B, C, D = polys
    assert B == C, (label, 'terminal symmetry')
    bc, ad = mul(B, C), mul(A, D)
    R = {degree: bc.get(degree, Q(0))-ad.get(degree, Q(0)) for degree in set(bc)|set(ad)}
    s = len(a)
    H2, W = independent_sos(a, core)
    assert R.get(2*s+4, Q(0)) == 0, (label, 'H0')
    assert R.get(2*s+3, Q(0)) == 0, (label, 'H1')
    assert R.get(2*s+2, Q(0)) == H2, (label, 'H2', R.get(2*s+2), H2)
    support_size = sum(v > 0 for v in a)
    assert (H2 > 0) == (support_size >= 2)
    if support_size == 1:
        assert all(value == 0 for value in R.values())
    if s == 2:
        assert H2 == 4*a[0]**2*a[1]**2*sum(a)**2
    return {'label': label, 'vertices': s+4, 'accepted_forests': accepted,
            'W': str(W), 'H0': str(R.get(2*s+4, Q(0))),
            'H1': str(R.get(2*s+3, Q(0))), 'H2': str(H2),
            'Rayleigh': {str(k): str(v) for k, v in sorted(R.items())}}


if __name__ == '__main__':
    cases = [
        ('one hub', [Q(3, 7)], []),
        ('two hubs no core', [Q(1,2), Q(4,3)], []),
        ('two hubs connected', [Q(1,2), Q(4,3)], [(0,1,Q(5,7))]),
        ('two hubs strongly connected', [Q(1,2), Q(4,3)], [(0,1,Q(19))]),
        ('three hubs empty', [Q(2,3),Q(7,5),Q(3,4)], []),
        ('three hubs path', [Q(2,3),Q(7,5),Q(3,4)], [(0,1,Q(4,3)),(1,2,Q(9,7))]),
        ('three hubs triangle', [Q(2,3),Q(7,5),Q(3,4)],
         [(0,1,Q(4,3)),(1,2,Q(9,7)),(0,2,Q(5,2))]),
        ('zero middle spoke weight', [Q(2,3),Q(0),Q(3,4)],
         [(0,1,Q(4,3)),(1,2,Q(9,7))]),
        ('single support connected core', [Q(2,3),Q(0),Q(0)],
         [(0,1,Q(4,3)),(1,2,Q(9,7)),(0,2,Q(5,2))]),
    ]
    output = [test(*case) for case in cases]
    path = '/workspace/scratch/61b7096f9f41/random_cluster_research/four_twins_sos_independent_audit_results.json'
    with open(path, 'w') as out:
        json.dump(output, out, indent=2)
    print(json.dumps({'cases': len(output), 'status': 'PASS',
                      'H2': {row['label']: row['H2'] for row in output}}, indent=2))
