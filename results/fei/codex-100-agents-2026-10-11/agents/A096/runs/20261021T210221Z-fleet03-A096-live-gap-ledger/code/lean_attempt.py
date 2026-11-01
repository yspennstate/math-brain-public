from pathlib import Path
import subprocess,sys,os,hashlib,json
R=Path(__file__).resolve().parents[1]
if (R/'out/LEAN_RECEIPT.json').exists():
    old=(R/'out/LEAN_RECEIPT.json').read_bytes()
    (R/'out'/('LEAN_RECEIPT_PRIOR_'+hashlib.sha256(old).hexdigest()[:10]+'.json')).write_bytes(old)
env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1';env['LEAN_CHECK_DIR']=str(R/'out/lean')
flags={'creationflags':subprocess.CREATE_NO_WINDOW} if os.name=='nt' else {}
gate=subprocess.run([sys.executable,'-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8',env=env,**flags)
(R/'out/MEMOK.txt').write_text(gate.stdout+gate.stderr,encoding='utf-8')
if gate.returncode:
    receipt={'status':'NOT_STARTED_MEMOK_HOLD','exit_code':gate.returncode}
else:
    source=R/'code/ResetAccount.lean';digest=hashlib.sha256(source.read_bytes()).hexdigest()
    cmd=[sys.executable,'-B',r'lean_check.py','--file',str(source),'--core','--target','reset_account','--reviewed-sha256',digest,'--timeout','45','--json']
    result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,**flags)
    try:receipt=json.loads(result.stdout)
    except ValueError:receipt={'status':'RUNTIME_UNVERIFIED','stdout':result.stdout,'stderr':result.stderr}
    receipt['wrapper_exit_code']=result.returncode
(R/'out/LEAN_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'receipt':str(R/'out/LEAN_RECEIPT.json'),'result':receipt.get('result',receipt.get('status'))}))
