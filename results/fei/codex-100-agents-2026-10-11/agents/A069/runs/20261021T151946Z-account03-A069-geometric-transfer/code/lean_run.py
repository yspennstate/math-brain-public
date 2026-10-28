from pathlib import Path
import subprocess,sys,os,hashlib,json
RUN=Path(__file__).resolve().parents[1]
src=RUN/'code/QuarterBank.lean'
env=dict(os.environ);env['LEAN_CHECK_DIR']=str(RUN/'out/lean')
cmd=[sys.executable,'-B','-X','utf8',r'lean_check.py','--core','--file',str(src),'--target','quarter_bank','--reviewed-sha256',hashlib.sha256(src.read_bytes()).hexdigest(),'--timeout','55','--json']
p=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
(RUN/'out/LEAN_RESULT.json').write_text(p.stdout,encoding='utf-8')
(RUN/'out/LEAN_STDERR.txt').write_text(p.stderr,encoding='utf-8')
print(json.dumps({'exit_code':p.returncode,'stdout':p.stdout[:2500],'stderr':p.stderr[:500]}))
