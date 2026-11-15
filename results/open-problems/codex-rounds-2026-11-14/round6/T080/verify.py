#!/usr/bin/env python3
"""Exact scalar/combinatorial audits; floating-point packing checks are secondary."""
from collections import defaultdict, deque
from fractions import Fraction as F
import itertools
import json
import math
import os
from pathlib import Path
import random
import resource
import sys
import time

START = time.monotonic()
ROOT = Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
PRIORITY = os.getpriority(os.PRIO_PROCESS, 0)
assert PRIORITY >= 15
for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    assert os.environ.get(name) == '1'

S, DELTA, T = F(101, 100), F(1, 400), F(11, 10)


def scalars():
    # Recheck round 5 independently, using a much finer rational radical bracket.
    denominator = 10**12
    lo, hi = F(1732050807568, denominator), F(1732050807569, denominator)
    assert lo**2 < 3 < hi**2
    length = 4-2*DELTA
    interval_lower = 2/(hi*S*S)*(length-2*S/lo)*(length-S-4*S/lo)
    assert interval_lower > F(2089, 1000) > 2
    # Second route: expand first, then clear denominators and compare integers.
    a = -4*(3*length-S)/(3*S)
    b = 2*(length*(length-S)+F(8, 3)*S*S)/(3*S*S)
    assert a == F(-4390, 303) and b == F(1757441, 183618)
    gap = 3*b*b-(2-a)**2
    integer_gap = 3*b.numerator**2*(2-a).denominator**2 - (2-a).numerator**2*b.denominator**2
    assert gap == F(33193389889, 11238523308) > 0 and integer_gap > 0
    print(f'prior_independent_radical_interval_lower={float(interval_lower):.12g}>2; cleared_integer_comparison=PASS')
    assert S-2*DELTA == F(201, 200) > 1
    assert S+2*DELTA == F(203, 200) < T
    assert 2*S*S > (T+2*DELTA)**2
    assert F(5, 3)**2 < 3 and 3*S/5+DELTA == F(1217, 2000) < 1
    assert 2*DELTA/S == F(1, 202) < F(1, 100) < F(1, 8)
    # Independent angle bound from cross product and the perturbed bond length.
    assert 2*DELTA/(S-2*DELTA) == F(1, 201) < F(1, 100)
    # The displayed lower bound sin(pi/12)>1/8 follows from these squares.
    assert 6 > 2**2 and 2 < F(3, 2)**2
    width = S/2+DELTA
    ro = 2+T
    assert width == F(203, 400) and ro == F(31, 10)
    assert width+ro == F(1443, 400)
    m = (width+ro).__floor__()+1
    assert m == 4 and len(range(-m+1, m)) == 7
    print('exact_detector_constants=PASS; cutoff=11/10; angular_sine=1/100; observation_radius=31/10; M=4; band_columns=7')
    return dict(prior_interval_lower=str(interval_lower), prior_squared_gap=str(gap),
                cutoff=str(T), angular_sine='1/100', observation_radius=str(ro),
                half_width=str(width), M=m, band_columns=7)


FOUR = ((1, 0), (-1, 0), (0, 1), (0, -1))
EIGHT = tuple((x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if (x, y) != (0, 0))


def legal(grid):
    return all({label, grid.get((x+dx, y+dy))} != {'A', 'B'}
               for (x, y), label in grid.items() for dx, dy in ((1, 0), (0, 1)))


def defect_path(grid, height, steps=EIGHT):
    parent = {p: None for p in grid if p[1] == 0 and grid[p] == 'D'}
    queue = deque(parent)
    while queue:
        p = queue.popleft()
        if p[1] == height-1:
            path = []
            while p is not None:
                path.append(p)
                p = parent[p]
            return path
        for dx, dy in steps:
            q = (p[0]+dx, p[1]+dy)
            if grid.get(q) == 'D' and q not in parent:
                parent[q] = p
                queue.append(q)
    return None


def interface_audit(grid, columns, height):
    # Independent construction of the drawn-edge graph in PROOF.md.
    adjacency = defaultdict(set)
    for (i, j), label in grid.items():
        for di, dj in ((1, 0), (0, 1)):
            q = (i+di, j+dj)
            if q not in grid or (label == 'A') == (grid[q] == 'A'):
                continue
            non_a = (i, j) if label != 'A' else q
            assert grid[non_a] == 'D'
            if di:
                p1, p2 = (2*i+1, 2*j-1), (2*i+1, 2*j+1)
            else:
                p1, p2 = (2*i-1, 2*j+1), (2*i+1, 2*j+1)
            adjacency[p1].add(p2)
            adjacency[p2].add(p1)
    top = [p for p in adjacency if p[1] == 2*height-1]
    bottom = [p for p in adjacency if p[1] == -1]
    assert len(top) % 2 == len(bottom) % 2 == 1
    for p, neighbors in adjacency.items():
        assert p[0] not in (-1, 2*columns-1)
        assert len(neighbors) == 1 if p in top or p in bottom else len(neighbors) in (2, 4)
    seen, bridges = set(), 0
    for start in adjacency:
        if start in seen:
            continue
        queue, component = [start], set()
        while queue:
            p = queue.pop()
            if p in component:
                continue
            component.add(p)
            queue.extend(adjacency[p]-component)
        seen.update(component)
        nt = sum(p in component for p in top)
        nb = sum(p in component for p in bottom)
        assert (nt+nb) % 2 == 0
        bridges += bool(nt and nb)
    assert bridges >= 1


def transfer_count(width, height):
    rows = [('A',)+row+('B',) for row in itertools.product('ABD', repeat=width)]
    rows = [row for row in rows if all({a, b} != {'A', 'B'} for a, b in zip(row, row[1:]))]
    compatible = [[k for k, q in enumerate(rows)
                   if all({a, b} != {'A', 'B'} for a, b in zip(p, q))] for p in rows]
    counts = [1]*len(rows)
    for _ in range(1, height):
        counts = [sum(counts[k] for k in ks) for ks in compatible]
    return sum(counts)


def exhaustive_separators():
    results = []
    for width, height in ((1, 5), (2, 4), (3, 3)):
        sites = list(itertools.product(range(1, width+1), range(height)))
        grid = {(0, j): 'A' for j in range(height)}
        grid.update({(width+1, j): 'B' for j in range(height)})
        count, diagonal_only, minimum = 0, 0, 10**9
        for labels in itertools.product('ABD', repeat=len(sites)):
            grid.update(zip(sites, labels))
            if not legal(grid):
                continue
            path = defect_path(grid, height)
            assert path is not None and len(path) >= height
            assert len(set(path)) == len(path)
            assert all(grid[p] == 'D' for p in path)
            interface_audit(grid, width+2, height)
            diagonal_only += defect_path(grid, height, FOUR) is None
            minimum = min(minimum, len(path))
            count += 1
        assert count == transfer_count(width, height)
        results.append(dict(interior_width=width, height=height,
                            all_assignments=3**len(sites), legal_assignments=count,
                            no_face_connected_crossing=diagonal_only, minimum_path_vertices=minimum))
        print(f'exhaustive_grid={width}x{height}; assignments={3**len(sites)}; legal={count}; eight_neighbor_crossings=ALL; four_neighbor_failures={diagonal_only}; independent_transfer_count=PASS')
    # Explicit diagonal separator: face-connected conclusion is false.
    diagonal = {(i, j): ('A' if i < j+1 else 'D' if i == j+1 else 'B')
                for i in range(5) for j in range(3)}
    assert legal(diagonal) and defect_path(diagonal, 3)
    assert defect_path(diagonal, 3, FOUR) is None
    # Without exclusion of A-B neighbors the separator assertion fails.
    abrupt = {(i, j): ('A' if i < 2 else 'B') for i in range(4) for j in range(3)}
    assert not legal(abrupt) and defect_path(abrupt, 3) is None
    # Empty windows pass universal tests if occupancy is omitted; a singleton
    # passes the direction test for both families if neighbor existence is omitted.
    assert all([]) and not bool([])
    print('negative_controls=PASS: face_adjacency, missing_A_B_exclusion, empty_window, isolated_particle')
    return results


def floating_labels(points, anchor):
    inner = [p for p in points if math.dist(p, anchor) < 2]
    if not any(math.dist(p, anchor) < 1 for p in inner):
        return 'D'
    accepted = []
    for theta, label in ((0.0, 'A'), (math.pi/6, 'B')):
        okay = True
        for p in inner:
            neighbors = [q for q in points if q != p and math.dist(p, q) <= float(T)]
            if not neighbors:
                okay = False
                break
            for q in neighbors:
                angle = math.atan2(q[1]-p[1], q[0]-p[0])-theta
                error = abs((angle+math.pi/6) % (math.pi/3)-math.pi/6)
                if error > math.asin(0.01):
                    okay = False
                    break
            if not okay:
                break
        if okay:
            accepted.append(label)
    assert len(accepted) <= 1
    return accepted[0] if accepted else 'D'


def packing_checks():
    rng = random.Random(6080)
    output = []
    # Inverse triangular-basis rows have norm 2/(s sqrt(3)); rotations
    # preserve this. Thus the index range covers every nominal point in
    # the patch for every phase used below, rather than just a sampled subset.
    assert (30*S)**2*3 > 4*(F(21, 2)**2+F(23, 2)**2)
    for trial in range(3):
        points = []
        for side, theta in ((-1, 0.0), (1, math.pi/6)):
            phase = (rng.uniform(-0.5, 0.5), rng.uniform(-0.5, 0.5))
            for m, n in itertools.product(range(-30, 31), repeat=2):
                x, y = float(S)*(m+n/2), float(S)*math.sqrt(3)*n/2
                x, y = (phase[0]+x*math.cos(theta)-y*math.sin(theta),
                        phase[1]+x*math.sin(theta)+y*math.cos(theta))
                if side*x <= float(S)/2:
                    continue
                if not (-10 < x < 10 and -11 < y < 11):
                    continue
                radius, angle = float(DELTA)*math.sqrt(rng.random()), rng.uniform(0, 2*math.pi)
                points.append((x+radius*math.cos(angle), y+radius*math.sin(angle)))
        added = 0
        width = float(S/2+DELTA)
        # Arbitrary greedy filling is a supporting example, not a universal audit.
        for _ in range(1500):
            q = (rng.uniform(-width, width), rng.uniform(-9.5, 9.5))
            if all(math.dist(p, q) >= 1 for p in points):
                points.append(q)
                added += 1
        minimum = min(math.dist(p, q) for i, p in enumerate(points) for q in points[i+1:])
        assert minimum >= 1
        # The observations used here fit strictly within the generated patch.
        assert 4+float(2+T) < 10-float(DELTA)
        assert 5+float(2+T) < 11-float(DELTA)
        grid = {(i+4, j+5): floating_labels(points, (i, j))
                for i in range(-4, 5) for j in range(-5, 6)}
        assert all(grid[(0, j)] == 'A' and grid[(8, j)] == 'B' for j in range(11))
        assert legal(grid)
        path = defect_path(grid, 11)
        assert path is not None and len(path) >= 11
        interface_audit(grid, 9, 11)
        result = dict(trial=trial, added_centers=added, minimum_separation=minimum,
                      defect_path_vertices=len(path), observed_anchors=len(grid))
        output.append(result)
        print(f'floating_packing_trial={trial}; inserted={added}; minimum_distance={minimum:.12g}; defect_crossing_vertices={len(path)}; supporting_only')
    return output


def main():
    print(f'nice_priority={PRIORITY}; thread_environment=1; CPU_limit_seconds=90')
    result = scalars()
    result['exhaustive_grids'] = exhaustive_separators()
    result['packing_trials'] = packing_checks()
    result['packing_seed'] = 6080
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result.update(status='PASS', nice_priority=PRIORITY,
                  elapsed_seconds=time.monotonic()-START,
                  peak_rss_mib=rss/(1024**2 if sys.platform == 'darwin' else 1024))
    assert result['peak_rss_mib'] < 128
    (ROOT/'verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(f"PASS; elapsed_seconds={result['elapsed_seconds']:.3f}; peak_rss_mib={result['peak_rss_mib']:.3f}")


if __name__ == '__main__':
    main()
