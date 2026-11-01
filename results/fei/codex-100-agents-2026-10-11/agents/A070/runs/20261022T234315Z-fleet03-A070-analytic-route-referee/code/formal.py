from pathlib import Path
import subprocess,sys,os,hashlib,json
run=Path(__file__).resolve().parents[1]
gate=subprocess.run([sys.executable,'-X','utf8',r'tools/memok.py'],capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
(run/'out/MEMOK.txt').write_text(gate.stdout+gate.stderr,encoding='utf-8')
if gate.returncode:
 result={'status':'BLOCKED_COMPUTE_ADMISSION','formal_target_verified':False,'memok_exit':gate.returncode}
 (run/'out/LEAN_RESULT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result));sys.exit(0)
src=run/'code/Budget.lean';env=dict(os.environ);env['LEAN_CHECK_DIR']=str(run/'out/lean')
cmd=[sys.executable,'-B','-X','utf8',r'lean_check.py','--core','--file',str(src),'--target','remaining_bank','--reviewed-sha256',hashlib.sha256(src.read_bytes()).hexdigest(),'--timeout','20','--json']
p=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
(run/'out/LEAN_RESULT.json').write_text(p.stdout,encoding='utf-8');(run/'out/LEAN_STDERR.txt').write_text(p.stderr,encoding='utf-8')
try:r=json.loads(p.stdout);print(json.dumps({'exit':p.returncode,'result':r.get('result'),'seconds':r.get('seconds')},indent=2))
except ValueError:print('Unparsed formal helper output; no verified theorem claimed.')
