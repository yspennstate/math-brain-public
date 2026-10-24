"""Run the specifically requested recall with publishing/logging disabled locally."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
env = dict(os.environ)
env.update(PYTHONDONTWRITEBYTECODE='1', BRAIN_RECALL_REFRESH='0',
           BRAIN_GRAPH_LAMBDA='0', BRAIN_RECALL_LOG='0', BRAIN_RECALL_QSEM_W='0')
cmd = [sys.executable, '-B', '-X', 'utf8', '~/.claude/dreaming/brain.py',
       'recall', 'C0017 square lattice percolation proof mistakes', '-n', '3']
start = time.monotonic()
try:
    r = subprocess.run(cmd, env=env, capture_output=True, text=True, encoding='utf-8', timeout=60)
    rec = {'command': cmd, 'returncode': r.returncode, 'stdout': r.stdout, 'stderr': r.stderr,
           'elapsed_seconds': time.monotonic() - start, 'local_env_overrides': {k:env[k] for k in
           ('PYTHONDONTWRITEBYTECODE','BRAIN_RECALL_REFRESH','BRAIN_GRAPH_LAMBDA','BRAIN_RECALL_LOG','BRAIN_RECALL_QSEM_W')}}
except subprocess.TimeoutExpired as exc:
    rec = {'command': cmd, 'status': 'TIMEOUT_60_SECONDS', 'elapsed_seconds': time.monotonic()-start,
           'fallback': 'Read the two explicitly named scar files directly; targeted MEMORY.md matches are next.'}
(root / 'recall_receipt.json').write_text(json.dumps(rec, indent=2, ensure_ascii=False), encoding='utf-8')
print(json.dumps(rec, ensure_ascii=False))
