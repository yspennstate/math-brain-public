import hashlib,json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
source='import Std\ntheorem vacuum_cancellation (a c rho q0 : Int) : a + (c + rho - q0) = (a + c) + rho - q0 := by omega\n'
target=root/'code'/'Vacuum.lean';target.write_text(source,encoding='utf-8',newline='\n')
old=root/'out'/'LEAN_RECEIPT.json'
if old.exists():
    (root/'out'/'LEAN_FIRST_ATTEMPT.json').write_bytes(old.read_bytes())
mem=subprocess.run([sys.executable,'-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8')
out={'memok_exit':mem.returncode,'memok_output':mem.stdout+mem.stderr,'scope':'integer vacuum cancellation only; not the tensor/entropy theorem'}
if mem.returncode==0:
    env=dict(os.environ);env['LEAN_CHECK_DIR']=str(root/'out'/'lean')
    cmd=[sys.executable,'-X','utf8',r'lean_check.py','--file',str(target),'--core','--target','vacuum_cancellation','--reviewed-sha256',hashlib.sha256(target.read_bytes()).hexdigest(),'--timeout','45','--json']
    try:
        p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,timeout=58)
        out.update(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
    except subprocess.TimeoutExpired as e:out.update(status='WRAPPER_TIMEOUT',stdout=str(e.stdout),stderr=str(e.stderr))
else:out['status']='ADMISSION_HELD'
(root/'out'/'LEAN_RECEIPT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
