#!/usr/bin/env python3
"""Exact checks for the Bernoulli-sleeper comparison in PROOF.md.

Run: OMP_NUM_THREADS=1 nice -n 15 python3 certificate.py
Only the standard library is used; no numerical eigenvalue calculation.
"""
import itertools
import json
import os
import resource
import signal
from fractions import Fraction as Q
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
try:
    resource.setrlimit(resource.RLIMIT_DATA, (512 * 1024**2, 512 * 1024**2))
except (OSError, ValueError) as exc:
    print(f'OS data-limit guard unavailable: {exc}; peak RSS checked below.')
signal.alarm(30)
TYPES = ('F', 'D', 'B')


def formula(d, q, t):
    s = d + 1
    return [
        [d*(1-q)/s/t, d*q/s/t, t/s],
        [d*(2*d*(1-q)+q)/s**2/t,
         d*(2*d*q+1)/s**2/t + t/s**2, 2*d*t/s**2],
        [(d-(d-1)*q)/s/t, (d-1)*q/s/t, t/s],
    ]


def enumerate_row(d, q, t, kind, height_one=False, c=None, v=None):
    """Enumerate ordered walker directions and sleepers at distinct targets.

    Direction -1 is the parent; 0,...,d-1 are distinct children.
    For B, child 0 is already empty. All backward targets are empty.
    This routine does not use the closed-form matrix entries.
    """
    row = [Q(0), Q(0), Q(0)]
    root_weight = Q(0)
    mass = Q(0)
    n = 2 if kind == 'D' else 1
    for choices in itertools.product(range(-1, d), repeat=n):
        targets = sorted(set(x for x in choices if x >= 0))
        fresh = [x for x in targets if not (kind == 'B' and x == 0)]
        for bits in itertools.product((0, 1), repeat=len(fresh)):
            prob = Q(1, (d+1)**n)
            marks = dict(zip(fresh, bits))
            for bit in bits:
                prob *= q if bit else 1-q
            mass += prob
            back = choices.count(-1)
            if back:
                if height_one:
                    root_weight += prob * t * back * c
                else:
                    row[TYPES.index('D' if back == 2 else 'B')] += prob*t
            for x in targets:
                count = choices.count(x) + marks.get(x, 0)
                if count >= 2:
                    row[1] += prob/t
                    count -= 2
                row[0] += prob/t*count
    assert mass == 1
    if height_one:
        return sum(a*b for a, b in zip(row, v)) + root_weight
    return row


def show(x):
    return str(x)


def certify(d, q, t, v):
    c = v[2]
    matrix = formula(d, q, t)
    for test_q in (Q(0), q, Q(1)):
        assert formula(d, test_q, t) == [
            enumerate_row(d, test_q, t, k) for k in TYPES]
    mv = [sum(a*b for a, b in zip(row, v)) for row in matrix]
    margins = [a-b for a, b in zip(v, mv)]
    root_out = ((1-q)*v[0] + q*v[1])/t
    # Independent root enumeration: choose each of d actual root children.
    root_enum = sum((Q(1, d)/t*((1-q)*v[0]+q*v[1])
                     for _ in range(d)), Q(0))
    assert root_enum == root_out
    assert min(v) > 0 and t > 1
    assert min(margins) > 0
    assert c > root_out and v[1] >= 2*c
    # The actual root boundary cannot cost more than the interior bound.
    boundary = [enumerate_row(d, q, t, k, True, c, v) for k in TYPES]
    assert all(x <= y for x, y in zip(boundary, mv))
    rho = max([x/y for x, y in zip(mv, v)] + [root_out/c])
    assert rho < 1
    baseline = Q((d-1)**2, 4*d)
    assert q > baseline
    # These very certificates do not certify the original q=1 problem.
    full_mv = [sum(a*b for a, b in zip(row, v))
               for row in formula(d, Q(1), t)]
    full_margins = [a-b for a, b in zip(v, full_mv)]
    assert min(full_margins) < 0
    out = {
        'd': d, 'q': show(q), 't': show(t),
        'v_F_D_B': list(map(show, v)), 'c': show(c),
        'matrix': [list(map(show, row)) for row in matrix],
        'Mv': list(map(show, mv)), 'v_minus_Mv': list(map(show, margins)),
        'root_out': show(root_out), 'root_margin': show(c-root_out),
        'pair_boundary_margin': show(v[1]-2*c),
        'height_one_weighted_rows': list(map(show, boundary)),
        'rho': show(rho), 'one_initial_frog_expected_visits_bound': show(1/(1-rho)),
        'elementary_q_threshold': show(baseline), 'improvement': show(q-baseline),
        'q_one_v_minus_Mv': list(map(show, full_margins)),
    }
    print(f'd={d} q={q} t={t} v={tuple(map(str,v))}')
    print('  v-Mv =', ', '.join(map(str, margins)))
    print(f'  root margin={c-root_out}; pair margin={v[1]-2*c}')
    print(f'  rho={rho}; E[visits including time 0]<={1/(1-rho)}')
    print(f'  elementary threshold={baseline}; improvement={q-baseline}')
    print('  q=1 margins =', ', '.join(map(str, full_margins)))
    return out


if __name__ == '__main__':
    results = [
        certify(3, Q(41,100), Q(41,20), [Q(203,200),Q(2),Q(483,500)]),
        certify(4, Q(33,50), Q(51,20), [Q(1017,1000),Q(2),Q(483,500)]),
    ]
    Path(__file__).with_name('certificate_data.json').write_text(
        json.dumps({'certificates': results}, indent=2)+'\n')
    peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS reports bytes (Linux reports KiB).
    import sys
    peak_bytes = peak_rss if sys.platform == 'darwin' else peak_rss*1024
    assert peak_bytes < 1024**3
    print(f'  peak RSS bytes={peak_bytes}')
    print('PASS: formulas equal exhaustive one-step enumeration at q=0,q0,1;')
    print('      exact positive margins, root boundary, and q=1 failures checked.')
