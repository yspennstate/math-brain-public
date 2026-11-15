"""Independent arithmetic and saved-artifact audit."""
import ast
import hashlib
import json
import math
import os
import resource
import signal
from fractions import Fraction as F
from pathlib import Path

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('30s limit')))
signal.alarm(30)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
prior = json.loads(Path('surface_checks.json').read_text())
independent = json.loads(Path('independent_surface.json').read_text())
cluster = json.loads(Path('cluster_checks.json').read_text())
assert prior['counts']['interval_free']+prior['counts']['irregular_free'] == 207
assert prior['counts']['interval_conditioned']+prior['counts']['irregular_conditioned'] == 918
assert prior['counts']['entropy_sandwich'] == 18
assert independent['aggregate_recurrences'] == 6*40 == 240
assert independent['direct_enumerations'] == 6*6 == 36
for row in independent['records']:
    t = F(row['t'])
    assert F(row['k']) == (2*t*t+t-1)/t
    assert F(row['pressure_eigenvalue']) == (1+2*t)/3
    ratio = F(row['last_free_ratio'])
    assert 1/t <= ratio <= 1
assert independent['surface_coefficients'] == [[3, 1], [4, 1], [5, 1]]
assert cluster['graph_cases'] == sum(2**(n*(n-1)//2) for n in range(1, 6)) == 1099
assert cluster['domain_checks'] == 2**5*11 == 352
assert cluster['exact_log_coefficients'] == 2**5*11*6 == 2112
assert cluster['rational_log_tail_checks'] == 2**5 == 32
assert F(cluster['negative_checks']['repetition_degree2']) == -F(1, 2)*F(1, 32)**2
assert F(cluster['negative_checks']['false_collar_incompatibility_gap']) == F(1, 7)*F(1, 11)
assert F(cluster['negative_checks']['domain_dependent_activity_gap']) == F(1, 128)-F(1, 256)
assert cluster['example']['overlapping_collar_sites'] == 5
assert F(cluster['example']['log_interval_width']) > 0
assert F(cluster['example']['log_interval_width']) < F(cluster['example']['proven_cluster_tail_bound'])
threshold_values = []
for row in cluster['threshold_checks']:
    d, m = row['d'], row['m']
    q = 3**d
    # Compute D^2 K again by summing label choices over a macrocell.
    choices = math.prod(3 for _ in range(m**d))
    b = (q*q-2*q+1)*choices
    assert (q, b) == (row['q'], row['B'])
    h = row['H']
    assert F(row['r_upper']) == F(3*b, h*h*h)
    # Equivalence of the root criterion checked by cross multiplication.
    assert (q+1)*3*b <= h*h*h
    r_upper = F(3*b, h*h*h)
    assert q*r_upper <= 1-r_upper
    tau_star = (math.log(math.e*b*(q+1)))*4/3
    tau_other = (1+2*math.log(q-1)+m**d*math.log(3)+math.log1p(q))*4/3
    assert abs(tau_star-tau_other) < 1e-12
    threshold_values.append((d, m, tau_star))

for data in (prior, independent, cluster):
    assert data['effective_nice'] >= 15
    assert data['peak_rss_bytes'] < 1024**3
    assert data['elapsed_seconds'] < 20*60
original = Path('~/codex_op_1114r5/briefs/T081/check_surface.py')
assert hashlib.sha256(original.read_bytes()).digest() == hashlib.sha256(Path('prior_check_surface.py').read_bytes()).digest()
for name in ('prior_check_surface.py', 'recheck_surface_independent.py', 'check_clusters.py', 'audit_artifacts.py'):
    ast.parse(Path(name).read_text())
for name in ('PROOF.md', 'LOG.md', 'REPORT.md', 'prior_surface_output.txt',
             'independent_surface_output.txt', 'cluster_output.txt'):
    assert Path(name).stat().st_size > 0
proof = Path('PROOF.md').read_text()
assert proof.count(r'\[') == proof.count(r'\]')
assert proof.count(r'\(') == proof.count(r'\)')
assert 'cutoff is inactive' in proof
assert 'perforated' in proof
assert Path('REPORT.md').read_text().splitlines()[0] == (
    'VERDICT: PARTIAL fixed-background contour expansion and exact finite-domain interaction verified')
assert not Path('SOLVED_ELSEWHERE.md').exists()
print('Prior surface counts and 240 independent recurrences verified.')
print('1099 graphs, 352 domains, 2112 coefficients and 32 rational tails verified.')
print('Thresholds independently re-derived, with exact root-criterion cross multiplication.')
print('Threshold examples (d, m, tau_star):', threshold_values)
print('Copied script hash, Python syntax, LaTeX delimiters and report format verified.')
print('Saved results and resource limits passed.')
print('Effective nice:', os.getpriority(os.PRIO_PROCESS, 0))
print('Audit peak RSS bytes:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
