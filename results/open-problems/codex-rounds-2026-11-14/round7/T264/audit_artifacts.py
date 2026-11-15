"""Read-only consistency check of the completed T264 deliverables."""
import ast
import json
import os
from pathlib import Path
import resource
import signal

assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
signal.alarm(15)
root = Path(__file__).resolve().parent
assert root == Path.cwd().resolve()
for name in ('recheck_round6.py', 'verify_finite_moments.py', 'audit_artifacts.py'):
    ast.parse((root/name).read_text())
v = json.loads((root/'verification_data.json').read_text())
p = json.loads((root/'prior_data.json').read_text())
assert len(v['configurations']) == 51
assert sum(r['compressed_cost'] is not None for r in v['configurations']) == 11
assert len(p['cases']) == 20 and p['ambient_directions'] == 1800
for data in (v, p):
    r = data['resources']
    assert r['nice'] >= 15 and r['threads'] == 1
    assert r['peak_rss_bytes'] < 1_000_000_000 and r['seconds'] < 1200
for r in v['configurations']:
    assert r['cost'] <= r['proved_cost_bound']*(1+1e-12)
    assert r['interpolation_error'] < 1e-8
    if r['compressed_cost'] is not None:
        assert r['compressed_cost'] <= r['cost']*(1+1e-12)
        assert r['compressed_interpolation_error'] < 1e-8
for name in ('prior_output.txt', 'verification_output.txt'):
    assert 'All assertions passed.' in (root/name).read_text()
report = (root/'REPORT.md').read_text()
proof = (root/'PROOF.md').read_text()
assert report.splitlines()[0].startswith('VERDICT: PROVED ')
assert '17,055,744' in report and '15,400,960' in report
assert '0.1363 seconds' in report and '0.0787 seconds' in report
assert '32(n-1)' in report and '32(n-1)' in proof
assert 'does not establish tempered overfitting' in report
assert not (root/'SOLVED_ELSEWHERE.md').exists()
assert (root/'LOG.md').is_file()
print('PASS: scripts parse; 51 competitors, 11 compressions, 20 prior cases;')
print('cost/interpolation bounds, output files, resource records and report agree.')
