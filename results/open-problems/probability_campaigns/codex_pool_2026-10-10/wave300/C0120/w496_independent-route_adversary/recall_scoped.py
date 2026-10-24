import subprocess
from pathlib import Path

out = Path(__file__).parent / 'recall_result.txt'
try:
    r = subprocess.run(
        ['python', '-X', 'utf8', '~/.claude/dreaming/brain.py',
         'recall', 'C0120 directed polymer variance independent route mistakes'],
        capture_output=True, text=True, encoding='utf-8', timeout=60,
    )
    s = r.stdout + '\n' + r.stderr[-2000:]
except subprocess.TimeoutExpired:
    s = 'RECALL_TIMEOUT_60S: use the scoped MEMORY.md fallback.\n'
out.write_text(s, encoding='utf-8')
print(s[:14000])
