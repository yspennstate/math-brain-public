from pathlib import Path
import subprocess,os,hashlib,json,sys
run=Path(__file__).resolve().parents[1]
source=run/'code/Padding.lean'
env=dict(os.environ,LEAN_CHECK_DIR=str(run/'out/lean'),PYTHONDONTWRITEBYTECODE='1')
command=[sys.executable,'-B','-X','utf8',r'lean_check.py','--core','--file',str(source),'--target','padding_bound','--reviewed-sha256',hashlib.sha256(source.read_bytes()).hexdigest(),'--timeout','45','--json']
try:
    result=subprocess.run(command,env=env,capture_output=True,text=True,encoding='utf-8',timeout=58)
    receipt={'command':command,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr}
except subprocess.TimeoutExpired:
    receipt={'command':command,'status':'WRAPPER_TIMEOUT_UNVERIFIED'}
(run/'out/LEAN_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2)[:7000])
