import json
from pathlib import Path
import subprocess
import time

out = Path(__file__).with_name('recall_mistakes.json')
argv = ['python', '-X', 'utf8', '~/.claude/dreaming/brain.py',
        'recall', 'C0049 random-cluster SLE martingale bridge mistakes']
started = time.monotonic()
try:
    result = subprocess.run(argv, capture_output=True, text=True, encoding='utf-8', timeout=60)
    row = dict(argv=argv, seconds=time.monotonic()-started, returncode=result.returncode,
               stdout=result.stdout, stderr=result.stderr)
except subprocess.TimeoutExpired as error:
    def decode(value):
        return value.decode('utf-8', errors='replace') if isinstance(value, bytes) else value
    row = dict(argv=argv, seconds=time.monotonic()-started, timeout=True,
               stdout=decode(error.stdout), stderr=decode(error.stderr))
out.write_text(json.dumps(row, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(row, ensure_ascii=False))
