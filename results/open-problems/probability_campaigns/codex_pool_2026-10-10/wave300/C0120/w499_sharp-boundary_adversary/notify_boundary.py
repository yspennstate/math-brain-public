from pathlib import Path
import subprocess
import sys

base = Path(__file__).resolve().parent
mesh = '~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py'
jobs = [
    [mesh, 'read', '--as', 'w499'],
    [mesh, 'say', '--as', 'w499', '--to', 'w498', '--kind', 'claim', 'C0120 boundary lane: independent Gaussian layer-mean obstruction saved before any paired proof at ~/brain_workers/w499/INDEPENDENT_BOUNDARY_20261010.md. Please point to your exact bridge statement/proof and claimed quantifiers; no parent solution claim.'],
    [mesh, 'say', '--as', 'w499', '--to', 'w500', '--kind', 'found', 'Independent C0120 boundary derivation ready at ~/brain_workers/w499/INDEPENDENT_BOUNDARY_20261010.md and BOUNDARY_RESULTS_20261010.jsonl: fixed Gaussian width W forces Var(logZ)>=beta^2 n/W. Please independently check the scope/identity and supply response-side served-model and independent-login evidence if available.'],
    ['~/primary_directive/pd_progress.py', '--event', 'C0120 independent Gaussian finite-width variance obstruction saved; parent target remains unresolved.', '--agent', 'w499', '--row', 'S1.C0120.B0', '--evidence', str(base / 'BOUNDARY_RESULTS_20261010.jsonl')],
]
for i, job in enumerate(jobs):
    try:
        run = subprocess.run([sys.executable, '-X', 'utf8', *job], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
        result = f'JOB {i}: exit={run.returncode}\n{run.stdout}\n{run.stderr}\n'
    except subprocess.TimeoutExpired:
        result = f'JOB {i}: timeout at 60s\n'
    with (base / 'NOTIFICATION_RECEIPTS.txt').open('a', encoding='utf-8') as out:
        out.write(result)
    print(result, flush=True)
