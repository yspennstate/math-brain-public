"""Bounded deterministic arithmetic replay; no model simulation or theorem proof."""
from pathlib import Path
import hashlib
import json
import math
import time

root = Path(__file__).resolve().parent
started = time.perf_counter()
rows = []
for eta in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5):
    mean_u = math.atan(1 / eta) / math.pi
    norm_sq = 1 / (2 * math.pi * eta)
    mean_abs_g_sq = math.atan(1 / eta) / eta
    assert mean_u <= 0.5
    assert math.isclose(eta * mean_abs_g_sq, math.pi * mean_u, rel_tol=1e-14)
    rows.append(dict(eta=eta, mean_poisson_density_at_zero=mean_u,
                     sample_poisson_l2_squared=norm_sq,
                     mean_absolute_resolvent_squared=mean_abs_g_sq))

def primitive(t, b):
    return t / (2 * (t*t + b*b)) + math.atan(t / b) / (2*b)

upper_checks = lower_checks = 0
for coupling in (0.2, 1.0, 3.0):
    for ratio in (0.001, 0.05, 0.2, 0.8):
        b = ratio * coupling
        for location in (-1.5, -0.8, 0.0, 0.8, 1.5):
            a = location * coupling
            exact = (primitive(coupling-a, b) - primitive(-coupling-a, b)) / (2*coupling*math.pi**2)
            upper = 1 / (4 * math.pi * coupling * b)
            assert exact >= 0 and exact <= upper * (1+1e-13)
            upper_checks += 1
            if abs(a)+b <= coupling:
                lower = 1 / (4 * coupling * math.pi**2 * b)
                assert exact >= lower * (1-1e-13)
                lower_checks += 1

claims = [json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
assert len({row['id'] for row in claims}) == len(claims)
for row in claims:
    for field in ('statement', 'assumptions', 'source', 'proof_or_counterexample', 'independent_reviewer', 'remaining_gap', 'status'):
        assert field in row, (row['id'], field)

metrics = dict(command='python -X utf8 ~/brain_workers/w484/verify_artifacts.py',
               method='deterministic closed-form arithmetic replay; not independent review and not a theorem prover',
               stochastic_samples=0, local_gpu_jobs=0,
               atomic_rows=rows, l2_growth_factor=rows[-1]['sample_poisson_l2_squared']/rows[0]['sample_poisson_l2_squared'],
               cavity_upper_checks=upper_checks, resonant_lower_checks=lower_checks,
               saved_claim_count=len(claims), elapsed_seconds=time.perf_counter()-started)
(root/'MEASUREMENTS.json').write_text(json.dumps(metrics, indent=2)+'\n', encoding='utf-8')

review_dir = root/'review'
review_dir.mkdir(exist_ok=True)
peer_path = Path('~/brain_workers/w483/ATTEMPT.md')
snapshot_path=review_dir/'w483_ATTEMPT_snapshot.md'
if peer_path.is_file() or snapshot_path.is_file():
    content = snapshot_path.read_bytes() if snapshot_path.is_file() else peer_path.read_bytes()
    if not snapshot_path.is_file():
        snapshot_path.write_bytes(content)
    receipt = dict(peer='w483', source_path=str(peer_path), snapshot_path=str(review_dir/'w483_ATTEMPT_snapshot.md'),
                   sha256=hashlib.sha256(content).hexdigest(), bytes=len(content),
                   scope='Directly audited L1-L5 conditional spectral route; no parent C0056 or GOE proof',
                   served_author_model_evidence='unavailable', served_auditor_model_evidence='unavailable',
                   live_peer_changed_since_snapshot=(peer_path.is_file() and peer_path.read_bytes()!=content))
    (review_dir/'CORE_RECEIPT.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
    print('CORE_SNAPSHOT', receipt['sha256'], receipt['bytes'])

print(json.dumps({k:metrics[k] for k in ('l2_growth_factor','cavity_upper_checks','resonant_lower_checks','saved_claim_count','elapsed_seconds')}, indent=2))
