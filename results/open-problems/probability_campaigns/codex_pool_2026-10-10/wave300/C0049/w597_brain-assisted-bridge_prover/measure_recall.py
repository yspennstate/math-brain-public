"""Bounded, read-only research recall; no model loading or store writes."""
import collections
import json
import os
from pathlib import Path
import subprocess
import sys
import time

root = Path(__file__).parent
env = os.environ.copy()
env['PYTHONDONTWRITEBYTECODE'] = '1'
env['PYTHONPATH'] = '~/math-brain-build/src'
argv = [sys.executable, '-X', 'utf8', '-m', 'math_brain.cli', 'recall',
        '~/math-brain-build/local/population/brain.sqlite3',
        'random-cluster parafermionic observable SLE martingale uniform integrability',
        '--limit', '5', '--decision', '--skip-unknown-edges']
started = time.monotonic()
run = subprocess.run(argv, capture_output=True, text=True, encoding='utf-8', env=env, timeout=60)
if run.returncode:
    raise RuntimeError(run.stderr)
decision = json.loads(run.stdout)
(root / 'math_recall_raw.json').write_text(json.dumps(decision, ensure_ascii=False, indent=2), encoding='utf-8')
summary = {'argv': argv, 'seconds': time.monotonic()-started,
           'raw_stdout_bytes': len(run.stdout.encode('utf-8')),
           'decision_keys': list(decision),
           'exclusion_count': len(decision.get('exclusions', [])),
           'exclusion_reason_counts': dict(collections.Counter(x.get('reason') for x in decision.get('exclusions', []))),
           'abstained': decision.get('abstained'), 'reason': decision.get('reason'),
           'hits': decision.get('hits', decision.get('results', [])),
           'stderr': run.stderr}
(root / 'math_recall_summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(summary, ensure_ascii=False))
