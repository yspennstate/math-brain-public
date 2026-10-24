"""One bounded, authorized brain recall; stdout contains only the first three hits."""
import os
import subprocess

env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
try:
    result = subprocess.run(
        ['python', '-B', '-X', 'utf8', '~/.claude/dreaming/brain.py',
         'recall', 'C0056 Anderson weak disorder sharp boundary proof mistakes'],
        capture_output=True, text=True, encoding='utf-8', timeout=60, env=env,
    )
    print(result.stdout[:11000])
    if result.stderr:
        print(result.stderr[:1000])
except subprocess.TimeoutExpired:
    print('RECALL_TIMEOUT_60S: use targeted MEMORY.md fallback')
