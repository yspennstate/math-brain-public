#!/usr/bin/env python3
"""Read-only consistency check of saved deliverables."""
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
required = ('REPORT.md', 'PROOF.md', 'LOG.md', 'verify.py', 'verification.json',
            'VERIFY_OUTPUT.txt', 'prior_recheck/verify.py',
            'prior_recheck/verification.json', 'prior_recheck/VERIFY_OUTPUT.txt')
for name in required:
    assert (root/name).stat().st_size > 0, name
old = Path('~/codex_op_1114r5/briefs/T080/verify.py')
assert old.read_bytes() == (root/'prior_recheck/verify.py').read_bytes()
# The inherited nested copies are identical to the scripts read in their source folders.
for later, earlier in (('r5', 'r4'), ('r4', 'r3')):
    base = Path('~')
    assert (base/f'codex_op_1114{later}/briefs/T080/prior_recheck/verify.py').read_bytes() == (base/f'codex_op_1114{earlier}/briefs/T080/verify.py').read_bytes()
report, proof, log = ((root/name).read_text() for name in ('REPORT.md', 'PROOF.md', 'LOG.md'))
assert report.splitlines()[0] == 'VERDICT: PARTIAL local bond-direction defects separate arbitrarily filled strips between two fixed orientations'
for name in ('VERIFY_OUTPUT.txt', 'prior_recheck/VERIFY_OUTPUT.txt'):
    assert (root/name).read_text().strip() in log, name
data = json.loads((root/'verification.json').read_text())
prior = json.loads((root/'prior_recheck/verification.json').read_text())
for record in (data, prior):
    assert record['status'] == 'PASS'
    assert record['nice_priority'] >= 15
    assert record['elapsed_seconds'] < 1200 and record['peak_rss_mib'] < 128
assert F(data['prior_interval_lower']) > 2
assert F(data['prior_squared_gap']) == F(33193389889, 11238523308) > 0
assert data['M'] == 4 and data['band_columns'] == 7
assert F(data['observation_radius']) == F(31, 10)
assert F(data['half_width']) == F(203, 400)
grids = data['exhaustive_grids']
assert sum(g['all_assignments'] for g in grids) == 26487
assert [g['legal_assignments'] for g in grids] == [1, 81, 400]
assert sum(g['no_face_connected_crossing'] for g in grids) == 188
assert [p['added_centers'] for p in data['packing_trials']] == [11, 11, 14]
assert all(p['minimum_separation'] >= 1 and p['defect_path_vertices'] >= 11 for p in data['packing_trials'])
assert prior['exact_count_cases'] == 560
assert F(prior['rational_lower']) == F(3317635, 1591356) > 2
assert proof.count('\\[') == proof.count('\\]')
for phrase in ('eight-neighbor', 'Gibbs', 'intermediate'):
    assert phrase in report and phrase in proof
assert 'T080 remains open' in report
assert not (root/'SOLVED_ELSEWHERE.md').exists()
print('PASS: unchanged prior sources; complete logged outputs; exact constants; exhaustive counts; resource records; eight-neighbor and Gibbs scope consistent.')
