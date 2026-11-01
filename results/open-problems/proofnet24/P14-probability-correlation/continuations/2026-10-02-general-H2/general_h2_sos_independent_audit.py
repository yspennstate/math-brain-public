"""Independent direct forest enumeration audit of a proposed global H2 SOS.

No Grassmann expansions or coefficient identities are used to get H0,H1,H2.
All calculations use exact integer/Fraction arithmetic.
"""
from fractions import Fraction as Q
import json


def invdet(mat):
    n = len(mat)
    a = [[Q(x) for x in row] + [Q(i == j) for j in range(n)]
         for i, row in enumerate(mat)]
    determinant = Q(1)
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            determinant *= -1
        p = a[j][j]
        determinant *= p
        a[j] = [x / p for x in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                p = a[i][j]
                a[i] = [x - p*y for x, y in zip(a[i], a[j])]
    return [row[n:] for row in a], determinant


def laplacian(n, edges):
    L = [[Q(0) for _ in range(n)] for _ in range(n)]
    for x, y, c in edges:
        L[x][x] += c
        L[y][y] += c
        L[x][y] -= c
        L[y][x] -= c
    return L


def proposed_sos(n, edges, root):
    L = laplacian(n, edges)
    nonground = [i for i in range(n) if i != root]
    G, tau = invdet([[L[i][j] for j in nonground] for i in nonground])
    fullG = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i, x in enumerate(nonground):
        for j, y in enumerate(nonground):
            fullG[x][y] = G[i][j]
    a, b, _ = edges[0]
    c, d, _ = edges[1]
    v = [fullG[x][a] - fullG[x][b] for x in range(n)]
    w = [fullG[x][c] - fullG[x][d] for x in range(n)]
    E = [x for x in range(n) if v[x]]
    F = [x for x in range(n) if w[x]]
    S = [x for x in range(n) if not v[x] and not w[x]]
    assert root in S
    assert not set(E) & set(F), (E, F)
    assert all(not ((x in E and y in F) or (x in F and y in E))
               for x, y, _ in edges)
    Sb = [x for x in S if x != root]
    interior = [x for x in range(n) if x not in S]
    Gi, _ = invdet([[L[x][y] for y in interior] for x in interior])
    p = [[Q(0) for _ in Sb] for _ in range(n)]
    for j, x in enumerate(Sb):
        p[x][j] = Q(1)
    for i, x in enumerate(interior):
        for j, s in enumerate(Sb):
            p[x][j] = -sum(Gi[i][k] * L[y][s]
                          for k, y in enumerate(interior))
    assert p[a] == p[b]
    assert p[c] == p[d]
    T = [[fullG[x][y] for y in Sb] for x in Sb]
    etav = []
    etaw = []
    for x, y, _ in edges:
        etav.append([v[x]*p[y][j] - v[y]*p[x][j]
                     - (v[x]-v[y])*p[a][j] for j in range(len(Sb))])
        etaw.append([w[x]*p[y][j] - w[y]*p[x][j]
                     - (w[x]-w[y])*p[c][j] for j in range(len(Sb))])
    total = Q(0)
    for g, (_, _, cg) in enumerate(edges):
        for h, (_, _, ch) in enumerate(edges):
            contraction = sum(etav[g][i]*T[i][j]*etaw[h][j]
                              for i in range(len(Sb)) for j in range(len(Sb)))
            total += cg*ch*contraction**2
    return tau**2*total, {
        'tau': str(tau), 'v': list(map(str, v)), 'w': list(map(str, w)),
        'E': E, 'F': F, 'S': S, 'harmonic_rows': [[str(x) for x in row] for row in p],
        'T': [[str(x) for x in row] for row in T],
    }


def forest_polynomials(n, edges):
    # e,f forced separately after the unmarked-edge forest enumeration.
    e, f = edges[:2]
    rest = edges[2:]
    polynomials = [[0] * n for _ in range(4)]
    count = 0
    for mask in range(1 << len(rest)):
        parents = list(range(n))
        weight = 1
        degree = 0
        def root(x):
            while parents[x] != x:
                x = parents[x]
            return x
        for j, (x, y, conductance) in enumerate(rest):
            if mask >> j & 1:
                rx, ry = root(x), root(y)
                if rx == ry:
                    break
                parents[rx] = ry
                degree += 1
                weight *= conductance
        else:
            count += 1
            polynomials[0][degree] += weight
            re0, re1 = root(e[0]), root(e[1])
            rf0, rf1 = root(f[0]), root(f[1])
            if re0 != re1:
                polynomials[1][degree] += weight
            if rf0 != rf1:
                polynomials[2][degree] += weight
            if re0 != re1 and rf0 != rf1:
                # Add e and then test f against the updated components.
                parents[re0] = re1
                if root(f[0]) != root(f[1]):
                    polynomials[3][degree] += weight
    return polynomials, count


def convolution(a, b):
    ans = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ans[i+j] += x*y
    return ans


def test(label, n, edges, root):
    predicted, metadata = proposed_sos(n, edges, root)
    (A, B, C, D), count = forest_polynomials(n, edges)
    BC, AD = convolution(B, C), convolution(A, D)
    rayleigh = [x-y for x, y in zip(BC, AD)]
    H0, H1, H2 = [rayleigh[2*n-4-k] for k in range(3)]
    assert H0 == H1 == 0, (label, H0, H1)
    assert H2 == predicted, (label, H2, predicted)
    return {'label': label, 'n': n, 'm': len(edges),
            'edges': edges, 'root': root, 'unmarked_forests': count,
            'H0': str(H0), 'H1': str(H1), 'H2': str(H2),
            'predicted_H2': str(predicted), 'rayleigh': list(map(str, rayleigh)),
            **metadata}


def make_non_twins(core_weight=2, marked_e=2, marked_f=2):
    # Vertex classes E={0,1,2}, F={3,4,5}, S={6,7}.
    # Marked endpoints are not twins. Currents on each three-vertex support
    # are proportional to (2,-2,1); interior vertex 2/5 has a harmonic exit
    # row different from the marked endpoints.
    edges = [(0,1,marked_e), (3,4,marked_f),
             (0,2,14), (1,2,2), (3,5,18), (4,5,2)]
    edges += [(0,6,6),(0,7,2),(1,6,7),(1,7,5),(2,6,2),(2,7,6)]
    edges += [(3,6,4),(3,7,8),(4,6,8),(4,7,10),(5,6,8),(5,7,4)]
    if core_weight:
        edges.append((6,7,core_weight))
    return edges


def make_non_twins_three_boundary():
    edges = [(0,1,2),(3,4,3),(0,2,9),(1,2,1),(3,5,9),(4,5,1)]
    for support, ca, cx in [
        ((0,1,2), (2,0,4), (0,2,4)),
        ((3,4,5), (0,4,2), (4,2,0)),
    ]:
        a, b, x = support
        for j, (ac, xc) in enumerate(zip(ca, cx)):
            for u, conductance in ((a, ac),(b, ac+xc//2),(x, xc)):
                if conductance:
                    edges.append((u, 6+j, conductance))
    edges += [(6,7,3),(7,8,5)]
    return edges


if __name__ == '__main__':
    cases = [
        ('four twins, two hubs', 6,
         [(0,1,1),(2,3,1)] + [(i,j,1) for i in range(4) for j in (4,5)], 5),
        ('two non-twin three-vertex supports', 8, make_non_twins(), 7),
        ('non-twin supports, no core edge', 8, make_non_twins(0), 7),
        ('non-twin supports, changed marked weights', 8, make_non_twins(5,7,11), 7),
        ('non-twin supports, three boundary vertices', 9, make_non_twins_three_boundary(), 8),
        ('three boundary vertices, different root', 9, make_non_twins_three_boundary(), 6),
    ]
    result = [test(*case) for case in cases]
    target = '/workspace/scratch/61b7096f9f41/random_cluster_research/general_h2_sos_independent_audit_results.json'
    with open(target, 'w') as out:
        json.dump(result, out, indent=2)
    print(json.dumps({'status': 'PASS', 'cases': len(result),
                      'H2': {x['label']: x['H2'] for x in result}}, indent=2))
