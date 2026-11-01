"""Foreground, bounded recall; all capture files are in this worker folder."""
import pathlib
import subprocess
import time

ROOT = pathlib.Path(__file__).resolve().parent
start = time.monotonic()
with (ROOT / 'brain_recall.txt').open('w', encoding='utf-8') as out:
    try:
        run = subprocess.run(
            ['python', '-X', 'utf8', '~/.claude/dreaming/brain.py',
             'recall', 'C0017 square bond percolation conformal invariance bridge mistakes', '3'],
            stdout=out, stderr=subprocess.STDOUT, timeout=60,
        )
        print(f'recall returncode={run.returncode}; seconds={time.monotonic()-start:.2f}')
    except subprocess.TimeoutExpired:
        print(f'recall TIMEOUT after {time.monotonic()-start:.2f}s; use targeted memory-index fallback')
print((ROOT / 'brain_recall.txt').read_text(encoding='utf-8')[:18000])
