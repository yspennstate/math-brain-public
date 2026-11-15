"""Independent exact enumeration of the round 3 conditional identity."""
import itertools
import json
import os
import resource
import signal
import time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
signal.alarm(60)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
start = time.monotonic()
results = []
for parents in ((-1,), (-1, 0, 0), (-1, 0, 0, 2)):
    n = len(parents)
    children = [[u for u in range(n) if parents[u] == v] for v in range(n)]
    for seed in range(2):
        def weight(v, c, s, ext, defect):
            # All dependencies are kept; no previous checker is imported.
            return 1 + (11*v + 7*c + 3*s + 5*ext + seed +
                        defect*(2 + v*c + s*ext)) % 7

        def child_phase(c, u, defect):
            return (c + defect*(1 + u % 2)) % 3

        @lru_cache(None)
        def parts(v, c, ext):
            ans = []
            for defect in (0, 1):
                total = 0
                for s in range(3):
                    w = weight(v, c, s, ext, defect)
                    for u in children[v]:
                        w *= sum(parts(u, child_phase(c, u, defect), s))
                    total += w
                ans.append(total)
            return tuple(ans)

        for c, exterior in itertools.product(range(3), repeat=2):
            # Direct physical enumeration, with phases propagated in preorder.
            physical = 0
            for assignment in itertools.product(range(6), repeat=n):
                phases, states, defects = [], [], []
                w = 1
                for v, digit in enumerate(assignment):
                    defect, s = divmod(digit, 3)
                    p = parents[v]
                    phase = c if p == -1 else child_phase(phases[p], v, defects[p])
                    ext = exterior if p == -1 else states[p]
                    w *= weight(v, phase, s, ext, defect)
                    phases.append(phase)
                    states.append(s)
                    defects.append(defect)
                physical += w
            # Sum actual family subsets for every pure microscopic state.
            auxiliary = F(0)
            for states in itertools.product(range(3), repeat=n):
                background = 1
                activities = []
                for v, s in enumerate(states):
                    ext = exterior if parents[v] == -1 else states[parents[v]]
                    background *= weight(v, c, s, ext, 0)
                    den, num = parts(v, c, ext)
                    activities.append(F(num, den))
                families = F(0)
                for mask in range(1 << n):
                    product = F(1)
                    for v in range(n):
                        if mask & (1 << v):
                            product *= activities[v]
                    families += product
                auxiliary += background*families
            assert physical == auxiliary == sum(parts(0, c, exterior))
            results.append(dict(parents=parents, seed=seed, phase=c,
                                exterior=exterior, partition=str(physical)))

examples = []
for reverse in (False, True):
    # Condition on the root state, independently of the general enumeration.
    physical = sum(2*(2+2*(1+2*s))*(2+2*(1+2*((1-s) if reverse else s)))
                   for s in (0, 1))
    mean_activity = F(1+3, 2)
    independently_averaged = 8*2*(1+mean_activity)**2
    assert physical == (128 if reverse else 160)
    assert independently_averaged == 144
    examples.append(dict(reverse=reverse, physical=physical,
                         independent_average=int(independently_averaged)))

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1024**3
data = dict(comparisons=results, examples=examples, nice=os.getpriority(os.PRIO_PROCESS, 0),
            peak_rss_bytes=rss, elapsed_seconds=time.monotonic()-start)
Path('independent_recheck.json').write_text(json.dumps(data, indent=2)+'\n')
print('Independent physical/family/recursion comparisons:', len(results))
print('Three phases, three microscopic states, both binary and asymmetric trees.')
print('Hand examples:', examples)
print('Effective nice:', data['nice'])
print('Peak RSS bytes:', rss)
print('Elapsed seconds:', data['elapsed_seconds'])
print('Earlier conditional replacement result holds under its hypotheses.')
