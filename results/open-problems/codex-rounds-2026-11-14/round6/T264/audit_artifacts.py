"""Read-only consistency audit of the saved deliverables."""
import ast
import json
import os
from pathlib import Path
import resource
import signal

assert os.environ['OMP_NUM_THREADS'] == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(15)
resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
root = Path(__file__).resolve().parent
assert root == Path.cwd().resolve()
for name in ('recheck_prior.py', 'verify_antipodal.py', 'audit_artifacts.py'):
    ast.parse((root/name).read_text())
report = (root/'REPORT.md').read_text()
assert report.splitlines()[0].startswith('VERDICT: PROVED ')
assert '+and ' not in report
assert not (root/'SOLVED_ELSEWHERE.md').exists()
v = json.loads((root/'verification_data.json').read_text())
p = json.loads((root/'prior_data.json').read_text())
assert len(v['exact_cases']) == 109
assert len(v['limits']) == 18
assert v['signed_directions'] == 9000
assert all(r['nice'] >= 15 and r['peak_rss_bytes'] < 1_000_000_000
           and r['seconds'] < 1200 for r in (v['resources'], p['resources']))
for r in v['limits']:
    assert abs(r['independent_arc_risk']-r['limit']) < 4e-6
for name in ('prior_output.txt', 'verification_output.txt'):
    assert 'All assertions passed.' in (root/name).read_text()
assert v['max_price_error'] < 1e-12
assert v['max_risk_error'] < 1e-9
assert '0.2533' in report and '16,252,928' in report
assert v['resources']['peak_rss_bytes'] == 16252928
assert (root/'PROOF.md').is_file() and (root/'LOG.md').is_file()
print('PASS artifact audit: verdict, parsed scripts, 109 exact cases, 18 direct limits,')
print('9000 signed directions, saved outputs, report figures and resource limits')
print('Final extension resources:', v['resources'])
