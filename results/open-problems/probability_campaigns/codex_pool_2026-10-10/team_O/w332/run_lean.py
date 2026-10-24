import json
import os
from pathlib import Path
import subprocess
import time

root = Path(__file__).resolve().parent
env = dict(os.environ)
env['LEAN_CHECK_DIR'] = str(root/'lean_receipts')
cmd = ['python','-X','utf8','~/.claude/dreaming/lean_check.py','--file',str(root/'KeyStep.lean'),'--target','w332_profile_sign','--timeout','50','--json']
start = time.perf_counter()
try:
    result = subprocess.run(cmd, env=env, timeout=60, capture_output=True, text=True, encoding='utf-8', errors='replace')
    receipt = {'command':cmd, 'elapsed_seconds':time.perf_counter()-start, 'returncode':result.returncode, 'stdout':result.stdout, 'stderr':result.stderr}
except subprocess.TimeoutExpired:
    receipt = {'command':cmd, 'elapsed_seconds':time.perf_counter()-start, 'outcome':'timeout; not Lean-checked'}
(root/'lean_result.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt, indent=2))
