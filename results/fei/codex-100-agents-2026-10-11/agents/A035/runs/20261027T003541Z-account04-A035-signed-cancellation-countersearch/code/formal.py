from pathlib import Path
import subprocess, os, hashlib, json
p=Path(__file__).resolve().parents[1]
src=p/'code/Cauchy.lean'
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',LEAN_CHECK_DIR=str(p/'out/lean'))
cmd=['python','-B','-X','utf8',r'lean_check.py','--core','--file',str(src),'--target','a035_cleared_cauchy','--reviewed-sha256',hashlib.sha256(src.read_bytes()).hexdigest(),'--timeout','45','--json']
r=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding='utf-8',timeout=75)
(p/'out/LEAN.json').write_text(json.dumps({'command':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr},indent=2)+'\n',encoding='utf-8')
print(r.returncode,r.stdout[:2200],r.stderr[:500])
