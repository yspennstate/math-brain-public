import json
import os
import pathlib
import subprocess

root=pathlib.Path(__file__).resolve().parent
environment=dict(os.environ)
environment['LEAN_CHECK_DIR']=str(root/'lean_receipts')
environment['PYTHONDONTWRITEBYTECODE']='1'
command=['python','-B','-X','utf8','~/.claude/dreaming/lean_check.py','--file',str(root/'GapIdentity.lean'),'--target','w335_gap_identity','--timeout','60','--json']
try:
    completed=subprocess.run(command,env=environment,capture_output=True,text=True,encoding='utf-8',timeout=90)
    receipt={'command':command,'returncode':completed.returncode,'stdout':completed.stdout,'stderr':completed.stderr,'scope':'Scalar rational identity only; translation and full open-problem proof are not formally certified.'}
except subprocess.TimeoutExpired as error:
    receipt={'command':command,'returncode':None,'status':'RUNNER_TIMEOUT_NOT_LEAN_CHECKED','scope':'No formal verification claimed.'}
(root/'lean_run_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False),flush=True)
