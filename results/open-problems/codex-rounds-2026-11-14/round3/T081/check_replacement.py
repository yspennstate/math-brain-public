"""Exact finite-state tests of conditional contour replacement; standard library."""
import itertools
import json
import math
import os
import random
import resource
import signal
import time
from fractions import Fraction as Q
from pathlib import Path

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('90s limit')))
signal.alarm(90)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
started = time.monotonic()


class Model:
    def __init__(self, n, seed=0, stagger=False, example=False):
        self.n = n
        self.parent = [None] + [(i-1)//2 for i in range(1, n)]
        self.children = [[j for j in range(n) if self.parent[j] == i] for i in range(n)]
        rng = random.Random(seed)
        self.a, self.b = {}, {}
        for v, c, s, ext in itertools.product(range(n), range(2), range(2), range(2)):
            key = v, c, s, ext
            if example:
                self.a[key] = Q(1)
                self.b[key] = Q(1 if v == 0 else
                                1+2*((1-ext) if stagger and v == 2 else ext))
            else:
                self.a[key] = Q(rng.randrange(1, 6), rng.randrange(1, 5))
                self.b[key] = Q(rng.randrange(1, 6), rng.randrange(1, 5))
        self.z, self.w = {}, {}
        for v in reversed(range(n)):
            for c, ext in itertools.product(range(2), repeat=2):
                den = sum(self.a[v,c,s,ext] * math.prod(self.z[u,c,s] for u in self.children[v])
                          for s in range(2))
                num = sum(self.b[v,c,s,ext] * math.prod(self.z[u,1-c,s] for u in self.children[v])
                          for s in range(2))
                self.z[v,c,ext] = den+num
                self.w[v,c,ext] = num/den

    def physical_enumeration(self, phase, exterior):
        total = Q(0)
        # Each digit specifies the physical support type and microscopic state.
        for digits in itertools.product(range(4), repeat=self.n):
            phases, states, weight = [], [], Q(1)
            for v, digit in enumerate(digits):
                defect, state = divmod(digit, 2)
                p = self.parent[v]
                c = phase if p is None else phases[p] ^ (digits[p]//2)
                ext = exterior if p is None else states[p]
                phases.append(c)
                states.append(state)
                weight *= (self.b if defect else self.a)[v,c,state,ext]
            total += weight
        return total

    def auxiliary_enumeration(self, phase, exterior, explicit_families=False):
        total = Q(0)
        baseline_total = Q(0)
        moments = [Q(0)]*self.n
        for states in itertools.product(range(2), repeat=self.n):
            baseline, activities = Q(1), []
            for v, state in enumerate(states):
                p = self.parent[v]
                ext = exterior if p is None else states[p]
                baseline *= self.a[v,phase,state,ext]
                activities.append(self.w[v,phase,ext])
            family_sum = math.prod(1+w for w in activities)
            if explicit_families:
                subset_sum = sum(math.prod(activities[v] for v in range(self.n) if mask >> v & 1)
                                 for mask in range(1 << self.n))
                assert subset_sum == family_sum
            total += baseline*family_sum
            baseline_total += baseline
            for v, w in enumerate(activities):
                moments[v] += baseline*w
        independently_averaged = baseline_total*math.prod(1+x/baseline_total for x in moments)
        return total, independently_averaged


results = []
for n, seeds in ((1, range(3)), (3, range(6)), (7, range(2))):
    for seed in seeds:
        model = Model(n, seed)
        for c, ext in itertools.product(range(2), repeat=2):
            physical = model.physical_enumeration(c, ext)
            auxiliary, wrong = model.auxiliary_enumeration(c, ext,
                                                        explicit_families=(seed == 0 and c == ext == 0))
            recursive = model.z[0,c,ext]
            assert physical == recursive == auxiliary
            results.append({'nodes': n, 'seed': seed, 'phase': c, 'exterior': ext,
                            'partition_function': str(physical),
                            'independent_average_matches': wrong == physical})

examples = []
for stagger in (False, True):
    model = Model(3, example=True, stagger=stagger)
    physical = model.physical_enumeration(0, 0)
    auxiliary, wrong = model.auxiliary_enumeration(0, 0, explicit_families=True)
    assert physical == auxiliary == (128 if stagger else 160)
    assert wrong == 144
    # A second derivation conditions only on the root microscopic state.
    leaf_z = [(4, 8), (8, 4) if stagger else (4, 8)]
    direct = 2*sum(leaf_z[0][s]*leaf_z[1][s] for s in range(2))
    assert direct == physical
    # Root activity is 1; baseline mass 8; leaf covariance is +/-1.
    covariance_gap = 8*2*(-1 if stagger else 1)
    assert physical-wrong == covariance_gap
    # Deliberately wrong denominator: use pure child backgrounds instead of
    # their physical diluted ensembles. For the aligned example it is 8, not 80.
    if not stagger:
        den = model.z[0,0,0]/2
        assert den == 80
        pure_den = Q(8)
        bad_root_weight = den/pure_den
        bad_denominator_partition = (1+bad_root_weight)*den
        no_nested_family_partition = den+pure_den
        assert bad_denominator_partition == 880 != physical
        assert no_nested_family_partition == 88 != physical
    examples.append({'staggered': stagger, 'physical': str(physical),
                     'conditional_replacement': str(auxiliary),
                     'independent_activity_average': str(wrong),
                     'gap': str(physical-wrong)})


def cube(radius, dim):
    return set(itertools.product(range(-radius, radius+1), repeat=dim))


def enlarge(points, dim):
    return {tuple(a+b for a, b in zip(p, delta)) for p in points
            for delta in itertools.product((-1, 0, 1), repeat=dim)}


geometry = []
for dim in (2, 3):
    for k in (1, 3):
        dense = cube(k, dim)
        universe = cube(k+3, dim)
        offsets = list(itertools.product((-1, 0, 1), repeat=dim))
        support = set()
        for p in universe:
            phases = {tuple(a+b for a, b in zip(p, delta)) in dense for delta in offsets}
            if len(phases) > 1:
                support.add(p)
        expected = cube(k+1, dim)-cube(k-1, dim)
        assert support == expected
        assert len(support) == (2*k+3)**dim-(2*k-1)**dim
        # Flood-fill complement from a corner to identify the bounded component.
        outside = universe-support
        todo = [tuple([k+3]*dim)]
        reached = set(todo)
        while todo:
            p = todo.pop()
            for delta in offsets:
                q = tuple(a+b for a, b in zip(p, delta))
                if q in outside and q not in reached:
                    reached.add(q)
                    todo.append(q)
        interior = outside-reached
        assert interior == cube(k-1, dim)
        if k == 3:
            inner_support = cube(1, dim)
            assert enlarge(inner_support, dim) == interior
            assert not (enlarge(inner_support, dim) & support)
        geometry.append({'dimension': dim, 'dense_block_radius': k,
                         'support_cells': len(support), 'interior_cells': len(interior)})

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 512*1024**2
data = {'exact_partition_comparisons': results, 'shared_boundary_examples': examples,
        'geometry_checks': geometry, 'peak_rss_bytes': rss,
        'elapsed_seconds': time.monotonic()-started}
Path('replacement_checks.json').write_text(json.dumps(data, indent=2)+'\n')
print('Exact recursion / physical enumeration / auxiliary integration comparisons:', len(results))
print('Tree sizes: 1,3,7; both phases; both microscopic exteriors.')
print('Explicit compatible-family subset enumeration agrees with product expansion.')
print('Shared-boundary example: exact 160; independent activity averaging 144; gap +16.')
print('Opposite-boundary example: exact 128; independent activity averaging 144; gap -16.')
print('Both example numbers independently re-derived from two conditional states.')
print('Adversarial tests: pure-interior denominator gives 880; forbidding nesting gives 88; correct is 160.')
print('Dense-block contour geometry:', geometry)
print('Effective nice:', os.getpriority(os.PRIO_PROCESS, 0))
print('Peak RSS bytes:', rss)
print('Elapsed seconds:', format(data['elapsed_seconds'], '.3f'))
print('All checks passed.')
