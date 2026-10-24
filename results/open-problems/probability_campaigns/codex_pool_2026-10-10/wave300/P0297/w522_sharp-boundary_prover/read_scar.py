"""Bounded, read-only recall for this job; save only in the worker folder."""
from pathlib import Path
import json
import subprocess
import sys

root = Path(__file__).resolve().parent
command = [sys.executable, '-X', 'utf8', '~/.claude/dreaming/brain.py',
           'recall', 'P0297 Liouville quantum gravity proof gaps mistakes']
record = {'command': command, 'timeout_seconds': 60}
try:
    run = subprocess.run(command, capture_output=True, text=True, encoding='utf-8',
                         errors='replace', timeout=60)
    record.update(returncode=run.returncode, stdout=run.stdout, stderr=run.stderr)
except subprocess.TimeoutExpired as exc:
    record.update(timeout=True, fallback='Targeted MEMORY.md grep and perceptron_proof_open_gaps_fleet_2026_07_12.md')
    for name in ('stdout', 'stderr'):
        value = getattr(exc, name, None)
        record[name] = value.decode('utf-8', 'replace') if isinstance(value, bytes) else value
(root / 'SCAR_RECALL.json').write_text(json.dumps(record, indent=2), encoding='utf-8')
print(json.dumps(record, ensure_ascii=False)[:7000])
