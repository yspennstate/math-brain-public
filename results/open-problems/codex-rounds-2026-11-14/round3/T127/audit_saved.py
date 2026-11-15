#!/usr/bin/env python3
"""Independent scalar audit of saved certificates and the actual root.

Enumerates marks on ALL children before walks, including untouched children.
Does not import either comparison script or construct its mean matrix.
"""
import json
import os
import resource
import signal
import sys
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
signal.alarm(60)
proof = Path('PROOF.md').read_text()
names = ('F','D','B','E')


def scalar_outputs(d,q,t,v,c,kind,height_one=False):
    n = 1 if kind in ('F','B') else 2
    known = kind in ('B','E')
    total = Q(0)
    mass = Q(0)
    for marks in product((0,1),repeat=d):
        mark_prob = q**sum(marks)*(1-q)**(d-sum(marks))
        for steps in product(range(d+1),repeat=n):
            p = mark_prob/Q((d+1)**n)
            mass += p
            value = Q(0)
            back = sum(x == 0 for x in steps)
            if back:
                value += t*(back*c if height_one else v[2 if back == 1 else 3])
            for child in range(1,d+1):
                count = sum(x == child for x in steps)
                if count:
                    count += 0 if known and child == 1 else marks[child-1]
                    # Explicit capacities: 1 -> F, 2 -> D, 3 -> D+F.
                    value += [Q(0),v[0],v[1],v[0]+v[1]][count]/t
            total += p*value
    assert mass == 1
    return total


for record in json.loads(Path('four_type_data.json').read_text()):
    d = record['d']
    q,t,c = (Q(record[k]) for k in ('q','t','c'))
    v = list(map(Q,record['v']))
    out = [scalar_outputs(d,q,t,v,c,k) for k in names]
    slack = [a-b for a,b in zip(v,out)]
    assert slack == list(map(Q,record['slack']))
    boundary = [scalar_outputs(d,q,t,v,c,k,True) for k in names]
    assert boundary == list(map(Q,record['height_one_weights']))
    assert all(a <= b for a,b in zip(boundary,out))
    root_out = Q(0)
    for child in range(d):
        for mark in (0,1):
            root_out += Q(1,d)*(q if mark else 1-q)*v[mark]/t
    assert c-root_out == Q(record['root_margin'])
    normalized = [(a-b)/a for a,b in zip(v,out)] + [(c-root_out)/c]
    epsilon = min(normalized)
    assert epsilon > 0
    assert Q(record['rho']) == 1-epsilon
    bound = Q(record['expected_visits_bound'])
    assert epsilon*bound == 1
    assert 1 <= bound < 100000
    q_one = [a-scalar_outputs(d,Q(1),t,v,c,k) for a,k in zip(v,names)]
    assert q_one == list(map(Q,record['q_one_slack'])) and max(q_one) < 0
    # Check transcription of all load-bearing fractions into the proof.
    for x in [q,t,c,*v,*slack,c-root_out,Q(record['rho']),bound]:
        assert str(x) in proof, str(x)
    worst = names[normalized.index(epsilon)]
    print(f'd={d}: complete child-mark enumeration recovered every slack and boundary.')
    print(f'  worst_row={worst}; epsilon={epsilon}; bound*epsilon={bound*epsilon}')
    print(f'  q=1 failed in all four rows; proof fractions match saved data.')

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss*1024
assert rss_bytes < 1024**3
print('peak_RSS_bytes =',rss_bytes)
print('PASS: saved-data scalar audit.')
