"""Finite exhaustive checks of collars, fillings and compatible supports."""
import itertools
import json
import os
import resource
import signal
import time
from pathlib import Path

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('180s limit')))
signal.alarm(180)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
start = time.monotonic()


class Grid:
    def __init__(self, dim, lo, hi):
        self.dim = dim
        self.sites = set(itertools.product(range(lo, hi+1), repeat=dim))
        self.edge = {p for p in self.sites if min(p) == lo or max(p) == hi}
        offsets = [a for a in itertools.product((-1, 0, 1), repeat=dim) if any(a)]
        self.neighbors = {p: {tuple(x+y for x, y in zip(p, a)) for a in offsets} & self.sites
                          for p in self.sites}

    def components(self, sites):
        left = set(sites)
        out = []
        while left:
            root = left.pop()
            found, todo = {root}, [root]
            while todo:
                new = self.neighbors[todo.pop()] & left
                left -= new
                found |= new
                todo.extend(new)
            out.append(found)
        return out

    def enlarge(self, sites):
        return set(sites).union(*(self.neighbors[p] for p in sites))

    def data(self, support):
        assert len(self.components(support)) == 1
        parts = self.components(self.sites-support)
        exterior = [a for a in parts if a & self.edge]
        assert len(exterior) == 1
        exterior = exterior[0]
        holes = [a for a in parts if not (a & self.edge)]
        fill = self.sites-exterior
        assert len(self.components(fill)) == 1
        for part in parts:
            boundary = part & self.enlarge(support)
            assert boundary and len(self.components(boundary)) == 1
        for hole in holes:
            assert len(self.components(self.sites-hole)) == 1
        return fill, holes

    def labeled(self, labels):
        # Values 0,1 are pure phases; 2 is the star macro label.
        candidates = self.enlarge(set(labels)) if labels else set()
        bad = set()
        for p in candidates:
            values = {labels.get(q, 0) for q in self.neighbors[p] | {p}}
            if len(values) != 1 or 2 in values:
                bad.add(p)
        supports = self.components(bad)
        fillings = []
        for support in supports:
            fill, holes = self.data(support)
            for part in self.components(self.sites-support):
                boundary = part & self.enlarge(support)
                assert not (boundary & bad)
                phases = {labels.get(p, 0) for p in boundary}
                assert len(phases) == 1 and 2 not in phases
                phase = next(iter(phases))
                support_collar = support & self.enlarge(part)
                assert support_collar
                assert all(labels.get(p, 0) == phase for p in support_collar)
            fillings.append((support, fill, holes))
        for a, b in itertools.combinations(fillings, 2):
            self.pair(a, b)
        return fillings

    def pair(self, a, b):
        s, fs, hs = a
        t, ft, ht = b
        assert not (self.enlarge(s) & t)
        if fs & ft:
            assert fs < ft or ft < fs
            inner, outer_holes = (s, ht) if fs < ft else (t, hs)
            assert sum(self.enlarge(inner) <= h for h in outer_holes) == 1
        else:
            assert not (self.enlarge(fs) & ft)
            assert len(self.components(self.sites-(fs | ft))) == 1


counts = dict(ternary_2d=0, binary_3d=0, sparse_ternary_3d=0, support_pairs=0)
g = Grid(2, -2, 4)
window = list(itertools.product(range(3), repeat=2))
for values in itertools.product(range(3), repeat=9):
    g.labeled({p: v for p, v in zip(window, values) if v})
    counts['ternary_2d'] += 1

g3 = Grid(3, -2, 3)
window3 = list(itertools.product(range(2), repeat=3))
for values in itertools.product(range(2), repeat=8):
    g3.labeled({p: v for p, v in zip(window3, values) if v})
    counts['binary_3d'] += 1
for values in itertools.product(range(3), repeat=6):
    g3.labeled({p: v for p, v in zip(window3[:6], values) if v})
    counts['sparse_ternary_3d'] += 1

# Independently vary two arbitrary connected supports, rather than derive them
# from a single labeling. All assignments on a 3 by 3 window are inspected.
catalog = {}
for mask in range(1, 1 << len(window)):
    s = frozenset(p for i, p in enumerate(window) if mask & (1 << i))
    if len(g.components(s)) == 1:
        fs, hs = g.data(s)
        catalog[s] = (s, fs, hs)
for s, a in catalog.items():
    for t, b in catalog.items():
        if s < t:  # set containment cannot be compatible
            continue
        if not (g.enlarge(s) & t):
            g.pair(a, b)
            counts['support_pairs'] += 1


def box(k, dim):
    return set(itertools.product(range(-k, k+1), repeat=dim))


examples = []
for dim in (2, 3):
    big = Grid(dim, -6, 6)
    # A real incorrect shell, computed locally before using volume formulas.
    states = {p: 1 for p in box(2, dim)}
    observed = big.labeled(states)
    assert len(observed) == 1
    s, fill, holes = observed[0]
    assert s == box(3, dim)-box(1, dim)
    assert fill == box(3, dim)
    domain = big.enlarge(s)
    assert domain == box(4, dim)-box(0, dim)
    assert fill-domain == box(0, dim)
    assert len(big.components(big.sites-domain)) == 2
    expected = ((7**dim-3**dim), (9**dim-1), 7**dim)
    observed_sizes = (len(s), len(domain), len(fill))
    assert observed_sizes == expected
    # Nested arbitrary connected supports, with full neighborhood containment.
    outer = box(4, dim)-box(3, dim)
    inner = box(1, dim)-box(0, dim)
    of, oh = big.data(outer)
    inf, inh = big.data(inner)
    big.pair((outer, of, oh), (inner, inf, inh))
    assert inf < of and big.enlarge(inner) <= oh[0]
    # A realized three-contour chain: both interfaces of a dense annulus,
    # followed by the incorrect component of a central star macrocell.
    larger = Grid(dim, -9, 9)
    states = {p: 1 for p in box(6, dim)}
    for p in box(3, dim):
        states.pop(p, None)
    origin = (0,)*dim
    states[origin] = 2
    family = larger.labeled(states)
    assert len(family) == 3
    assert any(a[1] < b[1] for a, b in itertools.permutations(family, 2))
    assert {len(a[1]) for a in family} == {3**dim, 9**dim, 15**dim}
    # Supports and fills must separate, but their one-cell enlargements can
    # overlap. This allows dependence on shared microscopic exterior states.
    left = (-2,)+(0,)*(dim-1)
    right = (2,)+(0,)*(dim-1)
    separated = big.labeled({left: 2, right: 2})
    assert len(separated) == 2
    a, b = separated
    shared = big.enlarge(a[0]) & big.enlarge(b[0])
    assert len(shared) == 5**(dim-1)
    assert not (a[1] & b[1])
    examples.append(dict(dimension=dim, support=observed_sizes[0],
                         neighborhood=observed_sizes[1], filled=observed_sizes[2],
                         omitted_filled_sites=1, realized_nested_supports=len(family),
                         shared_exterior_neighborhood_sites=len(shared)))

# The collar's correctness really needs a full incorrect component.
origin = (0, 0)
star_component = g.enlarge({origin})
assert star_component-{origin}  # all these neighbors are also incorrect
assert g.labeled({origin: 2})[0][0] == star_component

# The boundary-connectivity assertion requires dimension at least two.
g1 = Grid(1, -2, 2)
boundary1 = g1.enlarge({(0,)})-{(0,)}
assert len(g1.components(boundary1)) == 2

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1024**3
data = dict(counts=counts, examples=examples, connected_supports_3x3=len(catalog),
            effective_nice=os.getpriority(os.PRIO_PROCESS, 0), peak_rss_bytes=rss,
            elapsed_seconds=time.monotonic()-start)
Path('geometry_checks.json').write_text(json.dumps(data, indent=2)+'\n')
print(json.dumps(data, indent=2))
print('All geometry checks passed; unrestricted perforated-domain claim fails as expected.')
