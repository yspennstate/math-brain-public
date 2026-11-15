"""Reproducible serial sweep. No downloads, worker pool or third-party packages."""
import csv
import json
import os
from pathlib import Path
import resource
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
priority = os.getpriority(os.PRIO_PROCESS, 0)
if priority < 10:
    os.nice(10-priority)
address_limit_enforced = False
try:
    resource.setrlimit(resource.RLIMIT_AS, (3_500_000_000, 3_500_000_000))
    address_limit_enforced = True
except (ValueError, OSError) as error:
    # Mach-O executable virtual mappings may already exceed this limit.
    print('RLIMIT_AS unavailable:', error, flush=True)
started = time.time()
rows = []
for n in (1000, 10000, 100000):
    for j, c in enumerate((1.5, 1.55, 1.6, 1.75, 2, 2.25, 2.5)):
        state = Path.home() / '.claude/compute/compute_state.json'
        if state.exists():
            governor = json.loads(state.read_text())
            if governor.get('status') == 'distress':
                raise SystemExit('Governor distress; stopping before next batch')
        seed = 96000000 + n * 10 + j
        prefix = f'data/sweep_n{n}_c{int(c*100)}'
        with open(prefix + '.csv', 'w') as output:
            subprocess.run(['code/sim', str(n), str(c), '10', str(seed), '30', '200', prefix], stdout=output, check=True)
        batch = list(csv.DictReader(open(prefix + '.csv')))
        rows.extend(batch)
        with open('data/sweep.csv', 'w') as output:
            writer = csv.DictWriter(output, fieldnames=rows[0])
            writer.writeheader()
            writer.writerows(rows)
        print(n, c, sum(int(r['found']) for r in batch), '/', len(batch), 'elapsed', round(time.time()-started, 2), flush=True)
Path('data/sweep_resources.json').write_text(json.dumps({'wall_seconds': time.time()-started, 'self': list(resource.getrusage(resource.RUSAGE_SELF)), 'children': list(resource.getrusage(resource.RUSAGE_CHILDREN)), 'threads': 1, 'requested_address_space_limit_bytes': 3500000000, 'address_space_limit_enforced': address_limit_enforced, 'inherited_nice': priority}, indent=2))
