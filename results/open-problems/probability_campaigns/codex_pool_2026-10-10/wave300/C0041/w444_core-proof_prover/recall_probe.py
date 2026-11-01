import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
try:
    result = subprocess.run(
        ['python', '-X', 'utf8', '~/.claude/dreaming/brain.py', 'recall',
         'C0041 directional transience ballisticity proof mistakes'],
        capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60,
    )
    record = {'returncode': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
except subprocess.TimeoutExpired:
    record = {'status': 'RECALL_TIMEOUT_60S', 'fallback': 'targeted MEMORY.md and named scar'}
(ROOT / 'recall_receipt.json').write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(record, ensure_ascii=False)[:10000])
