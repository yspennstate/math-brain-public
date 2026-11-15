"""Independent midpoint-grid integration of the earlier four-particle witness."""
import itertools
import os
import resource
import signal
from collections import Counter
from fractions import Fraction as F

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
signal.alarm(30)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15


def histogram(points, m=8):
    d = len(points[0])
    counts = Counter()
    for k in itertools.product(range(m), repeat=d):
        shifts = [F(2*t+1, 2*m) for t in k]
        labels = [tuple((x-t).__floor__() for x, t in zip(p, shifts)) for p in points]
        edges = sum(sum(abs(x-y) for x, y in zip(a, b)) <= 1
                    for a, b in itertools.combinations(labels, 2))
        counts[edges] += 1
    return {e: F(c, m**d) for e, c in counts.items()}


checks = 0
for d in (2, 3):
    a = [(F(0),)*d, (F(3, 2),)+(F(0),)*(d-1)]
    assert histogram(a) == {0: F(1, 2), 1: F(1, 2)}
    for distance in (3, 9, 101):
        for offset in (F(0), F(1, 2)):
            b = [tuple(x+(offset if i == 0 else distance if i == 1 else 0)
                       for i, x in enumerate(p)) for p in a]
            joint = histogram(a+b)
            expected = {0: F(1, 2), 2: F(1, 2)} if offset == 0 else {1: F(1)}
            assert joint == expected
            for q in (2, 3, 5, 7):
                excess = sum(p*q**e for e, p in joint.items()) - F(1+q, 2)**2
                assert excess == (1 if offset == 0 else -1)*F((q-1)**2, 4)
                checks += 1
for n in range(1, 13):
    points = [(x, F(3*k)) for k in range(n) for x in (F(0), F(3, 2))]
    assert histogram(points) == {0: F(1, 2), n: F(1, 2)}
print('Independent uniform midpoint-grid integration; all cuts lie on grid edges.')
print('Exact four-particle excess checks:', checks)
print('Dimensions 2,3; separations 3,9,101; q=2,3,5,7; aligned and staggered.')
print('Exact distant-pair histograms n=1,...,12: passed')
print('Earlier main claim holds: excess = +/- (q-1)^2/4; aligned energy gap/particle -> -j/4.')
print('Effective nice:', os.getpriority(os.PRIO_PROCESS, 0))
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 512*1024**2
print('Peak RSS bytes:', rss)
