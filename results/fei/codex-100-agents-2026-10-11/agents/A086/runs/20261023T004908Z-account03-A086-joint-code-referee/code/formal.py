from pathlib import Path
import json,subprocess,hashlib,os,sys
R=Path(__file__).resolve().parents[1];O=R/'out';O.mkdir(exist_ok=True)
source='''import Lean
theorem A086_padding17 (m : Nat) : 16*m+17 <= 17*2^m := by
  induction m with
  | zero => decide
  | succ m ih =>
    rw [Nat.pow_succ]
    omega
'''
p=R/'code/Padding17.lean';p.write_text(source,encoding='utf-8',newline='\n')
receipt={'target':'A086_padding17','source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'translation':'For EVERY natural m,16m+17<=17*2^m. Padding induction only; not formal certification of entropy/reset theorem.'}
admission=subprocess.run([sys.executable,'-B','-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
(O/'LEAN_ADMISSION.txt').write_text(admission.stdout+admission.stderr,encoding='utf-8')
if admission.returncode:
    receipt['status']='ADMISSION_HELD';receipt['returncode']=admission.returncode
else:
    env=os.environ.copy();env['TEMP']=str(O);env['TMP']=str(O)
    command=[sys.executable,'-B','-X','utf8',r'lean_check.py','--core','--file',str(p),'--target','A086_padding17','--reviewed-sha256',receipt['source_sha256'],'--timeout','20','--json']
    completed=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',env=env,creationflags=subprocess.CREATE_NO_WINDOW)
    (O/'LEAN_RAW.json').write_text(completed.stdout,encoding='utf-8')
    (O/'LEAN_STDERR.txt').write_text(completed.stderr,encoding='utf-8')
    receipt['returncode']=completed.returncode
    try:
        receipt['wrapper']=json.loads(completed.stdout);receipt['status']=receipt['wrapper']['result']['status']
    except (json.JSONDecodeError,KeyError):receipt['status']='RUNTIME_UNVERIFIED'
(O/'LEAN_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k!='wrapper'}))
