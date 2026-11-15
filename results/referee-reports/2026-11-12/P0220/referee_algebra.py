"""Exact finite checks for boundary cases and the finite-cutoff extraction."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction as F
import itertools
import math
import time
import sympy as sp

START = time.monotonic()
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def parts(n, cap=None):
    if n == 0:
        yield ()
        return
    for first in range(min(n, n if cap is None else cap), 0, -1):
        for rest in parts(n-first, first):
            yield (first,)+rest


def contains(outer, inner):
    return len(inner) <= len(outer) and all(x >= y for x,y in zip(outer, inner))


@lru_cache(None)
def skew_count(outer, inner):
    if not contains(outer, inner):
        return 0
    if outer == inner:
        return 1
    count = 0
    for row, value in enumerate(outer):
        if row+1 == len(outer) or value > outer[row+1]:
            child = list(outer)
            child[row] -= 1
            child = tuple(v for v in child if v)
            count += skew_count(child, inner)
    return count


def rsk_checkpoints(perm, cut):
    rows = []
    checkpoint = ()
    for n, value in enumerate(perm, 1):
        row = 0
        while True:
            if row == len(rows):
                rows.append([value])
                break
            pos = next((i for i, x in enumerate(rows[row]) if x > value), len(rows[row]))
            if pos == len(rows[row]):
                rows[row].append(value)
                break
            rows[row][pos], value = value, rows[row][pos]
            row += 1
        if n == cut:
            checkpoint = tuple(map(len, rows))
    return checkpoint, tuple(map(len, rows))


def p(t, y, z):
    return F(0) if y < z else t**(y-z)/math.factorial(y-z)


def det(matrix):
    mat = [list(map(F, row)) for row in matrix]
    answer = F(1)
    for i in range(len(mat)):
        pivot = next((j for j in range(i, len(mat)) if mat[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            mat[i], mat[pivot] = mat[pivot], mat[i]
            answer = -answer
        value = mat[i][i]
        answer *= value
        for j in range(i+1, len(mat)):
            ratio = mat[j][i]/value
            for k in range(i+1, len(mat)):
                mat[j][k] -= ratio*mat[i][k]
    return answer


def main():
    checked = 0
    for n in range(1, 8):
        cut = n//2
        observed = Counter(rsk_checkpoints(perm, cut) for perm in itertools.permutations(range(n)))
        for (inner, outer), count in observed.items():
            expected = skew_count(outer, ())*skew_count(inner, ())*skew_count(outer, inner)
            assert count == expected
            checked += 1
    say(f'Lemma 3.1: all permutations through n=7, {checked} checkpoint/final-shape pairs: PASS')

    checked = 0
    for d in range(1, 5):
        partitions = [part for n in range(8) for part in parts(n) if len(part) <= d]
        for part in partitions:
            padded = part+(0,)*(d-len(part))
            pos = [padded[i]+d-1-i for i in range(d)]
            for m in range(d+1):
                assert (len(part) <= m) == set(range(d-m)).issubset(pos)
                checked += 1
    say(f'Lemma 3.2: {checked} occupancy tests, including m=0,d: PASS')

    checked = 0
    for d in range(1, 4):
        partitions = [part for n in range(7) for part in parts(n) if len(part) <= d]
        for inner in partitions:
            z = sorted((inner+(0,)*d)[j]+d-1-j for j in range(d))
            for outer in partitions:
                y = sorted((outer+(0,)*d)[j]+d-1-j for j in range(d))
                h = sum(outer)-sum(inner)
                for t in [F(0), F(1), F(2,3)]:
                    actual = det([[p(t, a,b) for b in z] for a in y])
                    expected = (skew_count(outer, inner)*t**h/math.factorial(h)
                                if contains(outer, inner) else 0)
                    assert actual == expected
                    checked += 1
    say(f'Lemma 3.3: {checked} exact determinants, including u=0 and nonnested shapes: PASS')

    checked = 0
    for end in range(7):
        for start in range(7):
            for u,v in [(F(0),F(2,3)), (F(1,3),F(2,3))]:
                assert sum(p(u,end,k)*p(v,k,start) for k in range(7)) == p(u+v,end,start)
                checked += 1
    say(f'Section 4: {checked} exact finite-cutoff semigroup tests: PASS')

    # d=2, Lambda=3, three markers including two at exactly the same time.
    size, d = 4, 2
    s1, s2, T = sp.Rational(1,4), sp.Rational(1,2), sp.Integer(1)
    markers = [(s1,0),(s1,1),(s2,0)]
    w = sp.symbols('w0:3')
    def P(t):
        return sp.Matrix(size,size,lambda i,j: 0 if i<j else t**(i-j)/sp.factorial(i-j))
    D1, D2 = sp.eye(size), sp.eye(size)
    D1[0,0] += w[0]
    D1[1,1] += w[1]
    D2[0,0] += w[2]
    K = P(T-s2)*D2*P(s2-s1)*D1*P(s1)
    boundary = P(1)[:, :d]
    M = boundary.T*K[:, :d]
    coefficient = sp.Poly(sp.expand(M.det()), *w).coeff_monomial(math.prod(w))
    A = boundary.T*P(T)[:, :d]
    G = sp.Matrix(d,3,lambda i,a: sum(P(1)[y,i]*P(T-markers[a][0])[y,markers[a][1]] for y in range(size)))
    Fm = sp.Matrix(3,d,lambda a,j: P(markers[a][0])[markers[a][1],j])
    Qt = sp.Matrix(3,3,lambda b,a: (P(markers[b][0]-markers[a][0])[markers[b][1],markers[a][1]]
                                    if markers[a][0] < markers[b][0] else 0))
    block = A.row_join(G).col_join((-Fm).row_join(-Qt))
    occupied_sum = 0
    sets = list(itertools.combinations(range(size),d))
    for y1,y2,y3 in itertools.product(sets, repeat=3):
        if not {0,1}.issubset(y1) or 0 not in y2:
            continue
        occupied_sum += (boundary[list(y3),:].det()*P(T-s2)[list(y3),list(y2)].det()
                         *P(s2-s1)[list(y2),list(y1)].det()*P(s1)[list(y1),:d].det())
    assert coefficient == block.det() == occupied_sum
    say(f'Section 4 cutoff extraction: coefficient=occupied Cauchy--Binet sum=block determinant={coefficient}: PASS')
    S = sp.diag(1,1,-1,-1,-1)
    target_transpose = S*block*S
    assert target_transpose.det() == block.det()
    say('Section 4 final transpose: requires diag(I_d,-I_q) conjugation; determinant unchanged: PASS')
    say(f'Elapsed seconds: {time.monotonic()-START:.3f}')
    with open('referee_algebra.txt','w') as output:
        output.write('\n'.join(LOG)+'\n')


if __name__ == '__main__':
    main()
