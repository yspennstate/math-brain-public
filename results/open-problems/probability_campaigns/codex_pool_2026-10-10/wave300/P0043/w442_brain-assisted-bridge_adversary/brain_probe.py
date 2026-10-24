"""Bounded, read-only math-brain recall and exact result-card preservation."""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CODE = Path('~/math-brain-build/src')
QUERY = 'critical percolation quasi-transitive exponential growth absence infinite cluster'
command = [sys.executable, '-X', 'utf8', '-m', 'math_brain.cli', 'recall',
           '~/math-brain-build/local/population/brain.sqlite3', QUERY, '--limit', '5']
environment = os.environ.copy()
environment['PYTHONPATH'] = str(CODE)
environment['PYTHONDONTWRITEBYTECODE'] = '1'
started = time.perf_counter()
try:
    result = subprocess.run(command, cwd=ROOT, env=environment, capture_output=True,
                            text=True, encoding='utf-8', errors='replace', timeout=60)
    receipt = {'command': command, 'query': QUERY, 'seconds': time.perf_counter()-started,
               'returncode': result.returncode, 'timed_out': False, 'store_access': 'read-only'}
    output = result.stdout + result.stderr
except subprocess.TimeoutExpired as exc:
    def decode(value):
        return value.decode('utf-8', errors='replace') if isinstance(value, bytes) else value or ''
    receipt = {'command': command, 'query': QUERY, 'seconds': time.perf_counter()-started,
               'returncode': None, 'timed_out': True, 'store_access': 'read-only'}
    output = decode(exc.stdout) + decode(exc.stderr)
(ROOT/'math_recall.txt').write_text(output, encoding='utf-8')
(ROOT/'math_recall_receipt.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt))
print(output[:19000])
