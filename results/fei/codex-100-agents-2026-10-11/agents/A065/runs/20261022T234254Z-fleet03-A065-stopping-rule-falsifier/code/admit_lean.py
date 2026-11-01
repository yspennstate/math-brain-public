from pathlib import Path
import subprocess,sys,os,json,hashlib
R=Path(__file__).resolve().parents[1]
env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1';env['LEAN_CHECK_DIR']=str(R/'out/lean')
gate=subprocess.run([sys.executable,'-B','-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8',env=env)
result={'memok_exit':gate.returncode,'memok_output':gate.stdout+gate.stderr,'status':'NOT_ADMITTED'}
if gate.returncode==0:
 p=R/'code/Interposition.lean'
 cmd=[sys.executable,'-B','-X','utf8',r'lean_check.py','--core','--file',str(p),'--target','interposition_power_certificate','--reviewed-sha256',hashlib.sha256(p.read_bytes()).hexdigest(),'--timeout','55','--json']
 completed=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env)
 result.update(status='ATTEMPTED',exit_code=completed.returncode,output=completed.stdout+completed.stderr)
 try:result['receipt']=json.loads(completed.stdout)
 except json.JSONDecodeError:pass
(R/'out/LEAN_ATTEMPT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
