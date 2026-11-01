"""One bounded recall; result written only in this worker's folder."""
from pathlib import Path
import subprocess
import json
import datetime

root = Path(__file__).resolve().parent
command = ['python', '-X', 'utf8', '~/.claude/dreaming/brain.py', 'recall', 'C0044 directional zero-one iid RWRE harmonicity conditioning mistakes']
receipt = {'command': command, 'started': datetime.datetime.now().isoformat()}
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
    receipt.update(returncode=result.returncode, outcome='returned')
    # Keep the first three results if separated by headings; otherwise a short scoped excerpt.
    lines = result.stdout.splitlines()
    receipt['output_excerpt'] = '\n'.join(lines[:90])
    receipt['stderr_excerpt'] = result.stderr[:1200]
except subprocess.TimeoutExpired:
    receipt.update(outcome='timeout_after_60_seconds', fallback='Targeted rg of MEMORY.md and cited scar files')
(root / 'RECALL_RECEIPT.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps(receipt, ensure_ascii=False))
