#!/usr/bin/env python3
"""Run one nice-10 worker; request memory limits and record any OS refusal."""
import datetime
import json
import os
from pathlib import Path
import resource
import subprocess

root = Path(__file__).resolve().parents[1]
os.chdir(root)
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 10, priority
governor = Path.home()/'.claude/compute/compute_state.json'
state = json.loads(governor.read_text())
if state.get('status') == 'distress':
    raise SystemExit('Compute governor reports distress; simulation not started.')
limit = 4 * 1024**3
limits = {}
for name in ['RLIMIT_AS', 'RLIMIT_RSS']:
    kind = getattr(resource, name)
    soft, hard = resource.getrlimit(kind)
    try:
        resource.setrlimit(kind, (min(limit, hard), hard))
        limits[name] = list(resource.getrlimit(kind))
    except (OSError, ValueError) as exc:
        limits[name] = {'error': str(exc), 'existing': [soft, hard]}
env = dict(os.environ)
for name in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS']:
    env[name] = '1'
metadata = {'start_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'priority': priority, 'threads': 1, 'requested_memory_limit_bytes': limit,
            'resource_limits': limits,
            'compute_status_at_start': state.get('status'),
            'compute_mode_at_start': state.get('mode'),
            'command': ['./code/arw', '--simulate', 'data/runs.csv']}
(root/'data'/'simulation_metadata.json').write_text(json.dumps(metadata, indent=2)+'\n')
with (root/'data'/'simulation.log').open('w') as f:
    result = subprocess.run(metadata['command'], env=env, stdout=f, stderr=subprocess.STDOUT)
metadata.update(end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                returncode=result.returncode)
(root/'data'/'simulation_metadata.json').write_text(json.dumps(metadata, indent=2)+'\n')
print(json.dumps(metadata))
raise SystemExit(result.returncode)
