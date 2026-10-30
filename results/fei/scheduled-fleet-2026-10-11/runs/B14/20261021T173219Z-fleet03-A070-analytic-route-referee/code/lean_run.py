from pathlib import Path
import subprocess,sys,os,hashlib,json
run=Path(__file__).resolve().parents[1]
gate=subprocess.run([sys.executable,'-X','utf8',r'~/brain_workers/FEI100_20261011/tools/memok.py'],capture_output=True,text=True,encoding='utf-8')
(run/'out/MEMOK.txt').write_text(gate.stdout+gate.stderr,encoding='utf-8')
if gate.returncode:
 (run/'out/LEAN_RESULT.json').write_text(json.dumps({'status':'NOT_STARTED_MEMOK_DENIED'}),encoding='utf-8');print('MEMOK denied');sys.exit(0)
src=run/'code/Telescope.lean';env=dict(os.environ);env['LEAN_CHECK_DIR']=str(run/'out/lean')
cmd=[sys.executable,'-B','-X','utf8',r'~/.claude/dreaming/lean_check.py','--core','--file',str(src),'--target','telescope','--reviewed-sha256',hashlib.sha256(src.read_bytes()).hexdigest(),'--timeout','45','--json']
p=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
(run/'out/LEAN_RESULT.json').write_text(p.stdout,encoding='utf-8');(run/'out/LEAN_STDERR.txt').write_text(p.stderr,encoding='utf-8')
print(p.stdout[:2800]);print('exit',p.returncode)
