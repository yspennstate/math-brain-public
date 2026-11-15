"""Exact edge enumeration for the two-flux finite-volume bound.

Standard library, one process. No imports from the earlier workers' scripts.
All partition sums are polynomials in c with integer coefficients.
"""
from collections import Counter, defaultdict
from itertools import product
import os
import resource
import sys
import time


def verify(h, v, width, height, n=None, m=None):
    at = lambda a, x, y: a[(y % height)*width + x % width]
    for y in range(height):
        for x in range(width):
            assert at(h, x-1, y) + at(v, x, y-1) == at(h, x, y) + at(v, x, y)
    ns = {sum(at(h, x, y) for y in range(height)) for x in range(width)}
    ms = {sum(at(v, x, y) for x in range(width)) for y in range(height)}
    assert len(ns) == len(ms) == 1
    if n is not None:
        assert ns == {n}
    if m is not None:
        assert ms == {m}
    return next(iter(ns)), next(iter(ms))


def exponent(h, width, height):
    return sum(h[y*width+x-1 if x else y*width+width-1] != h[y*width+x]
               for y in range(height) for x in range(width))


def configurations(width, height, n=None, m=None):
    """Enumerate horizontal edges, then solve vertical ice equations by seeds."""
    for h in product((0, 1), repeat=width*height):
        if n is not None and any(sum(h[y*width+x] for y in range(height)) != n
                                 for x in range(width)):
            continue
        columns = []
        for x in range(width):
            options = []
            for seed in (0, 1):
                b = seed
                tops = []
                for y in range(height):
                    t = b + h[y*width+(x-1) % width] - h[y*width+x]
                    if t not in (0, 1):
                        break
                    tops.append(t)
                    b = t
                if len(tops) == height and b == seed:
                    options.append(tuple(tops))
            if not options:
                break
            columns.append(options)
        if len(columns) != width:
            continue
        for cols in product(*columns):
            if m is not None and sum(col[-1] for col in cols) != m:
                continue
            v = tuple(cols[x][y] for y in range(height) for x in range(width))
            yield h, v


def polynomial(width, height, n, m):
    return Counter(exponent(h, width, height)
                   for h, v in configurations(width, height, n, m))


def insert(h, v, width, height, target_width, target_height, row_bit, col_bit):
    """Insert top rows, then right columns, retaining the labelled old block."""
    hh = list(h)
    vv = list(v)
    for _ in range(target_height-height):
        hh.extend([row_bit]*width)
        vv.extend(v[(height-1)*width:height*width])
    out_h, out_v = [], []
    for y in range(target_height):
        row_h = hh[y*width:(y+1)*width]
        out_h.extend(row_h + [row_h[-1]]*(target_width-width))
        out_v.extend(vv[y*width:(y+1)*width] + [col_bit]*(target_width-width))
    return tuple(out_h), tuple(out_v)


def free_fillings(width, height):
    """Enumerate independent incident edges, not six-letter vertex words."""
    groups = defaultdict(list)
    for h in product((0, 1), repeat=(width+1)*height):
        for v in product((0, 1), repeat=width*(height+1)):
            vertices = tuple((h[y*(width+1)+x], h[y*(width+1)+x+1],
                              v[y*width+x], v[(y+1)*width+x])
                             for y in range(height) for x in range(width))
            if not all(r+b == s+t for r, s, b, t in vertices):
                continue
            beta = (tuple(h[y*(width+1)] for y in range(height)),
                    tuple(h[y*(width+1)+width] for y in range(height)),
                    v[:width], v[-width:])
            groups[beta].append(vertices)
    return groups


def reflected(word, width, height, fx, fy):
    # Apply substitutions to the ice equation, then relocate vertices.
    out = [None]*len(word)
    for y in range(height):
        for x in range(width):
            r, s, b, t = word[y*width+x]
            xx, yy = x, y
            if fx:
                r, s, b, t = s, r, 1-b, 1-t
                xx = width-1-xx
            if fy:
                r, s, b, t = 1-r, 1-s, t, b
                yy = height-1-yy
            out[yy*width+xx] = r, s, b, t
    return out


def check_gluing():
    total = 0
    for width, height in ((1, 1), (2, 1), (1, 2), (2, 2)):
        counts = Counter()
        images = set()
        groups = free_fillings(width, height)
        for group in groups.values():
            for words in product(group, repeat=4):
                out = [None]*(4*width*height)
                for k, word in enumerate(words):
                    fx, fy = k % 2, k // 2
                    block = reflected(word, width, height, fx, fy)
                    for y in range(height):
                        for x in range(width):
                            out[(y+fy*height)*(2*width)+x+fx*width] = block[y*width+x]
                h = tuple(z[1] for z in out)
                v = tuple(z[3] for z in out)
                verify(h, v, 2*width, 2*height, height, width)
                for y in range(2*height):
                    for x in range(2*width):
                        z = out[y*2*width+x]
                        assert z[0] == h[y*2*width+(x-1) % (2*width)]
                        assert z[2] == v[((y-1) % (2*height))*2*width+x]
                degree = sum(r != s for word in words for r, s, b, t in word)
                assert exponent(h, 2*width, 2*height) == degree
                assert (h, v) not in images
                images.add((h, v))
                counts[degree] += 1
        target = polynomial(2*width, 2*height, height, width)
        assert all(target[k] >= val for k, val in counts.items())
        total += len(images)
        print('gluing %dx%d: images=%d polynomial=%s target=%s PASS' %
              (width, height, len(images), dict(sorted(counts.items())), dict(sorted(target.items()))))
    print('independent four-copy image checks=%d PASS' % total)


def check_enumerator():
    cases = 0
    for width, height in ((1, 1), (2, 1), (1, 2), (2, 2), (3, 2), (2, 3)):
        brute = set()
        for h in product((0, 1), repeat=width*height):
            for v in product((0, 1), repeat=width*height):
                try:
                    verify(h, v, width, height)
                except AssertionError:
                    continue
                brute.add((h, v))
        solved = set(configurations(width, height))
        assert brute == solved
        cases += 1
    print('all-edge versus solved-column enumeration: %d shapes PASS' % cases)
    assert polynomial(2, 2, 1, 1) == Counter({0: 4, 4: 2})
    print('hand formula Z(2,2;1,1)=4+2c^4 PASS')


def check_insertions():
    map_checks = poly_checks = 0
    for width, height in ((2, 2), (2, 4), (4, 2)):
        source = list(configurations(width, height, height//2, width//2))
        for dw, dh in ((0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (2, 2)):
            for row_bit, col_bit in product((0, 1), repeat=2):
                images = set()
                for h, v in source:
                    hh, vv = insert(h, v, width, height, width+dw, height+dh,
                                    row_bit, col_bit)
                    n, m = height//2+row_bit*dh, width//2+col_bit*dw
                    verify(hh, vv, width+dw, height+dh, n, m)
                    assert exponent(hh, width+dw, height+dh) == exponent(h, width, height)
                    assert (hh, vv) not in images
                    images.add((hh, vv))
                    # Explicit left inverse, including when an insertion count is zero.
                    old_h = tuple(hh[y*(width+dw)+x] for y in range(height) for x in range(width))
                    old_v = tuple(vv[y*(width+dw)+x] for y in range(height) for x in range(width))
                    assert (old_h, old_v) == (h, v)
                    map_checks += 1
                if (width+dw)*(height+dh) <= 16:
                    source_poly = Counter(exponent(h, width, height) for h, v in source)
                    target_poly = polynomial(width+dw, height+dh, n, m)
                    assert all(target_poly[k] >= val for k, val in source_poly.items())
                    poly_checks += 1
    print('two-direction insertion: %d map checks; %d polynomial comparisons PASS' %
          (map_checks, poly_checks))


def main():
    start = time.monotonic()
    print('OMP_NUM_THREADS=' + os.environ.get('OMP_NUM_THREADS', 'unset'))
    print('effective_nice=' + str(os.getpriority(os.PRIO_PROCESS, 0)))
    check_enumerator()
    check_gluing()
    check_insertions()
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    print('peak resident memory bytes=%d' % rss)
    print('elapsed seconds=%.3f' % (time.monotonic()-start))


if __name__ == '__main__':
    main()
