#!/usr/bin/env python3
"""Second counting route and explicit edge cases, independent of the simulator."""
import itertools
import os
import resource
import sys
import time
from fractions import Fraction


def main():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15
    resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
    started = time.monotonic()
    trajectories = guarded = 0
    for n in range(1, 5):
        count = 0
        # Sum over schedules first, rather than graphs first. Each schedule
        # forces the union of its clique pairs to be present; every other edge
        # can be chosen independently.
        for masks in itertools.product(*(range(1 << t) for t in range(1, n + 1))):
            required = set()
            for mask in masks:
                vertices = [v for v in range(n) if mask & (1 << v)]
                required.update(itertools.combinations(vertices, 2))
            count += 2 ** (n * (n - 1) // 2 - len(required))
        print(f'n={n}: legal graph/trajectory pairs={count}, guarded={count * 2**n}')
        trajectories += count
        guarded += count * 2 ** n
    assert trajectories == 23112
    assert guarded == 367036
    adaptive_original = (2 + 8 + 64 + 32) * 4 * 2 * 2
    adaptive_guarded = 3 * 4 * 2 * 2 * (2 * 4 + 8 * 8 + 64 * 16 + 32 * 32)
    assert trajectories + adaptive_original == 24808
    assert guarded + adaptive_guarded == 468796
    print(f'Independent totals: original={trajectories + adaptive_original}, guarded={guarded + adaptive_guarded}')

    # Set-theoretic witnesses, using actual sets rather than bit masks.
    histories = [
        # Arbitrary deletion/readmission with no final disagreement.
        [{0}, {0, 1}, set(), {0, 1, 3}],
        # Simultaneously nonempty core, final late set, and deleted set.
        [set(), {1}, {1, 2}, {2, 3}, {0, 2, 4}],
        # Multiple old vertices admitted at the last update.
        [set(), set(), set(), {0, 1, 2, 3}],
    ]
    expected = [({0, 1, 3}, set(), set()),
                ({2, 4}, {1, 3}, {0}),
                ({3}, set(), {0, 1, 2})]
    for states, (wanted_core, wanted_d, wanted_r) in zip(histories, expected):
        on_time = {t for t, state in enumerate(states) if t in state}
        final = states[-1]
        core, deleted, late = final & on_time, on_time - final, final - on_time
        assert (core, deleted, late) == (wanted_core, wanted_d, wanted_r)
        assert len(core) == len(final) - len(late)
        print(f'Witness: core={sorted(core)}, D={sorted(deleted)}, R={sorted(late)}')

    eps = Fraction(1, 2)
    h = min((eps / 2) ** 2, 1)
    xi, a = h / 64, h / 128
    for x in (4096, 8192):
        r, s = int(a * x), int(eps * x / 2)
        assert (1 + eps) * x - s == (1 + eps / 2) * x
        # Exact rational part of the log probability exponent. For r=2,
        # M=1+n+n(n-1)/2 has log2 M=x*2-1+o(1).
        quadratic = -xi * (x - 1) ** 2
        assert quadratic == -(xi - a) * x*x + 2*xi*x - xi - r*x
        print(f'Exact exponent components x={x}: negative_quadratic={quadratic}, r*x={r*x}, leading_coefficient={xi-a}')
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
    assert rss_bytes < 1_000_000_000
    print(f'PASS; nice={priority}; elapsed={time.monotonic()-started:.3f}s; peak_RSS={rss_bytes} bytes')


if __name__ == '__main__':
    main()
