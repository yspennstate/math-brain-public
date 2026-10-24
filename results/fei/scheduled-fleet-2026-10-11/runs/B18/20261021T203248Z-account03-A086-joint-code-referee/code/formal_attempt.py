from pathlib import Path
import json, subprocess, hashlib, os, sys
BASE=Path(__file__).resolve().parents[1]
root=Path(r'~')
checker=root/'.claude/dreaming/lean_check.py'
# Inspect only the command interface, never run a Mathlib import under the packet cap.
lines=checker.read_text(encoding='utf-8').splitlines()
print('\n'.join(s for s in lines if any(t in s for t in ['add_argument(',"'import Lean",'--core','import Std'])))
print('PIN', (root/'lean_verify/lean-toolchain').read_text(encoding='utf-8').strip())
source='''import Lean
theorem A086_padding_bound (m : Nat) : 16*m+37 <= 37*2^m := by
  induction m with
  | zero => decide
  | succ m ih =>
    rw [Nat.pow_succ]
    omega
'''
path=BASE/'code'/'Padding.lean'; path.write_text(source,encoding='utf-8',newline='\n')
result={'status':'SOURCE_PREPARED_NOT_CHECKED','target':'A086_padding_bound','source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'prose':'For each natural m, 16m+37 is at most 37 times 2 to the m; only the padding-tail induction, not the FEI theorem.'}
(BASE/'out'/'LEAN_RECEIPT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
if '--run' in sys.argv:
    admission=subprocess.run([sys.executable,'-B','-X','utf8',str(root/'brain_workers/FEI100_20261011/tools/memok.py')],capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
    (BASE/'out'/'LEAN_ADMISSION.txt').write_text(admission.stdout+admission.stderr,encoding='utf-8')
    if admission.returncode:
        result['status']='ADMISSION_HELD'; result['returncode']=admission.returncode
    else:
        env=os.environ.copy(); env['TEMP']=str(BASE/'out'); env['TMP']=str(BASE/'out')
        command=[sys.executable,'-B','-X','utf8',str(checker),'--file',str(path),'--core','--target','A086_padding_bound','--reviewed-sha256',result['source_sha256'],'--timeout','20','--json']
        process=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',env=env,creationflags=subprocess.CREATE_NO_WINDOW)
        (BASE/'out'/'LEAN_RAW.json').write_text(process.stdout,encoding='utf-8')
        (BASE/'out'/'LEAN_STDERR.txt').write_text(process.stderr,encoding='utf-8')
        result['returncode']=process.returncode
        try:
            receipt=json.loads(process.stdout); result['wrapper_receipt']=receipt
            result['status']=receipt.get('result',{}).get('status','RUNTIME_UNVERIFIED')
        except json.JSONDecodeError: result['status']='RUNTIME_UNVERIFIED'
    (BASE/'out'/'LEAN_RECEIPT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='wrapper_receipt'}))
