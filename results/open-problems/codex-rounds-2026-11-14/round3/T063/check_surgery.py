"""Exact finite checks of the two torus constructions in PROOF.md.

Standard library only; no floating point arithmetic, arrays, or workers.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb
import os
import resource
import sys


def transfer(height, n, c):
    states = [s for s in range(1 << height) if s.bit_count() == n]
    matrix = []
    for r in states:
        row = []
        for s in states:
            count = 0
            for v in range(1 << height):
                if all(((r >> y) & 1) + ((v >> ((y-1) % height)) & 1)
                       == ((s >> y) & 1) + ((v >> y) & 1)
                       for y in range(height)):
                    count += 1
            row.append(count * c ** ((r ^ s).bit_count()))
        matrix.append(row)
    return matrix


def torus(width, height, n, c):
    matrix = transfer(height, n, c)
    size = len(matrix)
    power = [[int(i == j) for j in range(size)] for i in range(size)]
    for _ in range(width):
        power = [[sum(power[i][k] * matrix[k][j] for k in range(size))
                  for j in range(size)] for i in range(size)]
    return sum(power[i][i] for i in range(size))


def free_boundaries(width, height, c):
    vertices = [v for v in product((0, 1), repeat=4)
                if v[0] + v[2] == v[1] + v[3]]  # left,right,bottom,top
    sums = defaultdict(int)
    for word in product(vertices, repeat=width * height):
        at = lambda x, y: word[y * width + x]
        if any(at(x, y)[1] != at(x+1, y)[0]
               for y in range(height) for x in range(width-1)):
            continue
        if any(at(x, y)[3] != at(x, y+1)[2]
               for y in range(height-1) for x in range(width)):
            continue
        boundary = (tuple(at(0, y)[0] for y in range(height)),
                    tuple(at(width-1, y)[1] for y in range(height)),
                    tuple(at(x, 0)[2] for x in range(width)),
                    tuple(at(x, height-1)[3] for x in range(width)))
        sums[boundary] += c ** sum(v[0] != v[1] for v in word)
    return sums


def fillings(width, height):
    """Separate enumerator returning actual vertex words for map checks."""
    vertices = [v for v in product((0, 1), repeat=4)
                if sum((v[0], 1-v[1], v[2], 1-v[3])) == 2]
    groups = defaultdict(list)
    for word in product(vertices, repeat=width*height):
        if any(word[y*width+x][1] != word[y*width+x+1][0]
               for y in range(height) for x in range(width-1)):
            continue
        if any(word[y*width+x][3] != word[(y+1)*width+x][2]
               for y in range(height-1) for x in range(width)):
            continue
        beta = (tuple(word[y*width][0] for y in range(height)),
                tuple(word[y*width+width-1][1] for y in range(height)),
                tuple(word[x][2] for x in range(width)),
                tuple(word[(height-1)*width+x][3] for x in range(width)))
        groups[beta].append(word)
    return groups


def transform(word, width, height, flip_x=False, flip_y=False):
    out = [None] * len(word)
    for y in range(height):
        for x in range(width):
            xx, yy = x, y
            r, s, b, t = word[y*width+x]
            if flip_x:
                xx = width-1-xx
                r, s, b, t = s, r, 1-b, 1-t
            if flip_y:
                yy = height-1-yy
                r, s, b, t = 1-r, 1-s, t, b
            out[yy*width+xx] = (r, s, b, t)
    return tuple(out)


def verify_torus(word, width, height, n):
    at = lambda x, y: word[(y % height)*width+(x % width)]
    for y in range(height):
        for x in range(width):
            r, s, b, t = at(x, y)
            assert r+b == s+t
            assert s == at(x+1, y)[0]
            assert t == at(x, y+1)[2]
    assert all(sum(at(x, y)[0] for y in range(height)) == n
               for x in range(width))


def check_actual_maps():
    count = 0
    for width, height in ((1, 1), (2, 1), (1, 2), (2, 2)):
        images = set()
        for group in fillings(width, height).values():
            for a, b, cc, d in product(group, repeat=4):
                blocks = (a, transform(b, width, height, flip_x=True),
                          transform(cc, width, height, flip_y=True),
                          transform(d, width, height, True, True))
                out = [None]*(4*width*height)
                for k, block in enumerate(blocks):
                    ox, oy = (k % 2)*width, (k // 2)*height
                    for y in range(height):
                        for x in range(width):
                            out[(y+oy)*(2*width)+x+ox] = block[y*width+x]
                out = tuple(out)
                verify_torus(out, 2*width, 2*height, height)
                assert sum(v[0] != v[1] for v in out) == sum(
                    v[0] != v[1] for block in (a, b, cc, d) for v in block)
                assert out not in images
                images.add(out)
                count += 1
        assert len(images) == sum(len(g)**4 for g in fillings(width, height).values())
    print('direct four-copy gluing: %d distinct images, all seams/fluxes/weights PASS' % count)
    inserted = 0
    for group in fillings(2, 2).values():
        for word in group:
            try:
                verify_torus(word, 2, 2, 1)
            except AssertionError:
                continue
            for target_height in (3, 4, 5):
                out = list(word)
                for _ in range(target_height-2):
                    out.extend((0, 0, word[2+x][3], word[2+x][3]) for x in range(2))
                verify_torus(out, 2, target_height, 1)
                assert sum(v[0] != v[1] for v in out) == sum(v[0] != v[1] for v in word)
                inserted += 1
    print('direct row insertion: %d seam/flux/weight checks PASS' % inserted)


def main():
    print('OMP_NUM_THREADS=' + os.environ.get('OMP_NUM_THREADS', 'unset'))
    print('effective_nice=' + str(os.getpriority(os.PRIO_PROCESS, 0)))
    insertion_checks = 0
    for c in (1, 2, 3):
        for height in range(3, 7):
            for n in range(1, height // 2 + 1):
                for width in (2, 3, 4):
                    lhs = torus(width, height, n, c)
                    rhs = torus(width, 2*n, n, c)
                    assert lhs >= rhs, (width, height, n, c, lhs, rhs)
                    insertion_checks += 1
    print('row insertion: %d exact comparisons PASS' % insertion_checks)
    for c in (1, 2, 3):
        for width, height in ((1, 1), (2, 1), (1, 2), (2, 2)):
            sums = free_boundaries(width, height, c)
            fourth_moment = sum(z**4 for z in sums.values())
            balanced = torus(2*width, 2*height, height, c)
            assert fourth_moment <= balanced
            free = sum(sums.values())
            bound_count = 2 ** (2*width + 2*height)
            assert free**4 <= bound_count**3 * balanced
            print('reflection c=%d rectangle=%dx%d sum_Zb^4=%d Zbal=%d PASS'
                  % (c, width, height, fourth_moment, balanced))
    # Independent hand enumeration of the one-vertex free square.
    for c in (1, 2, 3):
        assert sum(free_boundaries(1, 1, c).values()) == 4 + 2*c
        assert torus(2, 2, 1, c) == 8 + 2*c**4
    print('one-vertex and 2x2 torus hand formulas PASS')
    c = Fraction(1, 2)
    assert torus(3, 5, 2, c) >= torus(3, 4, 2, c)
    sums = free_boundaries(2, 2, c)
    assert sum(z**4 for z in sums.values()) <= torus(4, 4, 2, c)
    print('c=1/2 exact rational pressure comparisons PASS')
    check_actual_maps()
    print('largest transfer matrix dimension=%d' % comb(6, 3))
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    print('peak resident memory bytes=%d' % rss)


if __name__ == '__main__':
    main()
