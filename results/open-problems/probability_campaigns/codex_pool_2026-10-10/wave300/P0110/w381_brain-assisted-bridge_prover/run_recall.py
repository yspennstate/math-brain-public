"""Read-only brain recall, with the user-mandated 60 second deadline."""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

root = Path(__file__).resolve().parent
query = 'P0110 iid first passage percolation KPZ exponent bridge mistakes'
cmd = [sys.executable, '-B', '-X', 'utf8', r'~\.claude\dreaming\brain.py', 'recall', query, '-n', '3']
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
started = time.perf_counter()
try:
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60, env=env)
    receipt = {'command': cmd, 'query': query, 'elapsed_seconds': time.perf_counter()-started, 'returncode': result.returncode, 'timeout_seconds': 60, 'timed_out': False}
    out, err = result.stdout, result.stderr
except subprocess.TimeoutExpired as exc:
    receipt = {'command': cmd, 'query': query, 'elapsed_seconds': time.perf_counter()-started, 'timeout_seconds': 60, 'timed_out': True}
    out = exc.stdout or b''
    err = exc.stderr or b''
    if isinstance(out, bytes): out = out.decode('utf-8', errors='replace')
    if isinstance(err, bytes): err = err.decode('utf-8', errors='replace')
(root/'recall_output.txt').write_text(out, encoding='utf-8')
(root/'recall_stderr.txt').write_text(err, encoding='utf-8')
(root/'recall_receipt.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt, ensure_ascii=False))
print(out[:9000])
