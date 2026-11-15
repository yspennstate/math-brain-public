#!/usr/bin/env python3
"""Read-only consistency audit of the saved mathematical deliverables."""
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource

resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    assert os.environ.get(name) == '1'
root = Path(__file__).resolve().parent
required = ('REPORT.md', 'PROOF.md', 'LOG.md', 'verify.py', 'VERIFY_OUTPUT.txt',
            'verification.json', 'prior_recheck/verify.py',
            'prior_recheck/verification.json', 'prior_recheck/VERIFY_OUTPUT.txt')
for name in required:
    assert (root/name).stat().st_size > 0, name
old_source = Path('~/codex_op_1114r4/briefs/T080/verify.py')
assert old_source.read_bytes() == (root/'prior_recheck/verify.py').read_bytes()
report, proof, log = ((root/name).read_text() for name in ('REPORT.md', 'PROOF.md', 'LOG.md'))
assert report.splitlines()[0] == 'VERDICT: PARTIAL robust triangular interfaces evade the earlier underoccupation detector'
for name in ('VERIFY_OUTPUT.txt', 'prior_recheck/VERIFY_OUTPUT.txt'):
    assert (root/name).read_text().strip() in log, name
data = json.loads((root/'verification.json').read_text())
prior = json.loads((root/'prior_recheck/verification.json').read_text())
for record in (data, prior):
    assert record['status'] == 'PASS'
    assert record['elapsed_seconds'] < 1200 and record['peak_rss_mib'] < 128
    assert record['nice_priority'] >= 15
assert data['exact_count_cases'] == 560 and data['split_width_cases'] == 35
assert data['sample_minimum_safe_sites'] == 8
assert F(data['rational_lower']) == F(3317635, 1591356) > 2
assert F(data['excess_over_two']) == F(134923, 1591356)
a, b = map(F, data['exact_bound_Qsqrt3'])
assert b > 0 and 2-a > 0 and 3*b*b > (2-a)**2
assert prior['exact_graph_cases'] == 3072
assert '[+' not in proof
assert proof.count('\\[') == proof.count('\\]')
for text in (report, proof):
    assert 'Gibbs' in text and 'phase' in text
assert 'T080 remains open' in report
assert not (root/'SOLVED_ELSEWHERE.md').exists()
print('PASS: unchanged previous source; complete logged outputs; exact count constants; sampled/global distinction; resource records; report and proof scope agree.')
