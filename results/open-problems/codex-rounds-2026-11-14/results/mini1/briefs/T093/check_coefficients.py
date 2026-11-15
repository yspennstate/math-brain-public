#!/usr/bin/env python3
"""Exact integer audits of symmetry factors, overlaps, and K4 corrections."""
import itertools as it
import json
import math
import os
from pathlib import Path
import resource
import time

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (1140, resource.getrlimit(resource.RLIMIT_CPU)[1]))
start = time.monotonic()


def edges(vertices):
    return set(it.combinations(sorted(vertices), 2))


def audit_overlaps(A, B):
    a, b = A['n'], B['n']
    ea = set(map(tuple, A['edges']))
    minimum = 100
    cases = 0
    for t in range(min(a,b)+1):
        for common in it.combinations(range(b), t):
            for images in it.permutations(range(a), t):
                mapping = dict(zip(common, images))
                fresh = a
                for v in range(b):
                    if v not in mapping:
                        mapping[v] = fresh
                        fresh += 1
                eb = {tuple(sorted((mapping[u],mapping[v]))) for u,v in B['edges']}
                if a==b and ea==eb:
                    continue  # the same copy, not a factorial-moment pair
                union_excess = len(ea|eb) - (a+b-t)
                minimum = min(minimum, union_excess)
                assert union_excess >= 5
                cases += 1
                if time.monotonic()-start > 1100:
                    raise TimeoutError
    return dict(vertices=[a,b], cases=cases, minimum_union_excess=minimum)


data = json.load(open('obstructions.json'))
audits = [audit_overlaps(A,B) for i,A in enumerate(data['representatives'])
          for B in data['representatives'][i:]]
k4 = dict(n=4, edges=[list(e) for e in edges(range(4))])
audits += [audit_overlaps(k4,A) for A in data['representatives']]
for row in audits:
    print('overlap', json.dumps(row))

for n in range(4,11):
    cliques = list(map(frozenset,it.combinations(range(n),4)))
    actual = [0]*4
    for A,B in it.combinations(cliques,2):
        actual[len(A&B)] += 1
    expected = [math.comb(n,4)*math.comb(4,r)*math.comb(n-4,4-r)//2
                if n-4 >= 4-r else 0 for r in range(4)]
    assert actual == expected
print('PASS: K4 pair counts by direct enumeration for n=4,...,10')

triple_cases = 0
min_triple = 100
for r in range(4):
    A = set(range(4))
    B = set(range(r)) | set(range(4,8-r))
    U = A|B
    for t in range(5):
        for common in it.combinations(sorted(U),t):
            C = set(common) | set(range(len(U),len(U)+4-t))
            if C==A or C==B:
                continue
            excess = len(edges(A)|edges(B)|edges(C))-len(U|C)
            min_triple = min(min_triple, excess)
            assert excess >= 5
            triple_cases += 1
print('PASS: all K4 triple intersection types, minimum excess', min_triple)

poly = [1]
for j in range(4):
    result = [0]*(len(poly)+1)
    for i,v in enumerate(poly):
        result[i] += v
        result[i+1] -= j*v
    poly = result
assert poly == [1,-6,11,-6,0]
assert sum(it.starmap(lambda a,b:a*b,it.combinations(range(4),2))) == 11
print('PASS: falling-factorial coefficients', poly)

output = dict(overlap_audits=audits, k4_triple_cases=triple_cases,
              k4_triple_minimum_excess=min_triple,
              falling_factorial_coefficients=poly,
              failure_coefficients={
                  'n^-2': 'c^6/24', 'n^-3': '-c^6/4',
                  'n^-4': '11*c^6/24-c^9/12+c^10/10+c^11/8-c^12/1152'},
              k4free_failure_coefficient='c^10/10+c^11/8',
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              seconds=round(time.monotonic()-start,3))
assert output['peak_rss_bytes'] < 768*1024**2
Path('coefficient_checks.json').write_text(json.dumps(output,indent=2)+'\n')
print('PASS: coefficient and overlap checks')
print('seconds',output['seconds'])
print('peak_rss_bytes',output['peak_rss_bytes'])
