"""Final saved-result and syntax audit; standard library only."""
import ast
import json
import math
import os
import resource
import signal
from fractions import Fraction as Q
from pathlib import Path

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('30s limit')))
signal.alarm(30)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

geometry = json.loads(Path('geometry_checks.json').read_text())
replacement = json.loads(Path('independent_recheck.json').read_text())
surface = json.loads(Path('surface_checks.json').read_text())
calculation = json.loads(Path('calculation_audit.json').read_text())
assert geometry['counts'] == dict(ternary_2d=3**9, binary_3d=2**8,
                                  sparse_ternary_3d=3**6, support_pairs=204)
assert len(replacement['comparisons']) == 54
assert [v['physical'] for v in replacement['examples']] == [160, 128]
assert all(v['independent_average'] == 144 for v in replacement['examples'])
assert surface['counts'] == dict(interval_free=3*6, interval_conditioned=3*6*9,
                                density=3*6*9, irregular_free=3*63,
                                irregular_conditioned=3*63*4, eigenpairs=3*3,
                                entropy_sandwich=3*6)
for result in surface['spectral_checks']:
    t = Q(result['t'])
    k = Q(result['k'])
    lam = Q(result['pressure_eigenvalue'])
    ratio = Q(result['correlation_eigenvalue_ratio'])
    assert k == 1+2*t-1/t
    assert lam == (1+2*t)/3
    assert ratio == 1-1/(t*(1+2*t))
    assert abs(result['entropy_minus_energy']-math.log(float(lam))) < 1e-12
    assert abs(result['correlation_length']*math.log(float(ratio))+1) < 1e-12
assert calculation['exact_centering_and_free_identities'] == (2**6-1)*4*3
assert calculation['connected_supports'] == geometry['connected_supports_3x3'] == 388
assert calculation['separated_pairs'] == geometry['counts']['support_pairs']
assert calculation['coefficient_vectors']['upper_conditioned'] == [5, 1]
for n, result in enumerate(surface['negative_without_safe_state'], 1):
    assert result['n'] == n
    assert Q(result['free']) == Q(2, 2**n)
    assert result['incompatible_pinned'] == 0

for result in (geometry, replacement, surface, calculation):
    assert result['peak_rss_bytes'] < 1024**3
    assert result['elapsed_seconds'] < 20*60
    assert result.get('effective_nice', result.get('nice')) >= 15
for filename in ('prior_check_geometry.py', 'prior_recheck_replacement.py',
                 'check_surface.py', 'audit_calculations.py', 'audit_artifacts.py'):
    ast.parse(Path(filename).read_text())
for filename in ('PROOF.md', 'LOG.md', 'REPORT.md', 'surface_output.txt',
                 'prior_geometry_output.txt', 'prior_replacement_output.txt',
                 'calculation_audit.txt'):
    assert Path(filename).stat().st_size > 0
report = Path('REPORT.md').read_text()
assert report.splitlines()[0] == ('VERDICT: PARTIAL uniform surface-pressure estimate '
                                'verified for the safe-state restricted ensembles')
assert not Path('SOLVED_ELSEWHERE.md').exists()
proof = Path('PROOF.md').read_text()
assert proof.count(r'\[') == proof.count(r'\]')
assert proof.count(r'\(') == proof.count(r'\)')
assert 'cluster expansion is not reproved' in proof
assert 'It does not prove a liquid' in proof
print('Prior geometry and all 54 replacement comparisons verified.')
print('918 conditioned partition checks; 207 free-domain checks; 18 entropy checks verified.')
print('756 cases of each centering identity; exact pressure eigenvalues and constants verified.')
print('Resource bounds, syntax, report format, LaTeX delimiters and saved artifacts passed.')
print('Effective nice:', os.getpriority(os.PRIO_PROCESS, 0))
print('Audit peak RSS bytes:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
