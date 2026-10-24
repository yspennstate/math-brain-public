from pathlib import Path
import subprocess
import sys

out = Path(__file__).with_name('recall.txt')
args = [sys.executable, '-X', 'utf8', '~/.claude/dreaming/brain.py',
        'recall', 'probability P0104 first passage fluctuation proof mistakes', '-n', '3']
try:
    result = subprocess.run(args, capture_output=True, text=True,
                            encoding='utf-8', timeout=60)
    body = result.stdout + result.stderr
    out.write_text(body, encoding='utf-8')
    print(body)
    print('returncode', result.returncode)
except subprocess.TimeoutExpired:
    body = 'Recall exceeded the owner-specified 60-second limit. Use the named memory scars and the targeted index fallback.\n'
    out.write_text(body, encoding='utf-8')
    print(body)
