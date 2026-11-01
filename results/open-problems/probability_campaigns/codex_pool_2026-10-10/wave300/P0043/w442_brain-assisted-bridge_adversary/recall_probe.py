"""One user-required memory recall, bounded at 60 seconds; save its receipt locally."""
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
command = [sys.executable, '-X', 'utf8', '~/.claude/dreaming/brain.py',
           'recall', 'P0043 critical percolation quasi-transitive proof mistakes', '-n', '3']
started = time.perf_counter()
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8',
                            errors='replace', timeout=60)
    receipt = {'command': command, 'seconds': time.perf_counter()-started,
               'returncode': result.returncode, 'timed_out': False}
    output = result.stdout + result.stderr
except subprocess.TimeoutExpired as exc:
    def decode(value):
        return value.decode('utf-8', errors='replace') if isinstance(value, bytes) else value or ''
    receipt = {'command': command, 'seconds': time.perf_counter()-started,
               'returncode': None, 'timed_out': True,
               'fallback': 'Targeted MEMORY.md index lookup and perceptron_proof_open_gaps_fleet_2026_07_12.md'}
    output = decode(exc.stdout) + decode(exc.stderr)
(ROOT/'memory_recall.txt').write_text(output, encoding='utf-8')
(ROOT/'memory_recall_receipt.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt))
print(output[:14000])
