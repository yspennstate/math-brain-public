"""Final consistency audit of the theorem, report and exact computation records."""
from decimal import Decimal, localcontext
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(60)
START = time.monotonic()
HERE = Path(__file__).resolve().parent
proof = (HERE/'PROOF.md').read_text()
report = (HERE/'REPORT.md').read_text()
assert report.startswith('VERDICT: PARTIAL ')
saved = {}
for name in ('recheck', 'extension', 'audit', 'adversarial'):
    x = json.loads((HERE/(name+'.json')).read_text())
    assert x['status'] == 'PASS'
    usage = x['usage']
    assert usage['threads'] == 1 and usage['nice'] >= 15
    assert usage['seconds'] < usage['deadline'] <= 1200
    assert usage['peak_rss_bytes'] < 1024**3
    saved[name] = x
assert saved['recheck']['earlier_path_comparisons'] == 202
assert len(saved['recheck']['enlarged_full_graph_checks']) == 8
assert saved['adversarial']['oriented_lattice_checks'] == 132
assert [(x['candidates'], x['trees'], x['groups'])
        for x in saved['adversarial']['tree_checks']] == [(792, 128, 64), (497420, 12288, 1296)]

for row, audit in zip(saved['extension']['rows'], saved['audit']['rows']):
    d = row['d']
    assert d == audit['d']
    assert row['square_probability'] == audit['probability']
    total = sum((g['multiplicity']*F(g['probability']) for g in audit['groups']), F(0))
    assert total == F(row['square_probability'])
    assert sum(g['multiplicity'] for g in audit['groups']) == audit['tree_count']
    assert len(audit['groups']) == audit['integral_groups']
    m = 2*d-2
    assert audit['tree_count'] == (4*m+8)*8**(m-1)
    assert m*(total-F(row['previous_square'])) == F(row['gain'])
    assert F(row['previous_bound'])+F(row['gain']) == F(row['bound'])
    assert F(1, d) < F(row['previous_bound']) < F(row['bound']) < 1
    assert F(0) < F(row['previous_square']) < total < F(1, 4)
    assert row['gain'] == audit['gain'] and row['bound'] == audit['bound']
    for key in ('square_probability', 'gain', 'bound'):
        for integer in row[key].split('/'):
            assert integer in proof and integer in report, (d, key, integer)
    with localcontext() as context:
        context.prec = 90
        bound = F(row['bound'])
        decimal = str(Decimal(bound.numerator)/Decimal(bound.denominator))
        assert decimal[:23] in proof and decimal[:23] in report
    shape = row['geometry']
    assert shape['root'] == 4*d
    assert len(shape['internal']) == 3*m+3
    assert shape['total_original_edges'] == 2*m*m+5*m+5

row3 = saved['extension']['rows'][1]
assert F(row3['square_probability']) == F(106821527499174906671287753163603,
                                         8994156750072383564239397632800000)
assert F(row3['bound']) == F(265115546365736108233965694737821273,
                            674561756255428767317954822460000000)
required = ['LOG.md', 'PROOF.md', 'REPORT.md', 'recheck.py', 'both_ends.py',
            'audit.py', 'adversarial.py', 'final_check.py']
required += [name+ext for name in saved for ext in ('.json', '.txt')]
assert all((HERE/name).stat().st_size > 0 for name in required)
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != 'darwin':
    rss *= 1024
assert rss < 1024**3
print('PASS: 202 earlier path probabilities, 8 full-graph enlargement rechecks')
print('PASS: both new probabilities agree between full partitions and cycle integrals')
print('PASS: 12416 final trees, 1360 integral groups, all exhaustive multiplicities')
print('PASS: 132 oriented lattice/witness/counterexample checks, all sums and quoted values')
print('PASS: verdict, artifacts and resource records')
print(json.dumps(dict(seconds=time.monotonic()-START, peak_rss_bytes=rss,
                      nice=os.getpriority(os.PRIO_PROCESS, 0), threads=1, deadline=60)))
