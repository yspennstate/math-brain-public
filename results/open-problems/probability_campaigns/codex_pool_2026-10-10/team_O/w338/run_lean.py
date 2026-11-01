"""Run only the reviewed local source; keep checker outputs in this folder."""
from pathlib import Path
import hashlib
import json
import os
import subprocess

root = Path(__file__).resolve().parent
source = root/'CoreChecks.lean'
digest = hashlib.sha256(source.read_bytes()).hexdigest()
env = dict(os.environ)
env['PYTHONDONTWRITEBYTECODE'] = '1'
env['LEAN_CHECK_DIR'] = str(root/'lean_receipts')
args = ['python','-X','utf8','~/.claude/dreaming/lean_check.py',
        '--file',str(source),'--target','w338_checked_core',
        '--reviewed-sha256',digest,'--timeout','60','--json']
completed = subprocess.run(args,capture_output=True,text=True,encoding='utf-8',
                           errors='replace',env=env)
receipt = dict(command=args,source_sha256=digest,exit_code=completed.returncode,
               stdout=completed.stdout,stderr=completed.stderr,
               scope='Arithmetic and two-job ratio inequality only; no full probabilistic proof is certified.')
(root/'lean_result.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print('exit_code',completed.returncode)
print(completed.stdout[:3000])
