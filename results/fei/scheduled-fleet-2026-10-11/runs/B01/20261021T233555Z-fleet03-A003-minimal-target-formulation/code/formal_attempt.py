from pathlib import Path
import subprocess,sys,os,hashlib,json
R=Path(__file__).resolve().parents[1]
env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1';env['LEAN_CHECK_DIR']=str(R/'out/lean')
flags={'creationflags':subprocess.CREATE_NO_WINDOW} if os.name=='nt' else {}
gate=subprocess.run([sys.executable,'-X','utf8',r'~\brain_workers\FEI100_20261011\tools\memok.py'],capture_output=True,text=True,encoding='utf-8',env=env,**flags)
(R/'out/MEMOK.txt').write_text(gate.stdout+gate.stderr,encoding='utf-8')
if gate.returncode:
    receipt={'status':'NOT_STARTED_MEMOK_HOLD','exit_code':gate.returncode}
else:
    stmt='theorem reset_limit_integer : (3 : Nat)^18 < 2^29 := by decide'
    raw=(stmt+'\n').encode('utf-8');digest=hashlib.sha256(raw).hexdigest()
    (R/'code/ResetLimit.lean').write_bytes(raw)
    cmd=[sys.executable,'-B',r'~\.claude\dreaming\lean_check.py','--core','--stmt',stmt,'--target','reset_limit_integer','--reviewed-sha256',digest,'--timeout','25','--json']
    result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,**flags)
    try:receipt=json.loads(result.stdout)
    except ValueError:receipt={'status':'RUNTIME_UNVERIFIED','stdout':result.stdout,'stderr':result.stderr}
    receipt['wrapper_exit_code']=result.returncode
(R/'out/LEAN_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'receipt':str(R/'out/LEAN_RECEIPT.json'),'result':receipt.get('result',receipt.get('status'))}))
