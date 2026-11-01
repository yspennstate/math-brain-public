import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parent
query = 'C0064 nearest-neighbour percolation infrared bound triangle condition mistakes'
start = time.monotonic()
try:
    proc = subprocess.run(
        ['python', '-X', 'utf8', r'~\.claude\dreaming\brain.py', 'recall', query],
        capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60,
    )
    result = {'query': query, 'elapsed_seconds': time.monotonic()-start,
              'returncode': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr}
except subprocess.TimeoutExpired as exc:
    result = {'query': query, 'elapsed_seconds': time.monotonic()-start,
              'timeout_seconds': 60, 'stdout': (exc.stdout or b'').decode('utf-8', 'replace') if isinstance(exc.stdout, bytes) else (exc.stdout or ''),
              'stderr': (exc.stderr or b'').decode('utf-8', 'replace') if isinstance(exc.stderr, bytes) else (exc.stderr or '')}
(ROOT/'recall_measurement.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(result, ensure_ascii=False)[:16000])
