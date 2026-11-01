"""Independent exact local-score audit of the response absorption lemma.

Explicit exterior algebra, Fraction Dirichlet Green functions, rank-one Wick
derivatives. No forest enumeration or conjectured response formula is used to
compute the scores. Pairs of twin vertices are joined by complete bipartite
layers, with a marked edge in the innermost pair. The outermost pair is a free
two-port boundary. Adding one layer should delay the first nonconstant score
by exactly one order, preserving a PSD full-contrast bilinear response.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def add(A, B):
    out = dict(A)
    for m, c in B.items():
        out[m] = out.get(m, F(0)) + c
        if not out[m]:
            del out[m]
    return out


def scale(A, c):
    return {m: v*c for m, v in A.items() if v*c}


def mul(A, B):
    out = {}
    for m, a in A.items():
        for n, b in B.items():
            if m & n:
                continue
            inversions = 0
            z = m
            while z:
                bit = z & -z
                inversions += (n & (bit-1)).bit_count()
                z -= bit
            key = m | n
            out[key] = out.get(key, F(0)) + a*b*(-1 if inversions % 2 else 1)
            if not out[key]:
                del out[key]
    return out


def det(A):
    A = [list(row) for row in A]
    n = len(A)
    answer = F(1)
    for i in range(n):
        pivot = next((j for j in range(i, n) if A[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            A[i], A[pivot] = A[pivot], A[i]
            answer = -answer
        p = A[i][i]
        answer *= p
        for j in range(i+1, n):
            t = A[j][i]/p
            for k in range(i+1, n):
                A[j][k] -= t*A[i][k]
    return answer


def inverse(A):
    n = len(A)
    A = [list(row)+[F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if A[j][i])
        A[i], A[pivot] = A[pivot], A[i]
        p = A[i][i]
        A[i] = [x/p for x in A[i]]
        for j in range(n):
            if j != i:
                t = A[j][i]
                A[j] = [x-t*y for x, y in zip(A[j], A[i])]
    return [row[n:] for row in A]


def local_score(layers, order, rungs=False):
    # layers=1 reproduces the original two-interior/two-port gadget.
    n = 2*(layers+1)
    interior = n-2
    edges = [(0, 1, F(1))]
    for layer in range(layers):
        for i in (2*layer, 2*layer+1):
            for j in (2*layer+2, 2*layer+3):
                edges.append((i, j, F(1)))
    if rungs:
        for layer in range(1, layers):
            edges.append((2*layer, 2*layer+1, F(layer+1)))
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for x, y, c in edges:
        L[x][x] += c
        L[y][y] += c
        L[x][y] -= c
        L[y][x] -= c
    C = inverse([row[:interior] for row in L[:interior]])
    P = [[-sum(C[i][j]*L[j][s] for j in range(interior)) for s in range(interior, n)] for i in range(interior)]
    assert P[0] == P[1]
    v = [C[i][0]-C[i][1] for i in range(interior)]
    shifted = [[C[i][j]-v[i]*v[j] for j in range(interior)] for i in range(interior)]
    variables = [{1 << i: F(1)} for i in range(2*n)]
    bars, psis = [], []
    for i in range(n):
        if i < interior:
            b, p = variables[2*i], variables[2*i+1]
            for j in range(2):
                b = add(b, scale(variables[2*(interior+j)], P[i][j]))
                p = add(p, scale(variables[2*(interior+j)+1], P[i][j]))
        else:
            b, p = variables[2*i], variables[2*i+1]
        bars.append(b)
        psis.append(p)
    q = [mul(b, p) for b, p in zip(bars, psis)]
    V = {}
    for i in range(interior):
        V = add(V, q[i])
    for x, y, c in edges:
        V = add(V, scale(mul(q[x], q[y]), -c))
    marked_quartic = mul(q[0], q[1])
    moments, derivatives = {}, {}

    def moment(mask, derivative):
        cache = derivatives if derivative else moments
        if mask not in cache:
            bs = [i for i in range(interior) if mask & (1 << (2*i))]
            ps = [i for i in range(interior) if mask & (1 << (2*i+1))]
            if len(bs) != len(ps):
                cache[mask] = F(0)
            else:
                k = len(bs)
                inv = sum(i < j for i in ps for j in bs)
                sign = -1 if (inv+k*(k-1)//2) % 2 else 1
                base = det([[C[i][j] for j in ps] for i in bs])
                if derivative:
                    base = det([[shifted[i][j] for j in ps] for i in bs])-base
                cache[mask] = sign*base
        return cache[mask]

    interior_mask = (1 << (2*interior))-1

    def expect(poly, derivative=False):
        out = {}
        for m, c in poly.items():
            x = c*moment(m & interior_mask, derivative)
            key = m >> (2*interior)
            if x:
                out[key] = out.get(key, F(0))+x
                if not out[key]:
                    del out[key]
        return out

    powers = [{0: F(1)}]
    for k in range(1, order+1):
        powers.append(mul(powers[-1], V))
    partitions, dpartitions = [], []
    for k in range(order+1):
        partitions.append(scale(expect(powers[k]), F(1, factorial(k))))
        d = scale(expect(powers[k], True), F(1, factorial(k)))
        if k:
            d = add(d, scale(expect(mul(marked_quartic, powers[k-1])), F(-1, factorial(k-1))))
        dpartitions.append(d)
    reciprocal = [{0: F(1)}]
    for k in range(1, order+1):
        x = {}
        for i in range(1, k+1):
            x = add(x, mul(partitions[i], reciprocal[k-i]))
        reciprocal.append(scale(x, F(-1)))
    scores = []
    for k in range(order+1):
        x = {}
        for i in range(k+1):
            x = add(x, mul(dpartitions[i], reciprocal[k-i]))
        scores.append(x)
    first = next(k for k, x in enumerate(scores) if any(m for m in x))
    assert first == layers
    b = scores[first].get(3, F(0))
    assert b > 0
    assert scores[first].get(12, F(0)) == b
    assert scores[first].get(9, F(0)) == -b
    assert scores[first].get(6, F(0)) == b
    assert not scores[first].get(15, F(0))
    # Ward's next quartic must be exactly B_01=-b.
    if order > first:
        assert scores[first+1].get(15, F(0)) == -b
    return {'layers': layers, 'rungs': rungs, 'first_nonconstant_order': first,
            'leading_response_eigenvalue': str(2*b),
            'scores': [{str(m): str(c) for m, c in x.items()} for x in scores],
            'checked_next_Ward_quartic': order > first}


def main():
    out = []
    for layers, rungs in [(1, False), (2, False), (2, True), (3, False), (3, True)]:
        row = local_score(layers, layers+1, rungs)
        out.append(row)
        print('PASS', layers, rungs, row['leading_response_eigenvalue'], flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
