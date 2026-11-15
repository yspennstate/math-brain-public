"""Audit aggregate arithmetic and saved extrema; write a portable data manifest."""
import csv
import hashlib
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

summaries = list(csv.DictReader(Path('summary.csv').open()))
totals = {key: sum(int(row[key]) for row in summaries)
          for key in ('presentations', 'cyclic', 'chains', 'nonchains', 'width3', 'width3_indecomp')}
assert totals['presentations'] == sum(m**6 for m in range(1, 9))
assert totals['cyclic'] == sum((m*(m+1)//2)**3 for m in range(1, 9))
assert totals['chains'] == sum(3*(m-1) for m in range(1, 9))
assert totals['nonchains'] == totals['presentations']-totals['cyclic']-totals['chains'] == 364392

counts, equalities, widths = Counter(), Counter(), Counter()
minima = defaultdict(lambda: Fraction(1))
keys = 'mabcdef'
for row in csv.DictReader(Path('certificates.csv').open()):
    m, E, L = (int(row[key]) for key in ('m', 'extensions', 'x_before_y'))
    balance = Fraction(min(L, E-L), E)
    assert balance >= Fraction(1, 3)
    counts[m] += 1
    minima[m, 'min_all'] = min(minima[m, 'min_all'], balance)
    if balance == Fraction(1, 3):
        equalities[m] += 1
        assert row['width'] == '2' and row['indecomposable'] == '0'
    if row['width'] == '3':
        widths[m] += 1
        minima[m, 'min_width3'] = min(minima[m, 'min_width3'], balance)
        if row['indecomposable'] == '1':
            minima[m, 'min_width3_indecomp'] = min(minima[m, 'min_width3_indecomp'], balance)
for row in summaries:
    m = int(row['m'])
    assert counts[m] == int(row['nonchains'])
    assert widths[m] == int(row['width3'])
    if m > 1:
        for key in ('min_all', 'min_width3', 'min_width3_indecomp'):
            assert minima[m, key] == Fraction(row[key])

extrema = defaultdict(list)
for row in csv.DictReader(Path('extrema_pairs.csv').open()):
    key = tuple(int(row[k]) for k in keys)
    extrema[key].append(row)
for key, rows in extrema.items():
    n = 3*key[0]
    assert len(rows) == n*(n-1)//2
    assert {(int(r['x']), int(r['y'])) for r in rows} == {(x, y) for x in range(n) for y in range(x+1, n)}
    assert len({r['extensions'] for r in rows}) == 1
    assert max(Fraction(min(int(r['x_before_y']), int(r['extensions'])-int(r['x_before_y'])), int(r['extensions'])) for r in rows) >= Fraction(1, 3)

# Derive the largest unconstrained count without the factorial formula.
q = 9
paths = [[[0]*q for _ in range(q)] for _ in range(q)]
paths[0][0][0] = 1
for i in range(q):
    for j in range(q):
        for k in range(q):
            if i+j+k:
                paths[i][j][k] = ((paths[i-1][j][k] if i else 0)
                                  +(paths[i][j-1][k] if j else 0)
                                  +(paths[i][j][k-1] if k else 0))
assert paths[8][8][8] == math.factorial(24)//math.factorial(8)**3 == 9465511770

files = ('census.cpp', 'verify.cpp', 'run_limited.py', 'brute_small.py', 'audit_data.py',
         'certificates.csv', 'summary.csv', 'extrema_pairs.csv', 'census.out', 'verify.out', 'brute_small.out')
manifest = {
    'family': 'three chains of equal length m; A_a<B_b, B_c<C_d, C_e<A_f',
    'chain_lengths': list(range(1, 9)),
    'counts_are': 'parameter presentations, not isomorphism classes',
    'totals': totals,
    'equality_counts': dict(sorted(equalities.items())),
    'global_width_three_minimum': str(min(minima[m, 'min_width3'] for m in range(2, 9))),
    'files': {name: {'bytes': Path(name).stat().st_size,
                     'sha256': hashlib.sha256(Path(name).read_bytes()).hexdigest()}
              for name in files},
}
Path('manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
print('TOTALS', json.dumps(totals, sort_keys=True))
print('EQUALITY_COUNTS', json.dumps(dict(sorted(equalities.items())), sort_keys=True))
print('UNCONSTRAINED_COUNT_BY_DP_AND_FACTORIAL', paths[8][8][8])
print('EXTREMAL_PRESENTATIONS', len(extrema))
print('EXTREMAL_PAIR_COUNTS', sum(map(len, extrema.values())))
print('GLOBAL_WIDTH_THREE_MINIMUM', manifest['global_width_three_minimum'])
print('WROTE manifest.json')
