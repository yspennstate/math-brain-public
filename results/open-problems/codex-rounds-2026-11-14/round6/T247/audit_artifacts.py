"""Read-only consistency check of the completed research artifacts."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import json
import math
from pathlib import Path
import re
import signal
signal.alarm(30)
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
report = Path('REPORT.md').read_text()
proof = Path('PROOF.md').read_text()
assert report.splitlines()[0].startswith('VERDICT: PARTIAL ')
assert [int(x) for x in re.findall(r'\\tag\{(\d+)\}', proof)] == list(range(1, 32))
assert proof.count(r'\[') == proof.count(r'\]')
for path in Path('.').glob('*.py'):
    compile(path.read_text(), str(path), 'exec')
for target in re.findall(r'\]\(([^)]+)\)', report):
    if not target.startswith('https:'):
        assert Path(target).is_file(), target
def finite(value):
    if isinstance(value, float):
        assert math.isfinite(value)
    elif isinstance(value, dict):
        for v in value.values():
            finite(v)
    elif isinstance(value, list):
        for v in value:
            finite(v)
for name in ('recheck_results.json', 'results.json', 'forward_results.json'):
    data = json.loads(Path(name).read_text())
    finite(data)
    assert data['peak_rss_bytes'] < 10**9
    assert data['runtime_seconds'] < 180
    assert data['niceness'] >= 15
    if 'thread_environment' in data:
        assert all(v == '1' for v in data['thread_environment'].values())
    else:
        assert data['threads'] == 1
new = json.loads(Path('results.json').read_text())
assert len(new['coefficient_quadrature']) == 9
assert len(new['biased_comparison']) == 24
assert new['scalar']['rational_coefficients'] == 18
assert max(x['max_direct_determinant_error'] for x in new['full_products']) < 2e-13
assert 'All biased-network verification checks passed' in Path('recheck_output.txt').read_text()
assert 'All log-volume verification checks passed' in Path('verification_output.txt').read_text()
assert 'FloatingPointError' in Path('verification_first_failed.txt').read_text()
assert '27 path checkpoints passed' in Path('forward_summary.txt').read_text()
assert len(json.loads(Path('forward_results.json').read_text())['paths']) == 27
print('Final artifact audit passed: 31 equation labels, proof delimiters, script syntax, report links, '
      'exact and numerical check counts, finite data, preserved failure, saved outputs, and resource limits agree.')
