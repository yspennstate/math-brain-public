"""Publish the saved auditor request through the explicitly named progress route."""
import json
import os
from pathlib import Path
import subprocess

here = Path(__file__).resolve().parent
env = dict(os.environ)
env['PYTHONDONTWRITEBYTECODE'] = '1'
command = [
    'python', '-X', 'utf8', '~/primary_directive/pd_progress.py',
    '--event', 'w346: independent audit requested for w344: 10 bundles, 22 nodes, 25 relations. Mesh team route unavailable; complete request is saved.',
    '--agent', 'w344', '--row', 'S1.w344.028',
    '--evidence', str(here / 'AUDIT_REQUEST_w346.md'),
]
result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', env=env)
receipt = {'route': 'named progress page', 'command': command,
           'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr,
           'direct_mesh_notification': 'FAILED: no active team registration',
           'mathematical_acceptance': 'PENDING w346'}
(here / 'audit_progress_receipt.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt), flush=True)
raise SystemExit(result.returncode)
