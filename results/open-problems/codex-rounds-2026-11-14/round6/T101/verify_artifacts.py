#!/usr/bin/env python3
"""Check written tables, constants and syntax against the exact calculation."""
import ast
from collections import Counter
from fractions import Fraction as Q
import json
import os
from pathlib import Path
import re
import resource
import signal

resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
signal.alarm(60)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
data = json.loads(Path('repeated_data.json').read_text())
audit = json.loads(Path('repeated_audit.json').read_text())
prior = json.loads(Path('recheck.json').read_text())
proof = Path('PROOF.md').read_text()
report = Path('REPORT.md').read_text()
assert report.splitlines()[0] == (
    'VERDICT: PARTIAL exact probability of repeated-vertex periodic orbits with at most eight turning visits')
for path in Path('.').glob('*.py'):
    ast.parse(path.read_text(), filename=str(path))
for path in (Path('PROOF.md'), Path('REPORT.md'), Path('LOG.md')):
    assert not any(ord(c) < 32 and c not in '\n\t' for c in path.read_text())

table = Counter()
root_table = {}
mode = None
for line in proof.splitlines():
    if line.startswith('| \\(k\\) |'):
        mode = 'class'
    if line.startswith('| Length |'):
        mode = 'root'
    if not line.startswith('|') or not re.fullmatch(r'[\d| ]+', line):
        continue
    values = tuple(map(int, re.findall(r'\d+', line)))
    if len(values) != 6:
        continue
    if mode == 'class':
        k, t, c, a, b, n = values
        table[k, t, c, a, b] = n
    elif mode == 'root':
        root_table[values[0]] = values[1:]
expected = Counter()
for f in data['families']:
    for g in f['groups']:
        expected[f['k'], f['t'], f['c'], g['ones'], g['twos']] = g['count']
assert table == expected and sum(table.values()) == 62
assert len(root_table) == 5
for length, values in root_table.items():
    assert tuple(f['root_counts'][str(length)] for f in data['families']) == values
part = proof.split('They give')[1].split('The repeated-mirror family')[0]
terms = re.findall(r'\\frac\{(\d+)\\cdot(\d+)\}\{2\^\{(\d+)\}\}', part)
assert len(terms) == 7
assert sum(Q(int(n)*int(j), 2**int(d)) for n, j, d in terms) == Q(37, 4096)
assert audit['rank_count'] == len(data['shapes']) == 62
assert audit['bounded_walk_nodes'] == 21590
assert audit['new_linear_coefficient'] == '37/4096'
assert audit['combined_linear_coefficient'] == '669595/16777216'
assert audit['combined_half_density'] == '1969564021/56687040000'
assert audit['endpoint_combined'] == '387/2048'
assert prior['linear_coefficient'] == '20635/16777216'
assert len(audit['checks']) == 25
assert all(Q(row['tail_bound_exact']) < Q(1, 10**30) for row in audit['checks'])
for row in (audit, data, prior):
    assert row['priority'] >= 15
    assert row['full_peak_rss_bytes'] < 1_000_000_000
assert audit['environment_audit']['environments'] == 19683
assert audit['environment_audit']['successes'] == 36
for value in ('37/4096', '669595/16777216', '164/18225',
              '1969564021/56687040000', '387/2048'):
    assert value in report
print('PASS all 10 classification rows, five rooted rows, seven-term small-p sum,')
print('verdict, exact constants, 25 tail bounds, script syntax, document characters and resource limits.')
