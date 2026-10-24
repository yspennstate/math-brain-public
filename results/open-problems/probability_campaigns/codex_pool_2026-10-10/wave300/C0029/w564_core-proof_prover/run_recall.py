import os
import subprocess

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
try:
    result = subprocess.run(
        ['python', '-X', 'utf8', '~/.claude/dreaming/brain.py',
         'recall', 'C0029 Spielman Teng least singular value proof mistakes'],
        capture_output=True, encoding='utf-8', timeout=60)
    print(result.stdout[:14000])
    print(result.stderr[:2000])
except subprocess.TimeoutExpired:
    print('RECALL_TIMEOUT_60S: use scoped MEMORY.md fallback and cited scar.')
