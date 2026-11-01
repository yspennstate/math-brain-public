from pathlib import Path
import subprocess,json,sys,hashlib
R=Path(__file__).resolve().parents[1]; O=R/'out'; O.mkdir(exist_ok=True)
def save(f,x): (O/f).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='')
gate=subprocess.run([sys.executable,'-X','utf8','~/brain_workers/FEI100_20261011/tools/memok.py'],capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
save('MEMOK.json',{'exit_code':gate.returncode,'output':gate.stdout+gate.stderr})
if gate.returncode:
 save('LEAN.json',{'status':'ADMISSION_HELD','formal_target_verified':False,'scope':'two-allocation Nat bookkeeping only','reason':'fresh memok exit1; no compiler started'})
 print('FORMAL ADMISSION HELD; no compiler started')
else:
 source=R/'code/Book.lean'; digest=hashlib.sha256(source.read_bytes()).hexdigest()
 result=subprocess.run([sys.executable,'-X','utf8','~/.claude/dreaming/lean_check.py','--file',str(source),'--target','two_allocations','--reviewed-sha256',digest,'--core','--timeout','45','--json'],capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
 try: receipt=json.loads(result.stdout)
 except json.JSONDecodeError: receipt={'status':'UNVERIFIED','formal_target_verified':False,'output':result.stdout+result.stderr}
 receipt['wrapper_exit']=result.returncode; save('LEAN.json',receipt)
 print(json.dumps({'formal_status':receipt.get('result',receipt).get('status'),'exit_code':result.returncode}))
