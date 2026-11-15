"""Exact finite checks of the chunk-to-disjoint-witness reduction.
Run: OMP_NUM_THREADS=1 nice -n 15 python3 audit.py
Only stdlib; bounded fixtures, 60-second alarm, no file writes.
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
ROOT = Path(__file__).resolve().parent
STATS = dict(paths=0, chunks=0, intervals=0, cheap_full=0, negative=0,
             transverse=0, forward=0, backward=0, repeated_index_paths=0,
             shifted_phase=0, multiple_witness=0, packing=0, equality=0, crossing_only=0, tied_exit=0, empty_outer=0)


def walk(start, steps):
    result = [start]
    for dx, dy in steps:
        x, y = result[-1]
        result.append((x+dx, y+dy))
    assert len(set(result)) == len(result)
    return result


def fixture_paths(start, b, s, L):
    east, north, west, south = (1, 0), (0, 1), (-1, 0), (0, -1)
    for steps in ([east]*(4*L+3), [west]*(2*L+3),
                  [north]*(2*s+3), [south]*(2*s+3),
                  [east]*(2*L)+[north]*(2*s)+[west]*(2*L)+[south]*(2*s-1)):
        yield walk(start, steps)
    # A monotone digital path following the prescribed slope.
    x0, y0 = start
    steps = []
    last_y = y0
    for k in range(1, 4*L+4):
        steps.append(east)
        target = y0+math.floor(b*k)
        for _ in range(abs(target-last_y)):
            steps.append(north if target > last_y else south)
        last_y = target
    yield walk(start, steps)


def packing(intervals, n):
    # Maximum edge-disjoint intervals by two independent optimizers.
    right = 0
    greedy = 0
    for l, r in sorted(intervals, key=lambda v: (v[1], v[0])):
        if l >= right:
            greedy += 1
            right = r
    by_end = [[] for _ in range(n+1)]
    for l, r in intervals:
        by_end[r].append(l)
    dp = [0]*(n+1)
    for r in range(1, n+1):
        dp[r] = max([dp[r-1]]+[dp[l]+1 for l in by_end[r]])
    assert greedy == dp[-1]
    STATS['packing'] += 1
    return greedy


def check_path(vertices, weights, b, a, c, m0, s, L):
    eta = min(F(1), c/4)
    threshold = eta*s
    amin, aplus = a-c, a+c
    K = 100*(1+abs(amin)+abs(aplus))
    Cf = max(abs(m0-a*b), abs(a))
    assert Cf <= threshold
    assert 2*m0*L-abs(a)*(s+1) > threshold
    assert 3*threshold+2*abs(a)*(s+1) < K*s
    rcoords = [F(y)-b*x for x, y in vertices]
    costs = [F(0)]
    for w in weights:
        assert w >= 0
        costs.append(costs[-1]+w)
    cuts = []
    first = 0
    for j in range(1, len(vertices)):
        if (abs(vertices[j][0]-vertices[first][0]) >= 2*L
                or abs(rcoords[j]-rcoords[first]) >= s):
            cuts.append((first, j, True))
            first = j
    cuts.append((first, len(vertices)-1, False))
    indices = []
    maxsum = 0
    localsum = F(0)
    for first, last, full in cuts:
        STATS['chunks'] += 1
        x0 = vertices[first][0]
        r0 = rcoords[first]
        i, h = math.floor(F(x0, L)), math.floor(r0/s)
        indices.append((i, h))
        center = F(math.floor(b*i*L))+h*s-b*i*L
        crosscenter = F(math.floor(b*(i+1)*L))+h*s-b*(i+1)*L
        STATS['shifted_phase'] += center != crosscenter
        assert all(abs(x-i*L) <= 4*L and abs(r-center) <= 4*s
                   for (x, _), r in zip(vertices[first:last+1], rcoords[first:last+1]))
        assert all(abs(r-crosscenter) <= 2*s+2 for r in rcoords[first:last+1])
        dx = vertices[last][0]-x0
        dr = rcoords[last]-r0
        H = costs[last]-costs[first]-m0*dx-a*dr
        assert min(costs[last]-costs[first]-m0*dx-amin*dr,
                   costs[last]-costs[first]-m0*dx-aplus*dr) == H-c*abs(dr)
        n = last-first
        # Oracle: all contiguous subpaths, in both directions, tested
        # directly against the two defining alternatives of A_(i,h).
        found = set()
        first_alternative = set()
        for l in range(n):
            for end in range(l+1, n+1):
                STATS['intervals'] += 1
                ll, rr = first+l, first+end
                C = costs[rr]-costs[ll]
                ddx = vertices[rr][0]-vertices[ll][0]
                ddr = rcoords[rr]-rcoords[ll]
                for sign in [-1, 1]:
                    hminus = C-sign*(m0*ddx+amin*ddr)
                    hplus = C-sign*(m0*ddx+aplus*ddr)
                    if min(hminus, hplus) < -threshold:
                        first_alternative.add((l, end))
                        found.add((l, end))
                        break
                    p, q = (ll, rr) if sign == 1 else (rr, ll)
                    if (vertices[p][0] == (i+1)*L
                            and vertices[q][0] == (i+2)*L
                            and C < m0*L+K*s
                            and all(i*L <= vertices[z][0] <= (i+3)*L
                                    and abs(rcoords[z]-crosscenter) <= 8*s
                                    for z in range(ll, rr+1))):
                        found.add((l, end))
                        break
        M = packing(found, n)
        STATS['multiple_witness'] += M >= 2
        assert H >= -threshold-2*threshold*M
        if H < 0:
            STATS['negative'] += 1
        STATS['equality'] += H == threshold
        if full:
            if abs(dr) >= s:
                STATS['transverse'] += 1
            elif dx > 0:
                STATS['forward'] += 1
            else:
                STATS['backward'] += 1
            if H < threshold:
                STATS['cheap_full'] += 1
                STATS['crossing_only'] += not first_alternative
                STATS['tied_exit'] += abs(dr) >= s and abs(dx) == 2*L
                STATS['empty_outer'] += dx == 2*L and x0 == i*L
                assert M >= 1
            assert H >= threshold-4*threshold*M
            localsum += threshold-4*threshold*M
        else:
            localsum += -threshold-4*threshold*M
        maxsum += M
    N = len(cuts)-1
    total = costs[-1]-m0*(vertices[-1][0]-vertices[0][0])-a*(rcoords[-1]-rcoords[0])
    assert total >= localsum == (N-1)*threshold-4*threshold*maxsum
    STATS['repeated_index_paths'] += len(indices) > len(set(indices))
    STATS['paths'] += 1


def main():
    started = time.monotonic()
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15
    print('OMP_NUM_THREADS=1; process nice:', priority)
    s, L, m0 = 8, 16, F(1)
    for b in map(F, [-1, F(-2, 3), 0, F(1, 3), 1]):
        for a in [F(-1, 3), F(0), F(1, 3)]:
            for c in [F(1), F(4)]:
                for start in [(-L-1, -s-1), (L-1, s-1)]:
                    for vertices in fixture_paths(start, b, s, L):
                        for profile in [0, 1]:
                            weights = []
                            for p, q in zip(vertices, vertices[1:]):
                                dx, dy = q[0]-p[0], q[1]-p[1]
                                stepf = m0*dx+a*(dy-b*dx)
                                weights.append(F(1, 16) if profile == 0 else abs(stepf))
                            check_path(vertices, weights, b, a, c, m0, s, L)
    # A forward crossing with an empty final outer piece.
    vertices = walk((0, 0), [(1, 0)]*(2*L))
    check_path(vertices, [F(1)]*(2*L), F(0), F(0), F(1), m0, s, L)
    # Simultaneous longitudinal/transverse exit at the last step.
    vertices = walk((0, 0), [(1, 0), (0, 1)]*24+[(1, 0)]*8)
    check_path(vertices, [F(1, 16)]*(len(vertices)-1), F(1), F(0), F(4), m0, s, L)
    # Exact equality must not be rounded into the strict cheap inequality.
    vertices = walk((0, 0), [(1, 0)]*(2*L))
    check_path(vertices, [F(1)+F(2, 2*L)]*(2*L), F(0), F(0), F(1), m0, s, L)
    for key in ['cheap_full', 'negative', 'transverse', 'forward', 'backward',
                'repeated_index_paths', 'shifted_phase', 'multiple_witness', 'equality',
                'crossing_only', 'tied_exit', 'empty_outer']:
        assert STATS[key] > 0, key
    for key, val in STATS.items():
        print(key+':', val)
    verify = (ROOT/'VERIFY.md').read_text()
    count = 0
    for name in ['source-exponential-introduction.tex',
                 'source-no-bigeodesics-introduction.tex', 'source-qaoa-introduction.tex']:
        blocks = re.findall(r'\\begin\{theorem\}[\s\S]*?\\end\{theorem\}', (ROOT/name).read_text())
        for block in blocks:
            assert block in verify
        count += len(blocks)
    assert count == 4
    for doc in ['VERIFY.md', 'PROOF.md']:
        for target in re.findall(r'\]\(([^)]+)\)', (ROOT/doc).read_text()):
            if not target.startswith(('http://', 'https://')):
                assert (ROOT/target).exists(), target
    assert (ROOT/'REPORT.md').read_text().startswith('VERDICT: PARTIAL ')
    print('Four exact theorem blocks, report verdict and local links: PASS')
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert rss < 1024**3
    print('Peak RSS bytes (macOS):', rss)
    print('Elapsed seconds:', round(time.monotonic()-started, 3))


if __name__ == '__main__':
    main()
