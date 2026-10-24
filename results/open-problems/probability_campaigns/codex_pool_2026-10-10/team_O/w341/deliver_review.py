"""Fail-closed preparation: a failed validation cannot set review-ready status."""
import os
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
status=ROOT/'STATUS.md'
lines=status.read_text(encoding='utf-8').splitlines()
lines[0]='STATE: WORKING'
lines[1]='NEXT: Complete fail-closed driver validation; only then save STATE: NEEDS_REVIEW.'
status.write_text('\n'.join(lines)+'\n',encoding='utf-8')
env=dict(os.environ)
env['PYTHONDONTWRITEBYTECODE']='1'
for script in ['prepare_review.py','validate_package.py','read_team_ro.py','finalize_review.py']:
    print('DELIVERY STEP',script,flush=True)
    subprocess.run([sys.executable,'-X','utf8','-B',str(ROOT/script)],cwd=ROOT,env=env,check=True)
required=['REPORT.md','AUDITOR_PACKET.md','AUDIT_QUEUE.json','SESSION_RECEIPT.json','PROGRESS_EVENT.json','READY_ROWS.jsonl']
assert all((ROOT/name).is_file() and (ROOT/name).stat().st_size for name in required)
assert status.read_text(encoding='utf-8').splitlines()[0]=='STATE: NEEDS_REVIEW'
print('DELIVERY COMPLETE: all required handoff files exist; fresh validation passed.',flush=True)
