"""Check the theorem's displayed values, geometry and saved audit records."""
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as Q
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
data = {}
for name in ('recheck', 'extension', 'audit'):
    saved = json.loads((HERE/(name+'.json')).read_text())
    assert saved['status'] == 'PASS'
    assert saved['usage']['threads'] == 1
    assert saved['usage']['nice'] >= 15
    assert saved['usage']['elapsed_seconds'] < 900
    assert saved['usage']['peak_rss_bytes'] < 1024**3
    data[name] = saved
assert [data['recheck'][s] for s in ('square_comparisons', 'six_vertex_comparisons',
                                   'eight_vertex_comparisons')] == [11, 33, 158]
assert len(data['extension']['rows']) == 11
assert sum(len(row['probabilities_by_k']) for row in data['extension']['rows']) == 143
assert len(data['audit']['generic_checks']) == 8
assert [(r['trees'], r['simplices']) for r in data['audit']['integral_checks']] == [
    (16, 11520), (80, 3225600)]

for row in data['extension']['rows']:
    d, m = row['d'], row['m']
    assert m == 2*d-2
    ps = list(map(Q, row['probabilities_by_k']))
    assert len(ps) == m+1
    assert all(x < y for x, y in zip(ps, ps[1:]))
    assert ps[0] == Q(row['old_square_probability'])
    assert ps[-1] == Q(row['enlarged_square_probability'])
    assert m*(ps[-1]-ps[0]) == Q(row['gain'])
    assert Q(row['previous_bound'])+Q(row['gain']) == Q(row['bound'])
    assert Q(1, d) < Q(row['previous_bound']) < Q(row['bound']) < 1
    # Independently rebuild induced edges by pair distances, not neighbor lookup.
    shape = row['geometry']
    vertices = shape['vertices']
    induced = [(i, j) for i in range(len(vertices)) for j in range(i+1, len(vertices))
               if sum(abs(a-b) for a, b in zip(vertices[i], vertices[j])) == 1]
    assert induced == [tuple(e) for e in shape['internal']]
    degrees = Counter(v for edge in induced for v in edge)
    assert [2*d-degrees[i] for i in range(len(vertices))] == shape['spokes']
    assert len(induced)+sum(shape['spokes']) == (m+1)*(m+4) == shape['total_edges']
    # Independent literal convolution of the branch survival polynomial.
    polynomial = {0: 1}
    branch = {1: 1, m+1: 1, m+2: -1}
    for _ in range(m):
        updated = Counter()
        for i, a in polynomial.items():
            for j, b in branch.items():
                updated[i+j] += a*b
        polynomial = {i: a for i, a in updated.items() if a}
    assert polynomial == {int(i): a for i, a in row['signed_coefficients'].items()}

row3 = data['extension']['rows'][1]
assert row3['d'] == 3
assert Q(row3['old_square_probability']) == Q(5521, 658350)
assert Q(row3['enlarged_square_probability']) == Q(7175020914436910477, 722017042450235532000)
assert Q(row3['gain']) == Q(1120101659682220157, 180504260612558883000)
assert Q(row3['previous_bound']) == Q(21272798694838039662654613, 56120415572268307260000000)
assert Q(row3['bound']) == Q(237831533319331629226140743, 617324571294951379860000000)
for key in ('enlarged_square_probability', 'gain', 'bound'):
    for integer in row3[key].split('/'):
        assert integer in proof and integer in report
for row in data['extension']['rows'][:3]:
    value = Q(row['bound'])
    with localcontext() as ctx:
        ctx.prec = 60
        decimal = str(Decimal(value.numerator)/Decimal(value.denominator))
    assert decimal[:23] in proof and decimal[:23] in report

required = ['LOG.md', 'PROOF.md', 'REPORT.md', 'recheck.py', 'enlarge.py',
            'audit.py', 'final_check.py', 'recheck.json', 'recheck.txt',
            'extension.json', 'extension.txt', 'audit.json', 'audit.txt']
assert all((HERE/name).stat().st_size > 0 for name in required)
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != 'darwin':
    rss *= 1024
assert rss < 1024**3
print('PASS: 202 earlier probabilities, 143 enlarged probabilities, 8 generic checks')
print('PASS: 96 full-graph tree shapes, 3237120 explicit simplex integrals, 11 integer sums')
print('PASS: every induced edge, spoke count, survival polynomial, quoted fraction and decimal')
print('PASS: verdict, required artifacts and resource records')
print(json.dumps(dict(elapsed_seconds=time.monotonic()-START, peak_rss_bytes=rss,
                      nice=os.getpriority(os.PRIO_PROCESS, 0), threads=1)))
