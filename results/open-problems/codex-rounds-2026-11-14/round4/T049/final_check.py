#!/usr/bin/env python3
"""Check that the written theorem and report match the audited artifacts."""
from decimal import Decimal, localcontext
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource
import signal
import sys

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(60)
here = Path(__file__).resolve().parent
proof = (here/'PROOF.md').read_text()
report = (here/'REPORT.md').read_text()
assert report.startswith('VERDICT: PARTIAL ')

def read(name):
    data = json.loads((here/name).read_text())
    assert data['status'] == 'PASS', name
    assert data['usage']['nice'] >= 15
    assert data['usage']['OMP_NUM_THREADS'] == '1'
    assert data['usage']['peak_rss_bytes'] < 1024**3
    assert data['usage']['elapsed_seconds'] < 600
    return data

earlier = read('recheck.json')
geometry = read('graphs.json')
extension = read('extension.json')
audit = read('audit.json')
assert earlier['probability_comparisons'] == 44
assert len(earlier['rows']) == len(extension['rows']) == 11

baseline = {(i, i+1) for i in range(7)} | {(0, 7)}
for graph in geometry['graphs']:
    row = next(s for s in proof.splitlines() if s.startswith('| '+graph['id']+' |'))
    fields = [s.strip() for s in row.split('|')[1:-1]]
    chords = [] if fields[1] == 'empty' else [tuple(map(int, e))
                                            for e in fields[1].split(',')]
    assert baseline | set(chords) == set(map(tuple, graph['internal']))
    assert list(map(int, fields[2:])) == graph['support_counts']
assert geometry['support_totals'] == [28, 496, 1296]
print('PASS: all 15 proof-table chord sets and support triples')

active = sum(len(row['graphs']) for row in extension['rows'])
assert active == 158
assert audit['incompatible_pairs'] == 179700
assert sum(row['simplices'] for row in audit['integral_rows']) == 4838400
for row in extension['rows']:
    d = row['d']
    assert row['path_count'] == 4*(d-1)*(54*d*d-208*d+207)
    assert F(row['previous_bound'])+F(row['gain']) == F(row['bound'])
    assert F(1, d) < F(row['previous_bound']) < F(row['bound']) < 1
print('PASS: 158 probability comparisons, 4838400 simplex integrals, 11 sums')

row3 = next(row for row in extension['rows'] if row['d'] == 3)
D = 56120415572268307260000000
assert D % 922150845000 == 0
assert D // 922150845000 == 60858172908000
assert 347146143557*60858172908000+146118665900743508898613 == 21272798694838039662654613
assert F(row3['gain']) == F(146118665900743508898613, D)
assert F(row3['bound']) == F(21272798694838039662654613, D)
for number in ('60858172908000', '146118665900743508898613',
               '21272798694838039662654613', '56120415572268307260000000'):
    assert number in proof and number in report
assert '60858236760000' not in proof
with localcontext() as context:
    context.prec = 60
    for d in (2, 3, 4):
        row = next(r for r in extension['rows'] if r['d'] == d)
        value = F(row['bound'])
        decimal = str(Decimal(value.numerator)/Decimal(value.denominator))
        assert decimal[:17] in report
        assert decimal[:23] in proof
print('PASS: displayed d=3 integer identity and all quoted bound decimals')

required = ['LOG.md', 'PROOF.md', 'REPORT.md', 'seven.py', 'audit.py',
            'final_check.py', 'recheck.json', 'recheck.txt', 'graphs.json',
            'enumeration.txt', 'extension.json', 'extension.txt', 'audit.json',
            'audit.txt']
assert all((here/name).stat().st_size > 0 for name in required)
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != 'darwin':
    rss *= 1024
assert rss < 1024**3
print('PASS: verdict, required artifacts, resource records; final-check RSS bytes', rss)
