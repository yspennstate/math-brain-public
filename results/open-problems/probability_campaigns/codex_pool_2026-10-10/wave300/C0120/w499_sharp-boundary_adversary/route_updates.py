from pathlib import Path
import subprocess
import sys

base = Path(__file__).resolve().parent
mesh = '~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py'
messages = [
    ('w498', 'claim', 'Read your L1-L3 after saving independent Gaussian mean and ground-state derivations. Scoped mathematical KEEP; strip limits are correct. Taking a disjoint stronger auxiliary obstruction: complete layered Gaussian graph, N layers of N sites, Var=Theta(N/log N), polynomial-noise path changes with high probability but overlap tends to one. Checkpoint ~/brain_workers/w499/STRONGER_BRIDGE_CHECKPOINT.md; no lattice refutation.'),
    ('w500', 'found', 'Independent w499 Gaussian layer proof saved before w498 proof: ~/brain_workers/w499/INDEPENDENT_ZERO_TEMPERATURE_20261010.md. Scoped mathematical audit of w498 L1-L3 is KEEP, pending served-model/login gate. A disjoint stronger layered-graph bridge obstruction preserving O(n/log n) variance is in STRONGER_BRIDGE_CHECKPOINT.md; full proof packet follows. Please independently referee that new claim.'),
]
for peer, kind, message in messages:
    args = [sys.executable, '-X', 'utf8', mesh, 'say', '--as', 'w499', '--team', 'probability300-integration', '--to', peer, '--kind', kind, message]
    try:
        run = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
        receipt = f'{peer}: exit={run.returncode}\n{run.stdout}\n{run.stderr}\n'
    except subprocess.TimeoutExpired:
        receipt = f'{peer}: timeout at 60s\n'
    with (base / 'NOTIFICATION_RECEIPTS.txt').open('a', encoding='utf-8') as out:
        out.write(receipt)
    print(receipt, flush=True)
