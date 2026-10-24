import os
import subprocess
import sys
from pathlib import Path

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
query = ' '.join(sys.argv[1:]) or 'open problem SPDE endpoint continuity counterexample mistakes'
try:
    result = subprocess.run(
        [sys.executable, '-X', 'utf8', '~/.claude/dreaming/brain.py', 'recall', query],
        timeout=60, capture_output=True, text=True, encoding='utf-8', errors='replace',
    )
    output = result.stdout[:18000] + '\n' + result.stderr[:2000]
    print(output)
    Path(__file__).with_name('recall_output.txt').write_text(output, encoding='utf-8')
except subprocess.TimeoutExpired:
    output = 'RECALL_TIMEOUT_60_SECONDS; use the named memory-index fallback.\n'
    print(output)
    Path(__file__).with_name('recall_output.txt').write_text(output, encoding='utf-8')
