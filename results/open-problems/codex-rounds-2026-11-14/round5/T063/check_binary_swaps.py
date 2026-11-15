"""Exact finite audit of binary-bridge swaps. Python standard library only.

Local tests use monotone psi coordinates. Domain tests enumerate h coordinates
independently and calculate vertex weights by equality of opposite heights.
"""

from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
import os
import resource
import signal
import sys
import time


def prior_edge_recheck():
    both, single = Counter(), Counter()
    for h in product((0, 1), repeat=4):
        for v in product((0, 1), repeat=4):
            ix = lambda x, y: (y % 2) * 2 + x % 2
            if any(h[ix(x - 1, y)] + v[ix(x, y - 1)] != h[ix(x, y)] + v[ix(x, y)]
                   for x, y in product(range(2), repeat=2)):
                continue
            n = sum(h[ix(0, y)] for y in range(2))
            m = sum(v[ix(x, 0)] for x in range(2))
            degree = sum(h[ix(x - 1, y)] != h[ix(x, y)]
                         for x, y in product(range(2), repeat=2))
            if n == 1:
                single[degree] += 1
                if m == 1:
                    both[degree] += 1
    assert both == Counter({0: 4, 4: 2})
    assert single == Counter({0: 8, 4: 2})
    print('prior independent all-edge recheck: doubly balanced=%s; singly balanced=%s PASS'
          % (dict(sorted(both.items())), dict(sorted(single.items()))))


NN_BLOCK = ((0, 1), (0, 2), (1, 3), (2, 3))
DIAG_BLOCK = ((0, 3, 1, 2), (1, 2, 0, 3))


def admissible_psi(p):
    return all(p[v] - p[u] in (0, 1) for u, v in NN_BLOCK)


def to_h(p):
    return tuple(2 * z - offset for z, offset in zip(p, (0, 1, 1, 2)))


def a_values(p):
    return (int(p[3] - p[0] == 1), int(p[1] == p[2]))


def c_vertex(h, diag):
    return int(all(h[u] == h[v] for u, v, _, _ in diag))


def saddle(D, diagonal, ell=0):
    u, v, z, t = diagonal
    return D[u] == D[v] and abs(D[u] - ell) == 1 and D[z] == D[t] == ell


def bridge_probability(D, diagonals, eta, cs, ell=0):
    out = F(1)
    for d, opened, c in zip(diagonals, eta, cs):
        if saddle(D, d, ell):
            q = 1 / (c * c)
            out *= 1 - q if opened else q
        elif opened:
            return F(0)
    return out


def swap_pair(p1, p2, mask, ell=0):
    return (tuple(p2[i] - ell if mask[i] else p1[i] for i in range(len(p1))),
            tuple(p1[i] + ell if mask[i] else p2[i] for i in range(len(p1))))


def local_audit():
    blocks = [(0, x, y, z) for x, y, z in product(range(3), repeat=3)
              if admissible_psi((0, x, y, z))]
    assert len(blocks) == 6
    admissibility_checks = graph_checks = mass_checks = level_checks = 0
    chi_hist = Counter()
    cs = (F(1), F(3, 2), F(2), F(3))
    for p1, base, shift in product(blocks, blocks, range(-4, 5)):
        p2 = tuple(z + shift for z in base)
        D = tuple(v - u for u, v in zip(p1, p2))
        for mask in product((False, True), repeat=4):
            t1, t2 = swap_pair(p1, p2, mask)
            for ell in (-3, 2):
                shifted = tuple(z + ell for z in p2)
                l1, l2 = swap_pair(p1, shifted, mask, ell)
                assert l1 == t1 and l2 == tuple(z + ell for z in t2)
                level_checks += 1
            separated = all(not (mask[u] != mask[v] and D[u] != 0 and D[v] != 0)
                            for u, v in NN_BLOCK)
            assert (admissible_psi(t1) and admissible_psi(t2)) == separated
            admissibility_checks += 1
            if not separated:
                continue
            old_a = tuple(u + v for u, v in zip(a_values(p1), a_values(p2)))
            new_a = tuple(u + v for u, v in zip(a_values(t1), a_values(t2)))
            for d, before, after in zip(DIAG_BLOCK, old_a, new_a):
                u, v, z, t = d
                split = mask[u] != mask[v]
                monotone = {D[u], D[v]} == {-1, 1} and D[z] == D[t] == 0
                predicted = -2 if split and saddle(D, d) else 2 if split and monotone else 0
                assert after - before == predicted
                chi_hist[predicted] += 1
            DD = tuple(v - u for u, v in zip(t1, t2))
            for eta in product((0, 1), repeat=2):
                if any(e and not saddle(D, d) for d, e in zip(DIAG_BLOCK, eta)):
                    continue
                if any(e and mask[d[0]] != mask[d[1]] for d, e in zip(DIAG_BLOCK, eta)):
                    continue
                old_edges = {tuple(sorted((u, v))) for u, v in NN_BLOCK if D[u] and D[v]}
                old_edges.update(tuple(sorted(d[:2])) for d, e in zip(DIAG_BLOCK, eta) if e)
                new_edges = {tuple(sorted((u, v))) for u, v in NN_BLOCK if DD[u] and DD[v]}
                new_edges.update(tuple(sorted(d[:2])) for d, e in zip(DIAG_BLOCK, eta) if e)
                assert old_edges == new_edges
                assert all(not e or saddle(DD, d) for d, e in zip(DIAG_BLOCK, eta))
                assert swap_pair(t1, t2, mask) == (p1, p2)
                graph_checks += 1
                for c in cs:
                    old_mass = c ** (c_vertex(to_h(p1), DIAG_BLOCK) + c_vertex(to_h(p2), DIAG_BLOCK))
                    old_mass *= bridge_probability(D, DIAG_BLOCK, eta, (c, c))
                    new_mass = c ** (c_vertex(to_h(t1), DIAG_BLOCK) + c_vertex(to_h(t2), DIAG_BLOCK))
                    new_mass *= bridge_probability(DD, DIAG_BLOCK, eta, (c, c))
                    assert old_mass == new_mass
                    mass_checks += 1
    print('local psi audit: %d block pairs; %d mask admissibility checks PASS'
          % (len(blocks) ** 2 * 9, admissibility_checks))
    print('local diagonal changes=%s; %d graph/involution checks; %d rational mass checks PASS'
          % (dict(sorted(chi_hist.items())), graph_checks, mass_checks))
    print('nonzero-level covariance checks=%d PASS' % level_checks)
    # Explicit reason that NN components alone cannot be swapped at c>1.
    h1, h2 = (0, 1, 1, 0), (2, 1, 1, 2)
    tt1, tt2 = swap_pair(h1, h2, (True, False, False, False))
    c = F(2)
    before = c ** (c_vertex(h1, DIAG_BLOCK) + c_vertex(h2, DIAG_BLOCK))
    after = c ** (c_vertex(tt1, DIAG_BLOCK) + c_vertex(tt2, DIAG_BLOCK))
    assert before == 4 and after == 1
    assert before / (c * c) == after
    print('unbridged saddle counterexample at c=2: pair weight 4 -> 1; closed factor 1/4 repairs PASS')


def geometry(iw, ih):
    width, height = iw + 2, ih + 2
    coords = [(x, y) for y in range(height) for x in range(width)]
    boundary = {i for i, (x, y) in enumerate(coords)
                if x in (0, width - 1) or y in (0, height - 1)}
    nn = [(i, j) for i, a in enumerate(coords) for j, b in enumerate(coords)
          if i < j and abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1]
    blocks = []
    for y in range(height - 1):
        for x in range(width - 1):
            s = y * width + x
            blocks.append(((s, s + width + 1, s + 1, s + width),
                           (s + 1, s + width, s, s + width + 1)))
    diagonals = [d for block in blocks for d in block]
    return coords, boundary, nn, blocks, diagonals


def height_fillings(coords, boundary, nn, profile):
    """Enumerate heights with fixed collar, using distance bounds and NN tests."""
    n = len(coords)
    seed = [None] * n
    for i in boundary:
        x, y = coords[i]
        seed[i] = profile((x + y) % 2)
    interior = [i for i in range(n) if i not in boundary]
    options = {}
    for i in interior:
        x, y = coords[i]
        lo = max(seed[j] - abs(x - coords[j][0]) - abs(y - coords[j][1]) for j in boundary)
        hi = min(seed[j] + abs(x - coords[j][0]) + abs(y - coords[j][1]) for j in boundary)
        options[i] = [z for z in range(lo, hi + 1) if (z - x - y) % 2 == 0]
    neighbors = {i: [v if u == i else u for u, v in nn if i in (u, v)] for i in range(n)}
    out = []

    def visit(k):
        if k == len(interior):
            assert all(abs(seed[u] - seed[v]) == 1 for u, v in nn)
            out.append(tuple(seed))
            return
        i = interior[k]
        for z in options[i]:
            if all(seed[j] is None or abs(seed[j] - z) == 1 for j in neighbors[i]):
                seed[i] = z
                visit(k + 1)
        seed[i] = None

    visit(0)
    return out


def graph_components(D, eta, nn, diagonals, boundary):
    adj = {i: set() for i, d in enumerate(D) if d}
    for u, v in nn:
        if D[u] and D[v]:
            adj[u].add(v)
            adj[v].add(u)
    for (u, v, _, _), opened in zip(diagonals, eta):
        if opened:
            adj[u].add(v)
            adj[v].add(u)
    components, unseen = [], set(adj)
    while unseen:
        stack, seen = [min(unseen)], set()
        while stack:
            i = stack.pop()
            if i in seen:
                continue
            seen.add(i)
            stack.extend(adj[i] - seen)
        unseen -= seen
        components.append(tuple(sorted(seen)))
    components.sort()
    finite = [comp for comp in components if not boundary.intersection(comp)]
    edges = frozenset((min(u, v), max(u, v)) for u in adj for v in adj[u])
    return finite, edges


def independent_fillings_and_geometric_checks():
    # No recursion, distance bounds, or psi-coordinate local enumerator.
    for iw, ih, expected in ((2, 2, 7), (3, 2, 17)):
        coords, boundary, nn, _, _ = geometry(iw, ih)
        interior = [i for i in range(len(coords)) if i not in boundary]
        good = set()
        for bits in product((0, 1), repeat=len(interior)):
            h = [(x + y) % 2 for x, y in coords]
            for i, bit in zip(interior, bits):
                x, y = coords[i]
                h[i] = 2 * bit - (x + y) % 2
            if all(abs(h[u] - h[v]) == 1 for u, v in nn):
                good.add(tuple(h))
        direct = set(height_fillings(coords, boundary, nn, lambda parity: parity))
        assert len(good) == expected and good == direct
        print('independent full-assignment height count %dx%d=%d PASS' % (iw, ih, expected))
    checks = 0
    for c in (F(3, 2), F(2), F(3)):
        q = 1 / (c * c)
        # Exact infinite geometric sums, as a finite prefix plus its tail.
        closed = sum((1 - q) * q ** n for n in range(1, 8)) + q ** 8
        assert closed == q and (1 - q) + closed == 1
        for n in range(1, 8):
            assert c ** 2 * (1 - q) * q ** n == (1 - q) * q ** (n - 1)
            checks += 1
    print('independent geometric projection: closed probability q; %d saddle mass checks PASS' % checks)


def domain_audit(iw, ih, boundary_kind, weight_kind, ell=0):
    coords, boundary, nn, blocks, diagonals = geometry(iw, ih)
    profile1 = lambda parity: parity
    raw_profile2 = {'same': lambda parity: parity,
                'shifted': lambda parity: parity + 2,
                'reflected': lambda parity: -parity}[boundary_kind]
    profile2 = lambda parity: raw_profile2(parity) + 2 * ell
    fillings1 = height_fillings(coords, boundary, nn, profile1)
    fillings2 = height_fillings(coords, boundary, nn, profile2)
    if weight_kind == 'inhomogeneous':
        cycle = (F(1), F(3, 2), F(2), F(3))
        cs = [cycle[i % len(cycle)] for i in range(len(blocks))]
    else:
        cs = [F(weight_kind)] * len(blocks)
    diag_cs = [c for c in cs for _ in range(2)]
    groups = defaultdict(list)
    states = {}
    largest = 0
    for h1, h2 in product(fillings1, fillings2):
        base = F(1)
        for block, c in zip(blocks, cs):
            base *= c ** (c_vertex(h1, block) + c_vertex(h2, block))
        D = tuple((v - u) // 2 - ell for u, v in zip(h1, h2))
        choices = [(0, 1) if saddle(D, d) else (0,) for d in diagonals]
        total_bridge_mass = F(0)
        for eta in product(*choices):
            bridge_mass = bridge_probability(D, diagonals, eta, diag_cs)
            total_bridge_mass += bridge_mass
            if not bridge_mass:
                continue
            comps, edges = graph_components(D, eta, nn, diagonals, boundary)
            assert all(len({1 if D[i] > 0 else -1 for i in comp}) == 1 for comp in comps)
            largest = max(largest, len(comps))
            mass = base * bridge_mass
            key = (tuple(u + v for u, v in zip(h1, h2)), tuple(abs(d) for d in D), eta)
            signs = tuple(1 if D[comp[0]] > 0 else -1 for comp in comps)
            groups[key].append((signs, mass, len(comps)))
            state_key = (h1, h2, eta)
            assert state_key not in states
            states[state_key] = (mass, comps, edges)
        assert total_bridge_mass == 1
    swap_count = 0
    for (h1, h2, eta), (mass, comps, edges) in states.items():
        for selected in product((False, True), repeat=len(comps)):
            changed = {i for comp, choose in zip(comps, selected) if choose for i in comp}
            mask = tuple(i in changed for i in range(len(coords)))
            t1, t2 = swap_pair(h1, h2, mask, 2 * ell)
            new_mass, new_comps, new_edges = states[t1, t2, eta]
            assert mass == new_mass and comps == new_comps and edges == new_edges
            assert swap_pair(t1, t2, mask, 2 * ell) == (h1, h2)
            swap_count += 1
    for entries in groups.values():
        k = entries[0][2]
        assert len(entries) == 2 ** k
        assert {s for s, _, _ in entries} == set(product((-1, 1), repeat=k))
        total = sum(m for _, m, _ in entries)
        assert all(m / total == F(1, 2 ** k) for _, m, _ in entries)
    print('domain %dx%d boundary=%s c=%s ell=%d: fillings=%dx%d states=%d groups=%d max_clusters=%d swaps=%d PASS'
          % (iw, ih, boundary_kind, weight_kind, ell, len(fillings1), len(fillings2),
             len(states), len(groups), largest, swap_count))
    return len(states), len(groups), swap_count


def main():
    signal.alarm(120)
    start = time.monotonic()
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15
    print('OMP_NUM_THREADS=1; effective_nice=%d' % priority)
    prior_edge_recheck()
    local_audit()
    independent_fillings_and_geometric_checks()
    totals = [0, 0, 0]
    for shape, kind, c in product(((2, 2), (3, 2)),
                                  ('same', 'shifted', 'reflected'),
                                  ('1', '3/2', '2', 'inhomogeneous')):
        result = domain_audit(*shape, kind, c)
        totals = [a + b for a, b in zip(totals, result)]
    for kind, c, ell in (('same', '3/2', -2), ('reflected', 'inhomogeneous', 3)):
        result = domain_audit(3, 2, kind, c, ell)
        totals = [a + b for a, b in zip(totals, result)]
    print('domain totals: states=%d groups=%d swap images=%d PASS' % tuple(totals))
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1_000_000_000
    print('peak_RSS_bytes=%d; elapsed_seconds=%.3f' % (rss, time.monotonic() - start))


if __name__ == '__main__':
    main()
