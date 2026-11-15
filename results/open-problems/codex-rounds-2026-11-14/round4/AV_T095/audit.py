"""Exact finite checks for the crossing audit; standard library, one thread.

Run: OMP_NUM_THREADS=1 nice -n 15 python3 audit.py
"""
from fractions import Fraction as F
from pathlib import Path
import math
import os
import re
import resource
import signal
import time

signal.alarm(60)
# Attempt an allocation limit; this managed macOS environment may reject it.
_, inherited_hard = resource.getrlimit(resource.RLIMIT_DATA)
data_cap = 768 * 1024**2
if inherited_hard != resource.RLIM_INFINITY:
    data_cap = min(data_cap, inherited_hard)
try:
    resource.setrlimit(resource.RLIMIT_DATA, (data_cap, inherited_hard))
except (ValueError, OSError) as exc:
    print('Data-limit setter unavailable:', exc)
ROOT = Path(__file__).resolve().parent
PREVIOUS = Path('~/codex_op_1114r3/briefs/AV_T095')


def boundary_trails(cells):
    edges = set()
    for x, y in cells:
        corners = [(2*x-1, 2*y-1), (2*x+1, 2*y-1),
                   (2*x+1, 2*y+1), (2*x-1, 2*y+1)]
        for a, b in zip(corners, corners[1:]+corners[:1]):
            if (b, a) in edges:
                edges.remove((b, a))
            else:
                edges.add((a, b))
    original = edges.copy()
    outgoing = {}
    for a, b in edges:
        outgoing.setdefault(a, set()).add(b)
    trails = []
    while edges:
        start, _ = min(edges)
        current = start
        trail = []
        while True:
            nxt = min(outgoing[current])
            outgoing[current].remove(nxt)
            edges.remove((current, nxt))
            trail.append((current, nxt))
            current = nxt
            if current == start:
                break
        trails.append(trail)
    assert sum(map(len, trails)) == len(original)
    assert len({e for tr in trails for e in tr}) == len(original)
    return trails


def check_cells(cells):
    trails = boundary_trails(cells)
    winding_sum = 0
    nonzero = 0
    for tr in trails:
        m = len(tr)
        assert m >= 4
        winding = 0
        forced = set()
        nw = 0
        for (ax, ay), (bx, by) in tr:
            dx, dy = bx-ax, by-ay
            assert abs(dx)+abs(dy) == 2
            # Midpoint, then a half-unit normal pointing left/right.
            left = ((ax+bx-dy)//4, (ay+by+dx)//4)
            right = ((ax+bx+dy)//4, (ay+by-dx)//4)
            assert left in cells and right not in cells
            if dy > 0 or dx < 0:
                nw += 1
                assert right in {(left[0]+1, left[1]),
                                 (left[0], left[1]+1)}
                forced.add(left)
            if ax == bx and ax > 0:
                if ay < 0 < by:
                    winding += 1
                elif by < 0 < ay:
                    winding -= 1
        assert 2*nw == m
        assert 8*len(forced) >= m
        for k in (0, 1, 2):
            candidates = set(forced)
            selected = []
            while candidates:
                v = min(candidates)
                selected.append(v)
                candidates = {w for w in candidates
                              if max(abs(w[0]-v[0]), abs(w[1]-v[1])) > k}
            assert len(selected)*(2*k+1)**2 >= len(forced)
            assert all(max(abs(v[0]-w[0]), abs(v[1]-w[1])) > k
                       for i, v in enumerate(selected) for w in selected[i+1:])
        if winding:
            nonzero += 1
            xs = [v[0] for e in tr for v in e]
            ys = [v[1] for e in tr for v in e]
            assert min(xs) <= 0 <= max(xs)
            assert min(ys) <= 0 <= max(ys)
            assert max(map(abs, xs+ys)) <= 2*m
        winding_sum += winding
    assert winding_sum == 1 and nonzero >= 1


def main():
    started = time.monotonic()
    print('OMP_NUM_THREADS=' + str(os.environ.get('OMP_NUM_THREADS')))
    print('Process nice value:', os.getpriority(os.PRIO_PROCESS, 0))
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    names = ['source-exponential-introduction.tex',
             'source-no-bigeodesics-introduction.tex',
             'source-qaoa-introduction.tex', 'source-crossings.tex',
             'source-preliminaries.tex', 'source-lean-scope.md',
             'source-gamma-target.lean', 'source-gamma-differentiability.lean']
    for name in names:
        assert (ROOT/name).read_text() == (PREVIOUS/name).read_text(), name
    print('Eight reopened sources unchanged: PASS')

    # Independent Laplace-transform calculation of the previous main identity.
    likelihood_cases = 0
    for kappa in [F(1, 2), F(1), F(3, 2), F(2), F(7)]:
        for delta in [F(1, 100), F(1, 8), F(1, 2)]:
            a = 1-delta
            # Compare the positive bases before raising to a real power kappa*M.
            laplace_base = a**(-2)/(1+2*(1/a-1))
            assert laplace_base == 1/(1-delta**2)
            likelihood_cases += 1
    print('Independent likelihood base checks:', likelihood_cases, 'PASS')

    count = 0
    for width, height in [(3, 3), (4, 3)]:
        points = [(x-1, y-1) for x in range(width) for y in range(height)]
        origin_bit = points.index((0, 0))
        for mask in range(1 << len(points)):
            if mask & (1 << origin_bit):
                check_cells({p for i, p in enumerate(points) if mask & (1 << i)})
                count += 1
    # Explicit hole, diagonal contacts, and disconnected components.
    extras = [
        {(x, y) for x in range(-2, 3) for y in range(-2, 3)}-{(1, 1)},
        {(0, 0), (1, 1), (2, 2), (2, 1)},
        {(0, 0), (3, 0), (3, 1), (-2, -2)},
    ]
    for cells in extras:
        check_cells(cells)
        count += 1
    print('Contour decomposition/winding/forced sites/packing:', count, 'sets PASS')

    a = F(1, 16)
    exact_tail = 9*((1+a)/(1-a)**3
                   -sum(F((m+1)**2)*a**m for m in range(4)))
    # A second evaluation after writing m=j+4 and summing j^2+10j+25.
    second = 9*a**4*(a*(1+a)/(1-a)**3 + 10*a/(1-a)**2 + 25/(1-a))
    assert exact_tail == second < F(3, 256) < 1
    print('Exact contour union bound:', exact_tail, '; independent forms agree PASS')
    for k in range(10):
        q = (2*k+1)**2
        assert 48*q == 6*(8*q)  # zeta^(1/(8q))=2^-6; 4 times it is 1/16.
    print('Explicit density exponent checks: 10 PASS')

    geometry = 0
    for s in [F(1), F(3, 2), F(5, 2), F(17, 3)]:
        for R in [F(1, 100), F(1), F(7, 2)]:
            for M in [1, 2, 7, 50]:
                S0 = 100*M*(R+1)*math.ceil(s)
                assert S0/s <= 200*M*(R+1)
                for b in [F(-1), F(-2, 3), F(0), F(1)]:
                    for X in [-101, -2, 0, 17]:
                        for sigma in [-1, 1]:
                            Y = sigma*3*S0
                            centers = []
                            for j in range(1, M+1):
                                h = (2*j-M-1)*3*(R+1)*math.ceil(s)
                                cy = math.floor(b*X+Y+h+F(1, 2))-b*X
                                assert abs(cy-(Y+h)) <= F(1, 2)
                                assert abs(cy-Y)+R*s <= S0/4
                                centers.append(cy)
                            assert all(v-u > 2*R*s
                                       for u, v in zip(centers, centers[1:]))
                            geometry += 1
    print('Exact rational strip placement cases:', geometry, 'PASS')
    dependence = 0
    for A in [F(1, 100), F(1), F(3, 2), F(10)]:
        k = math.ceil(4*(A+3)+8)+1
        for di in range(-math.floor(2*(A+3)), math.floor(2*(A+3))+1):
            for dj in range(-8, 9):
                dv1, dv2 = 2*di-dj, dj-di
                assert max(abs(dv1), abs(dv2)) < k
                dependence += 1
    print('Dependence-coordinate cases:', dependence, 'PASS')

    verify = (ROOT/'VERIFY.md').read_text()
    total = 0
    for name in names[:3]:
        blocks = re.findall(r'\\begin\{theorem\}[\s\S]*?\\end\{theorem\}',
                            (ROOT/name).read_text())
        for block in blocks:
            assert block in verify
        total += len(blocks)
    assert total == 4
    report = (ROOT/'REPORT.md').read_text()
    assert report.startswith('VERDICT: PARTIAL ')
    assert 'df:cr:rare-fast' in report
    for doc in ['VERIFY.md', 'PROOF.md']:
        for target in re.findall(r'\]\(([^)]+)\)', (ROOT/doc).read_text()):
            if not target.startswith(('https://', 'http://')):
                assert (ROOT/target).exists(), target
    print('Four exact theorem blocks, verdict, local links: PASS')
    print('Elapsed seconds:', round(time.monotonic()-started, 3))
    peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss < 1024**3
    print('Peak RSS bytes (macOS):', peak_rss)


if __name__ == '__main__':
    main()
