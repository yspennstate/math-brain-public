"""One bounded, synchronous recall attempt; writes evidence only in this folder."""
from pathlib import Path
import json
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
command = [sys.executable, '-X', 'utf8', r'~\.claude\dreaming\brain.py', 'recall', 'P0117 planar iid first passage percolation bigeodesics proof mistakes', '-n', '3']
started = time.monotonic()
record = {'command': command, 'limit_seconds': 60}
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
    record.update(status='completed', exit_code=result.returncode)
    output = result.stdout + result.stderr
except subprocess.TimeoutExpired as error:
    record.update(status='timeout')
    output = (error.stdout or b'') + (error.stderr or b'')
    if isinstance(output, bytes):
        output = output.decode('utf-8', 'replace')
record['elapsed_seconds'] = round(time.monotonic() - started, 3)
(root / 'recall_raw.txt').write_text(output, encoding='utf-8')
(root / 'recall_measurement.json').write_text(json.dumps(record, indent=2), encoding='utf-8')
print(json.dumps(record))
print(output[:14000])
