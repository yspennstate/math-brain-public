"""Bounded, read-only brain recall for this task; output only in the worker folder."""
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
cmd = [sys.executable, '-X', 'utf8', '~/.claude/dreaming/brain.py',
       'recall', 'C0017 square lattice percolation conformal invariance mistakes', '-n', '3']
env = dict(os.environ)
env['PYTHONDONTWRITEBYTECODE'] = '1'
try:
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8',
                            errors='replace', timeout=60, env=env)
    body = f'COMMAND: {cmd!r}\nEXIT: {result.returncode}\n{result.stdout}\n{result.stderr}'
except subprocess.TimeoutExpired:
    body = f'COMMAND: {cmd!r}\nRECALL_TIMEOUT_60S: use the named memory scar and targeted index fallback.\n'
(root / 'RECALL_RECEIPT.txt').write_text(body, encoding='utf-8')
print(body[:12000])
