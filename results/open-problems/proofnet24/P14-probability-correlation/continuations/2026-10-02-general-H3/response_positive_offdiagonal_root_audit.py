"""Independent exact audit of the explicit non-Laplacian response matrix."""
from fractions import Fraction as Q
from pathlib import Path
import json

def solve(a, b):
    m = [[Q(x) for x in row] + [Q(y)] for row, y in zip(a, b)]
    for k in range(len(a)):
        j = next(j for j in range(k, len(a)) if m[j][k])
        m[k], m[j] = m[j], m[k]
        z = m[k][k]
        m[k] = [x / z for x in m[k]]
        for j in range(len(a)):
            if j != k:
                z = m[j][k]
                m[j] = [x-z*y for x, y in zip(m[j], m[k])]
    return [row[-1] for row in m]

spokes = [[3, 30, 1], [2, 28, 2], [15, 14, 3], [5, 2, 4]]
interior = [(0, 1, 1), (0, 2, 4), (1, 2, 14), (0, 3, 12), (1, 3, 2)]
edges = interior + [(i, 4+j, c) for i, row in enumerate(spokes) for j, c in enumerate(row)]
a = [[Q(0) for _ in range(4)] for _ in range(4)]
for x, y, c in edges:
    if x < 4: a[x][x] += c
    if y < 4: a[y][y] += c
    if x < 4 and y < 4: a[x][y] -= c; a[y][x] -= c
v = solve(a, [1, -1, 0, 0]) + [Q(0)] * 3
assert v[:4] == [Q(5,240), Q(-5,240), Q(-1,240), Q(2,240)]
assert all(sum(Q(spokes[i][j])*v[i] for i in range(4)) == 0 for j in range(3))
pcols = [solve(a, [row[j] for row in spokes]) for j in range(3)]
p = [[pcols[j][i] for j in range(3)] for i in range(4)]
p += [[Q(i == j) for j in range(3)] for i in range(3)]
assert p[0] == p[1]
b = [[Q(0) for _ in range(3)] for _ in range(3)]
for x, y, c in edges:
    eta = [v[x]*p[y][i]-v[y]*p[x][i]-(v[x]-v[y])*p[0][i] for i in range(3)]
    for i in range(3):
        for j in range(3): b[i][j] += c*eta[i]*eta[j]
numerator = [[96428607, -96696674, 268067], [-96696674,149117052,-52420378], [268067,-52420378,52152311]]
assert b == [[Q(x,31510540800) for x in row] for row in numerator]
assert all(sum(row) == 0 for row in b)
assert b[0][0]*b[1][1]-b[0][1]**2 > 0
assert b[0][2] > 0
result = {'status':'all exact assertions passed', 'matrix':[[str(x) for x in row] for row in b], 'positive_off_diagonal':str(b[0][2]), 'rank':2, 'PSD_reason':'positive-conductance Gram; null all-ones vector and positive principal minor'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
